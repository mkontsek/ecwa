const OPENCAGE = { URL: 'https://api.opencagedata.com/geocode/v1/json', API_KEY: '781d85f84a314053b29ca7755574cf65' };

function createLatLonUrl(latitude, longitude) {
    return [
        OPENCAGE.URL,
        '?key=',
        OPENCAGE.API_KEY,
        '&q=',
        encodeURIComponent(`${latitude},${longitude}`),
    ].join('');
}

function createQueryUrl(query) {
    return [
        OPENCAGE.URL,
        '?key=',
        OPENCAGE.API_KEY,
        '&q=',
        encodeURIComponent(query),
    ].join('');
}

function getLocation() {
    return new Promise(resolve => {
        const { geolocation } = navigator || {};

        if (!geolocation) {
            return;
        }

        geolocation.getCurrentPosition(resolve)
    })
}

function processOpencageResultCountryCode(data) {
    return data.results[0].components.country_code.toUpperCase();
}

function processOpencageResultIso3Code(data) {
    return data.results[0].components['ISO_3166-1_alpha-3'].toUpperCase();
}

export async function fetchCurrentCountry() {
    const { coords: { latitude, longitude } } = await getLocation();
    const url = createLatLonUrl(latitude, longitude);
    const response = await fetch(url);
    const jsonData = await response.json();

    return processOpencageResultCountryCode(jsonData);
}

export async function fetchCountryLocation(countryCode) {
    const url = createQueryUrl(countryCode);
    const response = await fetch(url);
    const jsonData = await response.json();

    return processOpencageResultIso3Code(jsonData);
}

export async function fetchCountryInfo(countryCode) {
    const url = `http://localhost:8000/${countryCode}`;
    const response = await fetch(url);
    const jsonData = await response.json();

    return jsonData;
}