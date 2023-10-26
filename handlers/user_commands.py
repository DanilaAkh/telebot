from aiogram import Router, types
from aiogram.filters import Command


router = Router()

@router.message(Command("start"))
async def start_command(message: types.Message):
    await message.answer("Привет, я эхо бот")

@router.message()
async def start_command(message: types.Message):
    await message.answer(message.text)