import asyncio
import json
import aiohttp

from ElectricityAccessService import getAccessByCountry, URL_ELECTRICITY_ACCESS
from ElectricityConsumptionService import getConsumptionByCountryPerCapita, URL_ELECTRICITY_CONSUMPTION
from CountriesService import getCountriesByCode, URL_LIST_OF_COUNTRIES
from DataService import DATA_DIRNAME, COUNTRY_FILENAME, ACCESS_FILENAME, CONSUMPTION_FILENAME, writeJsonToFile


async def downloadData(url):
    session = aiohttp.ClientSession()
    resp = await session.get(url)
    data = await resp.read()
    await session.close()
    return json.loads(data)


async def fetchCountries():
    rawResponseData = await downloadData(URL_LIST_OF_COUNTRIES)
    result = getCountriesByCode(rawResponseData)
    writeJsonToFile(COUNTRY_FILENAME, result)


async def fetchElectricityAccess():
    rawResponseData = await downloadData(URL_ELECTRICITY_ACCESS)
    result = getAccessByCountry(rawResponseData)
    writeJsonToFile(ACCESS_FILENAME, result)


async def fetchElectricityConsumption():
    rawResponseData = await downloadData(URL_ELECTRICITY_CONSUMPTION)
    result = getConsumptionByCountryPerCapita(rawResponseData)
    writeJsonToFile(CONSUMPTION_FILENAME, result)


async def main():
    print('Started download of countries...')
    countryTask = asyncio.create_task(fetchCountries())

    print('Started download of electricity access...')
    accessTask = asyncio.create_task(fetchElectricityAccess())

    print('Started download of electricity consumption...')
    consumptionTask = asyncio.create_task(fetchElectricityConsumption())

    await asyncio.gather(countryTask, accessTask, consumptionTask)


if __name__ == "__main__":
    asyncio.run(main())
