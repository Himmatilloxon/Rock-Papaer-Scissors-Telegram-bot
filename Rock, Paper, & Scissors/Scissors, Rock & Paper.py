import telebot, random
from telebot import types

bot=telebot.TeleBot('5700382521:AAEfVr0liGRz9O8JYwFl0LzomcEHCDkRjug')

@bot.message_handler(commands=['start'])
def start(message):
    if message.from_user.last_name is True:
        salom=f'Assalomu alaykum,  <b>{message.from_user.first_name} {message.from_user.last_name}</b>'
    else:salom=f'Assalomu alaykum,  <b>{message.from_user.first_name}</b>'
    bot.send_message(message.chat.id,salom, parse_mode='html')
    describtion='Please, choose scissors, rock, or paper\nIf you need help type: /help'
    bot.send_message(message.chat.id,describtion)

@bot.message_handler(commands=['help'])
def start(message):
    markup=telebot.types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=1)
    scissors = telebot.types.KeyboardButton('scissors')
    rock = telebot.types.KeyboardButton('rock')
    paper = telebot.types.KeyboardButton('paper')

    markup.add(scissors, rock, paper)
    bot.send_message(message.chat.id, 'Choose', reply_markup=markup)

@bot.message_handler()
def text(message):

    if message.text.lower() in ['scissors', 'rock', 'paper']:
        photo1=open(f'{message.text.lower()}.jpg', 'rb')
        a=random.choice(['scissors', 'rock', 'paper'])
        if a==message.text.lower():b='Draw!'
        elif message.text.lower()=='scissors' and a=='rock':b=('you lose')
        elif a=='scissors' and message.text.lower()=='rock':b=('you win')
        elif message.text.lower()=='scissors' and a=='paper':b=('you win')
        elif a=='scissors' and message.text.lower()=='paper':b=('you lose')
        elif message.text.lower()=='rock' and a=='paper':b=('you lose')
        elif a=='rock' and message.text.lower()=='paper':b=('you win')
        photo2=open(f'{a}.jpg', 'rb')

        bot.send_message(message.chat.id, 'You chose')
        bot.send_sticker(message.chat.id, photo1)
        bot.send_message(message.chat.id, f'bot chose {a}')
        bot.send_sticker(message.chat.id, photo2)
        bot.send_message(message.chat.id, b)

bot.polling(none_stop=True)