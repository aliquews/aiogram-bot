import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message


from config_reader import config
from handlers import private_games, recognize_song, checkin
from middlewares.weekend import WeekendCallbackMiddleware

logging.basicConfig(level=logging.INFO)

bot = Bot(token=config.bot_token.get_secret_value())
dp = Dispatcher()



@dp.message(commands=['start'])
async def init_bot(message: Message):
    await message.answer("Привет, отправь мне голосовое сообщение с музыкой, которую ты хочешь распознать.")


async def main():

    dp.callback_query.outer_middleware(WeekendCallbackMiddleware())
    dp.include_router(private_games.router)
    dp.include_router(recognize_song.router)
    dp.include_router(checkin.router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
