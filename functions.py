from termcolor import colored, cprint

def topbar():
    print("Welcome To Hotel Management System")
    text = colored('Release-Alpha 0.0.1  "Designed and Maintained by TeamPallav@"', 'red', attrs=['blink','bold','dark'])
    print(text)

def home():
    print("!!Shree!!")
    print("")
    print("Select task from the following list:-")
    print("")
    print("1]To Create a new user, Press 1")
    print("2]To Create a new admin Press 2")
    print("3]To New Check-In press 3")
    print("")
    print("")
    print("More comming soon.....")
