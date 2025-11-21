import json
import time

REM_FILE = "reminders.json"

def add_reminder(text, remind_time):
    try:
        with open(REM_FILE, "r") as f:
            data = json.load(f)
    except:
        data = {}

    data[text] = remind_time

    with open(REM_FILE, "w") as f:
        json.dump(data, f, indent=4)

    return "Reminder added!"

def check_reminders():
    try:
        with open(REM_FILE, "r") as f:
            data = json.load(f)
    except:
        return "No reminders found."

    current = time.strftime("%H:%M")
    due = [text for text, t in data.items() if t == current]

    return due if due else "No reminders due now."
