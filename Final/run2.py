# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 14:14:11 2017

@author: micha
"""


import mraa,serial
from twilio.rest import Client

oldState = 0
print (mraa.getVersion())
touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)
print('Off')

from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACf724412dff5c571d8ba30128c5aac4e1"
# Ask me for actual authorisation code
auth_token  = "_______"

ard = serial.Serial('/dev/tty96B0', 9600)

           
def distresssms():
    message = client.messages.create(
            to="_______", 
            from_="+441277505957",
            body= "help!!")
    print(message.sid)
def showTemp(temp):
    if temp >= 30:
        print('help it is '+str(temp)+ 'Degrees')
        distresssms()
        
        
    
    
if __name__ == '__main__':
    client = Client(account_sid, auth_token)
    while True:
        touchButton = int(touch.read())
        ardOut = ard.readline()
        ardTemp = ardOut.split('\n')
        showTemp(int(ardTemp))
        if(oldState == 0):
            if(touchButton == 1):
                print('On')
                distresssms()
                oldState = 1
        else:
            if(touchButton == 0):
                print('Off')
                oldState = 0
