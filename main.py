import telebot

TOKEN = 'Token'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def welcome(message):
    bot.send_message(message.chat.id,"Напишите ИИН")

@bot.message_handler(content_types=['text'])
def talk(message):
    if(message.text.isnumeric() and len(message.text)==12):
        bot.send_message(message.chat.id,"Правильно, теперь на этот каспий номер +7 776 221 9957 Илияс Н")
    if(message.text.isnumeric() and (len(message.text)>12 or len(message.text)<12)) :
        bot.send_message(message.chat.id,"не правилно напишите свой иин правильно")
    if(message.text.isnumeric()==False):
        bot.send_message(message.chat.id,"Напишите ИИН")    
    


bot.polling(none_stop=True)
