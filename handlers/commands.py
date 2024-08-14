from aiogram import types
from aiogram.dispatcher import Dispatcher
from keyboards.inlinekeyboards import create_math_keyboard

def register_handlers_commands(dp: Dispatcher):
    
    @dp.message_handler(commands="start")
    async def send_welcome(message: types.Message):
        question, keyboard = create_math_keyboard()
        await message.answer("Бот запущен и готов к работе!")
        await message.answer(question, reply_markup=keyboard)
