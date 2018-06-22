#!/usr/bin/python2

import time
import commands

#taking input from the user
object='''
Press 1 to check internet cable on your machine
press 2 to check internet access
Press 3 to check for google access
'''
print(object)
#storing the value in a variable 
choice=raw_input()
#if user press 1 check for cable connectivity
if choice == '1'  :
        print "please wait internet cable is being checked"
        cable=commands.getoutput('sudo mii-tool eno1')
        if 'link ok' in cable_check :
                print "cable is connected"
        else :
                print "not connected"
#if user press 2 check for internet connectivity

elif choice == '2' :
	print "please wait internet connectivity is being checked"
#if user press 3 check for google access 

elif choice == '3' :
	print "checking for google access"	
# otherwise specify a wrong choice

else :
	print "wrong option"



