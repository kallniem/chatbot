from text_to_speech import speak
from speech_to_text import transcribe
from openai import OpenAI

client = OpenAI(
    base_url="http://localhost:8080/v1", # "http://<Your api-server IP>:port"
    api_key = "sk-no-key-required"
)

def generate_response(messages=[]):
    """
    Generate a response based on the provided messages.

    Args:
        messages (list): A list of message dictionaries containing 'role' and 'content'.

    Returns:
        list: Updated list of messages including the assistant's response.
    """
    # Example implementation (to be replaced with actual logic)
    response = ""

    stream = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages,
        stream=True
        )
    
    for event in stream:
        if event.choices[0].delta.content is not None:
            print(event.choices[0].delta.content, end='', flush=True)
            response += event.choices[0].delta.content
    
    if not response.endswith('\n'):
        print("")

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
        text = transcribe(chat["message"]["content"])

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
        print("Assistant:", end=' ', flush=True)
        history = send_message(chat)
        speak(history[-1]['content'])