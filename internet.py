import requests


def check_internet():

    try:

        requests.get(

            "https://www.google.com",

            timeout=5

        )

        return "You are connected to the internet."

    except requests.ConnectionError:

        return "No internet connection detected."

    except Exception:

        return "Unable to determine internet status."