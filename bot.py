import telebot
import config
import random
import time

bot = telebot.TeleBot(config.TOKEN) 
		
# Start
@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'I greet you --$ {0.first_name} $-- (>_<)\nMy name is {1.first_name} \ncheck -- /help # help list '.format(message.from_user, bot.get_me()))
	bot.send_document(message.chat.id, 'https://media.giphy.com/media/xdgisqRDFyO9G/giphy.gif')
	
	if (True == True):
		time.sleep(3)
		bot.send_message(message.chat.id, 'You are like a wanderer wandering from neotkudap (')	
	else:
		print('Process stop')


# hey ( >_<)	
@bot.message_handler(commands=['Hey', 'hey', 'HEY', 'HEy', 'hEY', 'heY'])
def send_start(message):
	bot.send_message(message.chat.id, '( >_<)')

# gif	
@bot.message_handler(commands=['gif'])
def gif(message):
	bot.send_document(message.chat.id, 'https://media.giphy.com/media/oVREpe8qWMOqc/giphy.gif'  )	


# take Kera photo (want - hello)
@bot.message_handler(commands=['want'])
def send_text(message):
	bot.send_message(message.chat.id,' take me - /photo')

# Kera photo
@bot.message_handler(commands=['photo'])
def send_photo(message):
	bot.send_photo(message.chat.id,'https://raw.githubusercontent.com/CezSiex/rhent/master/photo/photo_2020-04-16_10-11-48.jpg')

# hentphoto
@bot.message_handler(commands=['hentphoto'])
def send_test(message): 
	bot.send_photo(message.chat.id, '<a href="https://github.com/CezSiex/rhent/blob/master/photo/photo_kerabot/photo1.jpg">&#8203;</a>',parse_mode="HTML")     # random.choice(os.listdir('https://github.com/CezSiex/rhent/tree/master/photo/hPhoto/photo_kerabot'))


# Help list 
@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, '''This is help list (>_<) -- # let's get started \n1$com -- /hey # HEY \n2$com -- /gif # check gif \n3$com -- /want # see \n4$com -- /photo # see photo Kera's \n5$com -- /hentphoto # ee baby \n6$com -- /help # Why?''')
		
#RUN
bot.polling(none_stop=True)


