# api/index.py (Versión con tu chatbot)
from flask import Flask, jsonify
from api.chatbot import chatbot_bp # <-- ¡Asegúrate de esta línea para importar tu Blueprint!

app = Flask(__name__)
app.register_blueprint(chatbot_bp) # <-- ¡Asegúrate de esta línea para registrar el Blueprint!

# Puedes mantener esta ruta raíz para verificar que la app principal carga
@app.route('/')
def home():
    return jsonify({"message": "Bienvenido al Chatbot de AIZ Agencia! API funcionando."})

# NO incluyas un if __name__ == '__main__': app.run() aquí.
