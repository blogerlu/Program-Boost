import telebot
import config #там лежит токен, в общий доступ не могу выкладывать
from telebot import TeleBot, types
import random

import numpy as np


from lightgbm import LGBMRegressor
import lightgbm

bot = telebot.TeleBot(config.TOKEN)
print('starting bot...')

model = lightgbm.Booster(model_file='model.txt')

states = {}	
inventories = {}


data = []


def process_state(user, state):

    # стикер ПОСЛУШАЙТЕ
    if state == 0:
        print(0)
        bot.send_message(user, 'Введиете ваш класс:')  

    # Союзмульт
    elif state == 1:
        print(1)
        bot.send_message(user, 'Введите код школы:') 

    elif state == 2:
        print(1)
        bot.send_message(user, 'Ваш средний балл:')

    elif state == 3:
        print(1)
        bot.send_message(user, 'Какой предмет сдаете?') 

    elif state == 4:
        print(1)
        bot.send_message(user, 'Олимпиадник?') 

    elif state == 5:
        print(5)
        bot.send_message(user, 'Отличник?') 

    elif state == 6:
        print(6)
        # print('ball', ball)
        df = np.array(data)
        bot.send_message(user, model.predict(df))
        # bot.send_message(user, 'Ваш возможный балл: 72') 

def process_answer(user, message):


    if states[user] == 0:
        print('state 0:', message.text)
        states[user] = 1
        data.append(int(message.text))

    elif states[user] == 1:
        print('state 1:', message.text)
        states[user] = 2
        data.append(int(message.text))
    elif states[user] == 2:
        print('state 1:', message.text)
        states[user] = 3
        # ball = int(message.text)
        data.append(int(message.text))
    elif states[user] == 3:
        print('state 1:', message.text)
        states[user] = 4
        data.append(int(message.text))
    elif states[user] == 4:
        print('state 1:', message.text)
        states[user] = 5
        data.append(int(message.text))
    elif states[user] == 5:
        print('state 5:', message.text)
        states[user] = 6 
        data.append(int(message.text))
    elif states[user] == 6:
        print('state 6:', message.text)
        states[user] = 7         
        data.append(int(message.text))
    process_state(user, states[user])


@bot.message_handler(commands=["start"])
def start_game(message):
    user = message.chat.id
    print(message.location)
    states[user] = 0
    inventories[user] = []

    bot.send_message(user, "Вас приветсвует бот по ЕГЭШКА!")

    print('sending start message')

    process_state(user, states[user])


# @bot.callback_query_handler(func=lambda call: True)
# def user_answer(call):
#     user = call.message.chat.id
#     print('call')
#     # process_answer(user, call.data)


@bot.message_handler(content_types=['text'])
def send_welcome(message):
	user = message.chat.id

	print('answer')
	process_answer(user, message)



# @bot.message_handler(content_types=['location'])
# def send_welcome(message):
# 	# японский сад
# 	print(message.location)
# 	bot.send_message(message.chat.id, message.location)

def starting():

	try:
		bot.polling(none_stop=True)
	except:
		starting()	

starting()