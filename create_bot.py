from aiogram import Bot
from aiogram.dispatcher import Dispatcher
from aiogram.contrib.fsm_storage.memory import MemoryStorage

strg = MemoryStorage()
bot = Bot(token='5482680028:AAGoSoHtL8dtSo-J2MCWMDFSJTQQfPyPMDk')
dp = Dispatcher(bot, storage=strg)