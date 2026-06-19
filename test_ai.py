from ai import ask_gemini

while True:

    user = input("You: ")

    if user.lower() == "exit":
        break

    reply = ask_gemini(user)

    print("\nOrvyn:", reply)
    print()