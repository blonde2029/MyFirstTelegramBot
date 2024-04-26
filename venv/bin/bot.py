import telebot
import numpy as np
import tarotDeck
bot = telebot.TeleBot('6721762272:AAEp01-ATOQrrIHvAREPS9NLq5WDfRPRE8k')

from telebot import types
@bot.message_handler(commands=['start'])
def start(message):
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = types.KeyboardButton("Pick a card")
    markup.add(btn1)
    bot.send_message(message.from_user.id, "Check your destiny", reply_markup=markup)
@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'Pick a card':
        deck = np.random.permutation(78)
        card = tarotDeck.taroDeck.returnCard(deck)
        #print(card)
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        #btn1 = types.KeyboardButton("How to become an author on Habr.com")
        #btn2 = types.KeyboardButton("Site rules")
        #btn3 = types.KeyboardButton("Clues on how to make a post")
        #markup.add(btn1, btn2, btn3)
        bot.send_message(message.from_user.id, card)
    elif message.text == 'How to become an author on Habr.com':
        bot.send_message(message.from_user.id, "Make a post and publish it")
    elif message.text == 'Site rules':
        bot.send_message(message.from_user.id, "Rule #1 - don't talk about club")
    elif message.text == 'Clues on how to make a post':
        bot.send_message(message.from_user.id, "Just make a goddamn post!")
bot.polling(none_stop=True, interval=0)




