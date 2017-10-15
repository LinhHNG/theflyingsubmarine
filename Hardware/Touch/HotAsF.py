import serial

ard = serial.Serial('/dev/tty96B0', 9600)


def showTemp(humid, temp):
	print('Humidity: '+str(humid))
	print('Temperature: '+str(temp))

if __name__ == '__main__':
	print("Welcome to the Humidity & Temperature reader!!!")
	try:
		while True:
			ardOut = ard.readline()
			if ardOut.find("Humidity:") != -1:
        		ardHumid = ardOut.split('Temperature')[0]
				ardTemp = ardOut.split('Temperature:')[1]
				showTemp(ardHumid,ardTemp)
	except KeyboardInterrupt:
		print("CTRL-C!! Exiting...")
