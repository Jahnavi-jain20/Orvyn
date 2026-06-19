import os


def shutdown_pc():

    os.system("shutdown /s /t 5")

    return "Shutting down your computer in 5 seconds."


def restart_pc():

    os.system("shutdown /r /t 5")

    return "Restarting your computer in 5 seconds."


def sleep_pc():

    os.system(
        "rundll32.exe powrprof.dll,SetSuspendState Sleep"
    )

    return "Putting your computer to sleep."


def cancel_shutdown():

    os.system("shutdown /a")

    return "Shutdown or restart cancelled."