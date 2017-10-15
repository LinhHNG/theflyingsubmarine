import serial,mraa,time

oldState = 0
print (mraa.getVersion())
touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)

ard = serial.Serial('/dev/tty96B0', 9600)


def showTemp(temp):
	if temp >= 30:
		print('help it is '+str(temp)+ 'Degrees')

if __name__ == '__main__':
    try:
        while True:
            input = []
            touchButton = int(touch.read())
            if(oldState == 0):
                if(touchButton == 1):
                    print('help')
                    time.sleep(1)
                    oldState = 1
            else:
                if(touchButton == 0):
                    oldState = 0
            ardOut = ard.read()
            ardTemp = ardOut.split('__*')
            while ardTemp[0] is not  '_' and not '':
                input.append(ardTemp[0])
                ardOut = ard.read()
                ardTemp = ardOut.split('__*')
            #while '' in showTemp:
                #showTemp.remove('')
            #Temp = ''.join(showTemp)
            #Temp = int(Temp)
            #showTemp(Temp)
            print(input)
    except KeyboardInterrupt:
        print("CTRL-C!! Exiting...")
		
