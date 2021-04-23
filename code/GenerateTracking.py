import mediapipe as mp
from HandTrackingModule import *
import sys




def tracking(img):
    detector = HandDetector()
    img = detector.findHands(img)
    lmList= detector.findPosition(img)

    if len(lmList) !=0:
        focusHand = detector.focusHand(img, lmList)
        cv2.imshow("focusHand", focusHand)

    return img

def tracking_points(img):
    detector = HandDetector()
    img = detector.findHands(img)
    lmList= detector.findPosition(img)

    if len(lmList) !=0:

        cx, cy = lmList[0][1:]
        cv2.circle(img, (cx, cy), 10, (0, 0, 255), cv2.FILLED)
        cx, cy = lmList[4][1:]
        cv2.circle(img, (cx, cy), 10, (0, 255, 0), cv2.FILLED)
        cx, cy = lmList[8][1:]
        cv2.circle(img, (cx, cy), 10, (255, 0, 255), cv2.FILLED)
        cx, cy = lmList[12][1:]
        cv2.circle(img, (cx, cy), 10, (0, 255, 255), cv2.FILLED)
        cx, cy = lmList[16][1:]
        cv2.circle(img, (cx, cy), 10, (0, 0, 0), cv2.FILLED)
        cx, cy = lmList[20][1:]
        cv2.circle(img, (cx, cy), 10, (255, 0, 0), cv2.FILLED)

        focusHand = detector.focusHand(img, lmList)
        cv2.imshow("focusHand", focusHand)

    return img



def video(mode_tracking="tracking"):
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    while True:
        sucess, img = cap.read()
        if mode_tracking == "tracking_point":
            img = tracking_points(img)
        else:
            img = tracking(img)

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        cv2.putText(img, str(int(fps)), (10, 70),cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)


def img(img, mode_tracking="tracking", path_default=True):
    img = cv2.imread(img)

    if mode_tracking == "tracking_point":
        img = tracking_points(img)
    else:
        img = tracking(img)
    if path_default:
        cv2.imwrite('./dir_tmp/opencv'+str(0)+'.png', img)
    else:
        cv2.imwrite("./test.jpg", img)


if __name__ == '__main__':
    video()
    #img(sys.argv[1])


