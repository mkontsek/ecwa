import React, { useEffect, useState } from 'react';

import { SearchBar } from './SearchBar';
import { Spinner } from './Spinner';
import { fetchCountryInfo, fetchCountryLocation, fetchCurrentCountry } from './RegionService';
import { ElectricityAccessConsumptionMap } from './charts/ElectricityAccessConsumptionMap';
import { Top10Charts } from './charts/Top10Charts';

export function App() {
    const [countryCode, setCountryCode] = useState();
    const [countryData, setCountryData] = useState();

    const handleRegionClick = async (newCountryCode) => {
        const iso3CountryCode = await fetchCountryLocation(newCountryCode);
        const newCountryData = await fetchCountryInfo(iso3CountryCode);

        setCountryCode(newCountryCode);
        setCountryData(newCountryData);
    };

    const loadAndRenderCountry = async () => {
        if (countryCode) {
            return;
        }

        const newCountryCode = await fetchCurrentCountry();
        const iso3CountryCode = await fetchCountryLocation(newCountryCode);
        const newCountryData = await fetchCountryInfo(iso3CountryCode);

        setCountryCode(newCountryCode);
        setCountryData(newCountryData);
    };

    useEffect(() => {
        setTimeout(() => loadAndRenderCountry(handleRegionClick), 1000);
    });

    return (
        <Spinner isActive={countryCode === undefined} text="Loading country data...">
            <SearchBar defaultCountry={countryCode} onSelect={handleRegionClick} />
            <ElectricityAccessConsumptionMap country={countryCode} countryData={countryData} />
            <Top10Charts country={countryCode} countryData={countryData} />
        </Spinner>
    );
}