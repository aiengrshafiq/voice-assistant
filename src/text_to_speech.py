import subprocess

def speak(text):
    cmd = ['piper', '--model', '../models/piper-en_US-lessac-medium.onnx', '--output_file', 'out.wav']
    subprocess.run(cmd, input=text.encode('utf-8'))
    subprocess.run(['aplay', 'out.wav'])
