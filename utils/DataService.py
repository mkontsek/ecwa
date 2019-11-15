import json
from os import path

DATA_DIRNAME = 'data'
POPULATION_FILENAME = 'population.csv'
COUNTRY_FILENAME = 'countriesByCode.json'
ACCESS_FILENAME = 'electricityAccessByCountry.json'
CONSUMPTION_FILENAME = 'electricityConsumptionByCountry.json'


def getOpenedDataFile(name, access='r'):
    filedir = path.dirname(path.realpath(__file__))
    filepath = path.join(filedir, DATA_DIRNAME, name)
    return open(filepath, access)


def writeJsonToFile(name, jsonData):
    OUTPUT_INDENTATION = 2
    file = getOpenedDataFile(name, access='w')
    file.write(json.dumps(jsonData, indent=OUTPUT_INDENTATION))
    file.close()
    print('Finished writing', name)

def getCountries():
    file = getOpenedDataFile(COUNTRY_FILENAME)
    result = json.loads(file.read())
    file.close()
    return result


def getAccesses():
    file = getOpenedDataFile(ACCESS_FILENAME)
    result = json.loads(file.read())
    file.close()
    return result

def getConsumptions():
    file = getOpenedDataFile(CONSUMPTION_FILENAME)
    result = json.loads(file.read())
    file.close()
    return result