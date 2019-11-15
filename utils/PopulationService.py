import functools
from os import path

from DataService import POPULATION_FILENAME, getOpenedDataFile

FIRST_YEAR_IN_FILE = 1960
FIRST_YEAR_INDEX = 5
TOTAL_YEARS_IN_FILE = 59
SEPARATOR = ','
COUNTRY_CODE_INDEX = 1


def getPopulationInt(str):
    try:
        cleanedPopulation = str.replace('"', '')
        return int(cleanedPopulation)
    except:
        return None


def createPopulationCountryYear(countryCode, dataPoints, yearOffset):
    currentIndex = FIRST_YEAR_INDEX + yearOffset
    year = str(FIRST_YEAR_IN_FILE + yearOffset)

    return {
        'countryCode': countryCode,
        'year': year,
        'population': getPopulationInt(dataPoints[currentIndex])
    }


def appendCountryYear(acc, csvLine):
    dataPoints = csvLine.split(SEPARATOR)
    countryCode = dataPoints[COUNTRY_CODE_INDEX].replace('"','')

    for yearOffset in range(TOTAL_YEARS_IN_FILE):
        acc.append(createPopulationCountryYear(countryCode, dataPoints, yearOffset))

    return acc


def getPopulations():
    file = getOpenedDataFile(POPULATION_FILENAME)
    csvData = file.readlines()
    file.close()
    jsonData = functools.reduce(appendCountryYear, csvData, [])

    return jsonData
