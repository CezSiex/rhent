import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_document(message.chat.id, 'https://media.giphy.com/media/xdgisqRDFyO9G/giphy.gif'  )

@bot.message_handler(commands=['Hey', 'hey', 'HEY', 'HEy', 'hEY', 'heY'])
def send_start(message):
	bot.send_message(message.chat.id, '( >_<)')

@bot.message_handler(commands=['want'])
def send_text(message):
	bot.send_message(message.chat.id,' take me - /photo')

@bot.message_handler(commands=['photo'])
def send_photo(message):
	bot.send_photo(message.chat.id,'https://raw.githubusercontent.com/CezSiex/rhent/master/photo/photo_2020-04-16_10-11-48.jpg')

	
@bot.message_handler(commands=['gif'])
def gif(message):
	bot.send_document(message.chat.id, 'https://media.giphy.com/media/oVREpe8qWMOqc/giphy.gif'  )	
	
	
#RUN
bot.polling(none_stop= True)
