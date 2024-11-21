from datetime import datetime
import requests
import json
import time
from base64 import b64decode

indentificator = "indentificator"

def image_gpt(prompt: str):
    yandex_cloud_catalog = "catalog"
    yandex_api_key = "key"
    temperature = 0
    seed = int(round(datetime.now().timestamp()))
    body = {
        "modelUri": f"art://{yandex_cloud_catalog}/yandex-art/latest",
        "generationOptions": {"seed": seed, "temperature": temperature},
        "messages": [
            {"weight": 1, "text": prompt},
        ],
    }

    url = "https://llm.api.cloud.yandex.net/foundationModels/v1/imageGenerationAsync"
    headers = {"Authorization": f"Api-Key {yandex_api_key}"}

    response = requests.post(url, headers=headers, json=body)
    response_json = json.loads(response.text)
    print(response_json)
    operation_id = response_json["id"]
    url = f"https://llm.api.cloud.yandex.net:443/operations/{operation_id}"
    headers = {"Authorization": f"Api-Key {yandex_api_key}"}

    while True:
        response = requests.get(url, headers=headers)
        response_json = json.loads(response.text)
        done = response_json["done"]
        if done:
            break
        else:
            time.sleep(2)

    image_data = response_json["response"]["image"]
    image_data = b64decode(image_data)
    # with open("image1.jpg", "wb") as file:
    #     file.write(image_data)
    return image_data

# print(image_gpt("картинка"))