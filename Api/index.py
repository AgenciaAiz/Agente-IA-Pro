# api/index.py (versión de prueba temporal)
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def hello_vercel():
    return jsonify({"message": "¡Hola desde Vercel con Flask!"})

@app.route('/test')
def test_route():
    return "Esta es una ruta de prueba."
