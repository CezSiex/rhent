import telebot
import config
import os

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, '( >_<)')


#RUN
bot.polling(none_stop= True)
