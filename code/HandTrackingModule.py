import mediapipe as mp
import time
import cv2

class HandDetector():
    def __init__(self, mode=False, maxHands=2, detectionCon=0.5, trackCon=0.5):
        self.mode = mode
        self.maxHands = maxHands
        self.dectectionCon = detectionCon
        self.trackCon = trackCon

        self.mpHands = mp.solutions.hands
        self.hands = self.mpHands.Hands(self.mode, self.maxHands, self.dectectionCon, self.trackCon)
        self.mpDraw = mp.solutions.drawing_utils
        self.cpt = 0

    def findHands(self, img, draw=True, onlyTracking=False):
        imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.hands.process(imgRGB)
        if self.results.multi_hand_landmarks:
            for handLms in self.results.multi_hand_landmarks:
                if draw:
                    if onlyTracking:
                        img = np.zeros((200,200,3), np.uint8)
                        self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                    else:
                        self.mpDraw.draw_landmarks(img, handLms, self.mpHands.HAND_CONNECTIONS)
                    

        return img


    def findPosition(self, img, handNo=0, draw=False, csv=False):
        lmList = []
        if self.results.multi_hand_landmarks:
            myhand = self.results.multi_hand_landmarks[handNo]
            for id, lm in enumerate(myhand.landmark):
                if csv: 
                    lmList.append((id, lm.x, lm.y, lm.z))
                else:
                    h, w, c = img.shape
                    cx, cy= int(lm.x * w), int(lm.y * h)
                    lmList.append((id, cx, cy))
                    if draw:
                        cv2.circle(img, (cx, cy), 15, (255,0,255), cv2.FILLED)
        return lmList

    def focusHand(self, img, lmList):
        padding = 200
        cx, cy = lmList[9][1:]
        focusHand = img[cy-padding:cy+padding, cx-padding:cx+padding]
        return focusHand

