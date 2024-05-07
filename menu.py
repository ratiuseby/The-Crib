# Creation Date: 2022.06.27
# Copyright Ratiu Sebastian, All rights reserved 2022

from telegram import InlineKeyboardButton, InlineKeyboardMarkup


def menu(update, context):
    keyboard = [
        [
            InlineKeyboardButton("Word of day", callback_data="word"),
            InlineKeyboardButton("Fact of day", callback_data="fact"),
        ],
        [InlineKeyboardButton("Today's recipe", callback_data="dishes")],
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if update.message == None:
        update.callback_query.message.reply_text("Please choose:",
                                                 reply_markup=reply_markup)
    else:
        update.message.reply_text("Please choose:", reply_markup=reply_markup)
