import serial

ard = serial.Serial('/dev/tty96B0', 9600)


def showTemp(temp):
	print(str(temp)+ Degrees)

if __name__ == '__main__':

	try:
		while True:
			ardOut = ard.readline()
			if ardOut.find("Humidity:") != -1:
				ardTemp = ardOut.split('__*')[1]
				showTemp(ardTemp)
	except KeyboardInterrupt:
		lcd.setColor(0,0,0)
		lcd.clear()
		print("CTRL-C!! Exiting...")
