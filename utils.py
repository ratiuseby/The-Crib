# Creation Date: 2022.06.27
# Copyright Ratiu Sebastian, All rights reserved 2022

import telegram.ext
from telegram.ext.filters import Filters
from telegram.ext import CallbackQueryHandler
from keep_alive import keep_alive
import trivia_funcs
import food
import menu

##################### whitelist #######################
whitelist = ["@SPAWN_LKD", "@Starstroke", "@sandorsinofobu", "@SergiuWat"]
#######################################################


def read_token(token_file):
    with open(token_file, 'r') as f:
        return f.read()


def start_bot():
    TOKEN = read_token("token.txt")

    updater = telegram.ext.Updater(TOKEN, use_context=True)
    disp = updater.dispatcher

    disp.add_handler(
        telegram.ext.CommandHandler("start", start,
                                    Filters.user(username=whitelist)))
    disp.add_handler(CallbackQueryHandler(button))
    disp.add_handler(
        telegram.ext.CommandHandler("help", help,
                                    Filters.user(username=whitelist)))

    keep_alive()
    updater.start_polling()
    updater.idle()


def start(update, context):
    update.message.reply_text(
        """Aloha! Welcome to The Crib! Here we can do all sorts of things, but for now, let me just say..Hi, I'm Jeff 🤖 and I'll be the one that helps you from now on. Just type /help and we'll get things going. Cheerio!"""
    )


def button(update, context) -> None:
    """Parses the CallbackQuery and updates the message text."""
    query = update.callback_query

    query.answer()
    if query.data == 'word':
        trivia_funcs.word_of_the_day(update, context)
    elif query.data == 'fact':
        trivia_funcs.fun_fact(update, context)
    elif query.data == 'dishes':
        food.daily_dishes(update, context)


def help(update, context):
    update.message.reply_text("""
  Hello there, the following commands are available:
  /start -> starting welcome message, brought by me, Your friendly Telegram-hood Jeff
  /help -> this wonderful helping message
                            """)
    menu.menu(update, context)
