from aiogram import Router, types, F
from aiogram.filters import Command
from aiogram.types import Message
from handlers.keyboards import start_button
from utils import currency_exchange

router = Router()

@router.message(Command())
async def cmd_start(msg: types.Message):
    await msg.answer(text="Assalomu alekum!\n"
                         "Valyuta Ayirboshlash", reply_markup = start_button)



@router.message(F.text == "uz ➡️ $")
async def sum_to_usd(msg: types.Message):
    await msg.answer("Sumani kiriting")



@router.message(F.text)
async def sum_to_usd(msg: types.Message):
    summa = int(msg.text)
    kurs = await currency_exchange("USD", "UZS")
    await msg.answer(f"{summa} --> UZS = {summa * kurs} USZ")

