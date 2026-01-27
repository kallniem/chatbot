import whisper

print("🔄️ Load Whisper model", end="\r")
model = whisper.load_model("turbo", download_root="models/whisper")
print("✅ Load Whisper model")

def transcribe(audio_file_path):
    """
    Send a message using speech-to-text conversion.
    Args:
        audio_file_path (str): The path to the audio file.
    Returns:
        str: The transcribed text from the audio file.
    """
    # Example implementation (to be replaced with actual logic)
    transcribed_text = model.transcribe(audio_file_path, language="fi", fp16=False)
    return transcribed_text

if __name__ == "__main__":
    result = model.transcribe("audio.wav", language="fi", fp16=False)
    print(result["text"])