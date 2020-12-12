# Travel Informer, Little Traveler (TILT)

COVID-19 project using Web Scraping and REST API to get current informasjon (in norwegian, from regjeringen.no) abour rules for entry at the destination and the covid situation.

## Content

1. [Technologies](https://github.com/KhaiHJN/TILT#technologies)
2. [Intention](https://github.com/KhaiHJN/TILT#intention)
3. [License](https://github.com/KhaiHJN/TILT#license)
4. [Installing and running](https://github.com/KhaiHJN/TILT#installing-and-running)
5. [Developers](https://github.com/KhaiHJN/TILT#developers)


## Technologies
+ [Python 3.8 or higher](https://www.python.org/downloads/)
+ [Docker](https://www.docker.com/get-started)

## Intention

The purpose of this project is to provide a solution for monitoring the status of a destination COVID-19 restrictions and situation, or whatever the user want to monitor the current situation. Travel Informer, Little Traveler (TILT) is a website that uses [Flask](http://flask.pocoo.org/) to run with [Docker](https://www.docker.com/get-started) for hosting. We are using it to deliver data such as:
+ [Entry rules (Regjeringen.no)](https://www.regjeringen.no/no/tema/Koronasituasjonen/id2692388/)
+ [COVID-19 statistics (Worldometers.info)](https://www.worldometers.info/coronavirus/)

This is to help the traveler determine what the situation is like at a destination before traveling. 

## License

## Installing and running
This webpage is meant to be run on docker.

Step-by step:

1. ```git clone https://github.com/KhaiHJN/TILT ```

2. ```cd TILT``` and run ```docker build -t tilt:latest .``` This will install Flask, Request and package the python files, making imports more trivial.

3. Then run ``` docker run -d -p 5000:5000 tilt``` This starts the webserver.

4. Go to ``` 0.0.0.0:5000 ``` on your browser to see the the webpage.

These steps will create a Flask webserver and run it on docker, but will only make it accessible from within the local network. Opening Port Forwarding at port :5000 means it can be accessed from outside network. Check with your internet provider how to do this. 

**DISCLAIMER:** Port forwarding is done at your own risk. We take no responsibility.

## Developers 

+ Khai H. J. Nguyen [@KhaiHJN](https://github.com/KhaiHJN)

+ Arian Nuland [@Nuskard](https://github.com/Nuskard)

+ Sven Opheim-Halsne [@svhalsne](https://github.com/svhalsne)

+ Andreas Perez [@motzic](https://github.com/motzic)

+ Christer Høiland [@ChristerHoei](https://github.com/ChristerHoei)

