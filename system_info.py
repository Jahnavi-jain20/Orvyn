import psutil

import socket

import platform


def cpu_usage():

    return (

        f"CPU Usage: "

        f"{psutil.cpu_percent()}%"

    )


def ram_usage():

    ram = psutil.virtual_memory()

    return (

        f"RAM Usage: "

        f"{ram.percent}%"

    )


def disk_usage():

    disk = psutil.disk_usage("/")

    return (

        f"Disk Usage: "

        f"{disk.percent}%"

    )


def ip_address():

    ip = socket.gethostbyname(

        socket.gethostname()

    )

    return (

        f"IP Address: {ip}"

    )


def system_name():

    return (

        platform.system()

        + " "

        + platform.release()

    )