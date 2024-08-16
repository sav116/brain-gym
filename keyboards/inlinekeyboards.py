from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
import random

def create_math_keyboard():
    a = random.randint(10, 1000)
    b = random.randint(10, 1000)
    operations = ['+', '-']
    operation = random.choice(operations)
    question = f"{a} {operation} {b} = ?"
    keyboard = InlineKeyboardMarkup(resize_keyboard=True)
    button_check = InlineKeyboardButton(text="Check", callback_data=f"check_result:{a}:{operation}:{b}")
    button_next = InlineKeyboardButton(text="Next", callback_data="next_question")
    keyboard.add(button_check, button_next)
    return question, keyboard
