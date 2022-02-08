from termcolor import colored, cprint

def topbar():
    print("Welcome To Hotel Management System")
    cprint('Release-Alpha 0.0.1  "Designed and Maintained by TeamPallav@"', 'red', attrs=['blink','bold','dark'])
def home():
    print("!!Shree!!")
    print("")
    cprint("Select task from the following list:-","yellow", attrs=["bold","dark",])
    print("")
    print("1]To Create a new user, Press 1")
    print("2]To Create a new admin, Press 2")
    print("3]To New Check-In press 3")
    print("")
    print("")
    print("More comming soon.....")
    print("Press 'Ctrl+C' to cancel/crash the programm and exit at any time")
def new_user():
    print("Creating New User......")
    username = input("Enter Your Name:- ")
    userverificationtype = input("Enter Verification ID type:- ")
    verifyid = input("Enter Verification ID Number:- ")
    amount =  input("Enter The Amount For Bill:- ")
    f = open("this.odf", "w")
    f.write("User Name:-"+username+"\n")
    f.write("User Verification type"+userverificationtype+"\n")
    f.write("User Verification ID"+verifyid+"\n")
    f.write("User Bill Amount Calculated As Per Reciptant"+amount+"\n")
    f.close()

    