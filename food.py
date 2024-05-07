# Creation Date: 2022.06.27
# Copyright Ratiu Sebastian, All rights reserved 2022


import bs4
import requests

import menu


##########
# UNUSED #
##########
def food(update, context):
    try:
        type = context.args[0]

        if type == 'dishes':
            daily_dishes(update, context)
        else:
            update.message.reply_text("""
      Sorry 🧐...doesn't seem like we have a food option like that. You can check the help page if you are lost, I got you covered 😉
                            """)

    except:
        update.message.reply_text("""
      Oops 😬...looks like you forgot to add your food option. You can check the help page if you are lost, I got you covered 😉
                            """)


##########


def daily_dishes(update, context):
    update.callback_query.message.reply_text("""
  Uuuuuu, hungry, aren't we 😊?                      
                            """)

    # Download page
    getPage = requests.get('https://recipes.net/recipe-of-the-day/')

    try:
        getPage.raise_for_status()

        # Parse the html page
        page_info = bs4.BeautifulSoup(getPage.text, 'html.parser')

        # Extract the word, word attributes, meaning and build the response
        dish_img_src = page_info.find(
            'img', {'class': 'attachment-medium size-medium'})

        h3_tag = page_info.find('h3', {'class': 'ellipsis-title-lines-2'})

        # Check if the <h3> tag exists
        if h3_tag:
            recipe_link = h3_tag.find_next('a')
            dish_title_src = recipe_link.text
            dish_recipe_src = recipe_link.get('href')

        update.callback_query.message.reply_photo(dish_img_src.get('data-src'))
        update.callback_query.message.reply_text(dish_title_src + ' ⇛\n' +
                                                 dish_recipe_src)

    except requests.exceptions.HTTPError as e:
        update.callback_query.message.reply_text(f"""
    Hmmmmmmm...seems like the following error has occured : {e} \nMaybe you can try again?            
                            """)

    menu.menu(update, context)
