import React from 'react';
import { Divider, Grid, List, ListItemText, makeStyles, Typography } from '@material-ui/core';

const useStyles = makeStyles(() => ({
    top10charts: {
        marginLeft: '2rem',
    },
    divider: {
        marginLeft: '-2rem',
    },
    consumptionChart: {
        marginTop: '1rem',
    },
}));

function renderAccesItem(obj) {
    return <ListItemText>{`${obj.iso2Code} - ${obj.electricityAccessPercentage}% of the population has access to electricity.`}</ListItemText>
}

function renderTop10Access(data) {
    const top10access = data['top10access'];

    return top10access.reduce((acc, obj) => {
        acc.push(renderAccesItem(obj));
        return acc;
    }, []);
}

function renderBottom10Access(data) {
    const bottom10access = data['bottom10access'];

    return bottom10access.reduce((acc, obj) => {
        acc.push(renderAccesItem(obj));
        return acc;
    }, []);
}

function renderTop10Consumption(data) {
    const top10consumption = data['top10consumptionPerCapita'];

    return top10consumption.reduce((acc, obj) => {
        acc.push(
            <ListItemText>{`${obj.iso2Code} - Each person uses on average ${obj.perCapita} MWh of electricity.`}</ListItemText>);
        return acc;
    }, []);
}

function renderYourCountry(data, classes) {
    const yourCountry = data['yourCountry'][0];

    if (!yourCountry) {
        return null;
    }

    const yourConsumption = data['yourConsumption'];
    const yourAccess = data['yourAccess'];

    return (
        <>
            <Divider className={classes.divider} />
            <Typography variant="h4" component="h2">{yourCountry.name}</Typography>
            <List>
                {yourAccess.map(obj => <ListItemText>Access in
                    year {obj.year} was {obj.electricityAccessPercentage}%.</ListItemText>)}
                {yourConsumption.map(obj => (
                    <ListItemText>
                        Consumption in year {obj.year} was {obj.perCapita} MWh per capita.
                    </ListItemText>
                ))}
            </List>
        </>
    );
}

export function Top10Charts({ countryData }) {
    const classes = useStyles();
    if (!countryData) {
        return null;
    }

    return (
        <div className={classes.top10charts}>
            <Grid container justify="space-between">
                <Grid item xs={6}>
                    <Typography variant="h4" component="h2">Top 10 access to electricity</Typography>
                    <List>
                        {renderTop10Access(countryData)}
                    </List>
                </Grid>
                <Grid item xs={6}>
                    <Typography variant="h4" component="h2">Bottom 10 access to electricity</Typography>
                    <List>
                        {renderBottom10Access(countryData)}
                    </List>
                </Grid>
            </Grid>
            <div className={classes.consumptionChart}>
                <Typography variant="h4" component="h2">Top 10 electricity consumption per capita</Typography>
                <List>
                    {renderTop10Consumption(countryData)}
                </List>
            </div>
            {renderYourCountry(countryData, classes)}
        </div>
    )
}