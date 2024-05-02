from aiogram import Bot, Dispatcher, types, executor
from config import token
import sqlite3, requests, time, logging

bot = Bot(token=token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)


start_buttons = [
    types.KeyboardButton('send contact', request_contact=True),
    types.KeyboardButton('send location', request_location=True)

]
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*start_buttons)

@dp.message_handler(commands='start')
async def start (message:types.Message):
    await message.answer(f"Привет {message.from_user.full_name}", reply_markup=start_keyboard)

@dp.message_handler(content_types=types.ContentType.CONTACT)
async def get_contact (message:types.Contact):
    # print(message)
    await message.answer(f"{message.contact.phone_number}")

@dp.message_handler(content_types=types.ContentType.LOCATION)
async def get_location (message:types.Message):
    print(message)
    await message.answer(f"Широта - {message.location.latitude} \nДолгота -  {message.location.longitude}")

executor.start_polling(dp, skip_updates=True)