from telegram.ext import ApplicationBuilder, MessageHandler, filters
from handlers import start_handler, recordar_handler, handle_invalid_command
from scheduler import scheduler
import os
from dotenv import load_dotenv

load_dotenv()

# Cargar la API key de Telegram desde el archivo .env
TELEGRAM_API_KEY = os.environ["TELEGRAM_API_KEY"]


def main():
    application = ApplicationBuilder().token(TELEGRAM_API_KEY).build()

    application.add_handler(start_handler)
    application.add_handler(recordar_handler)
    application.add_handler(
        MessageHandler(filters.TEXT & ~filters.COMMAND, handle_invalid_command)
    )
    # Iniciar el bot
    print("Bot iniciado, esperando comandos...")
    application.run_polling()


if __name__ == "__main__":
    main()
