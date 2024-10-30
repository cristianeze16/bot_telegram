from apscheduler.schedulers.background import BackgroundScheduler
from utils import send_reminder_sync

scheduler = BackgroundScheduler()
scheduler.start()


def schedule_reminder(chat_id, reminder_text, reminder_time):
    scheduler.add_job(
        send_reminder_sync,
        "date",
        run_date=reminder_time,
        args=[chat_id, reminder_text],
    )
