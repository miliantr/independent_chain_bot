from aiogram import Bot, Dispatcher

from database import Database, EventDatabase
from secret import API_TOKEN

bot: Bot = Bot(API_TOKEN, parse_mode="HTML")
dispatcher: Dispatcher = Dispatcher()
database: Database = Database()
event_database: EventDatabase = EventDatabase()