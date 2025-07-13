# api/index.py
from flask import Flask, jsonify
from api.chatbot import chatbot_bp # Importa el blueprint desde chatbot.py

app.register_blueprint(chatbot_bp)

# Puedes añadir una ruta raíz simple para verificar que la app funciona
@app.route('/')
def home():
    return jsonify({"message": "Bienvenido al Chatbot de AIZ Agencia!"})
