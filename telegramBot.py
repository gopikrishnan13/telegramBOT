helpMsg = """
This bot in under development 

You can control me by sending these commands:

/math - solve equation support[+,-,*,/,%]
/help - show help commands

"""
import os
import telebot
from functionClass import *
import json

Token = os.environ.get('TELEGRAM_TOKEN')
bot = telebot.TeleBot(Token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

try:
    @bot.message_handler(commands=['start'])
    def send_welcome(message):
        bot.reply_to(message, f"Hey {message.from_user.first_name}, how are  ?")


    @bot.message_handler(commands=['math'])
    def math(message):
        try:
            #Str = message.text.replace('/math','',1)
            Result = Math(message.text)
            Result = Result if Result else 'SOMETHING WRONG'
        except:
            Result = 'SOMETHING WRONG'
        bot.reply_to(message, f"{str(Result)}")


    @bot.message_handler(commands=['help'])
    def sendHelp(message):
        bot.reply_to(message, helpMsg)


    @bot.message_handler(func=lambda message:True)
    def echo(message):
        bot.reply_to(message, message.text)
    


except:
    @bot.message_handler(func=lambda message:True)
    def echo(message):
        bot.reply_to(message, 'SOMETHING WRONG')


print('BOT IS LISTENING...')
bot.polling()