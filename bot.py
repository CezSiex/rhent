import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
	bot.send_document(message.chat.id,'https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2Foriginals%2F38%2Fdb%2F07%2F38db0791549a04e0139e90cbdb8a5f32.gif&imgrefurl=https%3A%2F%2Fwww.pinterest.com%2Fpin%2F12455336456000157%2F&tbnid=szxC_FvCbq7FrM&vet=10CB4QxiAoCGoXChMI8Oi6-Ons6AIVAAAAAB0AAAAAEAc..i&docid=daWkArMm12S05M&w=800&h=600&itg=1&q=gif%20%D0%B4%D0%BB%D1%8F%20%D0%B1%D0%BE%D1%82%D0%B0%20%D1%82%D0%B5%D0%BB%D0%B5%D0%B3%D1%80%D0%B0%D0%BC%D0%BC&client=ubuntu&ved=0CB4QxiAoCGoXChMI8Oi6-Ons6AIVAAAAAB0AAAAAEAc')

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
