import random
from time import sleep
from pathlib import Path
from tuiwindows import window,cls,textInput,msgBox
from compy import askCompy,drawCompy
import platform
isInstalled = 0
currentUser = 1
usefulInteger = 0
upperBorder = 0
installPath1 = ""
installPath2 = ""
version = ""
isWorking = True
letter = "none"
current = 0
op =""
program1 =""
program2 =""
operation = "+"
num1 = 0
num2 = 0
answer = 0
ptsAmount = 100
executingNow = 0
memory = "16MB"
bought = False
bought1 = False
bought2 = False
counter = 0
happines = 0
counter2 = 0
ask = ""
chance = 0
num = 0
processor = 1
machineWorking = True
username = ""
name = 0
os = 0
workcycle = True
isAlpha = False
taken = False
name = ""
count = 0
spareint = int
os = ""
cake = "delicious!"
osDict = {"1":"TD 2","2":"TD 1","3":"TD 1.1","4":"TD 2","0":"TD 2","6":"PB 3.14","7":"PB 3.14","8":"PB 95","9":"PB RT 3.62","5":"PB 95"}
alreadyChecked = True
logonCycle = True
loggedOn = False
kernel = "Darwin"
pathFolder = "/Users/luigi/"
pathTheme = ""
pathRam = ""
pathPts = ""
pathProc = ""
pathName = ""
pathPassword = ""
pathSound = ""
spareStr = ""
spareStr1 = ""
spareStr2 = ""
spareStr3 = ""
spareStr4 = ""
spareStr5 = ""
sound = 0
startup = ""
error = ""
shutdown = ""
floppy = ""
hd = ""
cursor = 0
theme = ""
#function block start

try:
    from colorama import init,Fore,Back
    from playsound import playsound
except:
    window("Uh oh!","Looks like you don't have one of these","modules. Please ensure all of them are installed:","colorama ,playsound","To install module: 1. Insert diskette","2. Type 'pip install *module name*")

    


"""
def keyESC():
    if current == 3:
        if executingNow == 0:
            current = 0
        elif executingNow == 1:
            if program1 == "About":
                currrent = 1
            elif program1 == "Calc":
                current = 2
            elif program1 == "Upgrade":
                current = 4
            elif program1 == "SP":
                current = 5
            elif program1 == "Settings":
                current = 6
        elif executingNow == 2:
            if program2 == "About":
                current = 1
            elif program2 == "Calc":
                current = 2
            elif program2 == "Upgrade":
                current = 4 
            elif program2 == "SP":
                current = 5
            elif program2 == "Settings":
                current = 6
    if current == 7:
        if executingNow == 0:
            current = 0
        elif executingNow == 1:
            if program1 == "About":
                currrent = 1
            elif program1 == "Calc":
                current = 2
            elif program1 == "Upgrade":
                current = 4
            elif program1 == "SP":
                current = 5
            elif program1 == "Settings":
                current = 6
        elif executingNow == 2:
            if program2 == "About":
                current = 1
            elif program2 == "Calc":
                current = 2
            elif program2 == "Upgrade":
                current = 4 
            elif program2 == "SP":
                current = 5
            elif program2 == "Settings":
                current = 6  
"""      
       
def logon(name):
    cls()
    print("            Tangerine Desktop ",version)
    print("                              \u2551                    ")
    print("                              \u2551                    ")
    print("                              \u2551                    ")
    print("                              \u2551 ")
    print("              welcome         \u2551 1 "+name)
    print("                              \u2551")
    print("                              \u2551                    ")
    print("                              \u2551                    ")
    input("Press enter to log in...")

def do_nothing():
    return None
            
#0 : Desktop
#1 : About window
#2 : Calculator
#3 : Launcher
#4 : Hardware upgrade
#5 : Settings, Please!
#6 : Settings/Preferences
#7 : Task window
#8 : Compy(still in development) 
current = 0
version = "4.0 "
pathFolder = str(Path().absolute())
kernel = platform.system()
try:
    if kernel == "Windows":
        pathName = pathFolder + "\\Disk\\System\\name.txt"
        pathSound = pathFolder + "\\Disk\\System\\sound.txt"
        pathProc = pathFolder + "\\Disk\\System\\proc.txt"
        pathPts = pathFolder + "\\Disk\\System\\pts.txt"
        pathRam = pathFolder + "\\Disk\\System\\ram.txt"
        pathPassword = pathFolder + "\\Disk\\System\\pass.txt"
        pathTheme = pathFolder + "\\Disk\\System\\theme.txt"
        startup = pathFolder + "\\Disk\\System\\sounds\\startup.mp3"
        error = pathFolder + "\\Disk\\System\\sounds\\error1.mp3"
        shutdown = pathFolder + "\\Disk\\System\\sounds\\shutdown.mp3"
        hd = pathFolder + "\\Disk\\System\\sounds\\hard.mp3"
    else:
        pathName = pathFolder + "/Disk/System/name.txt"
        pathSound = pathFolder + "/Disk/System/sound.txt"
        pathProc = pathFolder + "/Disk/System/proc.txt"
        pathPts = pathFolder + "/Disk/System/pts.txt"
        pathRam = pathFolder + "/Disk/System/ram.txt"
        pathPassword = pathFolder +"/Disk/System/pass.txt"
        pathTheme = pathFolder +"/Disk/System/theme.txt"
        startup = pathFolder + "/Disk/System/sounds/startup.mp3"
        error = pathFolder + "/Disk/System/sounds/error1.mp3"
        shutdown = pathFolder + "/Disk/System/sounds/shutdown.mp3"
        hd = pathFolder + "/Disk/System/sounds/hard.mp3"
    isInstalled = 1
except:
    isInstalled = 0
    import os
    
    installPath1 = os.path.join(pathFolder,"Disk")
    installPath2 = os.path.join(pathFolder,"Disk","System")
try:
    init()
    print(Fore.BLACK+Back.WHITE)
    with open(pathTheme,mode="r") as f2:
        theme = f2.read()
    with open(pathSound,mode="r") as file:
        spareStr = file.read()
        sound = int(spareStr)
    with open(pathProc,mode="r") as ProcFile1:
        ask = ProcFile1.read()
        if ask == "1":
            processor = 1
        elif ask == "2":
            processor = 2
            bought1 = True
    with open(pathRam,mode="r") as ProcFile1:
        ask = ProcFile1.read()
        if ask == "1":
            memory = "16MB"
        elif ask == "2":
            memory = "32MB"
        elif ask == "3":
            memory = "64MB"
            bought = False
    with open(pathName, mode = "r") as NameFile1:
        username = NameFile1.read()
except:
    isInstalled = 0
    import os
    
    installPath1 = os.path.join(pathFolder,"Disk")
    installPath2 = os.path.join(pathFolder,"Disk","System")
while machineWorking:
    if isInstalled == 0:
        break
    cls()
    isWorking = True
    loggedOn = False
    while not(loggedOn):
        cls()
        print('Starting up TD',version)
        print('Loading system...')
        print('Finsesed loading system.')
        print('Loading standart applications')
        sleep(2)
        print('Finished loading applictaions')
        print("          "+Fore.RED+"\u2554\u2550\u2550\u256c\u2550\u2550\u2557")
        print("          "+Fore.YELLOW+"\u2551     \u2551")
        print("          "+Fore.GREEN+"\u2551     \u2551")
        print("          "+Fore.BLUE+"\u2551     \u2551")
        print("          "+Fore.MAGENTA+"\u255a\u2550\u2550\u2550\u2550\u2550\u255d"+Fore.BLACK)
        print("            TD",version[0:4])
        if sound == 1:
            playsound(startup)
        isWorking = True
        loggedOn = False        
        logon(username)
        loggedOn = True
        current == 0
        if currentUser == 1:
            with open(pathPts,mode="r") as f1:
                ptsAmount = f1.readline()
        while isWorking:
            cls()
            if theme == "01":
                print(Fore.BLACK+Back.WHITE+"")
            elif theme == "02":
                print(Fore.BLACK+Back.RED+"")
            elif theme == "03":
                print(Fore.BLACK+Back.GREEN+"")
            elif theme == "04":
                print(Fore.BLACK+Back.BLUE+"")
            elif theme == "05":
                print(Fore.BLACK+Back.YELLOW+"")
            elif theme == "06":
                print(Fore.BLACK+Back.CYAN+"")
            elif theme == "07":
                print(Fore.BLACK+Back.MAGENTA+"")
            elif theme == "11":
                print(Fore.WHITE+Back.BLACK+"")
            elif theme == "12":
                print(Fore.WHITE+Back.RED+"")
            elif theme == "13":
                print(Fore.WHITE+Back.GREEN+"")
            elif theme == "14":
                print(Fore.WHITE+Back.BLUE+"")
            elif theme == "15":
                print(Fore.WHITE+Back.YELLOW+"")
            elif theme == "16":
                print(Fore.WHITE+Back.CYAN+"")
            elif theme == "17":
                print(Fore.WHITE+Back.MAGENTA+"")  
            if current == 0:
                window("Tangerine Desktop","","","","","","")
            if current == 1:
                spareStr2 = "Version:" + version
                if processor == 1:
                    spareStr = "Processor: Lentium 1 115 MhZ"
                elif processor == 2:
                    spareStr = "Processor: AMB C6 178 MhZ"
                spareStr1 = "meRAM " + memory
                window("About TD",spareStr2,spareStr,spareStr1)
            if current == 2:
                spareStr = "(key 1)1st number : "+str(num1)
                spareStr1 = "(key 2)2nd number : "+str(num2)
                spareStr2 = "(key 3)Operation : "+operation
                if operation == "+":
                    answer = num1 + num2
                elif operation == "-":
                    answer = num1 - num2
                spareStr3 = "Answer : "+str(answer)
                window("Calculator",spareStr,spareStr1,spareStr2,spareStr3,"to get help, type 'h'")
            if current == 3:
                if currentUser == 0:
                    spareStr = "Current user : Guest"
                else:
                    spareStr = "Current user : " + username
                window("Programs",spareStr,"Hit esc to exit","S for shutdown/restart","1 : About","2 : Calculator","3 : Hardware Upgrade","4 : Settings, please!","5 : Settings","6 : Compy(unfinished)")
            if current == 4:
                if memory == "16MB":
                    spareStr = "Avalible - Type '1' to puchase it.Cost : 500 pts"
                    spareStr2 = "32 MB meRAM"
                elif memory == "32MB":
                    spareStr = "Avalible - Type '1' to puchase it.Cost : 1000 pts"
                    spareStr2 = "64 MB meRAM"                    
                else:
                    spareStr = "Not avalible =("
                    spareStr2 = "96 MB meRAM"
                if processor != 1:
                    spareStr1 = "Avalible - Type '2' to puchase it.Cost : 1000 pts"
                else:
                    spareStr1 = "Not avalible =("
                if bought == False & bought1 == False:
                    spareStr3 = "MusicBlaster 1 - Type '3' to puchase it. Cost: 1500 pts"
                    
                window("Hardware upgrade",spareStr2,spareStr,"AMB C6 178 MhZ",spareStr1)
            if current == 5:
                if alreadyChecked:
                    alreadyChecked = False
                    name = ""
                    if usefulInteger == 2:
                        upperBorder = 86
                        usefulInteger = 0
                    else:
                        upperBorder = 52
                        usefulInteger = usefulInteger + 1
                    while count < 16:
                        spareint = random.randint(1,upperBorder)
                        if spareint == 1:
                            name = name + "A"
                        elif spareint == 2:
                            name = name + "B"                
                        elif spareint == 3:
                            name = name + "C"
                        elif spareint == 4:
                            name = name + "D"
                        elif spareint == 5:
                            name = name + "E"                
                        elif spareint == 6:
                            name = name + "F"
                        elif spareint == 7:
                            name = name + "G"
                        elif spareint == 8:
                            name = name + "H"                
                        elif spareint == 9:
                            name = name + "I"
                        elif spareint == 10:
                            name = name + "J"
                        elif spareint == 11:
                            name = name + "K"                
                        elif spareint == 12:
                            name = name + "L"
                        elif spareint == 13:
                            name = name + "M"
                        elif spareint == 14:
                            name = name + "N"                
                        elif spareint == 15:
                            name = name + "O"
                        elif spareint == 16:
                            name = name + "P"
                        elif spareint == 17:
                            name = name + "Q"                
                        elif spareint == 18:
                            name = name + "R"
                        elif spareint == 19:
                            name = name + "S" 
                        elif spareint == 20:
                            name = name + "T"                
                        elif spareint == 21:
                            name = name + "U"
                        elif spareint == 22:
                            name = name + "V"
                        elif spareint == 23:
                            name = name + "W"                
                        elif spareint == 24:
                            name = name + "X"
                        elif spareint == 25:
                            name = name + "Y"
                        elif spareint == 26:
                            name = name + "Z"                
                        elif spareint == 27:
                            name = name + "a"
                        elif spareint == 28:
                            name = name + "b"                
                        elif spareint == 29:
                            name = name + "c"
                        elif spareint == 30:
                            name = name + "d"
                        elif spareint == 31:
                            name = name + "e"                
                        elif spareint == 32:
                            name = name + "f"
                        elif spareint == 33:
                            name = name + "g"
                        elif spareint == 34:
                            name = name + "h"                
                        elif spareint == 35:
                            name = name + "i"
                        elif spareint == 36:
                            name = name + "j"
                        elif spareint == 37:
                            name = name + "k"                
                        elif spareint == 38:
                            name = name + "l"
                        elif spareint == 39:
                            name = name + "m"
                        elif spareint == 40:
                            name = name + "n"                
                        elif spareint == 41:
                            name = name + "o"
                        elif spareint == 42:
                            name = name + "p"
                        elif spareint == 43:
                            name = name + "q"                
                        elif spareint == 44:
                            name = name + "r"
                        elif spareint == 45:
                            name = name + "s" 
                        elif spareint == 46:
                            name = name + "t"                
                        elif spareint == 47:
                            name = name + "u"
                        elif spareint == 48:
                            name = name + "v"
                        elif spareint == 49:
                            name = name + "w"                
                        elif spareint == 50:
                            name = name + "x"
                        elif spareint == 51:
                            name = name + "y"
                        elif spareint == 52:
                            name = name + "z"
                        elif spareint == 53:
                            name = name + "1"
                        elif spareint == 54:
                            name = name + "2"                
                        elif spareint == 55:
                            name = name + "3"
                        elif spareint == 56:
                            name = name + "4"
                        elif spareint == 57:
                            name = name + "5"                
                        elif spareint == 58:
                            name = name + "6"
                        elif spareint == 59:
                            name = name + "7"
                        elif spareint == 60:
                            name = name + "8"                
                        elif spareint == 61:
                            name = name + "9"
                        elif spareint == 62:
                            name = name + "0"
                        elif spareint == 63:
                            name = name + "|"                
                        elif spareint == 64:
                            name = name + "/"
                        elif spareint == 65:
                            name = name + "-"
                        elif spareint == 66:
                            name = name + "_"                
                        elif spareint == 67:
                            name = name + "-"
                        elif spareint == 68:
                            name = name + "!"
                        elif spareint == 69:
                            name = name + "@"                
                        elif spareint == 70:
                            name = name + "#"
                        elif spareint == 71:
                            name = name + "$" 
                        elif spareint == 72:
                            name = name + "%"                
                        elif spareint == 73:
                            name = name + "^"
                        elif spareint == 74:
                            name = name + "&"
                        elif spareint == 75:
                            name = name + "*"                
                        elif spareint == 76:
                            name = name + "("
                        elif spareint == 77:
                            name = name + ")"
                        elif spareint == 78:
                            name = name + "+"
                        elif spareint == 79:
                            name = name + "="                
                        elif spareint == 80:
                            name = name + "["
                        elif spareint == 81:
                            name = name + "]"
                        elif spareint == 82:
                            name = name + "{"
                        elif spareint == 83:
                            name = name + "}"                
                        elif spareint == 84:
                            name = name + "?"
                        elif spareint == 85:
                            name = name + ","
                        elif spareint == 86:
                            name = name + "."
                        count = count + 1
                    spareint = random.randint(0,9)
                    os = osDict[str(spareint)]
                    count = 0 
                spareStr = "Name:"+name
                spareStr1 = "OS:"+os
                window("Settings, please!","1 right stamp = 10 pts","1 wrong stamp = -5 pts",spareStr,spareStr1,"","(A)ccept,(D)ecline,get (H)elp")
                
            if current == 6:
                spareStr = "Username:"+username
                spareStr1 = "Theme:"+theme
                window("Settings",spareStr,"[Change:1]",spareStr1,"[Change:2]")
            if current == 7:
                #Window list
                if program1 !="":
                    spareStr = "2 "+program1
                else:
                    spareStr = ""
                if program2 !="":
                    spareStr1 = "3 "+program2
                else:
                    spareStr1 = ""
                window("Tasks","Type number to switch","1 Desktop",spareStr,spareStr1,"'esc' to close")
            if current == 8:
                drawCompy(".v.")
                print("Hello there",username)
                print("My happiness:",happines)
                
            print(u"\u2550"*6+u"\u2566"+u"\u2550"+"Dock"+u"\u2550"*43)            
            print("  TD  "+u"\u2551"+"Shutdown Reboot Programs Tasks")
            print(" "+version[0:4]+" "+u"\u2551"+"This is beta. It may contain bugs")  
            letter = textInput("Awating input...","Command")
            try:letter = letter.lower() 
            except:do_nothing()
            if letter == "a" or letter == "approve":
                if current == 5:
                    isAlpha = name.isalpha
                    
                    if isAlpha and "TD" in os:
                        print("Valid! +10 pts!")
                        input("Hit ENTER to continue..")
                        ptsAmount = ptsAmount + 10
                    else:
                        print("Not valid! -5 pts!")
                        input("Hit ENTER to continue..")
                        ptsAmount = ptsAmount - 5
                    alreadyChecked = True        
                    
            elif letter == "whatsnew":
                window("New features","Sounds(required soundcard)","Compy","Theming(eat that icoeye!)","Normal windows")
            elif letter == "d" or letter == "deny":
                if current == 5:
                    isAlpha = name.isalpha
                    if isAlpha and not("TD" in os):
                        print("Valid! +10 pts!")
                        input("Hit ENTER to continue..")
                        ptsAmount = ptsAmount + 10
                    else:
                        print("Not valid! -5 pts!")
                        input("Hit ENTER to continue..")
                        ptsAmount = ptsAmount - 5
                    alreadyChecked = True         
            elif letter == "c" or letter == "close" :
                if current == 3 or current == 7:
                            if executingNow == 0:
                                current = 0
                            elif executingNow == 1:
                                if program1 == "About":
                                    currrent = 1
                                elif program1 == "Calc":
                                    current = 2
                                elif program1 == "Upgrade":
                                    current = 4
                                elif program1 == "SP":
                                    current = 5
                                elif program1 == "Settings":
                                    current = 6
                            elif executingNow == 2:
                                if program2 == "About":
                                    currrent = 1
                                elif program2 == "Calc":
                                    current = 2
                                elif program2 == "Upgrade":
                                    current = 4
                                elif program2 == "DevCity":
                                    current = 5
                                elif program2 == "SP":
                                    current = 6
                elif current == 5:
                        alreadyChecked = False
                        if current != 0 and current !=2:
                            current = 0
                            if executingNow == 1:
                                executingNow = 0
                                if program2 != "":
                                    program1 = program2
                                    program2 = ""
                                else:
                                    program1 = ""
                                
                elif current == 2:
                            current = 0
                            num1 = 0
                            num2 = 0
                            operation = "+"
                            if executingNow == 1:
                                executingNow = 0
                                if program2 != "":
                                    program1 = program2
                                    program2 = ""
                                else:
                                    program1 = ""            
                            else:
                                ask = textInput("Required confirmation","Shutdown system?(Y/N)")
                                if ask == "Y" or ask == "y":
                                    isWorking = False
                                    
                                    machineWorking = False
                                else:
                                    print("Canceled.")                    
            elif letter == "1":
                if current == 3:
                    if program1 != "" and program2 != "":
                        msgBox("#","Memory overflow.")
                        if sound == 1:
                            playsound(error)                        
                        spareint = random.randint(0,99)
                        if spareint == 0:
                            cls()
                            print("Error name: SEGFAULT\nSorry, but TD experienced a problem.\nIt needs to restart.\nDo not press Ctrl-Alt-Del")
                            input("Press \u21a9(Return) to continue...")
                            isWorking = False
                            loggedOn = False                          
                    if program1 != "":
                        if memory == "16MB":
                            msgBox("#","Memory overflow.")
                            if sound == 1:
                                playsound(error)
                            spareint = random.randint(0,99)
                            if spareint == 0:
                                cls()
                                print("Error name: SEGFAULT\nSorry, but TD experienced a problem.\nIt needs to restart.\nDo not press Ctrl-Alt-Del")
                                input("Press \u21a9(Return) to continue...")
                                isWorking = False
                                loggedOn = False                            
                        else:
                            executingNow = 2
                            program2 = "About"
                            current = 1
                    else:
                        executingNow = 1
                        program1 = "About"
                        current = 1
                elif current == 7:
                    current = 0
                    executingNow = 0
                elif current == 2:
                    num1 = int(textInput("Enter a number","1st number"))
                elif current == 6:
                    username = textInput("Enter username","Enter new username")
                    with open(pathName,mode="w") as tmpfile:
                        tmpfile.write(username)
                elif current == 4:
                    if bought != True:
                        if current == 4:
                            if memory == "16MB":
                                if ptsAmount >= 500:
                                    with open(pathRam,mode="w+") as RamFile2:
                                        RamFile2.write("2")
                                    memory = "32MB"
                                    print("Thank you for puchasing our product!")
                            if memory == "32MB":
                                if ptsAmount >= 1000:
                                    with open(pathRam,mode="w+") as RamFile2:
                                        RamFile2.write("3")
                                    memory = "64MB"
                                    bought = True
                                    print("Thank you for puchasing our product!")                            
                            else:
                                print("Error! Not enoungh points!")          
            elif letter == "2":
                if current == 3:
                    if program1 != "" and program2 != "":
                        msgBox("#","Memory overflow.")
                        if sound == 1:
                            playsound(error)                        
                        spareint = random.randint(0,99)
                        if spareint == 0:
                            cls()
                            print("Error name: SEGFAULT\nSorry, but TD experienced a problem.\nIt needs to restart.\nDo not press Ctrl-Alt-Del")
                            input("Press \u21a9(Return) to continue...")
                            isWorking = False
                            loggedOn = False                       
                    if program1 != "":
                        if memory == "16MB":
                            msgBox("#","Memory overflow.")
                            if sound == 1:
                                playsound(error)                            
                            spareint = random.randint(0,99)
                            if spareint == 0:
                                cls()
                                print("Error name: SEGFAULT\nSorry, but TD experienced a problem.\nIt needs to restart.\nDo not press Ctrl-Alt-Del")
                                input("Press \u21a9(Return) to continue...")
                                isWorking = False
                                loggedOn = False                               
                        else:
                            executingNow = 2
                            program2 = "Calc"
                            current = 2
                    else:
                        executingNow = 1
                        program1 = "Calc"
                        current = 2
                elif current == 4:
                    if bought1 != True:
                        if current == 4:
                            if ptsAmount >= 1000:
                                with open(pathProc,mode="w+") as ProcFile2:
                                    ProcFile2.write("2")                            
                                processor = 2
                                bought1 = True        
                elif current == 7:
                    if program1 == "About":
                        current = 1
                    elif program1 == "Calc":
                        current = 2
                    elif program1 == "Upgrade":
                        current = 4 
                    elif program1 == "SP":
                        current = 5
                    elif program1 == "Settings":
                        current = 6
                    elif program1 == "Compy":
                        current = 8                    
                    executingNow = 1    
                elif current == 2:
                    num2 = int(textInput("Enter a number","2nd number"))
                elif current == 6:
                    window("Colors","0:Black","1:White")
                    ask = textInput("Input","Text color:")
                    if ask == "1":
                        theme = "1"
                        window("Colors","1:Black","2:Red","3:Blue","4:Green","5:Yellow","6:Cyan","7:Magenta")
                        ask = textInput("Input","Background color:")
                        if ask == "1" or ask == "2" or ask == "3" or ask == "4" or ask == "5" or ask == "6" or ask == "7":
                            theme = theme + ask
                        else:
                            theme = theme + "1"
                    else:
                        theme = "0"
                        window("Colors","1:Black","2:Red","3:Green","4:Blue","5:Yellow","6:Cyan","7:Magenta")
                        ask = textInput("Input","Background color:")
                        if ask == "1" or ask == "2" or ask == "3" or ask == "4" or ask == "5" or ask == "6" or ask == "7":
                            theme = theme + ask
                        else:
                            theme = theme + "1" 
                    with open(pathTheme,mode="w") as f:
                        f.write(theme)                    
                
            elif letter == "3":
                if current == 3:
                    if not(currentUser == 0):
                        if program1 != "" and program2 != "":
                            msgBox("#","Memory overflow.")
                            if sound == 1:
                                playsound(error)                            
                            spareint = random.randint(0,99)
                            if spareint == 0:
                                cls()
                                print("Error name: SEGFAULT\nSorry, but TD experienced a problem.\nIt needs to restart.\nDo not press Ctrl-Alt-Del")
                                input("Press \u21a9(Return) to continue...")
                                isWorking = False
                                loggedOn = False                           
                        if program1 != "":
                            if memory == "16MB":
                                msgBox("#","Memory overflow.")
                                if sound == 1:
                                    playsound(error)                                
                                spareint = random.randint(0,99)
                                if spareint == 0:
                                    cls()
                                    print("Error name: SEGFAULT\nSorry, but TD experienced a problem.\nIt needs to restart.\nDo not press Ctrl-Alt-Del")
                                    input("Press \u21a9(Return) to continue...")
                                    isWorking = False
                                    loggedOn = False         
                            else:
                                executingNow = 2
                                program2 = "Upgrade"
                                current = 4
                        else:
                            executingNow = 1
                            program1 = "Upgrade"
                            current = 4
                    else:
                        print("You have no permission to run this program.")
                        print("To run this program, log in as",username)
                        input("Awating input...")            
                elif current == 4:
                    if bought2 != True and bought == False and bought1 == False:
                        if current == 4:
                            if ptsAmount >= 1500:
                                with open(pathSound,mode="w+") as SoundFile2:
                                    SoundFile2.write("1")                            
                                sound = 1
                                bought1 = True
                                print("Thank you for puchasing our product!")
                            else:
                                print("Error! Not enoungh points!")         
                elif current == 7:
                    if program2 == "About":
                        current = 1
                    elif program2 == "Calc":
                        current = 2
                    elif program2 == "Upgrade":
                        current = 4 
                    elif program2 == "SP":
                        current = 5
                    elif program2 == "Settings":
                        current = 6
                    elif program2 == "Compy":
                        current = 8                    
                    executingNow = 2
                elif current == 2:
                    op = textInput("Enter operation","Operation(+/-)")
                    if op == "+":
                        operation = "+"
                    elif op == "-":
                        operation = "-"
                    else:
                        print("Wrong operation! Command cancelled.")                
                    
            elif letter == "4":
                if current == 3:
                    if program1 != "" and program2 != "":
                        msgBox("#","Memory overflow.")
                        if sound == 1:
                            playsound(error)                        
                        spareint = random.randint(0,99)
                        if spareint == 0:
                            cls()
                            print("Error name: SEGFAULT\nSorry, but TD experienced a problem.\nIt needs to restart.\nDo not press Ctrl-Alt-Del")
                            input("Press \u21a9(Return) to continue...")
                            isWorking = False
                            loggedOn = False                       
                    if program1 != "":
                        if memory == "16MB":
                            msgBox("#","Memory overflow.")
                            if sound == 1:
                                playsound(error)                            
                            spareint = random.randint(0,99)
                            if spareint == 0:
                                cls()
                                print("Error name: SEGFAULT\nSorry, but TD experienced a problem.\nIt needs to restart.\nDo not press Ctrl-Alt-Del")
                                input("Press \u21a9(Return) to continue...")
                                isWorking = False
                                loggedOn = False
                                
                        else:
                            executingNow = 2
                            program2 = "SP" 
                            current = 5
                    else:
                        executingNow = 1
                        program1 = "SP"
                        current = 5             
            elif letter == "5":
                if current == 3:
                    if not(currentUser == 0):
                        if program1 != "" and program2 != "":
                            msgBox("#","Memory overflow.")
                            if sound == 1:
                                playsound(error)                            
                            spareint = random.randint(0,99)
                            if spareint == 0:
                                cls()
                                print("Error name: SEGFAULT\nSorry, but TD experienced a problem.\nIt needs to restart.\nDo not press Ctrl-Alt-Del")
                                input("Press \u21a9(Return) to continue...")
                                isWorking = False
                                loggedOn = False                           
                        if program1 != "":
                            if memory == "16MB":
                                msgBox("#","Memory overflow.")
                                if sound == 1:
                                    playsound(error)                                
                                spareint = random.randint(0,99)
                                if spareint == 0:
                                    cls()
                                    print("Error name: SEGFAULT\nSorry, but TD experienced a problem.\nIt needs to restart.\nDo not press Ctrl-Alt-Del")
                                    input("Press \u21a9(Return) to continue...")
                                    isWorking = False
                                    loggedOn = False                                  
                            else:
                                executingNow = 2
                                program2 = "Settings"
                                current = 6
                        else:
                            executingNow = 1
                            program1 = "Settings"
                            current = 6   
                    else:
                        print("You have no permission to run this program.")
                        print("To run this program, log in as",username)
                        input("Awating input...")
            elif letter == "6":
                if current == 3:
                    if not(currentUser == 0):
                        if program1 != "" and program2 != "":
                            msgBox("#","Memory overflow.")
                            if sound == 1:
                                playsound(error)                            
                            spareint = random.randint(0,99)
                            if spareint == 0:
                                cls()
                                print("Error name: SEGFAULT\nSorry, but TD experienced a problem.\nIt needs to restart.\nDo not press Ctrl-Alt-Del")
                                input("Press \u21a9(Return) to continue...")
                                isWorking = False
                                loggedOn = False                           
                        if program1 != "":
                            if memory == "16MB":
                                msgBox("#","Memory overflow.")
                                if sound == 1:
                                    playsound(error)                                
                                spareint = random.randint(0,99)
                                if spareint == 0:
                                    cls()
                                    print("Error name: SEGFAULT\nSorry, but TD experienced a problem.\nIt needs to restart.\nDo not press Ctrl-Alt-Del")
                                    input("Press \u21a9(Return) to continue...")
                                    isWorking = False
                                    loggedOn = False                                  
                            else:
                                executingNow = 2
                                program2 = "Compy"
                                current = 8
                        else:
                            executingNow = 1
                            program1 = "Compy"
                            current = 8   
                    else:
                        print("You have no permission to run this program.")
                        print("To run this program, log in as",username)
                        input("Awating input...")                
            elif letter == "h" or letter == "help":
                if current == 0:
                    window("Buttons to push","Up/Down : select","c : close stuff","s : shutdown","h : help in programs")
                    input("Hit Enter")
                elif current == 2:
                    window("Help for Calculator","Select item to change (Up/Down keys)","Use Enter/Return key to edit.","Credits : Luigi180059","          aka Luigi64-Dev")
                    input("Hit dat Enter button!")
                elif current == 5:
                    window("Help for Settings, please!","a : approve", "d : deny", "c : close window")
                    input("Press Enter/Return")
            elif letter == "t" or letter == "tasks":
                current = 7
            elif letter == "p" or letter == "progs" or letter == "programs":
                current = 3
            elif letter == "play":
                if current == 8:
                    if counter2 > 25:
                        drawCompy("_u_")
                        spareStr = "i like u, " + username +"!" 
                        window("i like it!",spareStr)
                        happines = happines + 1
                        counter2 = 0
                    else:
                        spareint = random.randint(0,2)
                        if spareint == 2:
                            happines = happines - 1
                        window(":/","i'm not bored!")                 
            elif letter == "feed":
                if current == 8:
                    if counter2 > 50:
                        drawCompy("owo")
                        window("yummy!","thank you!")
                        happines = happines + 2
                        counter2 = 0
                    else:
                        spareint = random.randint(0,2)
                        if spareint == 2:
                            happines = happines - 1
                        window(":(","i'm not hungry!")                    
            elif letter == "s" or letter == "shutdown" or letter == "r" or letter == "reboot":
                ask = textInput("Required confirmation","(S)hutdown/(R)eboot?")
                try:ask = ask.lower()
                except:do_nothing()
                if ask == "s" or ask == "shutdown":
                    isWorking = False           
                    machineWorking = False
                    window("","Shutting down...","")
                    playsound(shutdown)
                    sleep(1)
                elif ask == "r" or ask == "reboot":
                    isWorking = False
                    window("","Rebooting...","")
                    playsound(shutdown)
                    sleep(1)
            counter2 = counter2 + 1
            if letter != "":
                playsound(hd)
            

if isInstalled == 0:
    import shutil
    if kernel == "Windows":
        hd = pathFolder + "\\hd.mp3"  
        floppy = pathFolder+ "\\floppy.mp3"
    else:
        floppy = pathFolder + "/floppy.mp3"  
        hd = pathFolder + "/hd.mp3"  
    cls()
    window("Loading...","Booting up installer...","","uwu installer system 1.0")
    playsound(floppy)
    sleep(4)
    window("Welcome!","Welcome to TD 4.0 installation process!","This program will help you install TD easily.")
    input("Press Enter to continue.")
    if kernel == "Windows":
        spareStr = pathFolder +"\\Disk\\System\\sounds"
        
    else:
        spareStr = pathFolder +"/Disk/System/sounds"
    if os.path.exists(spareStr):
        os.rmdir(spareStr)
        os.rmdir(installPath2)
        os.rmdir(installPath1)
    if os.path.exists(installPath2):
        os.rmdir(installPath2)
        os.rmdir(installPath1)
    if os.path.exists(installPath1):
        os.rmdir(installPath1)
    playsound(floppy)
    while True:
        window("Repartitioning","First, we will repartition your disk.","Type 1 to do auto-formatting","Type 2 to exit installer")
        ask = input("Select mode:")
        if ask == "1":
            cls()
            window("","Partitioning 50% complete")
            os.mkdir(installPath1)
            playsound(hd)
            sleep(1)
            window("","Partitioning 75% complete")
            sleep(1)
            playsound(hd)
            os.mkdir(installPath2)
            os.mkdir(spareStr)
            window("","Partitioning 100% complete")
            sleep(1)
            break
        if ask == "2":
            break
    while True:
        
        if ask == "2":
            break
        
        window("Installing","TD 4.0 will be installed on 'Disk'","Type 1 to start installation","Type 2 to exit installation.")
        ask = input("Select mode:")
        if ask == "1":
            import shutil
            if kernel == "Windows":
                pathName = pathFolder + "\\Disk\\System\\name.txt"
                pathSound = pathFolder + "\\Disk\\System\\sound.txt"
                pathProc = pathFolder + "\\Disk\\System\\proc.txt"
                pathPts = pathFolder + "\\Disk\\System\\pts.txt"
                pathRam = pathFolder + "\\Disk\\System\\ram.txt"
                pathPassword = pathFolder + "\\Disk\\System\\pass.txt"
                pathTheme = pathFolder + "\\Disk\\System\\theme.txt"
                startup = pathFolder + "\\Disk\\System\\sounds\\startup.mp3"
                error = pathFolder + "\\Disk\\System\\sounds\\error1.mp3"
                installPath1 = Path(pathFolder +"\\startup.mp3")
                installPath2 = Path(pathFolder +"\\error1.mp3")
                spareStr = Path(pathFolder +"\\shutdown.mp3")
                spareStr1 = Path(pathFolder +"\\hd.mp3")
                hd = pathFolder+ "\\Disk\\System\\sounds\\hd.mp3"
                floppy = pathFolder+ "\\floppy.mp3"
                shutdown = pathFolder+ "\\Disk\\System\\sounds\\shutdown.mp3"
            else:
                pathName = pathFolder + "/Disk/System/name.txt"
                pathSound = pathFolder + "/Disk/System/sound.txt"
                pathProc = pathFolder + "/Disk/System/proc.txt"
                pathPts = pathFolder + "/Disk/System/pts.txt"
                pathRam = pathFolder + "/Disk/System/ram.txt"
                pathTheme = pathFolder + "/Disk/System/theme.txt"
                pathPassword = pathFolder +"/Disk/System/pass.txt"
                startup = pathFolder + "/Disk/System/sounds/startup.mp3"
                error = pathFolder + "/Disk/System/sounds/error1.mp3"
                installPath1 = Path(pathFolder +"/startup.mp3")
                installPath2 = Path(pathFolder +"/error1.mp3")
                spareStr = Path(pathFolder +"/shutdown.mp3")
                spareStr2 = Path(pathFolder +"/hd.mp3")
                shutdown = pathFolder + "/Disk/System/sounds/shutdown.mp3"
                hd = pathFolder + "/Disk/System/sounds/hd.mp3"
                floppy = pathFolder + "/floppy.mp3"
            with open(pathProc, mode="w") as tmpfile:
                tmpfile.write("1")
            sleep(1)
            cls()
            input("Now insert 'Tangerine Desktop Installation Disk #1' and press Enter.")
            cls()
            window("Installing...","10% complete")
            with open(pathRam, mode="w") as tmpfile:
                tmpfile.write("1")
            playsound(floppy)
            cls()
            window("Installing...","25% complete")
            with open(pathSound, mode="w") as tmpfile:
                tmpfile.write("0")
            playsound(floppy)
            cls()
            window("Installing...","45% complete")
            cls()
            input("Insert 'Tangerine Desktop Installation Disk #2' and press Enter.")
            with open(pathName, mode="w") as tmpfile:
                tmpfile.write("User")
            playsound(floppy)
            cls()
            window("Installing...","60% complete")
            with open(pathPassword, mode="w") as tmpfile:
                tmpfile.write("cake = delicious")
            playsound(floppy)
            cls()
            window("Installing...","80% complete")
            input("Insert 'Tangerine Desktop Installation Disk #2' and press Enter.")
            with open(pathPts, mode="w") as tmpfile:
                tmpfile.write("100")
            playsound(floppy)
            cls()
            window("Installing...","100% complete")
            with open(pathTheme, mode="w") as tmpfile:
                tmpfile.write("01")
            shutil.copyfile(installPath2,error)
            shutil.copyfile(installPath1,startup)
            playsound(floppy)
            shutil.copyfile(spareStr,shutdown)
            shutil.copyfile(spareStr2,hd)
            playsound(floppy)
            sleep(1)
            cls()
            window("Installing...","100% complete")
            input("Remove disks from floppy drives.")
            cls()
            window("Congrats!","You have succesfuly installed TD!","Script will stop in 5 seconds","If you want to know what's new","type 'whatsnew'")
            sleep(5)
            break
    cls()
    window("","Installation is finished")
    sleep(1)
cls()    
window("Bye!","Now you can safely end your session.")
