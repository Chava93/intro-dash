import dash
import dash_html_components as html

app = dash.Dash(__name__)
app.title = "UMA Finance"

app.layout = html.Div([
    html.H1("Información financiera al instante"),
    html.P("""
    En esta aplicación creada por actuarios de la UMA podrás consultar información financiera
    directo de Yahoo Finance y visualizarla al instante.
    """)
])

app.server.run(debug=True)
