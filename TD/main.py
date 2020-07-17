import random
from time import sleep
from colorama import init,Fore,Back
import platform
from pathlib import Path
from tuiwindows import window,cls,textInput,msgBox
from playsound import playsound
currentUser = 1
version = ""
isWorking = True
inp = "none"
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
osDict = {"1":"TD 2","2":"TD 1","3":"TD 1.1","4":"TD 2","0":"TD 2","6":"PB 3.14","7":"PB 3.14","8":"PB 95","9":"PB RT 3.62","5":"PB 95"}
alreadyChecked = True
logonCycle = True
loggedOn = False
kernel = "Darwin"
pathFolder = "/Users/luigi/"
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
#function block start

def logon(name):
    while logonCycle:
        cls()
        print("            Tangerine Desktop ",version)
        print("                              \u2551                    ")
        print("                              \u2551                    ")
        print("                              \u2551                    ")
        print("                              \u2551 1 "+name)
        print("              welcome         \u2551                    ")
        print("                              \u2551 2 Guest")
        print("                              \u2551                    ")
        print("                              \u2551                    ")
        ask = textInput("Enter user number","User")
        if ask == name or ask == "1":
            currentUser = 1
            print("Succesfuly logged as",name)
            input("Hit ENTER to continue...")
            break
        elif ask == "Guest" or ask == "guest" or ask == "2":
            currentUser = 0
            print("Succesfuly logged as Guest")
            input("Hit ENTER to continue...")
            break            
        else:
            print("Unknown user.")
            input("Hit ENTER to continue...")        
            
#Hey! You looking at my code!
#Anyways, if you want to modify game, there is progam codes:
#0 : Desktop
#1 : About window
#2 : Calculator
#3 : Launcher
#4 : Hardware Upgrade
#5 : Settings, Please!
version = "4.0 beta 2"
pathFolder = str(Path().absolute())
kernel = platform.system()
if kernel == "Windows":
    pathName = pathFolder + "\\Disk\\System\\name.txt"
    pathSound = pathFolder + "\\Disk\\System\\sound.txt"
    pathProc = pathFolder + "\\Disk\\System\\proc.txt"
    pathPts = pathFolder + "\\Disk\\System\\pts.txt"
    pathRam = pathFolder + "\\Disk\\System\\ram.txt"
    pathPassword = pathFolder + "\\Disk\\System\\pass.txt"
    startup = pathFolder + "\\Disk\\System\\sounds\\startup.mp3"
    error = pathFolder + "\\Disk\\System\\sounds\\error1.mp3"
else:
    pathName = pathFolder + "/Disk/System/name.txt"
    pathSound = pathFolder + "/Disk/System/sound.txt"
    pathProc = pathFolder + "/Disk/System/proc.txt"
    pathPts = pathFolder + "/Disk/System/pts.txt"
    pathRam = pathFolder + "/Disk/System/ram.txt"
    pathPassword = pathFolder +"/Disk/System/pass.txt"
    startup = pathFolder + "/Disk/System/sounds/startup.mp3"
    error = pathFolder + "/Disk/System/sounds/error1.mp3"
init()
print(Fore.BLACK+Back.WHITE)
with open(pathSound,mode="r") as file:
    spareStr = file.read()
    sound = int(spareStr)
with open(pathProc,mode="r") as ProcFile1:
    ask = ProcFile1.read()
    if ask == 1:
        processor = 1
    elif ask == 2:
        processor = 2
        bought1 = True
with open(pathRam,mode="r") as ProcFile1:
    ask = ProcFile1.read()
    if ask == 1:
        memory = "16MB"
    elif ask == 2:
        memory = "32MB"
    elif ask == 3:
        memory = "64MB"
        bought = False
with open(pathName, mode = "r") as NameFile1:
    username = NameFile1.read()
while machineWorking:
    cls()
    print('Starting up TD',version)
    print('Loading system...')
    print('Finsesed loading system.')
    print('Loading standart applications')
    sleep(2)
    print('Finished loading applictaions')
    if sound == 1:
        playsound(startup)
    print("          "+Fore.RED+" __+___")
    print("          "+Fore.YELLOW+"/      \\")
    print("          "+Fore.GREEN+"|      |")
    print("          "+Fore.BLUE+"|      |")
    print("          "+Fore.MAGENTA+"\\______/"+Fore.BLACK)
    print("            TD",version)
    isWorking = True
    loggedOn = False
    sleep(3)
    while not(loggedOn):
        cls()
        logon(username)
        loggedOn = True
        current == 0
        if currentUser == 1:
            with open(pathPts,mode="r") as f1:
                ptsAmount = f1.readline()
        while isWorking:
            
                
            cls()
            chance = random.randint(0,99)
            if chance == 0:
                window("Install updates","To install newest updates, you have to reboot.")
                ask = textInput("Confirmation","Restart?(Y/N)")
                if ask == "N" or ask == "n":
                    
                    ask = ""
                    cls()
                else:
                    print("I just wanted to prank u!")
                    sleep(1)
                    isWorking = False
                    loggedOn = True
                     
            if current == 0:
                window("Tangerine Desktop","[C:]","","","","","")
            if current == 1:
                spareStr2 = "Version:" + version
                if processor == 1:
                    spareStr = "Processor: Lentium 1 115 MhZ"
                elif processor == 2:
                    spareStr = "Processor: AMB C6 178 MhZ"
                spareStr1 = "meRAM " + memory
                window("About TD",spareStr2,spareStr,spareStr1)
            if current == 2:
                spareStr = "1st number : "+str(num1)
                spareStr1 = "2nd number : "+str(num2)
                spareStr2 = "Operation : "+operation
                if operation == "+":
                    answer = num1 + num2
                elif operation == "-":
                    answer = num1 - num2
                spareStr3 = "Answer : "+str(answer)
                window("Calculator",spareStr,spareStr1,spareStr2,spareStr3)
                print(answer)
                print("To get help, print: help calc")
            if current == 3:
                if currentUser == 0:
                    spareStr = "Current user : Guest"
                else:
                    spareStr = "Current user : " + username
                window("Programs",spareStr,"Print esc to exit","Shutdown for shutdown/restart","1 : About","2 : Calculator","3 : Hardware Upgrade","4 : Settings, please!","5 : Settings")
            if current == 4:
                if memory == "16MB":
                    spareStr = "Avalible - Print *buy_1* to puchase it.Cost : 500 pts"
                    spareStr2 = "32 MB meRAM"
                elif memory == "32MB":
                    spareStr = "Avalible - Print *buy_1* to puchase it.Cost : 1000 pts"
                    spareStr2 = "64 MB meRAM"                    
                else:
                    spareStr = "Not avalible =("
                    spareStr2 = "96 MB meRAM"
                if processor != 1:
                    spareStr1 = "Avalible - Print *buy_2* to puchase it.Cost : 1000 pts"
                else:
                    spareStr1 = "Not avalible =("
                if bought == False & bought1 == False:
                    spareStr3 = "MusicBlaster 1"
                    
                window("Hardware upgrade",spareStr2,spareStr,"AMB C6 178 MhZ",spareStr1)
            if current == 5:
                if alreadyChecked:
                    alreadyChecked = False
                    name = ""
                    while count < 16:
                        spareint = random.randint(1,86)
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
                window("Settings, please!","1 right stamp = 10 pts","1 wrong stamp = -5 pts",spareStr,spareStr1,"","(A)ccept,(D)ecline,view (I)nstructions")
                
            if current == 6:
                spareStr = "Username:"+username
                window("Settings",spareStr,"{Change}")
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
            print(u"\u2550"*6+u"\u2566"+u"\u2550"+"Dock"+u"\u2550"*43)            
            print("  TD  "+u"\u2551"+"Shutdown Reboot Programs Tasks")
            print("Alpha "+u"\u2551"+"1 Desk 2",program1," ",end = "")
            if program2 != "":
                print("3",program2)
            else:
                print("")    
            inp = textInput("Awating input...","Command")
            if inp == "tasks":
                current = 7
            
            elif inp == "help":
                window("Command help","programs","close","tasks","shutdown")
                print("Press Enter to continue", end ="")
                input()               
            elif inp == "confirm":
                playsound(error)
                msgBox("?","Unknown cmd")  
            elif inp == "change":
                username = textInput("Change username","New username") 
                with open(pathName, mode = "w+") as NameFile1:
                    NameFile1.writelines(username)
            elif inp == "shutdown":
                ask = textInput("Required confirmation","(R)estart,(S)hutdown?")
                if ask == "R" or ask == "r" or ask == "Restart" or ask == "restart":
                    print("Now restarting...")
                    isWorking = False
                    cls()
                elif ask == "S" or ask == "s" or ask == "Shutdown" or ask == "shutdown":
                    print("Now shutting down...")
                    sleep(2)
                    machineWorking = False
                    isWorking = False
            elif inp == "esc":
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
            elif inp == "close":
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
                            currrent = 1
                        elif program2 == "Calc":
                            current = 2
                        elif program2 == "Upgrade":
                            current = 4
                        elif program2 == "DevCity":
                            current = 5
                        elif program2 == "SP":
                            current = 6
                if current == 5:
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
            elif inp == "programs":
                current = 3
            elif inp == "1" and current == 7:
                current = 0
                executingNow = 0
            elif inp == "2" and current == 7:
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
                executingNow = 1
            elif inp == "3" and current == 7:
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
                executingNow = 2            
            elif inp == "1" and current == 3:
                
                if program1 != "":
                    if memory == "16MB":
                        playsound(error)
                        msgBox("#","Memory overflow.")
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
            elif inp == "2" and current == 3:
                
                if program1 != "":
                    if memory == "16MB":
                        playsound(error)
                        msgBox("#","Memory overflow.")
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
                
            elif inp == "3" and current == 3:
                
                if not(currentUser == 0):
                    if program1 != "":
                        if memory == "16MB":
                            playsound(error)
                            msgBox("#","Memory overflow.")
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
            elif inp == "4" and current == 3:
                current = 5
                if program1 != "":
                    if memory == "16MB":
                        playsound(error)
                        msgBox("#","Memory overflow.")
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
                else:
                    executingNow = 1
                    program1 = "SP"
            elif inp == "5" and current == 3:
                
                if not(currentUser == 0):
                    if program1 != "":
                        if memory == "16MB":
                            playsound(error)
                            msgBox("#","Memory overflow.")
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
            elif inp == "help calc":
                window("Help for Calculator","num1 : edit first number","num2 : edit second number","op : edit operation")
            elif inp == "num 1" and current == 2:
                num1 = int(textInput("Enter a number","1st number"))
            elif inp == "num 2" and current == 2:
                num2 = int(textInput("Enter a number","2nd number"))
            elif inp == "op" and current == 2:
                op = textInput("Enter operation","Operation(+/-)")
                if op == "+":
                    operation = "+"
                elif op == "-":
                    operation = "-"
                else:
                    print("Wrong operation! Command cancelled.")
            elif inp == "buy_1":
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
            elif inp == "buy_2":
                if bought != True:
                    if current == 4:
                        if ptsAmount >= 1000:
                            with open(pathProc,mode="w+") as ProcFile2:
                                ProcFile2.write("2")                            
                            processor = 2
                            bought1 = True
            elif inp == "buy_3":
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
            elif inp == "switch":
                if executingNow == 0:
                    executingNow = 1
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
                elif executingNow == 1:
                    if program1 != "":
                        executingNow = 2
                        if program2 == "About":
                            current = 1
                        elif program2 == "Calc":
                            current = 2
                        elif program2 == "Upgrade":
                            current = 4
                        elif program1 == "SP":
                            current = 5
                        elif program1 == "Settings":
                            current = 6 
                    else:
                        executingNow = 0
                        current = 0
                elif executingNow == 2:
                    executingNow = 0
                    current = 0
            elif inp == "":
                #Do nothing...
                print("")
            elif inp == "A" and current == 5:
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
            elif inp == "D" and current == 5:
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
            elif inp == "I" and current == 5:
                print("Instructions:\n1:Only letters in name\n2.Let in only TD users")
                input("Hit ENTER to continue...")
            elif inp == "logoff":
                print(Back.GREEN+Fore.BLACK+"+Warning------------------+"+Back.WHITE+Fore.BLACK)
                ask = textInput("Required confirmation","Log off?(Y/N)")
                if ask =="Y" or ask == "y":
                    loggedOn = False
                    current = 0
                    program1 = ""
                    program2 = ""
                    with open(pathPts,mode="w+") as f1w:
                        f1w.write(str(ptsAmount))
                    break
                else:
                    print("Operation cancelled.")
                    input("Hit ENTER to continue...")
            else:
                playsound(error)
                msgBox("*","No such command!")
                
print("Thank you for taking a look at my project! :D")