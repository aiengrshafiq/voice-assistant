import pvporcupine
import pyaudio
import struct
from pathlib import Path
from dotenv import load_dotenv
import os

env_path = Path(__file__).resolve().parent.parent / 'config' / '.env'
load_dotenv(dotenv_path=env_path)

access_key = os.getenv("PORCUPINE_ACCESS_KEY")
print("Access Key Loaded:", access_key)

porcupine = pvporcupine.create(
    access_key=access_key,
    keyword_paths=[os.path.join(os.path.dirname(__file__), "../models/porcupine/jarvis_raspberry-pi.ppn")]
)

pa = pyaudio.PyAudio()

# Use ALSA default (which now resamples from hw:2,0 via .asoundrc)
stream = pa.open(
    rate=16000,
    channels=1,
    format=pyaudio.paInt16,
    input=True,
    input_device_index=None,
    frames_per_buffer=porcupine.frame_length
)

def listen_for_wake_word():
    print("Listening for 'Hello Jarvis'...")
    while True:
        pcm = stream.read(porcupine.frame_length, exception_on_overflow=False)
        pcm = struct.unpack_from("h" * porcupine.frame_length, pcm)
        if porcupine.process(pcm) >= 0:
            print("Wake word detected!")
            return
