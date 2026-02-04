import asyncio
from Token import Telegram_token
from aiogram import Bot, Dispatcher
from Handlers import router as start_router
import logging

bot = Bot(token=Telegram_token)
dp = Dispatcher()

async def main():
    logging.basicConfig(level=logging.INFO)
    dp.include_router(start_router)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())