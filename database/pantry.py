from . import helper
from database.models import *
from operator import itemgetter
import requests


class Pantry:
    base_url, token = itemgetter('BASE_URL', 'TOKEN')(helper.get_configs())

    @classmethod
    def get_game(cls, game: str) -> Game:
        url = f'{cls.base_url}{cls.token}/basket/{game}'
        with requests.get(url) as res:
            game_loaded = Game(**res.json())
            return game_loaded

    @classmethod
    def inscribe_chat(cls, game: str, chat_id: str) -> None:
        if cls.get_game(game).is_inscribe(chat_id):
            return

        url = f'{cls.base_url}{cls.token}/basket/{game}'
        with requests.put(url, json={"registered_chats": [f"{chat_id}"]}):
            return

    @classmethod
    def add_on_history(cls, game: str, item: any) -> None:
        url = f'{cls.base_url}{cls.token}/basket/{game}'
        with requests.put(url, json={"history": [item]}):
            return

