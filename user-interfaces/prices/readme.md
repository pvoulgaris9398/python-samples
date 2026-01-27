# Prices Sample

- This is a sample modular Python GUI app using `PyQt` and showing security prices from \
  [Alpha Vantage](https://www.alphavantage.co/documentation/)
- It requires a `.env` file with the following settings:

```bash
DBSERVER=*****
DBNAME=*****
DBPORT=*****
DEVUSERNAME=*****
DEVUSERPASSWORD=***** # user password for user set in `DEVUSERNAME`
ALPHA_VANTAGE_API_KEY=*****
```

## To Do:

### Rows

- Enable handling logic for each row/cell to allow for per-row and per-cell customization of display

### Filtering

- Add capability to filter by at least one column, `Symbol` perhaps

### Headers

- Implement code to map field names to header display text
- Provide way to format the header (evaluate if its possible)
- Provide way to handle click event on a header to enable sorting by that column

## Running the App:

- Run `python ./user-interfaces/prices/prices_module.py`

## Downloading Prices

- Run `python ./user-interfaces/prices/alphavantage.py AAPL` for example to download prices for `APPL`
- Note the free version of the API only provides the last 100 records, but it's enough for a sample demo
