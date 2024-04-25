import requests
from bs4 import BeautifulSoup
from aiogram import Bot, Dispatcher, executor, types
from config import token
from datetime import datetime
import asyncio
import logging


bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

async def send_currency(message):
    while True:
        url = 'https://www.nbkr.kg/index.jsp?lang=RUS'
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'lxml')
        time = datetime.now().strftime("%d-%m-%Y %H:%M:%S")

        usd_rate = soup.find_all('td', class_='exrate')[0].text
        eur_rate = soup.find_all('td', class_='exrate')[2].text
        rub_rate = soup.find_all('td', class_='exrate')[4].text
        kzt_rate = soup.find_all('td', class_='exrate')[6].text

        await message.answer(f"Валюта {time}:\nКурс USD: {usd_rate}\nКурс EUR: {eur_rate}\nКурс RUB: {rub_rate}\n КУРС KZT:{kzt_rate}\n")
        await asyncio.sleep(60)

@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Валюта")
    asyncio.create_task(send_currency(message))

async def on_startup(dispatcher):
    pass

executor.start_polling(dp)