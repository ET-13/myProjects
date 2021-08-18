import cv2
import time
import pyautogui
#import os
import numpy as np
import mediapipe as mp
import handtrackingmodule as htm #earlier module created that has necessary boilerplate from opencv and mediapipe libs for handtracking

windowopen = 0
#screenWidth = 1000
#screenHeight = 1000
#screenWidth, screenHeight = pyautogui.size()


if windowopen == 0:
    window = cv2.VideoCapture(0)
    
    



#folderPath = "CVImages" ##earlier iteration of this idea included comparing images of hand positions to current hand position of what's in the video frame to do x function(s)
#myList = os.listdir(folderPath)
#print(myList)
pTime = 0

detector = htm.handDetector(detectionCon=0.85)


while True:

    success, img = window.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img, draw=False) #turning the function in cv library which displays landmark points on hand, into a python list we can perform operations on
    #print(lmList)
   
    
       
     

    if len(lmList) != 0:
        indextip = lmList[8] #this gives us the position of the index tip if it's present in lmList, landmark 8
        indextiptrack = str(indextip)[3:] #this gives us the x and y coordinates nix the id
        indextiptrack2 = str(indextiptrack[:-1]) #cleans up last bracket in string
        indextiptrack3 = str(indextiptrack2[1:]) #clean up first space left over

        midtip = lmList[12]
        midtiptrack = str(indextip)[3:] #this gives us the x and y coordinates nix the id
        midtiptrack2 = str(indextiptrack[:-1]) #cleans up last bracket in string
        midtiptrack3 = str(indextiptrack2[1:])
        

        #using positional relativity in docs each landmark has list number
        if lmList[12][2] < lmList[6][2]:
            htm.counter2 = 1
            print("middle finger opened")
            print(midtiptrack3)
            print(indextiptrack3)
        
        elif lmList[12][2] > lmList[6][2]:
            htm.counter2 = 0
            print("middle finger closed")

        if lmList[8][2] < lmList[6][2]: #if point 8 [index tip] (relative to point 2) is lower than positional point 6 (relative to 2), we infer index finger is not out
            htm.counter = 1
            print("index finger opened") 
            print(indextiptrack3)
         
           
           
              
           
            if htm.counter == 1: #if instead of while worked better
                fingertiptrackercoord1 = indextiptrack3[0:3] #removing each individual coord from list of xy
                fingertiptrackercoord2 = indextiptrack3[5:8]
                print(fingertiptrackercoord1)
                print(fingertiptrackercoord2)
                intfingertiptrackercoord1 = int(fingertiptrackercoord1)
                intfingertiptrackercoord2 = int(fingertiptrackercoord2)
                #inttest = int(str(fingertiptrackercoord1))
                #print(inttest)
                ##need to insert each divided coord into mouse function as x y
              

                #pyautogui.dragTo(intfingertiptrackercoord1,intfingertiptrackercoord2, duration=.1)
                pyautogui.moveTo(intfingertiptrackercoord1, intfingertiptrackercoord2, duration=.1, tween=pyautogui.easeInOutQuad)   #tracks every 10th of a second, tween function eases it so it wont literally track every single coord input but every other and so on
                

            if htm.counter2 == 1 and htm.counter == 1:
                midtiptrackercoord1 = midtiptrack3[0:3]
                midtiptrackercoord2 = midtiptrack3[5:8]

                intmidtiptrackercoord1 = int(midtiptrackercoord1)
                intmidtiptrackercoord2 = int(midtiptrackercoord2)    
                #print("test")
                print(intmidtiptrackercoord2)
                pyautogui.scroll(1,intmidtiptrackercoord1, intmidtiptrackercoord2)



        else:
            print("index finger closed")
            htm.counter = 0
            pyautogui.click()
            #will click when no longer detecting index finger tip
        
        #if statements might not scale well with more detailed functionality but works for now, could subdivide landmark groups

    #working!!


        
    

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    #cv2.putText(img, f'FPS: {int(fps)}', (400,70), cv2.FONT_HERSHEY_PLAIN, 3, (255,0,0), 3)

    cv2.imshow("Window", img) #can turn this off for functionality
    cv2.waitKey(1) #1ms
    


 
        

  

    



