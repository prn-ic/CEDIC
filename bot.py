from aiogram import Bot, types
import logging
from datetime import datetime
import asyncio
from aiogram.dispatcher import Dispatcher
from aiogram.utils import executor
from aiogram.types import *
from zqmpwork import Parcer
from time import sleep

bot = Bot(token='YOUR TOKKEN')

dp = Dispatcher(bot)

logging.basicConfig(level=logging.INFO)

button_hello = KeyboardButton('🧨 Начать 🧨')
greet_kb = ReplyKeyboardMarkup(resize_keyboard=True)
greet_kb.add(button_hello)

keyboardMain = ReplyKeyboardMarkup(resize_keyboard=True)
button_main = ['Список оружий 🛠']
keyboardMain.add(*button_main)

button_back = ReplyKeyboardMarkup(resize_keyboard=True).add('Назад ↩️')

keyboardWeapon = ReplyKeyboardMarkup(resize_keyboard=True)
but_gun = ['AK', 'M4', 'GLOCK', 'AWP', 'DEAGLE']
keyboardWeapon.add(*but_gun)

@dp.message_handler(commands='start')
async def press_start(message: types.Message):
	await message.answer('Добро пожаловать в CEDIC. С помощью нашего бота ты сможешь:\n1)Узнавать скидки на скины 😁\n2) Забирать скины быстрее всех 🥵', reply_markup=greet_kb)

@dp.message_handler(lambda message: message.text=='🧨 Начать 🧨')
async def start(message: types.Message):
	await message.answer('Хорошо, давай начнем...\nВыбери операцию ниже 👇🏼', reply_markup=keyboardMain)

@dp.message_handler(lambda message: message.text=='Список оружий 🛠')
async def all_weapons(message: types.Message):
	await message.answer('Выбери, какое оружие тебе по душе!', reply_markup=keyboardWeapon)
		

@dp.message_handler(lambda message: message.text=='AK')
async def ak(message: types.Message):
	await message.reply('Загружаем информацию...')
	mess = Parcer().show_all()
	for item in mess:
		if 'AK-47' in item:
			await message.answer(f'{item}', reply_markup=button_back)
	else:
		await message.answer('На этом всё 😥')


@dp.message_handler(lambda message: message.text=='M4')
async def ak(message: types.Message):
	await message.reply('Загружаем информацию...')
	mess = Parcer().show_all()
	for item in mess:
		if 'M4A4' in item or 'M4A1-S' in item:
			await message.answer(f'{item}', reply_markup=button_back)
	else:
		await message.answer('На этом всё 😥')


@dp.message_handler(lambda message: message.text=='GLOCK')
async def ak(message: types.Message):
	await message.reply('Загружаем информацию...')
	mess = Parcer().show_all()
	for item in mess:
		if 'GLOCK' in item:
			await message.answer(f'{item}', reply_markup=button_back)
	else:
		await message.answer('На этом всё 😥')


@dp.message_handler(lambda message: message.text=='AWP')
async def ak(message: types.Message):
	await message.reply('Загружаем информацию...')
	mess = Parcer().show_all()
	for item in mess:
		if 'AWP' in item:
			await message.answer(f'{item}', reply_markup=button_back)
	else:
		await message.answer('На этом всё 😥')


@dp.message_handler(lambda message: message.text=='DEAGLE')
async def ak(message: types.Message):
	await message.reply('Загружаем информацию...')
	mess = Parcer().show_all()
	for item in mess:
		if 'DEAGLE' in item:
			await message.answer(f'{item}', reply_markup=button_back)
	else:
		await message.answer('На этом всё 😥')


@dp.message_handler(lambda message: message.text=='Назад ↩️')
async def get_back(message: types.Message):
	await message.answer('Возвращаемся...')
	await message.answer('Хорошо, давай начнем...\nВыбери операцию ниже 👇🏼', reply_markup=keyboardMain)


async def update_data(time_for):
	while True:
		now = datetime.utcnow()
		
		try:
		
			Parcer().get_data()

			with open('data/log.txt', 'a', encoding='utf-8') as file:
				file.write(f'[+] {now} | Data was updates succesfully\n')

		except Exception as ex:
			
			with open('data/log.txt', 'a', encoding='utf-8') as file:
				file.write(f'[-] {now} | {ex} |Data wasnt updates\n')

		await asyncio.sleep(time_for)

if __name__ == '__main__':

	loop = asyncio.get_event_loop()

	loop.create_task(update_data(40))
	
	executor.start_polling(dp, skip_updates=True)