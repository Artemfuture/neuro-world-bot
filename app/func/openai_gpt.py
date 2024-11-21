from openai import OpenAI


client = OpenAI(api_key="sk-key")
OpenAI.api_key = "key"


def openai(text: str):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": f"{text}"}])

    completion = response.choices[0].message.content
    return completion
