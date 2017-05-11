import telebot
from src.definitions import BOT_TOKEN

bot = telebot.TeleBot(BOT_TOKEN)


@bot.message_handler(commands=['start', 'help'])
def welcome_sender(message):
    bot.send_message(message.chat.id, "Здрасте, это бот, который считает длину вашего ( ͡° ͜ʖ ͡°) сообщения.")


@bot.message_handler(func=lambda message: True)
def length_sender(message):
    bot.send_message(message.chat.id, "Ваше сообщение вместило {} символов".format(len(message.text)))


if __name__ == '__main__':
    bot.polling(none_stop=True)
    