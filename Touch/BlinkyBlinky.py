import mraa,time

print (mraa.getVersion())
i= 0
while True:
    try:
        t = mraa.Gpio(i)
        t.dir(mraa.DIR_OUT)
    except:
        print('Error on Pin '+str(i))
    else:
        print('Works on '+str(i))

    
