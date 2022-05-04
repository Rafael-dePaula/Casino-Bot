from database.pantry import Pantry
from helper import regex


class Notifier:
    bot = None

    @classmethod
    def get_message(cls, game: str, message_name: str):
        try:
            return Pantry.get_game(game).messages[message_name]
        except Exception as e:
            print("message not found? : ", e)
            return None

    @classmethod
    def send_message(cls, game: str, message_name: str, **kwargs):
        message_template = cls.get_message(game, message_name)
        if message_template is None:
            return
        message = regex.sub_map(message_template, **kwargs)
        cls.bot.send_message_for_registered(game, message)

