This project is the first working version of an idea I have to create a robot that acts as a sort of assistant, particularly aimed at assisting programmers.

The bot will be programmed in python on a RaspberryPi, it will include some RPI hardware extensions like a batterypack, webcam, speaker, simple text-based screen, and small keyboard rigged onto a shell with wheels and an RC motor. I'd like to eventually add some OpenCV functionality that allows it to wheel around without hitting into walls and so forth but for now, it being stationary unless RC controlled is enough.

The concept here is that, at startup it will run a script similar to the one in this project "facerecogwithcam.py" in which a screenshot of your face will be taken
and matched against a database, if a match comes back, the user is verified and the assistant script or brains of the robot will run, else, it will turn off or try again. 

The assistant script will rely on inbuilt OS functionality for simple tasks such as searching the web, and for more complex tasks it will call other pre-written scripts such as the portscanner script included in this project. 

This project in its form right now, requires a Mac OS and plenty of libraries so its a bit impractical to run on any other machine but my own and this mostly exists on github for my own sake.

However, if you're interested in tracking down the dependencies and taking it for a spin, first, run the "facerecogwithcam.py" script, when the camera opens up, press "space" to take a screenshot, the terminal will say "image written" you can then press "ESC" to exit.

That screenshot will be tested against the database and it will verify you or it won't.

If verified the virtual assistant script will run and from there the rest is fairly intuitive. 

As stated earlier, this is just a proof of concept that I've made in the last few days. For the larger project, I'll be making quite a few changes, automating more things and migrating it to a RPI for the final iteration.


