from telegram import Update
from telegram.ext import CommandHandler, ContextTypes
from scheduler import schedule_reminder
from datetime import datetime


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text(
        "¡Hola! 🤖 Soy tu asistente para recordatorios 📝. Envía /recordar seguido del mensaje y la hora (HH:MM) para configurar un recordatorio."
    )


async def recordar(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    try:
        args = context.args
        if "a las" not in " ".join(args) or len(args) < 3:
            await update.message.reply_text(
                "👀 Formato incorrecto. Usa /recordar <mensaje> a las <HH:MM>"
            )
            return

        full_text = " ".join(args)
        reminder_text, reminder_time_str = full_text.rsplit(" a las ", 1)

        reminder_time = datetime.strptime(reminder_time_str.strip(), "%H:%M").replace(
            year=datetime.now().year, month=datetime.now().month, day=datetime.now().day
        )

        schedule_reminder(update.message.chat_id, reminder_text, reminder_time)
        await update.message.reply_text(
            f'📝 Recordatorio configurado para {reminder_time.strftime("%H:%M")}: {reminder_text}'
        )
    except Exception as e:
        await update.message.reply_text(
            f"Hubo un error al configurar el recordatorio: {e}"
        )


async def handle_invalid_command(
    update: Update, context: ContextTypes.DEFAULT_TYPE
) -> None:
    await update.message.reply_text(
        "Comando no reconocido. Por favor, usa /recordar seguido del mensaje y la hora (HH:MM) para configurar un recordatorio."
    )


start_handler = CommandHandler("start", start)
recordar_handler = CommandHandler("recordar", recordar)
