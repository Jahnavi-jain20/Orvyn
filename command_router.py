import os
import webbrowser
import subprocess
import ctypes
from intent_parser import detect_intent
from datetime import datetime
from file_search_local import find_file
from app_launcher import open_installed_app
from weather import get_weather
import pyautogui
from internet import check_internet
from calculator import calculate
from power_control import (
    shutdown_pc,
    restart_pc,
    sleep_pc,
    cancel_shutdown
)
import winshell
from volume_control import (
    mute_volume,
    unmute_volume,
    volume_up,
    volume_down,
    set_volume
)
from battery import battery_info
from file_manager import (
    delete_file,
    delete_folder,
    rename_item,
    move_item,
    copy_item
)
from memory import remember, recall


# ============================================================
# WEBSITE DATABASE
# ============================================================

WEBSITES = {

    "google": "https://www.google.com",

    "youtube": "https://www.youtube.com",

    "github": "https://github.com",

    "linkedin": "https://www.linkedin.com",

    "chatgpt": "https://chatgpt.com",

    "leetcode": "https://leetcode.com",

    "instagram": "https://www.instagram.com",

    "facebook": "https://www.facebook.com",

    "twitter": "https://x.com",

    "x": "https://x.com",

    "gmail": "https://mail.google.com",

    "netflix": "https://www.netflix.com",

    "amazon": "https://www.amazon.in",

    "flipkart": "https://www.flipkart.com",

    "spotify": "https://open.spotify.com",

    "canva": "https://www.canva.com",

    "figma": "https://www.figma.com",

    "stackoverflow": "https://stackoverflow.com",

    "reddit": "https://www.reddit.com",

    "wikipedia": "https://www.wikipedia.org"

}


# ============================================================
# SMART WEBSITE OPENER
# ============================================================

def open_website(name):

    name = name.lower().strip()

    if name in WEBSITES:

        url = WEBSITES[name]

    else:

        url = f"https://www.{name}.com"

    webbrowser.open(url)

    message = f"Opening {name.title()}."

    return message


# ============================================================
# GOOGLE SEARCH
# ============================================================
def open_spotify():

    try:

        subprocess.Popen("spotify")

        return "Opening Spotify."

    except Exception:

        return "Spotify is not installed."
    
def google_search(search):

    url = (
        "https://www.google.com/search?q="
        + search.replace(" ", "+")
    )

    webbrowser.open(url)

    message = f"Searching Google for {search}."

    return message


# ============================================================
# YOUTUBE SEARCH
# ============================================================

def youtube_search(search):

    url = (
        "https://www.youtube.com/results?search_query="
        + search.replace(" ", "+")
    )

    webbrowser.open(url)

    message = f"Searching YouTube for {search}."

    return message


# ============================================================
# FIXED WEBSITE COMMANDS
# ============================================================

def open_google():

    return open_website("google")


def open_youtube():

    return open_website("youtube")


def open_github():

    return open_website("github")


def open_linkedin():

    return open_website("linkedin")
# ============================================================
# APPLICATION COMMANDS
# ============================================================

def open_chrome():

    try:

        subprocess.Popen(
            r"C:\Program Files\Google\Chrome\Application\chrome.exe"
        )

        message = "Opening Chrome."

    except Exception:

        message = "Chrome is not installed."

    return message


def open_vscode():

    try:

        subprocess.Popen("code")

        message = "Opening Visual Studio Code."

    except Exception:

        message = "Visual Studio Code is not installed."

    return message


def open_notepad():

    try:

        subprocess.Popen("notepad.exe")

        message = "Opening Notepad."

    except Exception:

        message = "Unable to open Notepad."

    return message


def open_calculator():

    try:

        subprocess.Popen("calc.exe")

        message = "Opening Calculator."

    except Exception:

        message = "Unable to open Calculator."

    return message


def open_paint():

    try:

        subprocess.Popen("mspaint.exe")

        message = "Opening Paint."

    except Exception:

        message = "Unable to open Paint."

    return message


def open_file_explorer():

    try:

        subprocess.Popen("explorer.exe")

        message = "Opening File Explorer."

    except Exception:

        message = "Unable to open File Explorer."

    return message

# ============================================================
# TIME & DATE
# ============================================================

def tell_time():

    current = datetime.now().strftime("%I:%M %p")

    return f"The current time is {current}."


def tell_date():

    today = datetime.now().strftime("%d %B %Y")

    return f"Today is {today}."


# ============================================================
# SCREENSHOT
# ============================================================

def take_screenshot():

    try:

        image = pyautogui.screenshot()

        path = os.path.join(

            os.path.expanduser("~"),

            "Desktop",

            "orvyn_screenshot.png"

        )

        image.save(path)

        return "Screenshot saved on your Desktop."

    except Exception:

        return "Unable to take screenshot."


# ============================================================
# RECYCLE BIN
# ============================================================

def empty_recycle_bin():

    try:

        winshell.recycle_bin().empty(

            confirm=False,

            show_progress=False,

            sound=True

        )

        return "Recycle Bin emptied successfully."

    except Exception:

        return "Unable to empty the Recycle Bin."


# ============================================================
# LOCK COMPUTER
# ============================================================

def lock_pc():

    ctypes.windll.user32.LockWorkStation()

    return "Locking your computer."


# ============================================================
# PATH HELPER
# ============================================================

def get_location_path(location):

    home = os.path.expanduser("~")

    location = location.lower().strip()

    locations = {

        "desktop": os.path.join(home, "Desktop"),

        "downloads": os.path.join(home, "Downloads"),

        "documents": os.path.join(home, "Documents"),

        "pictures": os.path.join(home, "Pictures"),

        "music": os.path.join(home, "Music"),

        "videos": os.path.join(home, "Videos")

    }

    return locations.get(

        location,

        os.path.join(home, "Desktop")

    )


# ============================================================
# OPEN FOLDER
# ============================================================

def open_folder(location):

    try:

        path = get_location_path(location)

        os.startfile(path)

        return f"Opening {location.title()}."

    except Exception:

        return f"Unable to open {location}."


# ============================================================
# CREATE FOLDER
# ============================================================

def create_folder(name, location="Desktop"):

    try:

        base_path = get_location_path(location)

        folder_path = os.path.join(

            base_path,

            name

        )

        os.makedirs(

            folder_path,

            exist_ok=True

        )

        return f"Folder '{name}' created successfully."

    except Exception:

        return "Unable to create the folder."


# ============================================================
# CREATE TEXT FILE
# ============================================================

def create_text_file(name, location="Desktop"):

    try:

        base_path = get_location_path(location)

        file_path = os.path.join(

            base_path,

            f"{name}.txt"

        )

        with open(

            file_path,

            "w",

            encoding="utf-8"

        ):

            pass

        return f"File '{name}.txt' created successfully."

    except Exception:

        return "Unable to create the file."


# ============================================================
# MEMORY
# ============================================================

def save_memory(key, value):

    remember(

        key.lower(),

        value

    )

    return "Okay. I'll remember that."


def get_memory(key):

    value = recall(

        key.lower()

    )

    if value:

        return f"{key} is {value}"

    else:

        return "I don't have that information saved."


# ============================================================
# MAIN COMMAND EXECUTOR
# ============================================================

def execute(query):

    print("Received:", query)

    query = query.lower().strip()

    # ==========================================
# FORCE GEMINI QUESTIONS
# ==========================================

    gemini_prefixes = [

        "explain",
        
        "why",

        "how",

        "when",

        "where",

        "teach me",

        "write",

        "generate",

        "summarize",

        "compare",

        "difference between",

        "what are"

    ]

    if any(query.startswith(x) for x in gemini_prefixes):

        return None

    intent = detect_intent(query)
    # ========================================================
    # GOOGLE SEARCH
    # ========================================================

    if query.startswith("search google for"):

        search = query.replace(
            "search google for",
            ""
        ).strip()

        return google_search(search)
    
    if query.startswith("find "):

        filename = query.replace(
            "find",
            ""
        ).strip()

        path = find_file(filename)

        if path:

            os.startfile(path)

            return (
                f"I found and opened:\n"
                f"{os.path.basename(path)}"
            )

        return (
            "I couldn't find that file in the common folders "
            "(Desktop, Documents, Downloads, Pictures, Music, or Videos)."
        )

    # =====================================================
# POWER CONTROL
# =====================================================

    if query in [

    "shutdown",

    "shutdown pc",

    "shutdown computer"

    ]:

        return shutdown_pc()


    if query in [

    "restart",

    "restart pc",

    "restart computer"

]:

        return restart_pc()


    if query in [

    "sleep",

    "sleep pc",

    "sleep computer"

]:

        return sleep_pc()


    if query in [

    "cancel shutdown",

    "abort shutdown"

]:

        return cancel_shutdown()
    # ====================================================
# WEATHER
# ====================================================

    if query == "weather":

        return get_weather()


    if query == "weather today":

        return get_weather()


    if query.startswith("weather in"):

        city = query.replace(

            "weather in",

            ""

        ).strip()

        return get_weather(city)


    if query.startswith("temperature in"):

        city = query.replace(

            "temperature in",

            ""

        ).strip()

        return get_weather(city)
    # =====================================================
# CALCULATOR
# =====================================================

    if query.startswith("calculate"):

        expression = query.replace(

            "calculate",

            ""

        ).strip()

        return calculate(expression)
    
    
    # =====================================================
# INTERNET STATUS
# =====================================================

    if (
        "internet status" in query
        or "check internet" in query
        or "am i connected" in query
        or "am i connected to the internet" in query
        or "do i have internet" in query
    ):

        return check_internet()
    
    # ==========================================
# VOLUME CONTROL
# ==========================================

    if "mute volume" in query:

        return mute_volume()


    if "unmute volume" in query:

        return unmute_volume()


    if "increase volume" in query:

        return volume_up()


    if "decrease volume" in query:

        return volume_down()


    if "set volume to" in query:

        try:

            percent = int(

                query.replace(

                    "set volume to",

                    ""

                ).replace(

                    "%",

                    ""

                ).strip()

            )

            return set_volume(percent)

        except:

            return "Please specify a valid percentage."


    # ========================================================
    # YOUTUBE SEARCH
    # ========================================================

    if query.startswith("search youtube for"):

        search = query.replace(
            "search youtube for",
            ""
        ).strip()

        return youtube_search(search)



    # ========================================================
    # OPEN COMMON FOLDERS
    # ========================================================

    if "open downloads" in query:
        return open_folder("downloads")

    if "open documents" in query:
        return open_folder("documents")

    if "open desktop" in query:
        return open_folder("desktop")

    if "open pictures" in query:
        return open_folder("pictures")

    # ========================================================
    # GOOGLE SEARCH
    # ========================================================

    if intent == "google_search":

        search = query.replace(
            "search google for",
            ""
        ).strip()

        return google_search(search)

    # ========================================================
    # YOUTUBE SEARCH
    # ========================================================

    if intent == "youtube_search":

        search = query.replace(
            "search youtube for",
            ""
        ).strip()

        return youtube_search(search)

    # ========================================================
    # FIXED WEBSITES
    # ========================================================

    if intent == "open_google":
        return open_google()

    if intent == "open_youtube":
        return open_youtube()

    if intent == "open_github":
        return open_github()

    if intent == "open_linkedin":
        return open_linkedin()

    # ========================================================
    # SMART WEBSITE
    # ========================================================

    if intent == "open_website":

        website = query.replace(
            "open",
            ""
        ).strip()

        reserved = [

            "chrome",
            "spotify",
            "calculator",
            "paint",
            "notepad",
            "explorer",
            "file explorer",
            "vscode",
            "vs code"

        ]

        if website not in reserved:

            return open_website(website)

    # ========================================================
    # APPLICATIONS
    # ========================================================

    if intent == "open_chrome":
        return open_chrome()

    if intent == "open_vscode":
        return open_vscode()

    if intent == "open_spotify":
        return open_spotify()

    if "notepad" in query:
        return open_notepad()

    if "calculator" in query:
        return open_calculator()

    if "paint" in query:
        return open_paint()

    if "explorer" in query or "file explorer" in query:
        return open_file_explorer()

    # ========================================================
    # TIME & DATE
    # ========================================================

    if intent == "time":
        return tell_time()

    if intent == "date":
        return tell_date()

    # ========================================================
    # SCREENSHOT
    # ========================================================

    if intent == "take_screenshot":
        return take_screenshot()

    # ========================================================
    # RECYCLE BIN
    # ========================================================

    if intent == "empty_recycle":
        return empty_recycle_bin()

    # ========================================================
    # LOCK PC
    # ========================================================

    if intent == "lock_pc":
        return lock_pc()

    # ========================================================
    # CREATE FOLDER
    # ========================================================

    if query.startswith("create folder"):

        location = "desktop"

        for place in [
            "downloads",
            "documents",
            "pictures",
            "desktop"
        ]:

            if f"in {place}" in query:

                location = place

        name = query

        for word in [
            "create folder",
            "called",
            "named",
            "in downloads",
            "in documents",
            "in pictures",
            "in desktop"
        ]:

            name = name.replace(word, "")

        name = name.strip()

        if not name:

            return "Please provide a folder name."

        return create_folder(name, location)

    # ========================================================
    # CREATE FILE
    # ========================================================

    if query.startswith("create file"):

        location = "desktop"

        for place in [
            "downloads",
            "documents",
            "pictures",
            "desktop"
        ]:

            if f"in {place}" in query:

                location = place

        name = query

        for word in [
            "create file",
            "called",
            "named",
            ".txt",
            "in downloads",
            "in documents",
            "in pictures",
            "in desktop"
        ]:

            name = name.replace(word, "")

        name = name.strip()

        if not name:

            return "Please provide a file name."

        return create_text_file(name, location)


    # ========================================================
    # MEMORY SAVE
    # ========================================================

    if query.startswith("remember") and " is " in query:

        text = query.replace(
            "remember",
            ""
        ).strip()

        key, value = text.split(
            " is ",
            1
        )

        return save_memory(

            key.strip(),

            value.strip()

        )


    # ========================================================
    # MEMORY RECALL
    # ========================================================

    if query.startswith("what is my "):

        key = query.replace(
        "what is my",
        ""
        ).replace(
        "?",
        ""
        ).strip()

        return get_memory(key)


    if query.startswith("who is my "):

        key = query.replace(
        "who is my",
        ""
        ).replace(
        "?",
        ""
        ).strip()

        return get_memory(key)



    # ========================================================
    # NOT HANDLED
    # ========================================================
# ========================================================
# AI APP LAUNCHER
# ========================================================

    if query.startswith("open "):

        app = query.replace("open", "").strip()

        result = open_installed_app(app)

        if result:

            return result
    
    
    
    # ========================================================
# BATTERY
# ========================================================

    if "battery" in query:

        return battery_info()
        

    return None
