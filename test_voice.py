from speech import listen
from tts import speak

query = listen()

if query:

    speak(f"You said {query}")

else:

    speak("Sorry, I couldn't hear you.")