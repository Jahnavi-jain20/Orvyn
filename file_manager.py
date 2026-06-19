import os
import shutil


def delete_file(path):

    try:

        os.remove(path)

        return "File deleted successfully."

    except Exception as e:

        return f"Unable to delete file. {e}"


def delete_folder(path):

    try:

        shutil.rmtree(path)

        return "Folder deleted successfully."

    except Exception as e:

        return f"Unable to delete folder. {e}"


def rename_item(old_path, new_name):

    try:

        directory = os.path.dirname(old_path)

        new_path = os.path.join(directory, new_name)

        os.rename(old_path, new_path)

        return "Renamed successfully."

    except Exception as e:

        return f"Unable to rename. {e}"


def move_item(src, dest):

    try:

        shutil.move(src, dest)

        return "Moved successfully."

    except Exception as e:

        return f"Unable to move. {e}"


def copy_item(src, dest):

    try:

        if os.path.isdir(src):

            shutil.copytree(src, dest)

        else:

            shutil.copy2(src, dest)

        return "Copied successfully."

    except Exception as e:

        return f"Unable to copy. {e}"
    
import os


def find_file(filename):

    home = os.path.expanduser("~")

    filename = filename.lower()

    for root, dirs, files in os.walk(home):

        for file in files:

            if filename in file.lower():

                return os.path.join(root, file)

    return None