# From: https://github.com/PacktPublishing/Python-for-Algorithmic-Trading-Cookbook

import datetime

import dash
import dash_bootstrap_components as dbc

# import numpy as np
# import pandas as pdim
import plotly.graph_objs as go

# import plotly.io as pio
from dash import dcc, html
from dash.dependencies import Input, Output
from openbb import obb
from sklearn.decomposition import PCA

obb.user.preferences.output_type = "dataframe"

# Initialize the Dash app with bootstrap styling

app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# UI components for ticker input
ticker_field = [
    html.Label("Enter Ticker Symbols:"),
    dcc.Input(
        id="ticker-input",
        type="text",
        placeholder="Enter Tickers separated by commas (e.g., APPL,MSFT)",
        style={"width": "50%"},
    ),
]

# UI components for selecting number of PCA components
components_field = [
    html.Label("Select Number of Components:"),
    dcc.Dropdown(
        id="component-dropdown",
        options=[{"label": i, "value": i} for i in range(1, 6)],
        value=3,
        style={"width": "50%"},
    ),
]

# UI components for date range picker
date_picker_field = [
    html.Label("Select Date Range"),
    dcc.DatePickerRange(
        id="date-picker",
        start_date=datetime.datetime.now() - datetime.timedelta(365 * 3),
        end_date=datetime.datetime.now(),
        display_format="YYYY-MM-DD",
    ),
]

submit = [html.Button("Submit", id="submit-button")]

# Define the app layout
app.layout = dbc.Container(
    [
        html.H1("PCA on Stock Returns"),
        # Ticker input
        dbc.Row([dbc.Col(ticker_field)]),
        dbc.Row([dbc.Col(components_field)]),
        dbc.Row([dbc.Col(date_picker_field)]),
        dbc.Row([dbc.Col(submit)]),
        # Charts
        dbc.Row(
            [
                dbc.Col([dcc.Graph(id="bar-chart")], width=4),
                dbc.Col([dcc.Graph(id="line-chart")], width=4),
                dbc.Col([dcc.Graph(id="scatter-plot")], width=4),
            ]
        ),
    ]
)


@app.callback(
    [
        Output("bar-chart", "figure"),
        Output("line-chart", "figure"),
        Output("scatter-plot", "figure"),
    ],
    [Input("submit-button", "n_clicks")],
    [
        dash.dependencies.State("ticker-input", "value"),
        dash.dependencies.State("component-dropdown", "value"),
        dash.dependencies.State("date-picker", "start_date"),
        dash.dependencies.State("date-picker", "end_date"),
    ],
)
def update_graphs(n_clicks, tickers, n_components, start_date, end_date):
    """
    Update the graphs based on user input.

    Parameters
    ----------
    n_clicks : int
        Number of times the submit button has been clicked.
    tickers : str
        Comma-separated list of ticker symbols.
    n_components : int
        Number of principal components to compute.
    start_date : str
        Start date for the historical data in YYYY-MM-DD format.
    end_date : str
        End date for the historical data in YYYY-MM-DD format.

    Returns
    -------
    tuple
        A tuple containing three Plotly figures for the bar chart, line chart, and scatter plot.
    """
    if not tickers:
        return {}, {}, {}

    tickers = tickers.split(",")

    # Convert date strings, as needed
    start_date = datetime.datetime.strptime(start_date, "%Y-%m-%dT%H:%M:%S.%f").date()
    end_date = datetime.datetime.strptime(end_date, "%Y-%m-%dT%H:%M:%S.%f").date()

    # Download historical stock data
    data = obb.equity.price.historical(
        tickers, start_date=start_date, end_date=end_date, provider="yfinance"
    ).pivot(columns="symbol", values="close")

    # Calculate daily returns
    daily_returns = data.pct_change().dropna()

    # Apply PCA to daily returns
    pca = PCA(n_components=n_components)
    pca.fit(daily_returns)

    explained_var_ratio = pca.explained_variance_ratio_

    # Create a bar chart for individual explained variance
    bar_chart = go.Figure(
        data=[
            go.Bar(
                x=["PC" + str(i + 1) for i in range(n_components)],
                y=explained_var_ratio,
            )
        ],
        layout=go.Layout(
            title="Explained Variance by Component",
            xaxis=dict(title="Principal Component"),
            yaxis=dict(title="Explained Variance"),
        ),
    )

    return bar_chart, {}, {}


if __name__ == "__main__":
    # Run the Dash app
    app.run(debug=True)
