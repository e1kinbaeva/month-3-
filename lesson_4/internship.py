from aiogram import Bot, Dispatcher, types, executor
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.storage import FSMContext
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from config import token
import logging, time, sqlite3

bot = Bot(token=token)
storage = MemoryStorage()
dp = Dispatcher(bot, storage=storage)
logging.basicConfig(level=logging.INFO)

connection = sqlite3.connect('intership.db')
cursor = connection.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS users(
    id INTEGER PRIMARY KEY,
    username VARCHAR(255),
    first_name VARCHAR(255),
    last_name VARCHAR(255),
    created VARCHAR(255)
);
""")
cursor.execute("""CREATE TABLE IF NOT EXISTS internship(
    id INTEGER PRIMARY KEY,
    first_name VARCHAR(100),
    last_name VARCHAR(100),
    phone INTEGER,
    age INTEGER,
    created VARCHAR(255)
);
""")

start_inline_buttons = [
    types.InlineKeyboardButton('Стажировка', callback_data='intership_callback'),
    types.InlineKeyboardButton('Наш сайт', url='https://geeks.kg'),
    types.InlineKeyboardButton('Наш инстаграм', url='https://www.instagram.com/geeks_osh/')
]
start_keyboard = types.InlineKeyboardMarkup().add(*start_inline_buttons)

class UserRegisterState(StatesGroup):
    first_name = State()
    last_name = State()
    phone = State()
    age = State()

@dp.message_handler(commands='start')
async def start(message: types.Message):
    cursor.execute(f"SELECT id FROM users WHERE id = {message.from_user.id}; ")
    result = cursor.fetchall()
    if result == []:
        cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?, ?);",
                       (message.from_user.id, message.from_user.username, message.from_user.first_name,
                        message.from_user.last_name, time.ctime()))
        cursor.connection.commit()
    await message.answer(f"{message.from_user.full_name} привет", reply_markup=start_keyboard)

@dp.callback_query_handler(lambda call: call.data == "intership_callback")
async def intership_callback(callback: types.CallbackQuery, state: FSMContext):
    await callback.answer("Чтобы пройти стажировку, вам нужно зарегистрироваться:")
    await UserRegisterState.first_name.set()
    await bot.send_message(callback.from_user.id, "Введите ваше имя:")

@dp.message_handler(state=UserRegisterState.first_name)
async def process_first_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['first_name'] = message.text
    await UserRegisterState.next()
    await message.answer("Теперь введите вашу фамилию:")

@dp.message_handler(state=UserRegisterState.last_name)
async def process_last_name(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['last_name'] = message.text
    await UserRegisterState.next()
    await message.answer("Введите ваш номер телефона:")

@dp.message_handler(state=UserRegisterState.phone)
async def process_phone(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['phone'] = message.text
    await UserRegisterState.next()
    await message.answer("Введите ваш возраст:")

group_chat_id = -1002016992729  

@dp.message_handler(state=UserRegisterState.age)
async def process_age(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['age'] = message.text
        await bot.send_message(group_chat_id, f"Новая заявка на стажировку:\n\n"
                                              f"Имя: {data['first_name']}\n"
                                              f"Фамилия: {data['last_name']}\n"
                                              f"Телефон: {data['phone']}\n"
                                              f"Возраст: {data['age']}")
        cursor.execute("INSERT INTO internship (first_name, last_name, phone, age, created) VALUES (?, ?, ?, ?, ?);",
                       (data['first_name'], data['last_name'], data['phone'], data['age'], time.ctime()))
        cursor.connection.commit()
    await message.answer("Вы успешно зарегистрировались.")
    await state.finish()
executor.start_polling(dp, skip_updates=True)
