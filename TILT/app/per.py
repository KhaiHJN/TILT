import requests
import json

def getJsonPerHundreThousand(land):

    res = requests.get('https://opendata.ecdc.europa.eu/covid19/casedistribution/json/')

    for elem in res.json()['records']:
        if elem['countriesAndTerritories'] == land:

            return elem['Cumulative_number_for_14_days_of_COVID-19_cases_per_100000']