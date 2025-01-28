from openai import OpenAI

from portkey_ai import PORTKEY_GATEWAY_URL, createHeaders

LOCAL_BASE_URL = "http://localhost:8787/v1"

def test1():
    client = OpenAI(

        api_key= (''), ## replace it your Groq API key

        base_url=LOCAL_BASE_URL,

        default_headers=createHeaders(

            provider="groq"
        )

    )

    chat_complete = client.chat.completions.create(

        model="llama3-70b-8192",

        messages=[{"role": "user",

                   "content": "What's the purpose of Generative AI?"}],

    )

    print(chat_complete.choices[0].message.content)




def test2():
    from portkey_ai import Portkey

    client = Portkey(
        provider="groq",
        Authorization="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"
    )

    # Example: Send a chat completion request
    response = client.chat.completions.create(
        messages=[{"role": "user", "content": "Hello, how are you?"}],
        model="llama3-70b-8192"
    )
    print(response.choices[0].message.content)


if __name__ == '__main__.py':
    test2()