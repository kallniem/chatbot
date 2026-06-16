import whisper
import sounddevice as sd
from scipy.io.wavfile import write
import threading

print("🔄️ Load Whisper model", end="\r")
model = whisper.load_model("large-v3", download_root="models/whisper")
print("✅ Load Whisper model")


def record_until_enter(filename="audio.wav", samplerate=16000):
    print("🎤 Recording... Press Enter to stop.")

    stop_event = threading.Event()
    audio_chunks = []

    def callback(indata, frames, time, status):
        if status:
            print(status)
        audio_chunks.append(indata.copy())

    with sd.InputStream(
        samplerate=samplerate,
        channels=1,
        dtype="int16",
        callback=callback,
    ):
        input()  # Wait for Enter
        stop_event.set()

    import numpy as np

    audio = np.concatenate(audio_chunks, axis=0)
    write(filename, samplerate, audio)

    print(f"💾 Saved to {filename}")
    return filename


def transcribe(audio_file_path, language="fi"):
    result = model.transcribe(
        audio_file_path,
        language=language,
        fp16=True,
    )
    return result["text"]


if __name__ == "__main__":
    audio_file = record_until_enter()
    text = transcribe(audio_file, language="fi")
    print("\n📝 Transcription:")
    print(text)