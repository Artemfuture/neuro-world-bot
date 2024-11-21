import requests
import json
import time


yandex_cloud_catalog = "cloud"
yandex_gpt_api_key = "key"
yandex_gpt_model = "yandexgpt-lite"


def send_gpt_question(question: str):
    yandex_gpt_model = "yandexgpt"
    body = {
        "modelUri": f"gpt://{yandex_cloud_catalog}/{yandex_gpt_model}",
        "completionOptions": {"stream": False, "temperature": 0, "maxTokens": "2000"},
        "messages": [
            {"role": "user", "text": question},
        ],
    }
    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/completionAsync"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Api-Key {yandex_gpt_api_key}",
        "x-folder-id": yandex_cloud_catalog,
    }
    response = requests.post(url, headers=headers, json=body)
    response_json = json.loads(response.text)
    operation_id = response_json["id"]

    url = f"https://llm.api.cloud.yandex.net/operations/{operation_id}"
    headers = {"Authorization": f"Api-Key {yandex_gpt_api_key}"}

    done = False
    while not done:
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
        done = response_json["done"]
        time.sleep(0.5)

    if response.status_code != 200:
        return "Ошибка, попробуй ещё раз"

    answer = response_json["response"]["alternatives"][0]["message"]["text"]
    if len(answer) == 0:
        return "Ошибка, попробуй ещё раз"
    return answer
