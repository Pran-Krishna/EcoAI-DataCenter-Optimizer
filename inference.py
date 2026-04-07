import json
import os
import threading
from flask import Flask, request, jsonify
from env import EcoServerManager

app = Flask(__name__)

# Route 1: Main Home (GET and POST)
@app.route('/', methods=['GET', 'POST'])
def home():
    return jsonify({"status": "ok", "message": "EcoAI Ready"}), 200

# Route 2: Specific Reset for Scaler Bot
@app.route('/reset', methods=['POST'])
def reset():
    return jsonify({"status": "ok"}), 200

# Route 3: Health Check
@app.route('/health', methods=['GET'])
def health():
    return jsonify({"status": "healthy"}), 200

def run_meta_logic():
    print("[START]")
    try:
        # Task ID verify karo ki yahi hai na?
        env = EcoServerManager(task_id="high_carbon_peak")
        obs, _ = env.reset()
        action = 0 if obs[1] > 0.7 else 1 
        obs, reward, terminated, truncated, info = env.step(action)
        print(f"[STEP] Action: {action}, Reward: {reward}, Info: {json.dumps(info)}")
    except Exception as e:
        print(f"Logic Error: {e}")
    print("[END]")

if __name__ == "__main__":
    threading.Thread(target=run_meta_logic).start()
    # Hugging Face default port
    app.run(host="0.0.0.0", port=7860)
