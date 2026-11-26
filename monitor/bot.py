import os
import requests # для https запросов
from dotenv import load_dotenv # для загрузки скрытого токена (чтобы не украли пхХППХ)
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent
loadenv = (BASE_DIR / ".env")

load_dotenv(loadenv)

def send(text):
    token = os.getenv("TELEGRAM_TOKEN")
    chatid = os.getenv("TELEGRAM_CHAT_ID")
    url = f"https://api.telegram.org/bot{token}/sendMessage"
    requests.post(url, data={"chat_id": chatid, "text": text})

if __name__ == "__main__":
    send("Сдарова")

