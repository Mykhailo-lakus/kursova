import requests
from bs4 import BeautifulSoup
from telegram import Update
from telegram.ext import Updater, CommandHandler, CallbackContext
from os import environ
import logging

FORMAT = '%(asctime)-15s %(name)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logging.basicConfig(level=logging.ERROR, format=FORMAT)
logger = logging.getLogger()

# Функція для парсингу сайту
def get_random_fact():
    url = 'https://www.randomfunfacts.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    # Виведемо HTML-код для перевірки (тимчасово)
    # print(soup.prettify())
    
    # Знайдемо елемент, який містить факт
    fact_div = soup.find('i')  # Вибираємо елемент 'i' (курсивний текст) де містяться факти
    
    # Додамо обробку випадку, коли елемент не знайдено
    if not fact_div:
        return "Не вдалося знайти випадковий факт на сайті."
    
    fact = fact_div.get_text(strip=True)
    return fact

# Функція для команди /randomfact
def random_fact(update: Update, context: CallbackContext) -> None:
    fact = get_random_fact()
    update.message.reply_text(f'Random fact: {fact}')

# Функція для команди /start
def start(update: Update, context: CallbackContext) -> None:

    update.message.reply_text('Hello, I am a bot that provides random facts. Use /randomfact to get a fact.')

def main():
    # Ваш токен Telegram-бота
    token =environ.get("MY_TG_BOT_TOKEN","define me")
    updater = Updater(token, use_context=True)
    dispatcher = updater.dispatcher

    dispatcher.add_handler(CommandHandler("start", start))
    dispatcher.add_handler(CommandHandler("randomfact", random_fact))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()

