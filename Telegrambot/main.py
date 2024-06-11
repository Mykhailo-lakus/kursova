import requests
from bs4 import BeautifulSoup
from os import environ
import logging
import telethon
from telethon import TelegramClient, events

FORMAT = '%(asctime)-15s %(name)s %(levelname)s: %(message)s'
logging.basicConfig(level=logging.INFO, format=FORMAT)
logging.basicConfig(level=logging.ERROR, format=FORMAT)
logger = logging.getLogger()

api_id = 24223475

api_hash = '0f0c353cd431fa23d2e983cb792add8e'

bot_token = environ.get("MY_TG_BOT_TOKEN","define me")

client = TelegramClient('theker', api_id, api_hash).start(bot_token=bot_token)


@client.on(events.NewMessage(pattern='/start'))
async def start_command(event):
    await client.send_message(event.sender_id, 'Hello, I am a bot that provides random facts. Use /randomfact to get a fact.')

@client.on(events.NewMessage(pattern='/randomfact'))
async def fact_command(event):
    text = get_random_fact()
    print(text)
    await client.send_message(event.sender_id, text)

def get_random_fact():
    url = 'https://www.randomfunfacts.com/'
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    fact_div = soup.find('i')
    
    if not fact_div:
        return "Не вдалося знайти випадковий факт на сайті."
    
    fact = fact_div.get_text(strip=True)
    return fact


client.start()
client.run_until_disconnected()

