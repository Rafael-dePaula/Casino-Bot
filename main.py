from helper.roulette_helpers import get_dozens
from telegram.notifier import Notifier
from telegram.server import Server
from telegram.casinobot import CasinoBot
from threading import Thread

bot = CasinoBot()
polling = Thread(target=bot.polling)
polling.start()

Notifier.bot = bot

app = Server()
