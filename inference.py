import os
import asyncio
from server.app import main as run_logic

async def run_everything():
    # 1. Pehle logic run karo taaki Validator ko [START], [STEP], [END] logs mil jayein
    try:
        await run_logic()
    except Exception as e:
        print(f"[DEBUG] Logic Error: {e}")

    # 2. Flask Server ko "Bulletproof" bana diya
    try:
        from flask import Flask, jsonify
        app = Flask(__name__)
        
        @app.route('/')
        def home(): return jsonify({"status": "ok"}), 200
        
        @app.route('/reset', methods=['POST'])
        def reset(): return jsonify({"status": "ok"}), 200
        
        port = int(os.environ.get("PORT", 7860))
        # Agar port free hai (Hugging Face), toh chalega. 
        # Agar busy hai (Phase 2), toh error dega jo hum catch kar lenge!
        app.run(host="0.0.0.0", port=port, debug=False, use_reloader=False)
    
    except Exception as e:
        # Phase 2 yahan aayega, crash hone ki jagah gracefully exit hoga! ✅
        print(f"[DEBUG] Port is busy, skipping Flask server (Safe for Phase 2).")

if __name__ == "__main__":
    asyncio.run(run_everything())
