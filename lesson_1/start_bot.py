from aiogram import Bot, Dispatcher, types, executor
from config import token

bot = Bot(token=token)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def start(message:types.Message):
    await message.answer("Hello")


@dp.message_handler(commands='help')
async def start(message:types.Message):
    await message.answer('How can I help you?')

@dp.message_handler(text = "Hello")
async def start(message:types.Message):
    await message.reply('Hello, how are you?')

@dp.message_handler(commands= 'test')
async def start(message:types.Message):
    await message.answer_location(0, 0)
    await message.answer_photo("https://planetofhotels.com/guide/sites/default/files/styles/paragraph__live_banner__lb_image__1880bp/public/live_banner/Prophet-Mosqu--in-Medina.jpg")
    await message.answer_dice()


executor.start_polling(dp)
