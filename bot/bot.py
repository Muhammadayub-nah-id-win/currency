import asyncio
from os import getenv
from dotenv import load_dotenv
from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode

from handlers.commands import commands
from handlers.handlers import router as handler_router

load_dotenv()










TOKEN = getenv("BOT_TOKEN")

dp = Dispatcher()
dp.include_router(handler_router)


async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    await bot.set_my_commands(commands)
    await dp.start_polling(bot)



if __name__ == "__main__":
    print("Starting bot....")
    asyncio.run(main())
