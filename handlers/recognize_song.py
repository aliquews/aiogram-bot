from shazamio import Shazam
from aiogram import Router, F
from aiogram.types import Message, File
from aiogram.methods import GetFile
from pathlib import Path
from aiogram.utils.markdown import hide_link

from app import bot

router = Router()

@router.message(F.content_type.in_({'voice',}))
async def download_voice(message: Message):
    file_id = message.voice.file_id
    file = await bot.get_file(file_id=file_id)
    file_path = file.file_path
    await bot.download_file(file_path, "files/voices/audio.oga")
    shazam = Shazam()
    try:
        res = await shazam.recognize_song('files/voices/audio.oga')
        sbj = res['track']['share']['subject']
        link = res['track']['share']['href']
        pic = res['track']['images']['background']
        await message.answer(text=f'<b>{sbj}</b>\n\n{hide_link(pic)}', parse_mode='HTML')
    except:
        await message.reply(text='К сожалению я не смог распознать данную песню')
