export const BASE_CHART_PROPS = {
    mapsApiKey: "AIzaSyBQsTsscKN66W2A8ysX9RH2BGn43nUUGhI",
    chartType: "GeoChart",
    width: '80%'
}

export function getChartData(data) {
    if (!data) {
        return;
    }

    const top10access = data['top10access'];
    const bottom10access = data['bottom10access'];

    let result = top10access.reduce((acc, obj) => {
        acc.push([obj.iso2Code, `${obj.electricityAccessPercentage}%`]);
        return acc;
    }, [['Country', 'Electricity access']]);

    result = bottom10access.reduce((acc, obj) => {
        acc.push([obj.iso2Code, `${obj.electricityAccessPercentage}%`]);
        return acc;
    }, result);

    return result;
}