from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume


def get_volume_controller():

    speakers = AudioUtilities.GetSpeakers()

    interface = speakers._dev.Activate(
        IAudioEndpointVolume._iid_,
        CLSCTX_ALL,
        None
    )

    volume = cast(
        interface,
        POINTER(IAudioEndpointVolume)
    )

    return volume


def volume_up():

    volume = get_volume_controller()

    current = volume.GetMasterVolumeLevelScalar()

    volume.SetMasterVolumeLevelScalar(
        min(1.0, current + 0.1),
        None
    )

    return "Volume increased"


def volume_down():

    volume = get_volume_controller()

    current = volume.GetMasterVolumeLevelScalar()

    volume.SetMasterVolumeLevelScalar(
        max(0.0, current - 0.1),
        None
    )

    return "Volume decreased"


def mute_volume():

    volume = get_volume_controller()

    volume.SetMute(1, None)

    return "Volume muted"


def unmute_volume():

    volume = get_volume_controller()

    volume.SetMute(0, None)

    return "Volume unmuted"