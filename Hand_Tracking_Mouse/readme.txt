After learning about handtracking with openCV and the model available in the mediapipe library
I had an immediate desire to create a program which tied hand tracking to the mouse cursor

I figured it'd be fairly straightforward if we already had landmark data for hand positions, then it'd just be about extracting
the current x/y position of that landmark, continuously, and inserting it into some function which moved the mouse cursor
and that's exactly what this program does. It tracks the tip of the index finger as the cursor. Once the hand is closed or the index fingertip is no longer detected, that's counted as a mouse-click. It also tracks the tip of the middle finger, if both the middle and index fingers are held up, it will begin scrolling up. Though I'm having trouble getting it to work for scrolling down... The project is a WIP after all.

The first .py in this file is "handtrackingmodule" and that's simply a module I created which has the necessary boilerplate to be applied to this mouse-handtracking project. The actual project itself is the "handtrackingmouse.py" file and if you run that you can test it out for yourself. 

The last file is just something I coded while I was still learning how these libraries worked and I've left it here for posterity.

The libraries used in this project include: OpenCV, mediapipe, numpy & pyautoGUI

This project still has a lot of room for improvement and I might get around to it one day, but making it in this form is enough for me right now. I may reuse and refine it for other projects later on, but this can be thought of as a proof-of-concept. It's a bit impractical in its current state, though it could easily be made better.

