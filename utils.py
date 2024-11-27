import asyncio
from telegram.ext import ApplicationBuilder
import os
from dotenv import load_dotenv

load_dotenv()

TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]
application = ApplicationBuilder().token(TELEGRAM_API_KEY).build()


async def send_reminder(chat_id, reminder_text):
    await application.bot.send_message(
        chat_id=chat_id, text=f"Recordatorio: {reminder_text}"
    )


def send_reminder_sync(chat_id, reminder_text):
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(send_reminder(chat_id, reminder_text))
