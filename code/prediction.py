from HandTrackingModule import *
import mediapipe as mp
import pandas as pd
import pickle
import numpy as np
import time

with open('model_coord_finger.sav', 'rb') as model:
    model = pickle.load(model)
def detection(img):
    with open('model_coord_finger.sav', 'rb') as model:
        model = pickle.load(model)
    detector = HandDetector()

    img = detector.findHands(img)
    lmlist = detector.findPosition(img, csv=True)
    d = {}
    if lmlist != 0:
        for i in lmlist:
            finger = i[0]
            x = i[1]
            y = i[2]
            z = i[3]
            d[str(finger)+"x"] = x
            d[str(finger)+"y"] = y
            d[str(finger)+"z"] = z   
        
        df = pd.DataFrame([d])
        l = np.array(df.head(1))
        try:
            predict = model.predict(l)
            return predict
        except:
            return None



def video():
    pTime = 0
    cTime = 0
    cap = cv2.VideoCapture(0)
    while True:
        sucess, img = cap.read()
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime

        predict = detection(img)
        if  predict != None:
            cv2.putText(img, str(predict[0]), (10, 100),cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255), 3)

        cv2.putText(img, str(int(fps)), (10, 70),cv2.FONT_HERSHEY_PLAIN, 3,(255,0,255), 3)
        cv2.imshow("Image", img)
        cv2.waitKey(1)

video()