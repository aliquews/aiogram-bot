from aiogram.types import ReplyKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardBuilder


def main_kb() -> ReplyKeyboardMarkup:
    kb = ReplyKeyboardBuilder()
    kb.button(text="Погода")
    kb.button(text="<Какая либо другая кнопка>")
    kb.adjust(2)
    return kb.as_markup(resize_keyboard=True)
