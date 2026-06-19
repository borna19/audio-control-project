import math
import numpy as np
import cv2


class GestureControl:

    def volume_gesture(self, img, lmList, volumeControl):

        if len(lmList) == 0:
            return

        # Thumb tip
        x1, y1 = lmList[4][1], lmList[4][2]

        # Index finger tip
        x2, y2 = lmList[8][1], lmList[8][2]

        # Center point
        cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

        # Draw circles
        cv2.circle(img, (x1, y1), 10, (255, 0, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 10, (255, 0, 255), cv2.FILLED)

        # Draw line
        cv2.line(img, (x1, y1), (x2, y2), (255, 0, 255), 3)

        # Draw center point
        cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)

        # Distance between fingers
        length = math.hypot(x2 - x1, y2 - y1)

        # Convert distance to volume
        vol = np.interp(
            length,
            [30, 200],
            [volumeControl.minVol, volumeControl.maxVol]
        )

        # Volume percentage
        volPer = np.interp(length, [30, 200], [0, 100])

        # Volume bar
        volBar = np.interp(length, [30, 200], [400, 150])

        # ---------------- MUTE FEATURE ---------------- #

        # If fingers very close -> mute

        if length < 25:

            volumeControl.volume.SetMute(1, None)

            cv2.putText(
                img,
                "MUTED",
                (200, 100),
                cv2.FONT_HERSHEY_SIMPLEX,
                1,
                (0, 0, 255),
                3
            )

        else:

            # Unmute
            volumeControl.volume.SetMute(0, None)

            # Set volume
            volumeControl.set_volume(vol)

        # ---------------- VOLUME BAR UI ---------------- #

        cv2.rectangle(
            img,
            (50, 150),
            (85, 400),
            (0, 255, 0),
            3
        )

        cv2.rectangle(
            img,
            (50, int(volBar)),
            (85, 400),
            (0, 255, 0),
            cv2.FILLED
        )

        cv2.putText(
            img,
            f'{int(volPer)} %',
            (40, 450),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            3
        )