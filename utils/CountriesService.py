import functools

URL_LIST_OF_COUNTRIES = 'https://api.worldbank.org/v2/country/all?format=json&per_page=350'


def appendCountryCode(acc, obj):
    obj['countryCode'] = obj['id']
    del obj['id']

    acc.append(obj)

    return acc


def getCountriesByCode(rawResponseData):
    allValues = rawResponseData[1]
    result = functools.reduce(appendCountryCode, allValues, [])

    return result
