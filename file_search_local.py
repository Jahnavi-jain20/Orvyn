import os


# ============================================================
# COMMON SEARCH LOCATIONS
# ============================================================

SEARCH_PATHS = [

    os.path.join(os.path.expanduser("~"), "Desktop"),

    os.path.join(os.path.expanduser("~"), "Documents"),

    os.path.join(os.path.expanduser("~"), "Downloads"),

    os.path.join(os.path.expanduser("~"), "Pictures"),

    os.path.join(os.path.expanduser("~"), "Music"),

    os.path.join(os.path.expanduser("~"), "Videos"),

]


# ============================================================
# QUICK SEARCH
# ============================================================

def find_file(filename):

    filename = filename.lower().strip()

    for base in SEARCH_PATHS:

        if not os.path.exists(base):
            continue

        try:

            for root, dirs, files in os.walk(base):

                for file in files:

                    if filename in file.lower():

                        return os.path.join(root, file)

        except Exception:

            continue

    return None