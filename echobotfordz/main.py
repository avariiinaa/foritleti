#@Echoletibot
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

import logging

TOKEN = "Your token"

updater = Updater(token=TOKEN)
dispatcher = updater.dispatcher
logging.basicConfig(format="%(name)s - %(levelname)s - %(message)s", level=logging.INFO)


def text(update, context):
    context.bot.send_message(chat_id=update.effective_chat.id, text=update.message['text'])


text_handler = MessageHandler(Filters.text, text)
dispatcher.add_handler(text_handler)

updater.start_polling()
