from piper import PiperVoice
from sounddevice import OutputStream

print("🔄️ Load Piper model", end="\r")
voice = PiperVoice.load("models/voice/fi_FI-harri-medium.onnx")
print("✅ Load Piper model")
sample_rate = voice.config.sample_rate

def speak(text: str):
    with OutputStream(samplerate=sample_rate, channels=1) as stream:
        for chunk in PiperVoice.synthesize(voice, text):
            stream.write(chunk.audio_float_array)


if __name__ == "__main__":
    while True:
        user_input = input("Enter text to speak (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        speak(user_input)