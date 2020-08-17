import datetime
from os import remove
from sys import argv

import telebot
from telebot import types

from const import ID, TOKEN


class Bot(object):
    def __init__(self):
        self.bot = telebot.TeleBot(TOKEN)
    def start(self):
        @self.bot.message_handler(commands=['help', 'start'])
        def greet(message):
            print("Char ID: {}".format(message.chat.id))
            self.bot.send_message(message.chat.id, 'Hello!')

        self.bot.polling();

    def sendMsg(text):
        self.bot.send_message(ID, text)

    def sendPhoto(photo):
        self.bot.send_photo(ID, photo)
