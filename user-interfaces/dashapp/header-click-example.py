import dash
import dash_ag_grid as dag
import dash_mantine_components as dmc
from dash import Dash, Input, Output, State, dcc, html

app = Dash()

columnDefs = [{"headerName": "A", "field": "a"}, {"headerName": "B", "field": "b"}]

rowData = [{"a": 1, "b": 2}, {"a": 3, "b": 4}]


app.layout = dmc.MantineProvider(
    [
        dcc.Store(id="store-button"),
        dag.AgGrid(
            id="column-definition-ID",
            rowData=rowData,
            dashGridOptions={
                "sortable": False,
                "filter": False,
            },
            columnDefs=[
                {
                    "field": "a",
                    "headerName": "Column Name A",
                    "headerComponent": "ButtonHeader",
                    "headerComponentParams": {
                        "id": "button-header-a",
                        "className": "custom-button-class",
                    },
                },
                {
                    "field": "b",
                    "headerName": "Column Name B",
                    "headerComponent": "ButtonHeader",
                    "headerComponentParams": {
                        "id": "button-header-b",
                        "className": "custom-button-class",
                    },
                    "style": {
                        "backgroundColor": "transparent",
                        "border": "none",
                        "cursor": "pointer",
                        "padding": "5px",
                    },
                },
            ],
            columnSize="sizeToFit",
        ),
        html.Div(id="container"),
        html.Div(id="color-trigger", style={"display": "none"}),
        html.Button(id="new-btn", children=["Click me to apply color"], hidden=True),
        dmc.Modal(
            id="modal-test",
            children=[
                dmc.Text("Run Process"),
                html.Button(id="new-btn-backend", children=["Apply Filters"]),
            ],
        ),
    ]
)


# Backend Button
# --> Used for coloring header column
@app.callback(
    Output("new-btn", "n_clicks"),
    Input("new-btn-backend", "n_clicks"),
    prevent_initial_calback=True,
)
def update_backend(n_clicks):
    if n_clicks:
        return n_clicks + 1

    else:
        return dash.no_update


# Perform actual change of color
app.clientside_callback(
    """
    function(n_clicks, data) {
        if (data && data.id) {
            const button = document.getElementById(data.id);
            if (button) {
                // Check current background color
                const currentBg = button.style.backgroundColor;

                // Toggle: if green, remove color; if not green, make it green
                if (currentBg === 'rgb(76, 175, 80)' || currentBg === '#4CAF50') {
                    // Reset to default (no color)
                    button.style.backgroundColor = 'transparent';
                    button.style.color = '';
                    alert("Hello!");
                } else {
                    // Make it green
                    button.style.backgroundColor = '#4CAF50';
                    button.style.color = 'white';
                }
            }
        }
        return '';
    }
    """,
    Output("color-trigger", "children"),
    Input("new-btn", "n_clicks"),
    State("store-button", "data"),
)


# Regular callback to print and display info
# --> This should open modal
@app.callback(
    Output("container", "children"),
    Output("modal-test", "opened"),
    Input("store-button", "data"),
)
def update(data):
    print(data)

    if data:
        button_id = data.get("id")
        timestamp = data.get("timestamp")

        # Print in terminal
        print(f"Button ID: {button_id}")
        print(f"Timestamp: {timestamp}")

        print("************")

        # Display in UI
        return html.Div(
            [html.P(f"Last clicked button: {button_id}"), html.P(f"Time: {timestamp}")]
        ), True
    print("---------------")

    return "No button clicked yet", False


if __name__ == "__main__":
    app.run(debug=False)
