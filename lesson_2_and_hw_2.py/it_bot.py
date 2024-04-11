from aiogram import Bot, Dispatcher,types, executor
from config import token
import logging

bot = Bot(token)
dp = Dispatcher(bot)
logging.basicConfig(level=logging.INFO)

start_buttons = [
    types.KeyboardButton('About us'),
    types.KeyboardButton('Courses'),
    types.KeyboardButton('Contacts'),
    types.KeyboardButton('Address'),
    types.KeyboardButton('Sign up'),

]
# , one_time_keyboard=True
start_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True). add(*start_buttons)

@dp.message_handler(commands='start')
async def start (message:types.Message):
    await message.answer(f"Hello {message.from_user.first_name}!", reply_markup=start_keyboard)
    # await message.answer(f'{message}')

@dp.message_handler(text= 'About us')
async def start (message:types.Message):
    await message.reply("Geeks - это айти курсы в Бишкеке, Ташкенте и в Оше! Основано в 2019")

@dp.message_handler(text = "Contacts")
async def start (message:types.Message):
    await message.answer_contact("0777121212", "Nurbolot", "Erkinbaev")
    await message.answer_contact("0555121212", "Ulan", "Ashirov")
    await message.answer_contact("996 555837938", "Geeks", "Admin")

@dp.message_handler(text= 'Address')
async def start (message:types.Message):    
    await message.answer("Отправляю местоположение ....")
    await message.answer_location(40.52,72.8030)

@dp.message_handler(text='Sign up')
async def start (message:types.Message):
    await message.answer("""Для регистрации напишите:
                         1. ФИО
                         2. Номер телефона
                         3. Название курса
Мы с вами свяжемся""")

courses_buttons = [
    types.KeyboardButton("Backend"),
    types.KeyboardButton("Frontend"),
    types.KeyboardButton("Android"),
    types.KeyboardButton("IOS"),
    types.KeyboardButton("UX/UI"),
    types.KeyboardButton("EXIT")
]

courses_keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True).add(*courses_buttons)

@dp.message_handler(text = 'Courses')
async def start(message:types.Message):
    await message.answer("Вот все наши курсы: ", reply_markup=courses_keyboard)

@dp.message_handler(text='Backend')
async def start (message:types.Message):
    await message.reply('''Backend — это внутренняя часть продукта, которая находится на сервере и скрыта от пользователей. 
Для ее разработки могут использоваться самые разные языки, например, Python, PHP, Go, JavaScript, Java, С#.
Так как самым лёгким и понятным языком является Python, мы обучаем студентов именно на этом языке''')
    await message.answer_photo('https://248006.selcdn.ru/main/upload/setka_images/30c830da9f766d783e65d06a5393649fa02c6439.png')
    await message.answer_photo('https://cdn.sanity.io/images/35hw1btn/storage/2f4ecb947ad73a51d10bfbdf31e26be3b0885be4-800x400.png?auto=format')
    await message.answer("Цена: 10 000 сом")

@dp.message_handler(text='Frontend')
async def start (message:types.Message):
    await message.reply("Frontend — это публичная часть web-приложений (вебсайтов), с которой пользователь может взаимодействовать и контактировать напрямую. Во Frontend входит отображение функциональных задач, пользовательского интерфейса, выполняемые на стороне клиента, а также обработка пользовательских запросов. По сути, фронтенд — это всё то, что видит пользователь при открытии web-страницы.")
    await message.answer_photo('https://248006.selcdn.ru/main/upload/setka_images/30c830da9f766d783e65d06a5393649fa02c6439.png')
    await message.answer_photo('https://cdn.sanity.io/images/35hw1btn/storage/2f4ecb947ad73a51d10bfbdf31e26be3b0885be4-800x400.png?auto=format')
    await message.answer("Цена: 10 000 сом")

@dp.message_handler(text= 'Android')
async def start (message:types.Message):
    await message.reply('Android – это наиболее популярная и распространенная мобильная платформа в мире. Плюс в отличие от iOS, она используется на самых разнообразных устройствах.')
    await message.answer_photo('https://blog.skillfactory.ru/wp-content/uploads/2023/02/android_dev-6504975.png')
    await message.answer("Цена: 12 000 сом")

@dp.message_handler(text='IOS')
async def start (message:types.Message):
    await message.reply("iOS-разработчик, или iOS developer, — это программист, который пишет сервисы и программы для айфонов. Из-за особенностей устройств Apple и их операционной системы для них нужно писать специальный код. Основной язык, на котором пишут код iOS-разработчики, — Swift.")
    await message.answer_photo("https://web-academy.com.ua/images/stati/iosinfographic1.jpg")
    await message.answer_photo("https://cdn.myresume.ru/wp-content/uploads/2022/05/napravleniya-v-iOS-razrabotke-min.png")
    await message.answer("Цена: 11 000 сом")

@dp.message_handler(text='UX/UI')
async def start (message:types.Message):
    await message.reply("UI ― это user interface, пользовательский интерфейс, проще говоря ― оформление сайта: сочетания цветов, шрифты, иконки и кнопки. UX ― это функционал интерфейса, UI ― его внешний вид. В современном дизайне UX и UI практически всегда идут рядом, потому что они очень тесно связаны.")
    await message.answer_photo("https://digital-academy.ru/assets/components/phpthumbof/cache/03.fc1c5c5cf66bf4b475a0789c91068db8.png")
    await message.answer_photo("https://skillsetter.io/uploads/images/task_simple/85d8560e-8f73-44f2-bb23-73e1b7bdee17.jpeg")
    await message.answer("Цена:  9000 сом")

@dp.message_handler(text='EXIT')
async def start (message:types.Message):
    await message.answer("Вы вернулись в главное меню", reply_markup=start_keyboard)


@dp.message_handler()
async def not_found(message:types.Message):
    await message.reply("Я вас не понял введите кнопку /start")




executor.start_polling(dp)