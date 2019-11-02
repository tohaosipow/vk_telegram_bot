import logging
import threading
import time
from chatbot.clients.message import Message


class Bot(object):

    def messageHandler(self, message, client):
        m = message
        if message.content in self.routes:
            response = self.routes[message.content](message, client)
        else:
            response = self.routes['default'](message, client)
        if(type(response) is str):
            client.sendMessage(Message(content=response, fromUser=message.toUser, toUser=message.fromUser))

    def __init__(self, clients):
        self.routes = dict([])
        for client in clients:
            x = threading.Thread(target=client.recieveMessage, args=(self,))
            x.start()
 
    def message(self, message):
        def wrapper(f):
            self.routes[message] = f
            return f
        return wrapper
