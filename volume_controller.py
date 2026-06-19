from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL

from pycaw.pycaw import AudioUtilities
from pycaw.pycaw import IAudioEndpointVolume


class VolumeControl:

    def __init__(self):

        speakers = AudioUtilities.GetSpeakers()

        interface = speakers.Activate(
            IAudioEndpointVolume._iid_,
            CLSCTX_ALL,
            None
        )

        self.volume = cast(
            interface,
            POINTER(IAudioEndpointVolume)
        )

        self.volRange = self.volume.GetVolumeRange()

        self.minVol = self.volRange[0]
        self.maxVol = self.volRange[1]

    def set_volume(self, vol):

        self.volume.SetMasterVolumeLevel(vol, None)