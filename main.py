from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
from telegram import Update
from telegram.ext import CallbackContext

import logging

TOKEN = "5254891313:AAEJ8i-OTsmUgonyhj3FHlLa9KE7_kx6CTw"

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
logging.basicConfig(format="%(asktime)s - %(name)s - %(levelname)s - %(message)s", level = logging.INFO)

def start(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text="hello")
    print(update)
    print(context)


start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

updater.start_polling()