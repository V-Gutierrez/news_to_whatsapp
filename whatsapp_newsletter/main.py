from dotenv import dotenv_values
from send_news import send_news


config = dotenv_values(".env")
target = config['TARGET']
api_key = config['API_KEY']


send_news(
    'https://web.whatsapp.com/send?phone={target}',
    api_key,
    'pt',
    'br',
    'general',
)
