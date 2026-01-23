import requests
import piper_test

openai_compatible_api = "http://a1yvl114:8080/v1/chat/completions"

def speech_to_text(audio_file_path):
    """
    Send a message using speech-to-text conversion.
    Args:
        audio_file_path (str): The path to the audio file.
    Returns:
        str: The transcribed text from the audio file.
    """
    # Example implementation (to be replaced with actual logic)
    transcribed_text = "This is the transcribed text from the audio file."
    return transcribed_text

def generate_response(messages=[]):
    """
    Generate a response based on the provided messages.

    Args:
        messages (list): A list of message dictionaries containing 'role' and 'content'.

    Returns:
        list: Updated list of messages including the assistant's response.
    """
    # Example implementation (to be replaced with actual logic)
    response = "This is a generated response based on the provided messages."
    r = requests.post(
        url=openai_compatible_api,
        json={
            "model": "gpt-3.5-turbo",
            "messages": messages
        }
    )
    response = r.json()['choices'][0]['message']['content']
    new_messages = messages + [{"role": "assistant", "content": response}]
    
    return new_messages

def send_message(chat = {"message": {}, "history": []}):
    """
    Send a message and receive a response.

    Args:
        chat (dict): A dictionary containing 'message' and 'history' keys.
    Returns:
        list: Updated list of messages including the assistant's response.
    """

    text = chat["message"]["content"]

    if chat["message"]["type"] == "text":
        text = chat["message"]["content"]
    elif chat["message"]["type"] == "audio":
        text = speech_to_text(chat["message"]["content"])

    new_messages = chat["history"] + [{"role": "user", "content": text}]
    response = generate_response(messages=new_messages)
    return response

if __name__ == "__main__":
    history = []
    while True:
        user_input = input("You: ")
        chat = {
            "message": {
                "type": "text",
                "content": user_input
            },
            "history": history
        }
        history = send_message(chat)
        piper_test.speak(history[-1]['content'])
        print("Assistant:", history[-1]['content'])