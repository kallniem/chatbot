from piper import PiperVoice
import sounddevice as sd

voice = PiperVoice.load("models/voice/fi_FI-harri-medium.onnx")
sample_rate = voice.config.sample_rate

def speak(text: str):
    with sd.OutputStream(samplerate=sample_rate, channels=1) as stream:
        for chunk in PiperVoice.synthesize(voice, text):
            stream.write(chunk.audio_float_array)


if __name__ == "__main__":
    while True:
        user_input = input("Enter text to speak (or 'exit' to quit): ")
        if user_input.lower() == 'exit':
            break
        speak(user_input)