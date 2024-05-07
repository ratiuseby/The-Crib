# Creation Date: 2022.06.27
# Copyright Ratiu Sebastian, All rights reserved 2022

import time

import bs4
import requests

import menu


##########
# UNUSED #
##########
def trivia(update, context):
    try:
        type = context.args[0]

        if type == 'word':
            word_of_the_day(update, context)
        elif type == 'fact':
            fun_fact(update, context)
        else:
            update.message.reply_text("""
      Sorry 🧐...doesn't seem like we have a trivia option like that. You can check the help page if you are lost, I got you covered 😉
                            """)
    except:
        update.message.reply_text("""
      Oops 😬...looks like you forgot to add your trivia option. You can check the help page if you are lost, I got you covered 😉
                            """)


##########


def word_of_the_day(update, context):
    # update.message.reply_text("""
    # Word of the day incoming!
    #                           """)

    update.callback_query.message.reply_text(""" Word of the day incoming! """)

    # Download page
    cookies = requests.head('https://www.merriam-webster.com/word-of-the-day')
    getPage = requests.get('https://www.merriam-webster.com/word-of-the-day',
                           cookies=cookies)

    try:
        getPage.raise_for_status()

        # Parse the html page
        page_info = bs4.BeautifulSoup(getPage.text, 'html.parser')

        # Extract the word, word attributes, meaning and build the response
        todays_word = page_info.select('.word-header-txt')[0].text.strip()
        date = time.strftime("%B %d, %Y")
        main_attribute = page_info.select(
            '.word-attributes .main-attr')[0].text.strip()
        word_syllables = page_info.select(
            '.word-attributes .word-syllables')[0].text.strip()
        meaning = page_info.select(
            '.wod-definition-container p')[0].text.strip()
        did_you_know = page_info.select(
            '.did-you-know-wrapper p')[0].text.strip()

        update.callback_query.message.reply_text(f"""
    {date} ➼ \"{todays_word}\": 
    ‣ Main attribute: {main_attribute}
    ‣ Word syllables: {word_syllables}
    ‣ What it means: {meaning}
    ‣ Did you know?: {did_you_know}
                            """)

    except requests.exceptions.HTTPError as e:
        update.callback_query.message.reply_text(f"""
        Hmmmmmmm...seems like the following error has occured : {e}
        \nMaybe you can try again? """)
    except IndexError:
        update.callback_query.message.reply_text("""
        Hmmmmmmm...seems like the server has a small hiccup.
        \nMaybe you can try again? """)

    menu.menu(update, context)


def fun_fact(update, context):
    update.callback_query.message.reply_text("""
  Eyyy, someone wants a fun fact, gotcha!                      
                            """)

    # Download page
    getPage = requests.get('https://wtffunfact.com/fact-of-the-day/')

    try:
        getPage.raise_for_status()

        # Parse the html page
        page_info = bs4.BeautifulSoup(getPage.text, 'html.parser')

        # Extract the fact image source and build the response
        fact_img_src = page_info.find(
            'img', {
                'class':
                'attachment-large size-large wp-post-image jetpack-lazy-image'
            }).get('src')

        update.callback_query.message.reply_photo(fact_img_src)

    except requests.exceptions.HTTPError as e:
        update.callback_query.message.reply_text(f"""
    Hmmmmmmm...seems like the following error has occured : {e} \nMaybe you can try again?            
                            """)

    menu.menu(update, context)
