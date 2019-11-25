import functools

from utils.DataService import getCountries, getAccesses, getConsumptions


def isSameCountry(ranking):
    return lambda x: ranking['countryCode'] == x['countryCode']


def addUniqueCountry(acc, country):
    isUniqueCountry = True
    for i in range(len(acc)):
        if country['countryCode'] == acc[i]['countryCode']:
            isUniqueCountry = False
    if isUniqueCountry:
        acc.append(country)
    return acc


def uniqCountry(countries):
    return functools.reduce(addUniqueCountry, countries, [])


def appendCountryData(countries):
    def function(acc, ranking):
        sameCountries = list(filter(isSameCountry(ranking), countries))
        if len(sameCountries) == 0:
            return acc
        country = sameCountries[0]
        acc.append({**ranking, **country})
        return acc

    return function


def applyCountryData(countries, rankings):
    if rankings is None:
        return None
    return functools.reduce(appendCountryData(countries), rankings, [])


def getTop10Access(data):
    return sorted(uniqCountry(data), key=lambda x: x['electricityAccessPercentage'], reverse=True)[:11]


def getTop10Consumption(data):
    return sorted(uniqCountry(data), key=lambda x: x['perCapita'], reverse=True)[:10]


def getBottom10Access(data):
    return sorted(uniqCountry(data), key=lambda x: x['electricityAccessPercentage'])[:10]


def getYourCountryData(countryCode, statistics):
    if countryCode is None:
        return None
    countryData = list(filter(lambda x: x['countryCode'] == countryCode, statistics))
    return sorted(countryData, key=lambda x: x['year'])


def createRanking(countryCode=None):
    countries = getCountries()
    accesses = getAccesses()
    consumptions = getConsumptions()
    emptyRanking = [{'countryCode': countryCode}]
    return {
        'top10access': applyCountryData(countries, getTop10Access(accesses)),
        'top10consumptionPerCapita': applyCountryData(countries, getTop10Consumption(consumptions)),
        'bottom10access': applyCountryData(countries, getBottom10Access(accesses)),
        'yourAccess': getYourCountryData(countryCode, accesses),
        'yourConsumption': getYourCountryData(countryCode, consumptions),
        'yourCountry': applyCountryData(countries, emptyRanking)
    }
