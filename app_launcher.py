import os
import subprocess

COMMON_PATHS = [

    os.path.expandvars(r"%ProgramFiles%"),

    os.path.expandvars(r"%ProgramFiles(x86)%"),

    os.path.expandvars(r"%LOCALAPPDATA%"),

    os.path.expandvars(r"%APPDATA%")

]


def open_installed_app(app_name):

    app_name = app_name.lower()

    for base in COMMON_PATHS:

        for root, dirs, files in os.walk(base):

            for file in files:

                if file.lower().endswith(".exe"):

                    if app_name in file.lower():

                        path = os.path.join(root, file)

                        subprocess.Popen(path)

                        return f"Opening {file.replace('.exe', '')}."

    return None