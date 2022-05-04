from telebot import TeleBot, types
from database.pantry import Pantry
TOKEN = '5387669598:AAEqp7AMKM9fJMnmsVnO6eQRZfLhdGejNMU'


class CasinoBot(TeleBot):
    def __init__(self, token: str = TOKEN):
        super().__init__(token)
        self.configure_handlers()

    def configure_handlers(self):
        @self.message_handler(commands=['start'])
        def start_handler(message: types.Message):
            chat_id = message.chat.id
            Pantry.inscribe_chat('roulette', str(chat_id))

        @self.message_handler(commands=['last'])
        def get_last(message: types.Message):
            chat_id = message.chat.id
            history = Pantry.get_game("roulette").history
            history.reverse()
            self.send_message(chat_id, f'{str(history[:10])}')

    def send_message_for_registered(self, game: str, message: str):
        for chat in Pantry.get_game(game).registered_chats:
            self.send_message(chat_id=chat, text=message, parse_mode='Markdown')

# meu_telegram: {id: 5055154404}
