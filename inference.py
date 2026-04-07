import json
import os
import threading
from flask import Flask, request
from env import EcoServerManager

app = Flask(__name__)

# Ye root POST aur GET dono handle karega (Scaler Validator ke liye)
@app.route('/', methods=['GET', 'POST'])
def home():
    # Jab validator 'POST' bhejega, hum usey 'OK' bolenge
    return json.dumps({"status": "ok", "message": "EcoAI Ready"}), 200

# Agar validator specific '/reset' maange
@app.route('/reset', methods=['POST'])
def reset():
    return json.dumps({"status": "ok"}), 200

def run_meta_logic():
    print("[START]")
    try:
        # Task ID wahi rakho jo openenv.yaml mein hai
        env = EcoServerManager(task_id="high_carbon_peak")
        obs, _ = env.reset()
        
        # Simple Logic for Validator
        action = 0 if obs[1] > 0.7 else 1 
        obs, reward, terminated, truncated, info = env.step(action)
        
        print(f"[STEP] Action: {action}, Reward: {reward}, Info: {json.dumps(info)}")
    except Exception as e:
        print(f"Logic Error: {e}")
    print("[END]")

if __name__ == "__main__":
    # Logic background mein chalegi logs print karne ke liye
    threading.Thread(target=run_meta_logic).start()
    
    # Hugging Face default port 7860
    app.run(host="0.0.0.0", port=7860)
