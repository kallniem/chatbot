import openai

client = openai.OpenAI(
    base_url="http://localhost:8080/v1", # "http://<Your api-server IP>:port"
    api_key = "sk-no-key-required"
)

completion = client.completions.create(
  model="gemma-4-E4B-it-Q4_K_M",
  prompt="I believe the meaning of life is",
  max_tokens=8
)

print(completion.choices[0].text)