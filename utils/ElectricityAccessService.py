import functools

URL_ELECTRICITY_ACCESS = 'https://api.worldbank.org/v2/country/all/indicator/1.1_ACCESS.ELECTRICITY.TOT?format=json&per_page=7000'


def hasValueAndCurrentDate(acc, obj):
    electricityAccessPercentage = obj['value']
    countryCode = obj['country']['id']
    surveyYear = obj['date']

    if electricityAccessPercentage is None:
        return acc

    dataPoint = {
        'countryCode': countryCode,
        'electricityAccessPercentage': electricityAccessPercentage,
        'year': surveyYear
    }

    acc.append(dataPoint)

    return acc


def getAccessByCountry(rawResponseData):
    allValues = rawResponseData[1]
    byCountries = functools.reduce(hasValueAndCurrentDate, allValues, [])

    return byCountries
