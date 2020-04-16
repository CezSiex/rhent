import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_document(message.chat.id,'https://www.google.com/url?sa=i&url=https%3A%2F%2Fgifer.com%2Fru%2F9Ptf&psig=AOvVaw3OPM8H9_Ns6iGHPlgGN2pc&ust=1587124778848000&source=images&cd=vfe&ved=0CAIQjRxqFwoTCIDy4Njy7OgCFQAAAAAdAAAAABAD')

@bot.message_handler(commands=['Hey', 'hey', 'HEY', 'HEy', 'hEY', 'heY'])
def send_start(message):
	bot.send_message(message.chat.id, '( >_<)')

@bot.message_handler(commands=['want'])
def send_text(message):
	bot.send_message(message.chat.id,' take me - /photo')

@bot.message_handler(commands=['photo'])
def send_photo(message):
	bot.send_photo(message.chat.id,'https://raw.githubusercontent.com/CezSiex/rhent/master/photo/photo_2020-04-16_10-11-48.jpg')

#RUN
bot.polling(none_stop= True)
