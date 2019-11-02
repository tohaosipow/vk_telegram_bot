import vk_api
import random
from vk_api.longpoll import VkLongPoll, VkEventType
from chatbot.clients.base_client import BaseClient
from chatbot.clients.message import Message


class VkClient(BaseClient):
    def __init__(self, access_token):
        self.vk = vk_api.VkApi(token=access_token)
        self.longpoll = VkLongPoll(self.vk)

    def sendMessage(self, message):
        params = {'user_id': message.toUser, 'message': message.content, 'random_id': random.randint(1, 1000000)}
        return self.vk.method('messages.send', params)

    def recieveMessage(self, handler):
        for event in self.longpoll.listen():
            if event.type == VkEventType.MESSAGE_NEW and event.to_me:
                handler.messageHandler(Message(event.text, event.user_id, None), self)
