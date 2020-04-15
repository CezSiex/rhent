import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, '( >_<)')
@bot.message_handler1(commands=['text'])
def send_message():
	bot.send_message('take me 👿')

#RUN
bot.polling(none_stop= True)
