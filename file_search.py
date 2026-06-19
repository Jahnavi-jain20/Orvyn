import os

SEARCH_PATHS = [

    os.path.expanduser("~/Desktop"),
    os.path.expanduser("~/Documents"),
    os.path.expanduser("~/Downloads")

]


def find_file(filename):

    for base in SEARCH_PATHS:

        for root, dirs, files in os.walk(base):

            for file in files:

                if filename.lower() == file.lower():

                    return os.path.join(root, file)

    return None