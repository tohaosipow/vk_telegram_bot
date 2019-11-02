from abc import ABCMeta, abstractmethod
from chatbot.clients.message import Message


class BaseClient(object):
    @abstractmethod
    def sendMessage(self, message):
        pass

    @abstractmethod
    def recieveMessage(self):
        pass
