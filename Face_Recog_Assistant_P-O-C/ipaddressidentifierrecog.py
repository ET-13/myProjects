import tkinter as tk
import os




window = tk.Tk()

urlstring = tk.StringVar

label1 = tk.Label(window,text="Enter URL: " )
label1.pack()

entry1 = tk.Entry(window, textvariable="urlstring")
entry1.pack()



def toIP():
    urltochange = str(entry1.get())
    activator = "host" + " " + urltochange
    ipis = os.system(activator)
    stringip = str(os.system(activator))
    print(stringip)
    
    
    pusher = "echo" + " " + stringip + ">" + " " + "ipaddresslist.txt"
    os.system(pusher)

  
    #tkinter for gui
    label2 = tk.Label(ipis)
    label2.pack()


button1 = tk.Button(window,command=toIP, text="run script")
button1.pack()









window.mainloop()

