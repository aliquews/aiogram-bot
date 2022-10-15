from aiogram import Router, F
from aiogram.types import Message
from aiogram.dispatcher.filters import Command


router = Router()

router.message.filter(F.chat.type.in_({"private", "group", "supergroup"}))


@router.message(
    commands=['dice'],
)
async def cmd_dice(message: Message):
    await message.answer_dice(emoji="🎲")


@router.message(
    commands=['basketball']
)
async def cmd_basketball(message: Message):
    await message.answer_dice(emoji="🏀")
