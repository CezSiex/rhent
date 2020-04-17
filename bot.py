import telebot
import config

bot = telebot.TeleBot(config.TOKEN) 

# Help list 
@bot.message_handler(commands=['help'])
def help(message):
	bot.send_message(message.chat.id, '''This is help list (>_<) -- # let's get started \n1$com -- /hey # HEY \n2$com -- /gif # check gif \n3$com -- /want # see \n4$com -- /photo # see photo Kera's \n5$com -- /help # Why?''')
		
# Start
@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_message(message.chat.id, 'I greet you -$ {0.first_name} My name is {1.first_name} \ncheck -- /help # help list'.format(message.from_user, bot.get_me()) )
	

@bot.message_handler(commands=['Hey', 'hey', 'HEY', 'HEy', 'hEY', 'heY'])
def send_start(message):
	bot.send_message(message.chat.id, '( >_<)')

@bot.message_handler(commands=['want'])
def send_text(message):
	bot.send_message(message.chat.id,' take me - /photo')
# glav photo
@bot.message_handler(commands=['photo'])
def send_photo(message):
	bot.send_photo(message.chat.id,'https://raw.githubusercontent.com/CezSiex/rhent/master/photo/photo_2020-04-16_10-11-48.jpg')

# gif	
@bot.message_handler(commands=['gif'])
def gif(message):
	bot.send_document(message.chat.id, 'https://media.giphy.com/media/oVREpe8qWMOqc/giphy.gif'  )	


		
#RUN
bot.polling(none_stop= True)
