from gigachat import GigaChat


def gigachat(text: str) -> str:
    with GigaChat(credentials="key", verify_ssl_certs=False) as giga:
        response = giga.chat(text)
        completion = response.choices[0].message.content
        chat_response = completion
    return chat_response
