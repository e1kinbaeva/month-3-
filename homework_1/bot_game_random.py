from aiogram import Bot, Dispatcher, types, executor
from config import token
import random

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Добро пожаловать в игру 'Угадай число'")
    await message.answer("Для начало игры напишите команду /startgame ")

@dp.message_handler(commands='startgame')
async def start(message:types.Message):
    await message.answer("Бот: Я загадал число от 1 до 3 угадайте")

num = random.randint(1,3)   

@dp.message_handler(content_types=types.ContentType.TEXT)
async def check_number(message: types.Message):
    global num
    intnum = int(message.text)
    if intnum == num:
        await message.reply('Правильно вы отгадали')
        await message.answer_photo ("https://media.makeameme.org/created/you-win-nothing-b744e1771f.jpg")
    else: 
        await message.answer_photo("https://media.makeameme.org/created/sorry-you-lose.jpg")

executor.start_polling(dp)