import cv2
import mediapipe as mp
import time
import numpy as np

#first experiment with handtracking, re-used bits for final project

window = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands() ##only uses RGB images so needs to be converted
mpDraw = mp.solutions.drawing_utils


pTime = 0 #previous
cTime = 0 #current


while True:

    success, img = window.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    
    
    
    ##print(results.multi_hand_landmarks) #shows what data the mediapipe solution is getting
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                #print(id, lm)
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y * h)
                print(id, cx, cy)

                

                
                #if id == 4:
                    #cv2.circle(img, (cx, cy), 15, (255, 0, 255), cv2.FILLED)
                    #print("Test")
                
                

                   
               
                
                

            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)


            


            

            #can put these landmarks in a list, or any other number of variables to manipulate

            #now how to use these values


    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_PLAIN, 3, 3)


    cv2.imshow("Image", img)
    cv2.waitKey(1)


### ABOVE IS THE BASE HANDTRACKING CODE MODULE

