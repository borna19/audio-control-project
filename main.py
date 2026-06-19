import cv2

from hand_tracker import HandTracker
from volume_controller import VolumeControl
from gesture_control import GestureControl


cap = cv2.VideoCapture(0)

tracker = HandTracker()

volumeControl = VolumeControl()

gesture = GestureControl()

while True:

    success, img = cap.read()

    if not success:
        break

    img = cv2.flip(img, 1)

    img = tracker.find_hands(img)

    lmList = tracker.find_position(img)

    gesture.volume_gesture(
        img,
        lmList,
        volumeControl
    )

    cv2.putText(
        img,
        "AI AUDIO CONTROL",
        (150, 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (255, 255, 255),
        3
    )

    cv2.imshow("Audio Control", img)

    key = cv2.waitKey(1)

    if key == 27:
        break

cap.release()

cv2.destroyAllWindows()