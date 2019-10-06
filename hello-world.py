import dash
from dash_html_components import H1

app = dash.Dash(__name__)
app.title = "Hola Uma"

app.layout = H1("Hola amigos de la UMA!")

app.server.run(debug=True)
