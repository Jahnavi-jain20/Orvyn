import speech_recognition as sr

recognizer = sr.Recognizer()


def listen():

    try:

        with sr.Microphone() as source:

            print("🎤 Listening...")

            recognizer.adjust_for_ambient_noise(
                source,
                duration=0.5
            )

            audio = recognizer.listen(
                source,
                timeout=5,
                phrase_time_limit=8
            )

        text = recognizer.recognize_google(audio)

        print("You:", text)

        return text.lower()

    except sr.WaitTimeoutError:

        print("No speech detected.")

        return None

    except sr.UnknownValueError:

        print("Could not understand.")

        return None

    except sr.RequestError as e:

        print("Speech API Error:", e)

        return None

    except Exception as e:

        print("Speech Error:", e)

        return None