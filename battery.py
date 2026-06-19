
import psutil


def battery_info():

    battery = psutil.sensors_battery()

    if battery is None:

        return "Battery information is not available."

    status = (
        "charging"
        if battery.power_plugged
        else "not charging"
    )

    return (
        f"Your battery is at "
        f"{battery.percent} percent "
        f"and is currently {status}."
    )
