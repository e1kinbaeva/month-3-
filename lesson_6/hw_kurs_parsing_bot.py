from aiogram import Bot, Dispatcher, types, executor
from logging import basicConfig, INFO
from bs4 import BeautifulSoup
from config import token
import requests
import asyncio

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)


async def scheduled(wait_for):
    while True:
        await asyncio.sleep(wait_for)
        await check_exchange_rates()



async def check_exchange_rates():
    url = "https://www.nbkr.kg/index.jsp?lang=RUS"
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    titles = soup.find_all('td', class_='excurr')
    prices = soup.find_all('td', class_='exrate')
    date = soup.find_all('span', class_='gold-date')
    
    for date in date:
        today = date.text
    
    message_text = f"Актуальный курс {today}: \n"
    
    for title, price in zip(titles, prices):
        true_price = "".join(price.text.split())
        message_text += f"{title.text}- {true_price}\n"
    
    await bot.send_message(chat_id='766589023', text=message_text)


@dp.message_handler(commands='start')
async def start(message: types.Message):
    await message.answer("Добро пожаловать на Официальный курс валют ")
    await message.answer("Чтобы узнать актуальный курс валют нажмите следующую команду \n /course")


@dp.message_handler(commands='course')
async def course(message: types.Message):
    await check_exchange_rates()


loop = asyncio.get_event_loop()
loop.create_task(scheduled(60))
executor.start_polling(dp, skip_updates=True)

