import chatbot
from chatbot.clients.bot import Bot
from chatbot.clients.vk_client import VkClient
from chatbot.clients.telegram_client import TelegramClient
from chatbot.clients.message import Message

vk_token = ''
tg_token = ''
bot = Bot((VkClient(access_token=vk_token), TelegramClient(tg_token)))


@bot.message('привет')
def onHello(message, client):
    return 'Привет! Как дела?'


@bot.message('default')
def default(message, client):
    return 'Я не знаю ответа на этот вопрос.'
