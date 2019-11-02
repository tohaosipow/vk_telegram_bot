from chatbot.clients.base_client import BaseClient
from chatbot.clients.message import Message
import telebot
from telebot import apihelper


class TelegramClient(BaseClient):
    def __init__(self, access_token):
        self.telebot = telebot.TeleBot(access_token)
        apihelper.proxy = {'https': 'https://36.83.66.97:8080'}
        pass

    def sendMessage(self, message):
        self.telebot.send_message(message.toUser, message.content)
        pass

    def recieveMessage(self, handler):
        def on_message(message):
            fromUser = message.from_user.id
            text = message.text
            handler.messageHandler(Message(text, fromUser, None), self)
            pass
        self.telebot.message_handler(func=lambda message: True)(on_message)
        self.telebot.polling()
        pass
