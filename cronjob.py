#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telebot
from parser import parse_page
from config import token, chat_ids

bot = telebot.TeleBot(token)

list = parse_page()
for text in list:
    try:
      for id in chat_ids:
        bot.send_message(id, text, parse_mode='HTML')
    except Exception as e:
      #bot.send_message(chat_id, 'Свежих новостей не появилось')
      break

