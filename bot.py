#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from parser import parse_page
from config import token

bot = telebot.TeleBot(token)

@bot.message_handler(commands=['start', 'help'])
def handle_start_help(msg):
  start_text = 'Hello :)'
  bot.send_message(msg.chat.id, start_text)

@bot.message_handler(commands=['news'])
def handle_news(msg):
  bot.send_message(msg.chat.id, msg.chat.id)
  list = parse_page()
  for text in list:
    try:
      bot.send_message(msg.chat.id, text, parse_mode='HTML')
    except Exception as e:
      bot.send_message(msg.chat.id, 'Свежих новостей не появилось')
      break

if __name__ == '__main__':
  print('News bot started')
  bot.polling(none_stop=True)
