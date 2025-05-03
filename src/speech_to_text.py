import vosk
import pyaudio
import json
from pathlib import Path

# Always resolve absolute path
MODEL_PATH = Path(__file__).resolve().parent.parent / "models" / "vosk-model-small-en-us-0.15"
model = vosk.Model(str(MODEL_PATH))

rec = vosk.KaldiRecognizer(model, 16000)
pa = pyaudio.PyAudio()

def transcribe():
    stream = pa.open(rate=16000, channels=1, format=pyaudio.paInt16, input=True, frames_per_buffer=8000)
    print("Listening command...")
    while True:
        data = stream.read(4000, exception_on_overflow=False)
        if rec.AcceptWaveform(data):
            result = json.loads(rec.Result())
            return result['text']
