# dash in 20 minutes
# hello world

from dash import Dash, html

app = Dash()

app.layout = [html.Div(children='Hello World')]
# app components provided as a list... can also be a dash component

if __name__ == '__main__':
    app.run(debug=True)
