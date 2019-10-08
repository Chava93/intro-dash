import dash
import dash_html_components as html
import dash_core_components as dcc
import plotly.graph_objects as go

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
    html.H1("Información financiera al instante"),
    html.P("""
    En esta aplicación creada por actuarios de la UMA podrás consultar información financiera
    directo de Yahoo Finance y visualizarla al instante.
    """),
    html.Label("Escribe tu consulta:"),
    html.Br(),
    dcc.Input(id="security"),
    html.Br(),
    dcc.Graph(figure=fig, id="plot_security")
])

app.server.run(debug=True)
