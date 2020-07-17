def window(title,*contents):
    '''
    Name : window
    Input : title,*lines
    Output : beautiful TUI window
    '''
    print(u"\u2554"+"X"+u"\u2550"*4+title+u"\u2550"*30+u"\u2193\u2557")
    for lines in contents:
        print(u"\u2551"+lines+" "*(len(title)+35-len(lines)),"\u2551")
    print(u"\u255a"+u"\u2550"*36+u"\u2550"*len(title)+u"\u255d")

def cls():
    '''
    Name : cls
    Input : none
    Output: \n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n
    '''
    print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
    
def textInput(title, text):
    """
    
    """
    print(u"\u2554"+"X"+u"\u2550"*4+title+u"\u2550"*30+u"\u2193\u2557")
    print(u"\u2551",end="")
    return input(text+"[")

def msgBox(icon,text):
    print(icon+"\u2550"*20+"\u2557")
    print("\u2551"+text+" "*(20-len(text))+"\u2551")
    print("\u2551        \u25baOK\u25c4        \u2551")
    print("\u255a"+"\u2550"*20+"\u255d")
    input()
    