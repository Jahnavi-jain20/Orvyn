import pyttsx3
import threading

_tts_lock = threading.Lock()


def speak(text):

    if not text:

        return

    with _tts_lock:

        try:

            # Create a NEW engine every time
            engine = pyttsx3.init()

            engine.setProperty("rate", 180)

            voices = engine.getProperty("voices")

            if len(voices) > 1:

                engine.setProperty(

                    "voice",

                    voices[1].id

                )

            engine.say(str(text))

            engine.runAndWait()

            engine.stop()

        except Exception as e:

            print(e)


def stop_speaking():

    # pyttsx3 cannot reliably stop a temporary engine.
    # Keep this empty for now.

    pass