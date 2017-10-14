import mraa

print (mraa.getVersion())
i= 29
touch = mraa.Gpio(i)
touch.dir(mraa.DIR_OUT)
