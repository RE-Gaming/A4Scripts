#Used to determine minimum and maximum values
import os
import time
import uinput
import spidev

#Variable Definitions
spiBus = 0
spiDevice = 0
joystickValue = 0
values = [512, 512, 512, 512]
LINE_UP = '\033[1A'
LINE_CLEAR = '\x1b[2K'

#GPIO Definitions
battLow = 4
battCrit = 5
spiCS = 8
spiMISO = 9
spiMOSI = 10
spiCLK = 11

#GPIO Initialization
spi = spidev.SpiDev()
spi.open(spiBus, spiDevice)
spi.max_speed_hz = 800000
spi.mode = 0b01

#global min0
#global max0
#global min1
#global max1



def joystickReading(channel):
	joystickBuffer = spi.xfer(channel, 800000, 10, 8)
	joystickValue = int((((joystickBuffer[0] & 0x0F) * 256) + joystickBuffer[1]) / 4)
	#print(axis, joystickValue)
	#print(LINE_UP, end=LINE_CLEAR)
	return joystickValue

#Setup Code


#Looping Code
def main():
	print('move the joystick in circles along the outer edges')
	for i in range(2000):
		time.sleep(0.01)
		joystickValueX = joystickReading([0x00, 0x00])
		joystickValueY = joystickReading([0x08, 0x00])
		if values[0] > joystickValueX:
			values[0] = joystickValueX
		if values[1] < joystickValueX:
			values[1] = joystickValueX
		if values[2] > joystickValueY:
			values[2] = joystickValueY
		if values[3] < joystickValueY:
			values[3] = joystickValueY
		print(joystickValueX, joystickValueY)
		print(LINE_UP, end=LINE_CLEAR)

	print(values[0])
	print(values[1])
	print(values[2])
	print(values[3])

	if os.path.exists("/home/pi/A4Scripts/joystickCalibration.txt"):
		os.remove("/home/pi/A4Scripts/joystickCalibration.txt")

	f = open("/home/pi/A4Scripts/joystickCalibration.txt", "w")
	f.write(str(values[0]))
	f.write("\n")
	f.write(str(values[1]))
	f.write("\n")
	f.write(str(values[2]))
	f.write("\n")
	f.write(str(values[3]))
	f.write("\n")


if __name__ == "__main__":
	main()
