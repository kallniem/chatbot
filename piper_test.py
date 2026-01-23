import wave
from piper import PiperVoice
import simpleaudio as sa

def speak(text: str):
    voice = PiperVoice.load("models/voice/fi_FI-harri-medium.onnx")
    with wave.open("test.wav", "wb") as wav_file:
        voice.synthesize_wav(text, wav_file)

    wave_obj = sa.WaveObject.from_wave_file("test.wav")
    play_obj = wave_obj.play()
    play_obj.wait_done()  # blocks until finished