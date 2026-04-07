import json
from env import EcoServerManager

def run_inference():
    print("[START]")
    env = EcoServerManager(task_id="high_carbon_peak")
    obs, _ = env.reset()
    # Simple Rule: High carbon intensity? Go Eco (0). Else Normal (1).
    action = 0 if obs[1] > 0.7 else 1 
    obs, reward, terminated, truncated, info = env.step(action)
    print(f"[STEP] Action: {action}, Reward: {reward}, Info: {json.dumps(info)}")
    print("[END]")

if __name__ == "__main__":
    run_inference()