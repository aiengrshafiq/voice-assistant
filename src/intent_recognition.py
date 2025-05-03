import os
import json
from openai import OpenAI
from dotenv import load_dotenv
from pathlib import Path
env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(dotenv_path=env_path)

OPENAI_API_KEY = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=OPENAI_API_KEY)
import re

def detect_intent(user_input):
    prompt = f"""
You are a smart home assistant. Extract the intent and parameters from this command:

"{user_input}"

Respond ONLY in this JSON format (no explanation):
{{
  "intent": "intent_name",
  "parameters": {{
    "key1": "value1",
    "key2": "value2"
  }}
}}

Valid intents: turn_on_light, turn_off_light, set_thermostat, turn_on_plug, turn_off_plug, set_reminder
"""

    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful home assistant."},
                {"role": "user", "content": prompt}
            ]
        )

        result = response.choices[0].message.content.strip()
        print("[GPT Raw Output]", result)

        # Extract JSON block safely
        match = re.search(r'{[\s\S]*}', result)
        if match:
            parsed = json.loads(match.group(0))
            return parsed.get("intent"), parsed.get("parameters")
        else:
            print("[Intent Error] Could not extract JSON")
            return None, None

    except Exception as e:
        print("[Intent Error]", str(e))
        return None, None