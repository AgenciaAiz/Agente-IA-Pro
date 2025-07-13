# api/index.py
from flask import Flask, jsonify
from api.chatbot import chatbot_bp # Importa el blueprint desde chatbot.py

# Crea la instancia principal de la aplicación Flask
app = Flask(__name__) # ¡Esta línea es CRÍTICA y la variable debe llamarse 'app'!
app.register_blueprint(chatbot_bp)

# Añade una ruta raíz simple para probar si la app funciona.
# Si tu navegador accede a 'agente-ia-pro.vercel.app/', esta ruta debería responder.
@app.route('/')
def home():
    return jsonify({"message": "Bienvenido al Chatbot de AIZ Agencia! API funcionando."})

# Asegúrate de NO tener un if __name__ == '__main__': app.run(debug=True) aquí.
# Vercel maneja la ejecución, no se necesita esta parte en producción.
