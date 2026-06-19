
import time

from google import genai

from config import GEMINI_API_KEY
from conversation import add, build


# ==========================================================
# GEMINI CLIENT
# ==========================================================

client = genai.Client(api_key=GEMINI_API_KEY)


# ==========================================================
# SYSTEM PROMPT
# ==========================================================

SYSTEM_PROMPT = """
You are Orvyn.

You are an AI desktop assistant developed by Jahnavi.

You help with coding, studies, research, productivity,
laptop automation, career guidance, and general conversations.

Never mention Gemini or Google AI.

Always identify yourself as Orvyn.

Keep answers concise by default.

If the user requests a detailed explanation,
respond step by step.

If asked who created you, answer:

"I was developed by Jahnavi."
"""


# ==========================================================
# ASK GEMINI
# ==========================================================

def ask_gemini(query):

    # Save user message
    add("User", query)

    prompt = f"""

{SYSTEM_PROMPT}

Conversation:

{build()}

Assistant:

"""

    reply = None

    # Retry up to 3 times for temporary rate limits
    for attempt in range(3):

        try:

            response = client.models.generate_content(

                model="gemini-2.5-flash",

                contents=prompt

            )

            reply = response.text

            break

        except Exception as e:

            error = str(e)

            print("Gemini Error:", error)

            # Temporary rate limit
            if "429" in error:

                if attempt < 2:

                    print("Retrying after 40 seconds...")

                    time.sleep(40)

                    continue

                reply = (
                    "⚠️ I'm temporarily being rate-limited by the AI service.\n\n"
                    "Please wait about a minute and try again."
                )

            # Server busy
            elif "503" in error:

                reply = (
                    "⚠️ The AI service is currently experiencing high demand.\n\n"
                    "Please try again in a few moments."
                )

            # Any other error
            else:

                reply = (
                    "⚠️ I couldn't connect to the AI service.\n\n"
                    f"Details:\n{error}"
                )

            break

    # Save assistant reply
    add("Orvyn", reply)

    return reply
