import datetime
from fastapi import APIRouter
from database.pantry import Pantry
from helper.roulette_helpers import get_dozens
from telegram import pattern
from telegram.notifier import Notifier
from .models.history_models import RouletteModel


router = APIRouter()

last_time = {
    'roulette': None
}


@router.post('/roulette/')
async def set_number(roulette: RouletteModel):
    print(roulette)
    Pantry.add_on_history('roulette', roulette.number)
    res = pattern.add_item('roulette', roulette.number)
    res["status"] = "success"
    dozens = get_dozens(res['dozen'])
    dozens['n'] = "5"
    Notifier.send_message('roulette', res['notifier'], **dozens)
    return res
