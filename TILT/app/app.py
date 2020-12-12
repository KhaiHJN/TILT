import requests
import bs4
import listLand
import per
from flask import Flask, render_template, redirect, url_for, request
app = Flask(__name__)

def get_html_data(url):
    data = requests.get(url)
    return data

@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        land = request.form["land"]
        land = land.title()

        if land in listLand.CountriesList:
            return redirect(url_for("get_country", land=land))
        else:
            colours = listLand.CountriesList
            url = "https://www.worldometers.info/coronavirus/"
            html_data = get_html_data(url)
            bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
            info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
            all_detail = ""

            for block in info_div:
                text = block.find("h1", class_=None).get_text()
                count = block.find("span", class_=None).get_text()
                all_detail = all_detail + text + " " + count + "<br>"
   
            return render_template('home.html', colours=colours, all_detail=all_detail, msg="Du har tastet inn feil. <br>")      
    else:
        colours = listLand.CountriesList
        url = "https://www.worldometers.info/coronavirus/"
        html_data = get_html_data(url)
        bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
        info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap")
        all_detail = ""

        for block in info_div:
            text = block.find("h1", class_=None).get_text()
            count = block.find("span", class_=None).get_text()
            all_detail = all_detail + text + " " + count + "<br>"

        return render_template('home.html', colours=colours, all_detail=all_detail)    
 
@app.route("/<land>")
def get_country(land):
    newURL = listLand.CountriesURL.get(land)
    url = f"https://www.regjeringen.no{newURL}"
    html_data = requests.get(url)
    bs = bs4.BeautifulSoup(html_data.text, 'html.parser')

    info_p = bs.find("div", class_="article-body").findAll(['h2', "p", "strong"])
    result = ''
    for n, elem in enumerate(info_p):
        if ('Innreise') in elem:
            for data in info_p[n+1:]:
                if str(data).startswith('<h2><a id='):
                    break
                result += str(data)

    nyland = listLand.CountriesEng.get(land)

    if nyland == "not found":
        msg = "Finnes ingen tall fra landet."
        return render_template("country.html", land=land, result=result, msg=msg)
    else:    
        url = f"https://www.worldometers.info/coronavirus/country/{nyland}"
        html_data = get_html_data(url)
        bs = bs4.BeautifulSoup(html_data.text, 'html.parser')
        info_div = bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap", style="margin-top:15px") + bs.find("div", class_="content-inner").findAll("div", id="maincounter-wrap", style="margin-top:15px;")
        all_detail = ""

        for block in info_div:    
            text = block.find("h1").get_text()
            count = block.find("span").get_text()
            all_detail = all_detail + text + " " + count + "<br>"              
        
        perDetails = per.getJsonPerHundreThousand(land)

        return render_template("country.html", land=land, result=result, all_detail=all_detail, perDetails=perDetails )

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
