import mraa,time

print (mraa.getVersion())
i= 0
while True:
    time.sleep(0.5)
    try:
        touch = mraa.Gpio(i)
        touch.dir(mraa.DIR_IN)
        touchButton = int(touch.read())
        if(touchButton == 1):
            print('yay something happened')
    except:
        print('Error on ' str(i))
