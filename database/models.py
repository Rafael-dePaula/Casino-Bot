from pydantic import BaseModel


class Game(BaseModel):
    name: str
    registered_chats: list[str]
    history: list[int]
    messages: dict

    def is_inscribe(self, chat_id: str) -> bool:
        if chat_id in self.registered_chats:
            return True
        return False
