import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['Hey', 'hey', 'HEY', 'HEy', 'hEY', 'heY'])
def send_start(message):
	bot.send_message(message.chat.id, '( >_<)')

@bot.message_handler(commands=['text'])
def send_text(message):
	bot.send_message(message.chat.id,' take me ')

#RUN
bot.polling(none_stop= True)
