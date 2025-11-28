import requests
import json

def check_website_status(url):
    try:
        responce = requests.get(url,timeout=10)
        responce.raise_for_status()
        print(f"Сайт {url} доступен. Код статуса: {responce.status_code}")
        return True
    except requests.exceptions.RequestException as e:
        print(f"Не удалось подключиться к {url}. Ошибка {e}")
        return False

if __name__ == "__main__":
    WEBSITE_URL = ("https://httpbin.org/status/404")
    check_website_status(WEBSITE_URL)