"""Estrutura de API RESTful"""

from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/data", methods=["GET"])
def get_data():
    data = {"id": 1, "name": "limão", "descrição": "Isso é um limão!"}
    return jsonify(data)


@app.route("/data", methods=["POST"])
def criar_data():
    novo_dado = request.get_json()
    return jsonify(novo_dado), 201


if __name__ == "__main__":
    app.run(debug=True)
