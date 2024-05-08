import logging 
from aiogram import Bot,Dispatcher,executor,types
from dotenv import load_dotenv
import os

load_dotenv()
API_TOKEN=os.getenv("TELEGRAM_BOT_TOKEN")

logging.basicConfig(level=logging.INFO)

bot=Bot(token=API_TOKEN)
dp=Dispatcher(bot)

@dp.message_handler(commands=["start","help"])
async def command_start_handler(message:types.Message):

    await message.reply("Hi\n I am googly bot!.")
    
    
@dp.message_handler()
async def echo(message:types.Message):

    await message.answer(message.text)
    
    
if __name__=="__main__":
    executor.start_polling(dp,skip_updates=True)   