# city_news_parser_for_tg
Just for fun project to forwarding any news from google about your city

Parse any news by string at last hour in google every minute.

## Installation
Before start the bot you need create a config.py file with content like this:

```
token = 'xxxxxxxxxxxxxxxxxxxxxxx'
chat_ids = [-12345678]
dork = 'moscow'
timeshift = 's90'
durl = 'https://www.google.com/search?q={}&tbs=qdr:{}&tbo=1&tbm=nws'.format(dork, timeshift)
```
In crontab set something like this:

```
* * * * * /path/to/python3 /path/to/cronjob.py
```
