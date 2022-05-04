from pydantic import BaseModel


class RoulettePattern:
    class HistoryItem(BaseModel):
        number: int
        dozen: int

    dozens: list[list[int]] = [[0], [*range(1, 13)], [*range(13, 25)], [*range(25, 37)]]
    observers: dict = {
        'n_of_same_dozen': []
    }

    @classmethod
    def get_dozen(cls, item: int) -> int:
        for index, dozen in enumerate(cls.dozens):
            if item in dozen:
                return index

    # Override
    @classmethod
    def add_history_item(cls, item: int) -> dict:
        new_item = cls.HistoryItem(number=item, dozen=cls.get_dozen(item))
        return cls.n_of_same_dozen(new_item)

    # Check Patterns
    @classmethod
    def n_of_same_dozen(cls, item: HistoryItem, n: int = 6) -> dict:
        observer = cls.observers['n_of_same_dozen']
        if len(observer) == 0:
            observer.append(item)
            return {"sequence_length": 1, "notifier": None, "dozen": item.dozen}

        if observer[0].dozen != item.dozen:
            islast = len(observer) == n-1
            observer.clear()
            observer.append(item)
            if islast:
                return {"sequence_length": 1, "notifier": "success_message", "dozen": item.dozen}
            return {"sequence_length": 1, "notifier": None, "dozen": item.dozen}

        observer.append(item)
        if len(observer) == n-2:
            return {"sequence_length": n-2, "notifier": "attentive_message", "dozen": item.dozen}

        if len(observer) == n-1:
            return {"sequence_length": n-1, "notifier": "play_in_next_message", "dozen": item.dozen}

        if len(observer) == n:
            observer.clear()
            return {"sequence_length": 0, "notifier": "failure_message", "dozen": item.dozen}

        return {"sequence_length": len(observer), "notifier": None, "dozen": item.dozen}


mapping_add_item = {
    "roulette": RoulettePattern.add_history_item
}


# Controller function for add items
def add_item(game: str, item: any) -> dict:
    res = mapping_add_item[game](item)
    return res
