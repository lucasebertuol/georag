import os
from dotenv import load_dotenv
from huggingface_hub import InferenceClient

load_dotenv()

client = InferenceClient(
    provider="cerebras",
    api_key=os.getenv("HF_TOKEN"),
)

completion = client.chat.completions.create(
    model="google/gemma-4-31B-it",
    messages=[
        {
            "role": "user",
            "content": "Responda apenas com a palavra OK."
        }
    ],
)

print(completion.choices[0].message.content)