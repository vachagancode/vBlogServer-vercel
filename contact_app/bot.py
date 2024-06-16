import os

# Telegram, Aiogram
from aiogram import Bot

# Env
from dotenv import load_dotenv


load_dotenv()

TOKEN = os.environ.get("7414808495:AAEoRe-O9fJfcHcSkUUsxuR2Brc6n9c0lpw")
ID = os.environ.get("1038108849")

bot = Bot(token=TOKEN)

async def send_data(data):
	try:
		await bot.send_message(ID, "NEW CONTACT MESSAGE")
		await bot.send_message(ID, data)
		await bot.send_message(ID, "🫡")
		print(ID)
	except:
		await bot.send_message(ID, "Failed to send the data")
