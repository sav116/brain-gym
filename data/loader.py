from aiogram import Bot, Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from data.config import config

storage = MemoryStorage()

bot = Bot(config.bot_token)
dp = Dispatcher(bot, storage=storage)

bot = Bot(token=config.bot_token)
dp = Dispatcher(bot, storage=storage)
dp.middleware.setup(LoggingMiddleware())