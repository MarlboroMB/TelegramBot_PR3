import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
import asyncio
from aiogram import Bot, Dispatcher, executor
import csv, datetime, pymysql

API_TOKEN = '2015778913:AAH_y0Lrn2k1wVwpKBNqB0kWvoSxw_VAgcQ'

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands='start')
async def cmd_start(message: types.Message):
    await message.reply("Привет славянам!")
    statistics(message.chat.id, message.text)

def statistics (user_id, command):
    data = datetime.datetime.today().strftime("%d-%m-%y %H:%M")
    with open('data.csv', 'a', newline="") as fil:
        wr = csv.writer(fil, delimiter=";")
        wr.writerow([data, user_id, command])

if __name__ == '__main__':
    executor.start_polling(dp)
