inited = True
spareBool = False
spareStr = ""
spareStr2 = ""
spareStr3 = ""
lastkey = ""
spareInt = 0
example_db = {"respond":"Responding u","test":"print('hello world')","error":"Genereal database searching error."}
from time import sleep

def drawCompy(face):
    if inited:
        print("\u2554\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2557")
        print("\u2551 "+face[:1]+" "+face[2:]+" \u2551 \u2551")
        print("\u2551  "+face[1:2]+"  \u2551 \u2551")
        print("\u255a\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u255d")        

def askCompy(answerBase):
    spareInt = 0
    if inited:
        print("\u2554\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2557")
        print("\u2551 o o \u2551 \u2551")
        print("\u2551  u  \u2551 \u2551")
        print("\u255a\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u255d")
        spareStr = input("Ask me! >")
        lastkey = "key"
        spareStr2 = list(answerBase.keys())[-1]
        while lastkey != spareStr2 :
            spareStr3 = list(answerBase.keys())[spareInt]
            spareBool = spareStr3 in spareStr
            if spareBool:
                break
            lastkey = list(answerBase.keys())[spareInt]
            spareInt = spareInt + 1
        if not(spareBool):
            print("\u2554\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2557")
            print("\u2551 0 0 \u2551 \u2551")
            print("\u2551  _  \u2551 \u2551")
            print("\u255a\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u255d")            
            print(list(answerBase.values())[-1])
        else:
            print("\u2554\u2550\u2550\u2550\u2550\u2550\u2566\u2550\u2557")
            print("\u2551 u u \u2551 \u2551")
            print("\u2551  w  \u2551 \u2551")
            print("\u255a\u2550\u2550\u2550\u2550\u2550\u2569\u2550\u255d")
            try:
                exec(list(answerBase.values())[spareInt])
            except:
                print(list(answerBase.values())[spareInt])
        spareInt = 0

        
        
