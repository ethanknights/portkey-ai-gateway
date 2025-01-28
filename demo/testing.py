
from portkey_ai import Portkey

client = Portkey(
    provider="groq",
    Authorization=""
)


response = client.chat.completions.create(
    messages=[{"role": "user", "content": "Hello, how are you?"}],
    model="llama3-8b-8192"
)
print(response.choices[0].message.content)


