import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message


from config_reader import config
from handlers import private_games, recognize_song, checkin, getw
from middlewares.weekend import WeekendCallbackMiddleware

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()



@dp.message(commands=['help'])
async def init_bot(message: Message):
    await message.answer(f"<u><b>FAQ</b></u>\nчто я могу:\n  -распознать музыку по гс\n  -найди погоду в любом городе по твоему запросу\n  на клавиатуре РАБОЧАЯ кнопка только ПОГОДА, но это пока что", parse_mode="HTML")


async def main():

    dp.include_router(getw.router)
    dp.include_router(private_games.router)
    dp.include_router(recognize_song.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
