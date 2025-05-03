from wake_word import listen_for_wake_word
from speech_to_text import transcribe
from intent_recognition import get_intent
from text_to_speech import speak
from home_assistant_api import ha_call

while True:
    listen_for_wake_word()
    command = transcribe()
    intent, slots = get_intent(command)

    if intent == "turn_on_light":
        ha_call("light/turn_on", f"light.{slots['location']}")
        speak(f"Turning on {slots['location']} lights.")
    elif intent == "set_reminder":
        speak(f"Reminder set to {slots['task']} at {slots['time']}")
