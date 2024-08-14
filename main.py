import logging
from aiogram import executor
from handlers.commands import register_handlers_commands
from handlers.callbacks import register_handlers_callbacks

from data.loader import dp

logging.basicConfig(level=logging.INFO)

register_handlers_commands(dp)
register_handlers_callbacks(dp)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
