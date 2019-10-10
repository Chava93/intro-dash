import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go
from dash.dependencies import Input, Output
from pandas_datareader import data
app = dash.Dash(__name__)
app.title = "UMA Finance"

fig = go.Figure(
    data= go.Scatter(x=list(range(1,10)), y=[10]*9),
    layout={
        "title":"Mis calificaciones de Cálculo actuarial",
        "xaxis":{"title":"Semestre"},
        "yaxis":{"title":"Calificación"}
    }

)

app.layout = html.Div([
    html.Section([
        html.Div([
            html.Div([
                html.H1("Información Financiera al instante.", className="title"),
                html.H2("Una aplicación diseñada por actuarios de la UMA", className="subtitle")
            ], className="container")
        ],className="hero-body" )
    ], className="hero is-info"),
    html.Br(),
    html.Div([
        html.Div([
            html.Div("""
                En esta aplicación creada por actuarios de la UMA podrás consultar información financiera
                directo de Yahoo Finance y visualizarla al instante.
                """, className="notification")
        ], className="column is-8 is-offset-2")
    ], className="container"),
    html.Div([
        html.Label("Escribe tu consulta:", className="label"),
        dcc.Input(id="security", className="input", value="aapl"),
    ], className="column is-4 is-offset-2"),
    html.Br(),
    dcc.Graph(figure=fig, id="plot_security", config={"displayModeBar": False})
], className="container main-container")

@app.callback(
    Output("plot_security", "figure"),
    [Input("security", "value")]
)
def YahooQuery(sec):
    try:
        info = data.DataReader(sec, start='2017-1-1', data_source='yahoo')
        DATA = go.Scatter(x=info.index, y=info["Adj Close"])
        layout={
            "title":f"Historico de precios para {sec}",
            "xaxis":{"title":"Fecha"},
            "yaxis":{"title":"Precio"}
        }
    except:
        DATA= go.Scatter(x=list(range(1,10)), y=[10]*9),
        layout={
            "title":f"No se encontró info para {sec}",
            "xaxis":{"title":"Semestre"},
            "yaxis":{"title":"Calificación"}
        }
    return go.Figure(data=DATA, layout=layout)

if __name__=="__main__":
    app.server.run(debug=True)
