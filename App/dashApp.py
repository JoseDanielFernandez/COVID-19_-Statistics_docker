import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
import mysql.connector
import pymysql
import matplotlib.pyplot as plt

external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

app = dash.Dash(__name__, external_stylesheets=external_stylesheets)

connection = pymysql.connect(host='30.10.0.1', port=3306, user='root', password='root', database='covid')
cursor = connection.cursor(pymysql.cursors.DictCursor)

query = "SELECT casos_confirmados, fallecidos, recuperados FROM `casos` WHERE region LIKE 'Capital District'"

cursor.execute(query)
for i in cursor:
    confirmados = i['casos_confirmados']
    fallecidos = i['fallecidos']
    recuperados = i['recuperados']

cursor = connection.cursor(pymysql.cursors.DictCursor)
query2 = "SELECT casos_confirmados, fallecidos, recuperados FROM `casos` WHERE region LIKE 'Antioquia'"

cursor.execute(query2)
for i in cursor:
    confirmados2 = i['casos_confirmados']
    fallecidos2 = i['fallecidos']
    recuperados2 = i['recuperados']

cursor = connection.cursor(pymysql.cursors.DictCursor)
query3 = "SELECT casos_confirmados, fallecidos, recuperados FROM `casos` WHERE region LIKE 'Valle del Cauca'"

cursor.execute(query3)
for i in cursor:
    confirmados3 = i['casos_confirmados']
    fallecidos3 = i['fallecidos']
    recuperados3 = i['recuperados']

df = pd.DataFrame({
    "Ciudad": ["Bogotá DC", "Antioquia", "Valle del Cauca", "Bogotá DC", "Antioquia", "Valle del Cauca", "Bogotá DC", "Antioquia", "Valle del Cauca"],
    "Número de contagiados": [confirmados, confirmados2, confirmados3, fallecidos, fallecidos2, fallecidos3, recuperados, recuperados2, recuperados3],
    "Tipo": ["Confirmados", "Confirmados", "Confirmados", "Fallecidos", "Fallecidos", "Fallecidos","Recuperados","Recuperados","Recuperados"]
})

cursor = connection.cursor(pymysql.cursors.DictCursor)
query4 = "SELECT SUM(casos_confirmados), SUM(fallecidos), SUM(recuperados) FROM `casos`"

cursor.execute(query4)
for i in cursor:
    confirmados4 = i['SUM(casos_confirmados)']
    fallecidos4 = i['SUM(fallecidos)']
    recuperados4 = i['SUM(recuperados)']

df2 = pd.DataFrame({
    "País": ["Colombia", "Colombia", "Colombia"],
    "Número de contagiados": [confirmados4, fallecidos4, recuperados4],
    "Tipo": ["Confirmados", "Fallecidos", "Recuperados"]
})



#df = pd.DataFrame({
#    "Fruit": ["Apples", "Oranges", "Bananas", "Apples", "Oranges", "Bananas"],
#    "Amount": [4, 1, 2, 2, 4, 5],
#    "City": ["SF", "SF", "SF", "Montreal", "Montreal", "Montreal"]
#})*/

fig = px.bar(df, x="Ciudad", y="Número de contagiados", color="Tipo", barmode="group")
fig2 = px.bar(df2, x="País", y="Número de contagiados", color="Tipo", barmode="group")


app.layout = html.Div(children=[
    html.H1(children='Estadísticas de casos de COVID-19 en Colombia'),

    html.Div(children='''
        A continuación se mostrarán las estadísticas del contagio por COVID-19 en las 3 ciudades en las que hay más contagio:
    '''),

    dcc.Graph(
        id='example-graph',
        figure=fig
    ),

    html.Div(children='''
        Ahora, podrá bservar las estadísticas del contagio por COVID-19 en toda Colombia:
    '''),

    dcc.Graph(
        id='example-graph2',
        figure=fig2
    )
])



if __name__ == '__main__':
  app.run_server(host='0.0.0.0', port=8080, debug=True)
