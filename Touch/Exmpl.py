import mraa
oldState = 0
print (mraa.getVersion())
touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)
print('Off')
while True:
    touchButton = int(touch.read())
    if(oldState == 0):
        if(touchButton == 1):
            print('On')
            oldState = 1
    else:
        if(touchButton == 1):
            print('Off')
            oldState = 1
