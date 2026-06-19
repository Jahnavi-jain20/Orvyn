import re


def normalize(query: str):

    query = query.lower().strip()

    query = re.sub(r"[^\w\s]", "", query)

    return query


def detect_intent(query):

    query = normalize(query)

    # =====================================================
    # GOOGLE
    # =====================================================

    if any(x in query for x in [

        "open google",
        "launch google",
        "start google"

    ]):

        return "open_google"

    # =====================================================
    # YOUTUBE
    # =====================================================

    if any(x in query for x in [

        "open youtube",
        "launch youtube",
        "start youtube"

    ]):

        return "open_youtube"

    # =====================================================
    # GITHUB
    # =====================================================

    if any(x in query for x in [

        "open github",
        "launch github"

    ]):

        return "open_github"

    # =====================================================
    # LINKEDIN
    # =====================================================

    if any(x in query for x in [

        "open linkedin",
        "launch linkedin"

    ]):

        return "open_linkedin"

    # =====================================================
    # CHROME
    # =====================================================

    if any(x in query for x in [

        "open chrome",
        "launch chrome",
        "start chrome"

    ]):

        return "open_chrome"

    # =====================================================
    # VS CODE
    # =====================================================

    if any(x in query for x in [

        "open vscode",
        "open vs code",
        "launch vscode",
        "launch vs code"

    ]):

        return "open_vscode"

    # =====================================================
    # SPOTIFY
    # =====================================================

    if any(x in query for x in [

        "open spotify",
        "launch spotify",
        "start spotify"

    ]):

        return "open_spotify"

    # =====================================================
    # SCREENSHOT
    # =====================================================

    if any(x in query for x in [

        "take screenshot",
        "capture screen",
        "take a screenshot"

    ]):

        return "take_screenshot"

    # =====================================================
    # RECYCLE BIN
    # =====================================================

    if any(x in query for x in [

        "empty recycle bin",
        "clear recycle bin",
        "empty the recycle bin"

    ]):

        return "empty_recycle"

    # =====================================================
    # LOCK PC
    # =====================================================

    if any(x in query for x in [

        "lock pc",
        "lock computer",
        "lock my computer"

    ]):

        return "lock_pc"

    # =====================================================
    # TIME
    # =====================================================

    if any(x in query for x in [

        "what time is it",
        "tell me the time",
        "current time"

    ]) or query == "time":

        return "time"

    # =====================================================
    # DATE
    # =====================================================

    if any(x in query for x in [

        "what is today's date",
        "todays date",
        "today date",
        "tell me the date"

    ]) or query == "date":

        return "date"

    # =====================================================
    # GOOGLE SEARCH
    # =====================================================

    if query.startswith("search google for"):

        return "google_search"

    # =====================================================
    # YOUTUBE SEARCH
    # =====================================================

    if query.startswith("search youtube for"):

        return "youtube_search"

    # =====================================================
    # SMART WEBSITE
    # =====================================================

    if query.startswith("open "):

        return "open_website"

    return None