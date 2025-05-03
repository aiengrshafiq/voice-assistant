import pyaudio

pa = pyaudio.PyAudio()

print("PyAudio Device List (explicit indices):")
for i in range(pa.get_device_count()):
    device = pa.get_device_info_by_index(i)
    print(f"Index {i}: {device['name']} - Input Channels: {device['maxInputChannels']} - Output Channels: {device['maxOutputChannels']}")
