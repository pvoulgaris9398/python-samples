import logging

import dash_ag_grid as dag
import pandas as pd
import plotly.express as px
from dash import Dash, Input, Output, callback, dcc, html

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder2007.csv"
)

# Initialize the app - incorporate css
external_stylesheets = ["https://codepen.io/chriddyp/pen/bWLwgP.css"]

# app = Dash()
app = Dash(name=__name__, external_stylesheets=external_stylesheets)

app.layout = [
    html.Div(id="log-output"),
    html.Div(id="clicked-output"),
    html.Div(
        className="row",
        children="Dash Sample with Data",
        style={"textAlign": "center", "color": "blue", "fontSize": 30},
    ),
    html.Hr(),
    dcc.RadioItems(
        options=["pop", "lifeExp", "gdpPercap"],
        value="lifeExp",
        inline=True,
        id="controls-and-radio-item",
    ),
    dag.AgGrid(
        id="test-grid-001",
        dashGridOptions={"filter": True},
        rowData=df.to_dict("records"),
        columnDefs=[
            {
                "headerName": i,
                "field": i,
                "id": i,
                "headerComponent": "HeaderClickable",
                "headerComponentParams": {"enableCallback": True},
            }
            for i in df.columns
        ],
    ),
    # dcc.Graph(figure=px.histogram(df, x="continent", y="lifeExp", histfunc="avg")),
    dcc.Graph(figure={}, id="controls-and-graph"),
]


"""
analagous to your databinding in WPF/xaml world
we know the column_chosen field (or "value" property on the RadioItems control)
is the column name (because we set it up that way here)

in effect, binds "value" property of component named "controls-and-radio-item" with the
"figure" property of the component named "controls-and-graph"

"""


@callback(
    Output(component_id="controls-and-graph", component_property="figure"),
    Input(component_id="controls-and-radio-item", component_property="value"),
)
def update_graph(column_chosen):
    logger.info(f"update_graph: {column_chosen}")
    fig = px.histogram(df, x="continent", y=column_chosen, histfunc="avg")
    return fig


@callback(
    Output("clicked-output", "children"), Input("test-grid-001", "virtualRowData")
)
def display_header_click(clicked_column):
    print("Clicked!!!")
    if clicked_column:
        return f"Header Clicked: {clicked_column}"
    return "Click a header"


if __name__ == "__main__":
    app.run(debug=True)
