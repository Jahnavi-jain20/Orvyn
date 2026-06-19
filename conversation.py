
history = []


def add(role, text):

    history.append(

        {

            "role": role,

            "text": text

        }

    )

    # Keep only last 10 messages

    if len(history) > 10:

        history.pop(0)


def build():

    prompt = ""

    for item in history:

        prompt += (

            f"{item['role']}: "

            f"{item['text']}\n"

        )

    return prompt


def clear():

    history.clear()
