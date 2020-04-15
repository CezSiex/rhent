import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def send_start(message):
	bot.send_message(message.chat.id, '( >_<)')

@bot.message_handler_1(commands=['text'])
def send_text(message):
	bot.send_message(message.chat.id,' take me ')

#RUN
bot.polling(none_stop= True)
