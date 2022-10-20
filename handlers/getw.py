from aiogram import Router
from aiogram.types import Message
from aiogram.dispatcher.fsm.context import FSMContext
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.dispatcher.filters.text import Text


from keyboards.main_kb import main_kb
from misc.weather import getWeather

class GetWeather(StatesGroup):
    city = State()


router = Router()


@router.message(commands=["start"])
async def cmd_start(message: Message):
    await message.answer("Здравствуйте", reply_markup=main_kb())


@router.message(Text(text="Погода"))
async def cmd_weather(message: Message, state: FSMContext):
    await message.answer("Пожалуйста, укажите город")
    await state.set_state(GetWeather.city)


@router.message(state=GetWeather.city)
async def find_city(message: Message, state: FSMContext):
    await state.update_data(city=message.text.lower())
    try:
        text = getWeather(message.text.lower())
        await message.answer(text=text)
        await state.clear()
    except:
        await message.answer(text="Я не знаю такого города, попробуйте еще раз")
