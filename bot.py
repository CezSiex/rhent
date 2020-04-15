import telebot
import config

bot = telebot.TeleBot(config.TOKEN)

@bot.message_handler(commands=['start'])
def send_welcome(message):
	bot.reply_to(message, '( >_<)')
@bot.command(pass_context = True)
async def text():
	await Bot.say('take me 👿')

#RUN
bot.polling(none_stop= True)
