# -*- coding: utf-8 -*-
"""
Created on Sun Oct 15 13:58:17 2017

@author: micha
"""

import mraa
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
auth_token  = "_____"


           
def distresssms():
    message = client.messages.create(
            to="______", 
            from_="+441277505957",
            body= "help!!")
    print(message.sid)
    
if __name__ == '__main__':
    client = Client(account_sid, auth_token)
    while True:
        touchButton = int(touch.read())
        if(oldState == 0):
            if(touchButton == 1):
                print('On')
                distresssms()
                oldState = 1
        else:
            if(touchButton == 0):
                print('Off')
                oldState = 0
