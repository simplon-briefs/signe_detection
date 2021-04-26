from HandTrackingModule import *
import mediapipe as mp
import pandas as pd
import pickle
import numpy as np
import time
import cv2
from collections import Counter

with open('C:/Users/utilisateur/Documents/microsoft_ia/Devoirs/signe_detection/model_coord_finger.sav', 'rb') as model:
    model = pickle.load(model)
def detection(img):
    with open('C:/Users/utilisateur/Documents/microsoft_ia/Devoirs/signe_detection/model_coord_finger.sav', 'rb') as model:
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
    liste = []
    pTime = 0
    cTime = 0

    cap = cv2.VideoCapture(0)
    phrase = ""
    occurence  = ""
    while True:
        sucess, img = cap.read()
        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        
        predict = detection(img)
        if  predict != None:
            
            cv2.putText(img, str(predict[0]), (10, 100),cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255), 3)
            #On récupère les lettre
            liste += str(predict[0])
            #une fois qu'on a 15 lettre on recupère la lettre ayant le plus d'occurences puis on l'affiche à chaque boucle
            if len(liste) == 15:
                occurence = Counter(liste).most_common(1)
                #compteur = 0
                phrase += occurence[0][0]
                       
                liste = ""   
                # print(phrase)    
        cv2.putText(img, str(int(fps)), (10, 70),cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255), 3)
        cv2.putText(img, "phrase:", (10, 400),cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255), 3)
        cv2.putText(img, phrase, (10, 450),cv2.FONT_HERSHEY_PLAIN, 3,(0,0,255), 3)
        cv2.imshow("Image", img)
        
        if cv2.waitKey(1) & 0xFF == ord('q'):
            print(phrase)
            break
        

video()