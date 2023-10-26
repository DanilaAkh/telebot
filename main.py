from aiogram import Dispatcher, Bot
import asyncio

from handlers.user_commands import router
from data.auth_data import TOKEN


async def main():
    bot = Bot(TOKEN)
    dp = Dispatcher()

    dp.include_router(router)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)
    
if __name__ == "__main__":
    asyncio.run(main())