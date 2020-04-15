import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(func=lambda message:True, content_types=['start'])
def send_welcome(message):
	bot.reply_to(message, '( >_<)')



#RUN
bot.polling(none_stop= True)
