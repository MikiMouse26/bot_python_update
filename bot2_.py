import random
import telebot
    
# Инициализация бота с использованием его токена
bot = telebot.TeleBot("7954242429:AAFgG7-OFT76ztZ_n3i0eGaT-f6Ze2YBr4M")
    
# Обработчик команды '/start' и '/hello'
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, f'Привет! Я бот {bot.get_me().first_name}!')
@bot.message_handler(commands=['coin'])
def send_coin(message):
    number = random.randint(1,2)
    if number == 1:
        bot.reply_to(message,"Орел")
    if number==2:
        bot.reply_to(message,"Решка")

    
# Обработчик команды '/heh'
@bot.message_handler(commands=['heh'])
def send_heh(message):
    count_heh = int(message.text.split()[1]) if len(message.text.split()) > 1 else 5
    bot.reply_to(message, "he" * count_heh)
@bot.message_handler(commands=['la'])
def send_la(message):
    bot.reply_to(message,"lalala")


# Запуск бота
bot.polling()