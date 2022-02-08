from functions import *
topbar()
home()
hometask = input(":-")

if "1" in hometask:
    new_user()
elif "2" in hometask:
    print("")
elif "3" in hometask:
    print("")
elif "find" in hometask:
    file = open("this.odf", "r")     #Opens the file in r mode
    for lines in file:
        if "pallav" in lines:
            print("True"+lines)
        else:
            print("False")
    # text = file()          #Read its content
    # print(text)     #Print its contents
    file.close() 
else:
    print("403 Unknown Error Occured :/")