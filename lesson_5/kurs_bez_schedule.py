from aiogram  import Bot,Dispatcher, types, executor 
from logging import basicConfig, INFO 
from bs4 import BeautifulSoup 
from config import token 
import schedule, requests, time 
 
bot = Bot(token=token) 
dp = Dispatcher(bot) 
basicConfig(level=INFO) 
 
@dp.message_handler(commands='start') 
async def start(message:types.Message): 
    await message.answer("Добро пожаловать на Официальный курс валют ") 
    await message.answer("Чтобы узнать актуальный курс валют нажмите следующую команду \n /course") 
     
@dp.message_handler(commands='course') 
async def start(message:types.Message): 
    url="https://www.nbkr.kg/index.jsp?lang=RUS" 
    response = requests.get(url=url) 
    soup = BeautifulSoup(response.text, 'lxml') 
    titles = soup.find_all('td', class_ = 'excurr')  
    prices = soup.find_all('td', class_ = 'exrate') 
    date = soup.find_all('span', class_ = 'gold-date') 
    for date in date: 
        today = date 
    await message.answer(f"Актуальный курс {today.text}: ") 
    for title,price in zip(titles,prices): 
        true_price = "".join(price.text.split ()) 
        await message.answer(f"{title.text}- {true_price}\n ") 
     
     
executor.start_polling(dp, skip_updates=True)
