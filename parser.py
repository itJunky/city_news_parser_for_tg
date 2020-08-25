#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Crated by ITJunky

# Подгружаем поддержку для обращения к сайтам
import requests

# Подгружаем библиотеку для парсинга текста
from bs4 import BeautifulSoup

# Подгружаем настройки
from config import durl
# Основная функция, реализующая парсинг страниц
def parse_page(url='xx'):
  if url is 'xx':
    url = durl
  result = []
  # Открываем страницу
  page = requests.get(url).content
  # Перевариваем страницу в удобный для разбора формат xml
  soup = BeautifulSoup(page, 'lxml')

  for match in soup.findAll('span'):
    match.replace_with('')

  all_news = soup.findAll('div', {'class': 'kCrYT'})
  previous_url = ''
  for news in all_news:
    try:
      print(news.find('a')['href'])
      news_url = news.find('a')['href'].split('q=')[1].split('&sa=U')[0]
      print(news_url)
    except Exception as e:
      print(e)
      print('----\r\n' + str(news.find('a')))
      news_url = None

    print('\r\n\r\n')

    try:
      item = "🌍 {} \n <a href='{}'>Подробнее</a>".format(news.text, news_url)
    except Exception as e:
      print(e)
      item = None
    if previous_url == news_url or news_url is None:
      pass
    else:
      result.append(item)
      previous_url = news_url

  return result

# Основной код скрипта, запускающий все ранее объявленные функции
if __name__ == "__main__":
  print('Trying to parse url')
  print(parse_page())

