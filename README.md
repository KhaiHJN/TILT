# Travel Informer, Little Traveler (TILT)

COVID-19 project using Web Scraping and REST API to get current informasjon (in norwegian, from regjeringen.no) abour rules for entry at the destination and the covid situation.

## Content

1. [Technologies](https://github.com/KhaiHJN/IS-308#technologies)
2. [Intent](https://github.com/KhaiHJN/IS-308#intent)
3. [License](https://github.com/KhaiHJN/IS-308#license)
4. [Installing and running](https://github.com/KhaiHJN/IS-308#installing-and-running)
5. [Developers](https://github.com/KhaiHJN/IS-308#developers)
6. [Acknowledgements](https://github.com/KhaiHJN/IS-308#acknowledgements)

## Technologies
+ [Python 3.6 or higher](https://www.python.org/downloads/)
+ [Docker](https://www.docker.com/get-started)

## Intention

The purpose of this project is to provide an solution for monitoring the status at the destination COVID-19 rules and situation, or whatever the user want to monitor the current situation. Travel Informer, Little Traveler (TILT) is a website that uses [Flask](http://flask.pocoo.org/) to run with [Docker](https://www.docker.com/get-started) for hosting. We are using it to deliver data such as:
+ [Entry rules (Regjeringen.no)](https://www.regjeringen.no/no/tema/Koronasituasjonen/id2692388/)
+ [COVID-19 statistics](https://www.worldometers.info/coronavirus/)

This is to help the traveler determine what is the situation at the destination before traveling. 

## Installing and running
This webpage is meant to be run on docker, but also possible locally on your pc. 

Step-by step:

1. ```git clone https://github.com/KhaiHJN/IS-308 ```

2. ```cd IS-308``` and run ```docker build -t reise:latest .``` This will install Flask, Request and package the python files, making imports more trivial.

3. Then run ``` docker run -d -p 5000:5000 flask-tutorial``` This starts the webserver.

4. Go to ``` 0.0.0.0:5000 ``` on your browser to see the the webpage.

These steps will create a Flask webserver and run it on docker, but will only make it accessible from within the local network. Opening Port Forwarding at port :5000 means it can be accessed from outside network. Check with your internet provider how to do this. 

**DISCLAIMER:** Port forwarding and remote access is done at your own risk. We take no responsibility.

## Developers 

+ Nguyen. Khai H. J. [@KhaiHJN](https://github.com/KhaiHJN)

+ Nuland. Arian [@Nuskard](https://github.com/Nuskard)

+ Opheim-Halsne. Sven [@svhalsne](https://github.com/svhalsne)

+ Perez. Andreas [@motzic](https://github.com/motzic)

+ Høiland. Christer [@ChristerHoei](https://github.com/ChristerHoei)

