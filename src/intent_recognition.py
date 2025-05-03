from rhasspynlu.nlu import RhasspyNLU

nlu = RhasspyNLU.from_yaml_file("../config/intents.yml")

def get_intent(text):
    intent = nlu.recognize(text)
    return intent.intent.name, intent.slots
