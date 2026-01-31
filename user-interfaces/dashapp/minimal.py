import logging

import dash_ag_grid as dag
from dash import Dash, html  # Input, Output, callback, dcc,

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

columnDefs = [
    {"headerName": "Symbol", "field": "symbol", "filter": True},
    {"headerName": "Exchange", "field": "exchange"},
    {"headerName": "Price", "field": "price"},
    {"headerName": "Date", "field": "price_dt"},
]

rowData = [
    {"symbol": "AAPL", "exchange": "NYSE", "price": 101.455, "price_dt": "1 / 31 / 26"},
    {"symbol": "IBM", "exchange": "NYSE", "price": 202.25, "price_dt": "1 / 4 / 26"},
    {"symbol": "AZ", "exchange": "NYSE", "price": 303.33, "price_dt": "1 / 1 / 26"},
]

app = Dash()

app.layout = [
    html.Div("Minimal Sample"),
    dag.AgGrid(id="minimal-grid-001", rowData=rowData, columnDefs=columnDefs),
    html.Div(id="log-output"),
]


if __name__ == "__main__":
    app.run(debug=True)
