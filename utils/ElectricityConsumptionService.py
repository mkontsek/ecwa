import functools

from PopulationService import getPopulations

URL_ELECTRICITY_CONSUMPTION = 'https://api.worldbank.org/v2/country/all/indicator/1.1_TOTAL.FINAL.ENERGY.CONSUM?format=json&per_page=7000'
MWH_IN_TERAJOULE = 277.777778


def getMwhFromTeraJoule(teraJoules):
    if teraJoules is None:
        return 0

    return MWH_IN_TERAJOULE * teraJoules


def appendConsumptionCountryYear(acc, obj):
    consumptionTeraJoules = obj['value']
    countryCode = obj['country']['id']
    surveyYear = obj['date']

    acc.append({
        'countryCode': countryCode,
        'electricityConsumptionInMwh': getMwhFromTeraJoule(consumptionTeraJoules),
        'year': surveyYear
    })

    return acc


def calculatePerCapita(consumption, population):
    try:
        return consumption['electricityConsumptionInMwh'] / population
    except:
        return None


def isSameYearAndCountry(obj):
    return lambda x: obj['year'] == x['year'] and \
                     obj['countryCode'] == x['countryCode']


def createPerCapitaByPopulationYear(consumption, populations):
    populationYearList = list(filter(isSameYearAndCountry(consumption), populations))

    if len(populationYearList) == 0:
        return None

    population = populationYearList[0]['population']
    perCapita = calculatePerCapita(consumption, population)

    if perCapita is None:
        return None

    return {
        **consumption,
        'perCapita': perCapita
    }


def appendPerCapita(populations):
    def function(acc, consumption):
        item = createPerCapitaByPopulationYear(consumption, populations)
        if item is not None:
            acc.append(item)
        return acc

    return function


def getConsumptionByCountryPerCapita(rawResponseData):
    allValues = rawResponseData[1]
    populations = getPopulations()
    countriesConsumptions = functools.reduce(appendConsumptionCountryYear, allValues, [])
    countriesConsumptionsPerCapita = functools.reduce(appendPerCapita(populations), countriesConsumptions, [])
    return countriesConsumptionsPerCapita
