# Import library
import aiogram
from main import bot, dp
from aiogram import types
from aiogram.types import Message
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher, executor
import csv, datetime, sqlite3

API_TOKEN = '2015778913:AAH_y0Lrn2k1wVwpKBNqB0kWvoSxw_VAgcQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

keyboard_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
array_keyboard = ['Компьютерные мышки','Клавиатуры','Коврики','Гарнитуры','Другие товары']

# Send message to admin
async def send_to_admin(dp):
        await bot.send_message(chat_id=admin_id, text="Bot start")	
# Function of start bot
@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
        keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
        await message.answer(text='Приветствуем Вас! Что Вас интересует?',reply_markup=keyboard_markup)
        statistics(message.chat.id, message.text)
        stat(message.chat.id, message.text)
        array_keyboard.clear()

def stat(user_id, command):
    sqlite_connection = sqlite3.connect('bot.db')
    cursor = sqlite_connection.cursor()
    data = datetime.datetime.today().strftime("%Y-%m-%d %H:%M")
    cursor.execute("INSERT INTO stat(user_id, user_command, date) VALUES('%s','%s','%s')" % (user_id, command, data))
    sqlite_connection.commit()
    cursor.close()

try:
    sqlite_connection = sqlite3.connect('bot.db')
    cursor = sqlite_connection.cursor()
    print("База данных создана и успешно подключена к SQLite")

    sqlite_select_query = "select sqlite_version();"
    cursor.execute(sqlite_select_query)
    record = cursor.fetchall()
    print("Версия базы данных SQLite: ", record)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при подключении к sqlite", error)
finally:
    if (sqlite_connection):
        sqlite_connection.close()
        print("Соединение с SQLite закрыто")

def statistics (user_id, command):
    data = datetime.datetime.today().strftime("%d-%m-%y %H:%M")
    with open('data.csv', 'a', newline="") as fil:
        wr = csv.writer(fil, delimiter=";")
        wr.writerow([data, user_id, command])

@dp.message_handler(commands=['help'])
async def send_help(message: types.Message):
        keyboard_markup.add(*(types.KeyboardButton(text) for text in array_keyboard))
        await message.answer(text='Если Вы хотите обратиться в нашу тех.поддержку, перейдите по сайту: https://support.logitech.com/ru_ru/contact-support',reply_markup=keyboard_markup)
        array_keyboard.clear()

@dp.message_handler(lambda message: message.text == 'Компьютерные мышки')
async def computer_mice(message: types.Message):
        await message.reply("Высылаем вам ссылку на официальный сайт для просмотра подробной информации")
        await message.answer(text='https://www.logitechg.com/ru-ru/products/gaming-mice.html',reply_markup=keyboard_markup)
        array_keyboard.clear()

@dp.message_handler(lambda message: message.text == 'Клавиатуры')
async def keyboards(message: types.Message):
        await message.reply("Высылаем вам ссылку на официальный сайт для просмотра подробной информации")
        await message.answer(text='https://www.logitechg.com/ru-ru/products/gaming-keyboards.html',reply_markup=keyboard_markup)
        array_keyboard.clear()

@dp.message_handler(lambda message: message.text == 'Коврики')
async def mats(message: types.Message):
        await message.reply("Высылаем вам ссылку на официальный сайт для просмотра подробной информации")
        await message.answer(text='https://www.logitechg.com/ru-ru/products/gaming-mouse-pads.html',reply_markup=keyboard_markup)
        array_keyboard.clear()

@dp.message_handler(lambda message: message.text == 'Гарнитуры')
async def headsets(message: types.Message):
        await message.reply("Высылаем вам ссылку на официальный сайт для просмотра подробной информации")
        await message.answer(text='https://www.logitechg.com/ru-ru/products/gaming-audio.html',reply_markup=keyboard_markup)
        array_keyboard.clear()

@dp.message_handler(lambda message: message.text == 'Другие товары')
async def computer_mice(message: types.Message):
        await message.reply("Высылаем вам ссылку на официальный сайт для просмотра подробной информации")
        await message.answer(text='PRESS F TO REP',reply_markup=keyboard_markup)
        array_keyboard.clear()

def statistics (user_id, command):
    data = datetime.datetime.today().strftime("%d-%m-%y %H:%M")
    with open('data.csv', 'a', newline="") as fil:
        wr = csv.writer(fil, delimiter=";")
        wr.writerow([data, user_id, command])

if __name__ == '__main__':
    executor.start_polling(dp)
