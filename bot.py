import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, '( >_<)')

@bot.message_handler(content_types=['text'])
def send_message(text):
	bot.send_message(text='take me 👿')

#RUN
bot.polling(none_stop= True)
