# Root app.py (Sirf Hugging Face ke liye)
import os
import asyncio
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({"status": "Online", "message": "EcoAI Ready"}), 200

@app.route('/reset', methods=['POST'])
def reset():
    # Phase 1 ka bot ye ping karta hai
    return jsonify({"status": "ok"}), 200

def run_flask():
    # Hugging Face default port 7860 leta hai
    port = int(os.environ.get("PORT", 7860))
    app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)

if __name__ == "__main__":
    run_flask()
