#import speech_recognition as sr
import playsound
from gtts import gTTS
import os




num = 1
def assistant_speaker(output):
    global num
    num += 1
    print("PerSon : ", output)

    toSpeak = gTTS(text = output, lang="en", slow = False)

    file = str(num)+".mp3"
    toSpeak.save(file)

    playsound.playsound(file, True)
    os.remove(file)



def open_application(input):

    ##willworkonthis
    print(input)



#def get_audio():

 #input("Please enter input: ")

     

#def get_audio():

   # rObject = sr.Recognizer()
   # audio = ''

   # with sr.Microphone() as source:
       # print("Speak...")

       # audio = rObject.listen(source, phrase_time_limit=5)
       # print("Stop.") #5 second limitation

       # try: 

          #  text = rObject.recognize_google(audio, language ='en-US')
           # print("You: ", text)
           # return text
        
       # except:

            #assistant_speaker("I could not understand you, please try again.")
           # return 0


def search_web():

     assistant_speaker("Please type in what you wanted to search")
     
     usersearch = str(input("Search:"))
     #print(usersearch)
     usersearch2 = usersearch.replace(" ", "")
     #print(usersearch2)
     googlevariable = "\"http://www.google.com/search?q="
     

     command1 = "cd" + " " + "~"
     command2 = "open" + " " + googlevariable + usersearch2 + "\""
     os.system(command1)
     os.system(command2)

     #search_web_commands()

def open_app():

    assistant_speaker("What app would you like to run?")

    userappopen = str(input("Open:"))
    print(userappopen)

    command3 = "cd" + " " + "~"
    command4 = "open" + " " + "-a" + " " + userappopen

    os.system(command3)
    os.system(command4)

def check_weather():

    assistant_speaker("What place would you like the forecast of?")

    userweathercheck = str(input("Weather:"))
    print(userweathercheck)
    userweathercheck2 = userweathercheck.replace(" ", "")
    googlevariable2 = "\"http://www.google.com/search?q=weather+"

    command5 = "cd" + " " + "~"
    command6 = "open" + " " + googlevariable2 + userweathercheck2 + "\""

    assistant_speaker("The weather in" + " " + userweathercheck + " " + "is ...")
    os.system(command5)
    os.system(command6)

def goto_youtube():
    
    assistant_speaker("Input what you'd like to YouTube")
    useryoutube = str(input("YouTube:"))
    print(useryoutube)
    useryoutube2 = useryoutube.replace(" ", "")
    youtubevariable = "\"https://www.youtube.com/results?search_query="

    command7 = "cd" + " " + "~"
    command8 = "open" + " " + youtubevariable + useryoutube2 + "\""

    assistant_speaker("Youtubing" + " " + useryoutube)
    os.system(command7)
    os.system(command8)

def portscan_website():

    assistant_speaker("Scanning ports of target...")
 
    command11 = "python3" + " " + "portscannerrecog.py"

   
    os.system(command11)



def ipaddress_identifier():

    assistant_speaker("Opening IP address finder")
   
    command17 = "python3" + " " + "ipaddressidentifierrecog.py"

   
    os.system(command17)





def cantunderstand():
  

    
    assistant_speaker("yes, reload, or exit?")

    userunderstandinput = input("...")
    userinputparse = str(userunderstandinput)
    counter = 1
    print(userinputparse)

    while counter > 0:

        if(userinputparse == "yes"):
            search_web()
            counter = 0
    

        elif(userinputparse == "reload"):
            reloadit = "python3" + " " + "speechassistant.py"
            os.system(reloadit)
            #exit()
            #counter = 0
            #print("exit test")
        
        else:
            exit()

            

        break



    
globalvalue = 1


if __name__ == "__main__":

    assistant_speaker("What's your name?")
    
    name = str(input("Enter your input: "))
    

    assistant_speaker("Hello," + name)

    while(1):

        

        assistant_speaker("What can I help you with?")
        text = str(input("Enter your input: "))

        if text == 0:
            continue
        
        if "exit" in text or "bye" in text:
            assistant_speaker("Alright, goodbye" + " " +  name + ".")
            break

        if "search" in text or "google" in text:
            
            assistant_speaker("Okay I will search the web for that")
            search_web()
           
            break

        if "app" in text or "run" in text or "open app" in text or "application" in text:
            assistant_speaker("Okay I will open that application for you")
            open_app()

            continue

        if "weather" in text or "forecast" in text or "temperature" in text:
            assistant_speaker("Okay, would you like me to tell you the weather?")
            check_weather()

            continue

        if "who are you" in text or "what are you" in text or "what is your name" in text or "what is this" in text or "what can you do" in text:
            assistant_speaker("I am your personal assistant")
            assistant_speaker("I can search the web, run applications, check the weather and more")

            continue

        if "youtube" in text:
            assistant_speaker("You would like me to youtube that?")
            goto_youtube()    

            continue

        #if "alarm" in text:
            #assistant_speaker("You'd like me to set an alarm?")
            #set_alarm()
            ##needs work

        #if "calculator" in text or "calculate" in text or "subtract" in text or "divide" in text or "multiply" in text:
            #assistant_speaker("You would like me to calculate something?")
            #calculate()

            #break

        if "ip" in text or "find ip" in text or "identify ip" in text:

            assistant_speaker("You want the ip address of a website?")
            ipaddress_identifier()

            continue


        if "portscan" in text or "port" in text:
            assistant_speaker("I can run a portscan of your target website")
            assistant_speaker("To change the default, you will need to manually adjust the IP address of the target variable")
            assistant_speaker("You can do so in the portscanner.py file contained in this folder")
            portscan_website()

            break

            
        else:
            assistant_speaker("I don't understand" + " " + text + " "  + "would you like me to search for it?")
            cantunderstand()

            break


    

        



            
            

        




            
        

                
        
        

        


            
           

        








