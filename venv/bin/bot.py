import os.path
import random
import telebot
import tarotDeck

bot = telebot.TeleBot('6721762272:AAEp01-ATOQrrIHvAREPS9NLq5WDfRPRE8k')
from telebot import types

@bot.message_handler(commands=['start'])
def start(message):
    sticker_path = os.path.join(os.getcwd(),'resources', 'tarot_picture.png')
    bot.send_photo(message.from_user.id, open(sticker_path, 'rb'))
    markup = types.ReplyKeyboardMarkup(resize_keyboard=False)
    btn1 = types.KeyboardButton(text='ВЫТЯНУТЬ КАРТУ')
    markup.add(btn1)
    bot.send_message(message.from_user.id, '<b>Узнай свою судьбу</b>', reply_markup=markup, parse_mode='html')
    global deck
    deck = random.sample(range(0,78),78)


@bot.message_handler(content_types=['text'])
def get_text_message(message):
    if message.text == 'ВЫТЯНУТЬ КАРТУ':
        randomCardIndex = deck[random.randint(0, len(deck)-1)]
        print(randomCardIndex)
        card = tarotDeck.taroDeck.returnCard(deck, randomCardIndex)
        deck.remove(randomCardIndex)
        print(deck)
        bot.send_message(message.from_user.id, card)
    elif message.text == 'Как это работает':
        bot.send_message(message.from_user.id, "Что такое карты Таро")
bot.polling(none_stop=True, interval=0)




