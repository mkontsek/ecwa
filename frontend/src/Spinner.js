import React from 'react';
import CircularProgress from '@material-ui/core/CircularProgress';
import { makeStyles } from '@material-ui/core/styles';
import { Typography } from '@material-ui/core';

const useStyles = makeStyles(() => ({
    spinner: {
        position: 'absolute',
        display: 'flex',
        flexDirection: 'column',
        justifyContent: 'center',
        alignItems: 'center',
        height: '60%',
        width: '100%',
    },
}));

export function Spinner({ isActive, text, children }) {
    const classes = useStyles();

    if (isActive) {
        return (
            <div className={classes.spinner}>
                <CircularProgress size={200} />
                <Typography variant="h2" component="h1">{text}</Typography>
            </div>
        )
    }

    return children;
}