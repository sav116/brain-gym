from aiogram import types
from aiogram.dispatcher import Dispatcher
from aiogram.dispatcher.filters import Text
from aiogram.types import CallbackQuery
from keyboards.inlinekeyboards import create_math_keyboard

def calculate_result(a: int, operation: str, b: int) -> int:
    operations = {
        '+': a + b,
        '-': a - b,
        '*': a * b,
        '/': a // b  # Integer division
    }
    return operations.get(operation)

def register_handlers_callbacks(dp: Dispatcher):
    
    @dp.callback_query_handler(Text(startswith="check_result"))
    async def process_check_result(callback_query: CallbackQuery):
        data = callback_query.data.split(":")
        a, operation, b = int(data[1]), data[2], int(data[3])
        result = calculate_result(a, operation, b)
        
        if result is not None:
            await callback_query.answer(f"{a} {operation} {b} = {result}", show_alert=False)
        else:
            await callback_query.answer("Unknown operation", show_alert=True)

    @dp.callback_query_handler(Text(equals="next_question"))
    async def process_next_question(callback_query: CallbackQuery):
        question, keyboard = create_math_keyboard()
        await callback_query.message.edit_text(question, reply_markup=keyboard)