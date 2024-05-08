import logging 
from aiogram import Bot,Dispatcher,executor,types
from dotenv import load_dotenv
import os
import openai
import sys

class Reference:
    
    def __init__(self)->None:
        self.response=""
        
load_dotenv()
openai.api_key=os.getenv("open_ai_key")

reference=Reference()

TOKEN=os.getenv("TELEGRAM_BOT_LINK")

MODEL_NAME="gpt-33.5-turbo"

bot=Bot(token=TOKEN)
dispatcher=Dispatcher(bot)

def clear_past():
    reference.response=""
    
    
@dispatcher.message_handler(command=['clear'])
async def welcome(message:types.Message):
    await message.reply("How can i assist you")


@dispatcher.message_handler(command=['clear'])
async def clear(message:types.Message):
    clear_past()
    await message.reply("I ve cleared the past coversation")
    
    
@dispatcher.message_handler(command=["help"])
async def helper(message:types.Message):
    help_command="""
    Hi There, I'm chatGPT Telegram bot created by PWskills! Please follow these commands - 
    /start - to start the conversation
    /clear - to clear the past conversation and context.
    /help - to get this h    
    """
    
    await message.reply(help_command)
    
@dispatcher.message_handler()
async def chatgpt(message:types.Message):
    print(f"user : {message.text}")
    response=openai.ChatCompletion.create(
        model=MODEL_NAME,
        messages=[
            {"role":"assistant","content":reference.response},
            {"role":"user","content":message.text}    
        ]
    )
    reference.response=response.choices[0]['message']['content']
    print(f">>>chatGPT:\n\t{reference.response}")
    await bot.send_message(chat_id=message.chat.id,text=reference.response)
    
    
if __name__=="__main__":
    executor.start_pooling(dispatcher,skip_updates=False)
    