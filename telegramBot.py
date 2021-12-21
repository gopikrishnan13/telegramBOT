Token = '5041935271:AAGnDJnJFhapW8RFxFYqkJXtssQs5Vww5lk'

import telebot
bot = telebot.TeleBot(Token, parse_mode=None) # You can set parse_mode by default. HTML or MARKDOWN

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, f"Hey {message.chat.first_name}, how are you ?")

@bot.message_handler(commands=['gopi'])
def send_gopi(message):
    bot.reply_to(message, "இங்கு எதுவும் இல்லை")

@bot.message_handler(commands=['add'])
def add(message):
    try:
        s = message.text.replace('/add','',1)
        num = sum(list(map(int,s.split('+'))))
    except:
        num = message.text
    bot.reply_to(message, f"{num}")

@bot.message_handler(func=lambda message:True)
def echo(message):
    bot.reply_to(message, message.text)

print('BOT IS LISTENING...')
bot.polling()