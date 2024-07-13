import requests

from config import settings


def send_tg_message(chat_id, message):
    """Функция отправки уведомления в телеграмм"""
    params = {
        "chat_id": chat_id,
        "text": message,
    }
    requests.get(f'{settings.TG_URL}{settings.TG_BOT_TOKEN}/sendMessage', params=params)
