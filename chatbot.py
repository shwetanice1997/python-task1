import os
import pyttsx3

print("____________________________________________ Welcome to the Service Menu Bot____________________________________________")
pyttsx3.speak("\n\n\n\n\n\n  Welcome to the Service Menu Bot \n\n\n")
pyttsx3.speak(" My Name is Myira,, How can i help you!")

print()
while True:   
    print("Hey user what you want to run \t\t" ,end='')
    pyttsx3.speak("Type Service Name You want to run ")
    p = input()
    if("run" in p) and ("chrome" in p) :
        print("Opening a Browser!")
        os.system("chrome")
    elif("run" in p) and (("mediaplayer" in p) or ("songplayer" in p)):
        print("Opening Media Player!")
        os.system("wmplayer")
    elif("run" in p) and (("notepad" in p)or("editor" in p)):
        print("Opening Text Editor! ")
        os.system("notepad")
    elif("calculator" in p):
        print("Opening Calculator")
        os.system("calc")    
    elif("run" in p) and (("jupyter" in p)or("IDE" in p)):
        print("Opening Jupyter IDE")
        os.system("jupyter notebook")
    elif("run" in p) and (("paint" in p) or ("drawing software" in p)):
        print("Opening Paint Software!")
        os.system("mspaint")
    elif("run" in p) and ("youtube" in p):
        print("Opening YouTube")
        os.system("chrome www.youtube.com")
    elif ("linkedin" in p):
        print("Opening Linkedin")
        os.system("chrome www.linkedin.com")
    elif  ("twitter" in p):
        print("Opening Twitter")
        os.system("chrome www.twitter.com")
    elif  ("gmail" in p):
        print("Opening Gmail")
        os.system("chrome www.gmail.com")
    elif ("whatsapp" in p):
        print("Opening Whatsapp")
        os.system("chrome web.whatsapp.com")
    elif ("facebook" in p):
        print("Opening Facebook")
        os.system("chrome www.facebook.com")
    elif ("amazon" in p):
        print("Opening Amazon")
        os.system("chrome www.amazon.in")  
    elif ("flipkart" in p):
        print("Opening Flipkart")
        os.system("chrome www.flipkart.com")
    elif ("run" in p) and (" gitbash" in p):
        print("Opening Git Bash")
        os.system("git bash")
    elif("run" in p) and ("putty" in p):
        print("Opening Putty Software....")
        os.system("putty")
    elif("run" in p) and("kubernetes" in p):
        print("Opening the Kubernetes Cluster in VM....Might Take some time.....")      
        os.system("minikube.exe start") 
    elif ("virtualbox" in p) or ("virtual box" in p) or ("VM" in p) or ("vbox" in p) or ("vm" in p): 
        print("Opening VirtualBox")
        os.system("virtualbox")
    elif ("anydesk" in p): 
        print("Opening Anydesk")
        os.system("anydesk")
    elif ("teamviewer" in p): 
        print("Opening TeamViewer")
        os.system("teamviewer")
    elif(("show" in p)or("listout" in p))and("directory" in p):  
        print("We are Listing all the directories...")
        os.system("dir")  
    elif("clear" in p)and("screen" in p):
        os.system("cls")     
                      
    elif("exit" in p):
        pyttsx3.speak("Hope You Like Our Services,, have a nice day...!!!")
        print("We are closing the program!")
        print("________________________________________________________________________________________________________________________")
        os.system(exit())
        break