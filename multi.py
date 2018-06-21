#!/usr/bin/python 

import time

#creating a menu for the user

menu='''
Press 1 to check current time and date
Press 2 to scan all your MAC address in connection network 
Press 3 to shutdown your machine after 15 min 
Press 4 to search something on google
Press 5 to logout your current machine
Press 6 to shutdown all your connected systems in current network
Press 7 to update status on fb 
Press 8 to list ip address of given website
'''
#printing the menu 

print(menu)

#taking input from the user
#assigning the input to a variable 

choice=input()
#checking for the option and displaying input

if choice == '1' :
        print ("curent date and time is : ", time.ctime())

elif choice == '2' :
        print ("wait till we scan all your MAC address in connection network")
elif choice == '3' :
        print ("shutting down the machine in 15 mins....wait")
elif choice == '4' :
        print ("directing to google")
elif choice == '5' :
        print ("logging out of your current machine")
elif choice == '6' :
        print ("shutting down all connecting systems in current network")
elif choice == '7' :
        print ("updating status on fb ")
elif choice == '8' :
        print ("listing the ip address of the website")
else :
        print ("wrong choice")

