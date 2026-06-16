from speech_to_text import record_until_enter, transcribe
from likeness_test import find_semantic_matches
import json
quiz = json.load(open('questions.json'))

def ask_lawrence(question, transcription):
    myArray = []
    myArray.append(question)
    matches = find_semantic_matches(transcription, myArray, threshold=0.45)
    for match in matches:
        print(f"✅ Proceeding to retrieve traffic legislation for question: {match['keyword']}")
    if not matches:
        print("❌ I'm sorry, I couldn't understand your question.")

for question in quiz:
    print(f"\nQuestion:\n{question['question']}\n")
    for option in question['answers']:
        print(f"{option['key']}: {option['text']}")
    audio_file = record_until_enter()
    answer = transcribe(audio_file, language="en")
    ask_lawrence(answer, question['question'])