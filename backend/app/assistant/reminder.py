import json
import os
import threading
import time

from app.assistant.speech import speak

REMINDER_FILE = "reminders.json"


def load_reminders():

    if not os.path.exists(REMINDER_FILE):
        return []

    try:
        with open(REMINDER_FILE, "r") as file:
            return json.load(file)

    except:
        return []


def save_reminders(reminders):

    with open(REMINDER_FILE, "w") as file:
        json.dump(reminders, file, indent=4)


def add_reminder(text):

    reminders = load_reminders()

    reminders.append({
        "text": text
    })

    save_reminders(reminders)


def get_reminders():

    return load_reminders()


def clear_reminders():

    save_reminders([])


def timed_reminder(minutes, task):

    def worker():

        time.sleep(minutes * 60)

        speak(f"Reminder. {task}")

    threading.Thread(
        target=worker,
        daemon=True
    ).start()