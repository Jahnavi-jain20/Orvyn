from ctypes import POINTER, cast

from comtypes import CLSCTX_ALL

from pycaw.pycaw import (
    AudioUtilities,
    IAudioEndpointVolume
)


def get_volume():

    devices = AudioUtilities.GetSpeakers()

    interface = devices.Activate(

        IAudioEndpointVolume._iid_,

        CLSCTX_ALL,

        None

    )

    return cast(

        interface,

        POINTER(IAudioEndpointVolume)

    )


def mute_volume():

    volume = get_volume()

    volume.SetMute(1, None)

    return "Volume muted."


def unmute_volume():

    volume = get_volume()

    volume.SetMute(0, None)

    return "Volume unmuted."


def volume_up():

    volume = get_volume()

    current = volume.GetMasterVolumeLevelScalar()

    volume.SetMasterVolumeLevelScalar(

        min(current + 0.1, 1.0),

        None

    )

    return "Volume increased."


def volume_down():

    volume = get_volume()

    current = volume.GetMasterVolumeLevelScalar()

    volume.SetMasterVolumeLevelScalar(

        max(current - 0.1, 0.0),

        None

    )

    return "Volume decreased."


def set_volume(percent):

    volume = get_volume()

    percent = max(0, min(100, int(percent)))

    volume.SetMasterVolumeLevelScalar(

        percent / 100,

        None

    )

    return f"Volume set to {percent} percent."