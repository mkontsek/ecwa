import React, { useState } from 'react';
import TextField from '@material-ui/core/TextField';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(theme => ({
    textField: {
        position: 'absolute',
        top: 20,
        left: 20,
        background: 'white',
        zIndex: 9,
        marginLeft: theme.spacing(1),
        marginRight: theme.spacing(1),
        width: 240,
    },
}));

export function SearchBar({ defaultCountry, onSelect }) {
    const classes = useStyles();
    const [query, setQuery] = useState(defaultCountry);

    return (
        <TextField
            id="outlined-basic"
            className={classes.textField}
            value={query}
            label="Search countries by 2-letter code"
            margin="normal"
            variant="outlined"
            onKeyUp={(ev) => {
                if (ev.keyCode === 13) {
                    onSelect(query.toUpperCase())
                }
            }}
            onChange={(ev) => {
                const char = ev.target.value;
                setQuery(char)
            }}
        />
    )
}