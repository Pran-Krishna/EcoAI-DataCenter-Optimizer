import jsom
import os
import threading
from flask import Flask
from env import EcoServerManager

# 1. Flask Web Server Setup (For Hugging Face Health Check)
app = Flask(__name__)

@app.route('/')
def home():
    return "GreenMind AI is Running! [Meta x PyTorch Hackathon]"

def run_meta_logic():
    # Mandatory Log Format for Meta Validator
    print("[START]")
    env = EcoServerManager(task_id="high_carbon_peak")
    obs, _ = env.reset()
    
    # Logic
    action = 0 if obs[1] > 0.7 else 1 
    obs, reward, terminated, truncated, info = env.step(action)
    
    print(f"[STEP] Action: {action}, Reward: {reward}, Info: {json.dumps(info)}")
    print("[END]")

# 2. Main Execution
if __name__ == "__main__":
    # Logic ko alag thread mein chalao taaki Logs print ho jayein
    threading.Thread(target=run_meta_logic).start()
    
    # Flask ko Port 7860 par chalao (Hugging Face default port)
    app.run(host="0.0.0.0", port=7860)
