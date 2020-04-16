import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['Hey', 'hey', 'HEY', 'HEy', 'hEY', 'heY'])
def send_start(message):
	bot.send_message(message.chat.id, '( >_<)')

@bot.message_handler(commands=['want'])
def send_text(message):
	bot.send_message(message.chat.id,' take me - /photo')

#RUN
bot.polling(none_stop= True)
