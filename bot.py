# -*- coding: utf-8 -*-
import os
import telebot
import requests
# import some_api_lib
# import ...

#653592451:AAFQE_iGtgiPUPb-z0kzqk6Gz4ekHSGUaKY
#T6gnlNPRvszFzlFmAb7nkZ24YhRMjyqFZqibOy1wgznLPRkqOORNwnCWkLzN0qna
# Example of your code beginning
#           Config vars
token = os.environ['TELEGRAM_TOKEN']
some_api_token = os.environ['SOME_API_TOKEN']
#             ...


#       Your bot code below
# bot = telebot.TeleBot(token)
# some_api = some_api_lib.connect(some_api_token)
#              ...

bot = telebot.TeleBot(f"{token}")
artist = ""
title = ""

@bot.message_handler(commands=['start','help'])
def send_welcome(message):
    bot.reply_to(message, "I can help you find lyrics for your songs.\n\nYou can request lyrics by sending me Artis\nand Title name separated by '-'\n\n\nExample:\n\n'Michael Jackson - Thriller'")

@bot.message_handler(content_types=['text'])
def find_lyrics(message):
    chat_id = message.chat.id
    user_input = message.text
    data_list = user_input.split('-')
    contents = requests.get(f'https://orion.apiseeds.com/api/music/lyric/{data_list[0]}/{data_list[1]}?apikey={some_api_token}').json()
    try:
        lyrics = contents['result']['track']['text']
    except KeyError:
        bot.reply_to(message, text="Sorry, I couldn't find lyrics for this song")
    else:
        bot.reply_to(message, text=lyrics)



bot.polling()
