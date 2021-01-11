
from taskExec import *
from learn import *

def find(line):
    quest = ["who", "what", "where", "when", "why", "how", "search"]
    action = ["show", "tell", "play", "start", "can", "open", "create", "display"]
    command = line.split()[0].lower()
    if command in quest:
            quest_parser(line, command)
            filio(line, command, "success")
    elif command in action:
            action_parser(line, command)
            filio(line, command, "success")
    else:
            #Could implement command checker
                #ex- user enters: whta
                #bot - Did you mean to say 'what'?
            filio(line, command, "unknown")
            print("Sorry I couldn't perform that operation")
    #theme parser
    if command == "play":
        return "music"
    elif command == "start" or command == "create":
        return "reminder"
    elif command == "show" or command == "display":
        return "photos"
    else:    
        return "unknown"

def start(): #remove this line if you want to start think.py for terminal interaction 
    print("Welcome")
    line = ""
    while line != "stop":
        #after every ':' for input, it can offer a prediction of what you might want using machine learning
        line = input(":")
        if line != "stop":
            find(line)