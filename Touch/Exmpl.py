import mraa
print (mraa.getVersion())
touch = mraa.Gpio(29)
touch.dir(mraa.DIR_IN)
while True:
  touchButton = int(touch.read())
  if(touchButton == 1):
      print('On')
  else:
      print('Off')
