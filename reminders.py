import json
import os


FILE = "reminders.json"


def load():

    if not os.path.exists(FILE):

        return []

    with open(

        FILE,

        "r"

    ) as f:

        return json.load(f)


def save(data):

    with open(

        FILE,

        "w"

    ) as f:

        json.dump(

            data,

            f,

            indent=4

        )


def add_reminder(text):

    reminders = load()

    reminders.append(text)

    save(reminders)

    return "Reminder saved."


def show_reminders():

    reminders = load()

    if not reminders:

        return "No reminders."

    return "\n".join(reminders)