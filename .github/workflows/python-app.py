import telebot
from telebot import types
from random import randrange

Token = '5750388095:AAE_EUvhisYyL8SJ5S8QqIoYowa3ruhKmlQ'

bot = telebot.TeleBot(Token, parse_mode=None)


@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("✊ Камень")
    btn2 = types.KeyboardButton("✌️ Ножницы")
    btn3 = types.KeyboardButton("💸 Бумага")

    markup.add(btn1, btn2,btn3)
    bot.send_message(message.chat.id,text="Привет я бот 'Камень, ножницы, бумага', рано или позно я получу ИИ и выйграю тебя, сейчас я слишком глуп =) \n Что бы играть тыкай кнопки".format(message.from_user), reply_markup=markup)


@bot.message_handler(content_types=['text'])
def func(message):
    # генерируем рандомный ответ
    bot_answer =  randrange(0,3)
     
    # для удобства выносим тексты сообщений
    msg_paper ='Мой ответ 💵 Бумага 💵'
    msg_rock ='Мой ответ ✊ Камень ✊ '
    msg_sis ='Мой ответ ✌️ Ножницы ✌️  '

    msg_v = 'Ты победил!!!!!!Опять ты выйграл, тебя невозможно победить'
    msg_f = 'Ты проиграл!!!!!!Попробуй еще раз!'
    msg_n = 'Таки ничья! Давай еше раз!'


    if (message.text == "✌️ Ножницы") and bot_answer==0:
        bot.send_message(message.chat.id, f'{msg_rock}\n{msg_f}'.format(message.from_user), parse_mode='html')
    elif (message.text == "✌️ Ножницы") and bot_answer==1:
        bot.send_message(message.chat.id, f'{msg_paper}\n{msg_v}'.format(message.from_user), parse_mode='html')
    elif (message.text == "✌️ Ножницы") and bot_answer==2:
        bot.send_message(message.chat.id, f'{msg_sis}\n{msg_n}'.format(message.from_user), parse_mode='html')

    elif (message.text == "✊ Камень") and bot_answer==0:
        bot.send_message(message.chat.id, f'{msg_rock}\n{msg_n}'.format(message.from_user), parse_mode='html')
    elif (message.text == "✊ Камень") and bot_answer==1:
        bot.send_message(message.chat.id, f'{msg_paper}\n{msg_f}'.format(message.from_user), parse_mode='html')
    elif (message.text == "✊ Камень") and bot_answer==2:
        bot.send_message(message.chat.id, f'{msg_sis}\n{msg_v}'.format(message.from_user), parse_mode='html')

    elif (message.text == "💸 Бумага") and bot_answer==0:
        bot.send_message(message.chat.id, f'{msg_rock}\n{msg_v}'.format(message.from_user), parse_mode='html')
    elif (message.text == "💸 Бумага") and bot_answer==1:
        bot.send_message(message.chat.id, f'{msg_paper}\n{msg_n}'.format(message.from_user), parse_mode='html')
    elif (message.text == "💸 Бумага") and bot_answer==2:
        bot.send_message(message.chat.id, f'{msg_sis}\n{msg_f}'.format(message.from_user), parse_mode='html')

 


bot.polling(none_stop=True)


