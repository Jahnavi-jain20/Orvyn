import json
import os

CHAT_FILE = "chat_history.json"


def load_chat():

    if not os.path.exists(CHAT_FILE):

        with open(CHAT_FILE, "w", encoding="utf-8") as f:

            json.dump([], f)

    with open(CHAT_FILE, "r", encoding="utf-8") as f:

        return json.load(f)


def save_chat(role, text):

    history = load_chat()

    history.append({

        "role": role,

        "text": text

    })

    history = history[-20:]      # Keep last 20 messages

    with open(CHAT_FILE, "w", encoding="utf-8") as f:

        json.dump(history, f, indent=4)


def build_chat():

    history = load_chat()

    prompt = ""

    for item in history:

        prompt += f"{item['role']}: {item['text']}\n"

    return prompt