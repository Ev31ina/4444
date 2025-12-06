import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
BOT_TOKEN = '8590387627:AAGi0dTbmim_15aEaXtg0neXtJTceWLWtg0'
bot = Bot(token = BOT_TOKEN)
dp = Dispatcher()
@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer('Привет! Я - твой первый бот на aiogram. Используй /help для списка комманд')
@dp.message(Command('hi'))
async def cmd_hi(message: types.Message):
    await message.answer('Привет)')
@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    help_text = """
    Доступные команды:
/start - Начать работу
/hi - Поприветствовать
/help - Справка
/time - Текущее время
/random - Рандомное число
/menu - Меню с кнопками
/about - О боте
/inline - Inline-кнопки
    """
    await message.answer(help_text)
async def main():
    await dp.start_polling(bot)
if __name__ == '__maim__':
    asyncio.run(main())