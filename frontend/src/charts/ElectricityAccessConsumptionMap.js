import React from 'react';
import { Chart } from 'react-google-charts';

import { BASE_CHART_PROPS, getChartData } from './ChartService'

export function ElectricityAccessConsumptionMap({ country, countryData }) {
    if (!country) {
        return null;
    }

    return (
        <Chart
            {...BASE_CHART_PROPS}
            data={getChartData(countryData)}
        />
    )
}