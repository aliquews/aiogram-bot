from aiogram import F, Router
from aiogram.dispatcher.filters import Command
from aiogram.types import Message,CallbackQuery

from keyboards.checkin import get_checkin_kb
from middlewares.weekend import WeekendMessageMiddleware

router = Router()
router.message.filter(F.chat.type.in_({"private", "group", "supergroup"}))
router.message.middleware(WeekendMessageMiddleware())


@router.message(Command(commands=['check']))
async def cmd_checkin(message: Message):
    await message.answer(
        "Пожалуйста, нажми на кнопку ниже",
        reply_markup=get_checkin_kb()
    )
@router.callback_query(
    text='confirm'
)
async def checkin_confirm(callback: CallbackQuery):
    await callback.answer(
        "Спасибо, подтверждено!",
        #show_alert=True
    )
