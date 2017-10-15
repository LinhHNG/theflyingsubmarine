import mraa

print (mraa.getVersion())
i= 24
touch = mraa.Gpio(i)
touch.dir(mraa.DIR_OUT)
toutch.write(0)
touch.dir(mraa.DIR_IN)
    while True:
        touchButton = int(touch.read())
        if(touchButton == 1):
            print('yay something happened')
