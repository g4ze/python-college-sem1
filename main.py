from fetcher import *
from userupdate import userupdate
from displayinfo import displayinfo
from variables import *
from menus import *
#=====================================================
# # OBJECT CREATION FOR ALL CLASSES
#-----------------------------------------------------
menu=menus()
info=Reader()
userup=userupdate()
display=displayinfo()
#======================================================
username=''

print("====================== HELLO I'M ARORA A PERSONAL FINANCE ADVISOR=================================")
while True:
    
    print('==================DEAR USER, PLEASE ENTER YOUR NAME===========================')
    print('type "ex" to exit anytime')
    username=input('NAME: ')
    if username=='ex':
        break
    # print(info.check(username))
    if info.check(username):
        print('==========================WHAT DO YOU WANT ME TO ASSIST WITH============================')
    else:
        print('===============USER NOT FOUND===========================')
        while True:
            print('================DO YOU WANT TO CREATE A NEW PROFILE?=================')
            print('Y/N')
            chc=input()
            if chc=='Y':
                print('==================ENTERING PROFILE CREATION===================')
                userup.newUser(username)
                print('============GREAT! NOW I SHALL ASK YOU A FEW MORE DETAILS FOR THIS MONTH==========')
                userup.infoUpdate(username)
                print('==========NOW WE ARE GOOD TO GO!!=================')
                print('================USER PROFILE COMPLETE==================')
                print('===========DO YOU WANT TO CONTINUE?============')
                while True:
                    chc=input('Y/N')
                    if chc=='N': break
                    else:
                        menus().menu1()
            elif chc=='N':
                print('=======YOU ENTERED NO!===========')
                break
            elif chc=='ex':
                break
            else:
                print('================Enter again============')




