
# api/index.py
from flask import Flask, jsonify
from api.chatbot import chatbot_bp # Assuming chatbot.py is in 'api'

app = Flask(__name__)
app.register_blueprint(chatbot_bp)

# Add a simple root route for testing if you don't have one
@app.route('/')
def home():
    return jsonify({"message": "API is working!"})
