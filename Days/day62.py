"""Servidor Web"""

import flask as fl

app = fl.Flask(__name__)


@app.route("/")
def home():
    return "Olá, este é um servidor web Flask!"


@app.route("/sobre")
def sobre():
    return "Este é um exemplo de servidor com Flask."


if __name__ == "__main__":
    app.run(debug=True)
