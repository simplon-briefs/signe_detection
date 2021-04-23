from HandTrackingModule import *
import mediapipe as mp
import pandas as pd
import math
import sys
import os


def img_to_csv(img):
    categories = img.split("/")[1]
    img = cv2.imread(img)
    detector = HandDetector()

    img = detector.findHands(img)
    lmlist = detector.findPosition(img, csv=True)
    d = {}
    #lmlist = lmlist[0]
    if lmlist != 0:
        for i in lmlist:
            finger = i[0]
            x = i[1]
            y = i[2]
            z = i[3]
            d["categories"] = categories
            d[str(finger)+"x"] = x
            d[str(finger)+"y"] = y
            d[str(finger)+"z"] = z

        if os.path.exists("df.csv"):
            print(True)
            df = pd.read_csv("df.csv")
            df = df.append(d, ignore_index=True)
        else:
            df = pd.DataFrame([d])

        df.to_csv("df.csv",index=False)
        

    

if __name__ == '__main__':
    #img_to_csv("archive/A/A0001_test.jpg")
    img_to_csv(sys.argv[1])
