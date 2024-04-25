from aiogram  import Bot,Dispatcher, types, executor
from logging import basicConfig, INFO
from bs4 import BeautifulSoup
from config import token
import requests

bot = Bot(token=token)
dp = Dispatcher(bot)
basicConfig(level=INFO)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Hello \n/Acer \n /All_products")

@dp.message_handler(commands='Acer')
async def start(message:types.Message):
    await message.answer("Start parsing")
    url = "https://barmak.store/category/Acer/"
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')

    titles = soup.find_all('div', class_ = 'tp-product-tag-2')
    prices = soup.find_all('span', class_ = 'tp-product-price-2 new-price')

    for title,price in zip(titles,prices):
        true_price = "".join(price.text.split ())
        await message.answer(f"{title.text}- {true_price} \n ")
    
@dp.message_handler(commands='All_products')
async def start(message:types.Message):
    await message.answer("Start parsing")
    url = "https://barmak.store/products/"
    response = requests.get(url=url)
    soup = BeautifulSoup(response.text, 'lxml')
    
    titles = soup.find_all('div', class_ = 'tp-product-tag-2')
    prices = soup.find_all('span', class_ = 'tp-product-price-2 new-price')

    for title,price in zip(titles,prices):
        true_price = "".join(price.text.split ())
        await message.answer(f"{title.text}- {true_price} \n ")
    

executor.start_polling(dp)