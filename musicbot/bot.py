import asyncio
import logging
from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
import ffmpeg

API_TOKEN = "8886685360:AAEVYpm4Q5cm6uKpaIDOEkWQUd6Fal_UKtk"
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

@dp.message(Command("start"))
async def start_cmd(message: types.Message):
    await message.answer("Привет! Бот готов работать с аудио/видео 🎥")

@dp.message(Command("info"))
async def info_cmd(message: types.Message):
    # Проверка, что FFmpeg доступен
    try:
        ffmpeg_version = await asyncio.create_subprocess_exec(
            "ffmpeg", "-version", 
            stdout=asyncio.subprocess.PIPE, 
            stderr=asyncio.subprocess.PIPE
        )
        stdout, _ = await ffmpeg_version.communicate()
        version_str = stdout.decode().split("\n")[0]
        await message.answer(f"FFmpeg работает: {version_str}")
    except Exception as e:
        await message.answer(f"Ошибка: {e}")

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())