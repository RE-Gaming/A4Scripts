
import RPi.GPIO as GPIO
import os
import time
import uinput
import spidev

#Variable Definitions
spiBus = 0
spiDevice = 0
battIndicator = [0, 0, 0, 0, 0, 0]
joystickValue = 0
deadZone = 18
calValues = []
debounce = 5

f = open("/home/A4Scripts/joystickCalibration.txt", "r")
calValues = f.readlines()
calValues[0] = int(calValues[0])
calValues[1] = int(calValues[1])
calValues[2] = int(calValues[2])
calValues[3] = int(calValues[3])
f.close()

#GPIO Definitions
battLow = 4
battCrit = 5
spiCS = 8
spiMISO = 9
spiMOSI = 10
spiCLK = 11

enPI = 6
keepAlive = 7
fanPWM = 45

right = 0
up = 1
down = 2
left = 3
option = 14
leftShoulder = 15
joystick = 16
leftTrigger = 17
rightTrigger = 12
rightShoulder = 13
z = 20
c = 44
y = 22
b = 23
x = 24
a = 25
start = 26
select = 27

#GPIO Initialization
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(battLow, GPIO.IN)
GPIO.setup(battCrit, GPIO.IN)

GPIO.setup(keepAlive, GPIO.OUT)
GPIO.setup(enPI, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.output(keepAlive, GPIO.HIGH)

GPIO.setup(fanPWM, GPIO.OUT)
#fan = GPIO.PWM(fanPWM, 1000)
#fan.start(0)
GPIO.output(fanPWM, 1)

spi = spidev.SpiDev()
spi.open(spiBus, spiDevice)
spi.max_speed_hz = 1000000
spi.mode = 0b01

GPIO.setup(right, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(up, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(down, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(left, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(option, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(leftShoulder, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(joystick, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(leftTrigger, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightTrigger, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(rightShoulder, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(z, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(c, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(y, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(b, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(x, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(a, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(start, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(select, GPIO.IN, pull_up_down=GPIO.PUD_UP)

def buttonPress(channel):
	if (not buttonStatus[channel]):
		buttonStatus[channel] = 1
		device.emit(eventsMask[channel], 1)
	if (buttonStatus[channel]):
		buttonStatus[channel] = 0
		device.emit(eventsMask[channel], 0)

def buttonPress2(channel):
	if (not GPIO.input(channel)):
		buttonStatus[channel] = 1
		device.emit(eventsMask[channel], 1)
	if (GPIO.input(channel)):
		buttonStatus[channel] = 0
		device.emit(eventsMask[channel], 0)

GPIO.add_event_detect(right, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
GPIO.add_event_detect(up, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
GPIO.add_event_detect(down, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
GPIO.add_event_detect(left, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
#GPIO.add_event_detect(option, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
#GPIO.add_event_detect(leftShoulder, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
GPIO.add_event_detect(joystick, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
#GPIO.add_event_detect(leftTrigger, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
#GPIO.add_event_detect(rightTrigger, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
#GPIO.add_event_detect(rightShoulder, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
GPIO.add_event_detect(z, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
GPIO.add_event_detect(c, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
GPIO.add_event_detect(y, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
GPIO.add_event_detect(b, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
GPIO.add_event_detect(x, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
GPIO.add_event_detect(a, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
GPIO.add_event_detect(start, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)
GPIO.add_event_detect(select, GPIO.BOTH, callback=buttonPress2, bouncetime=debounce)

#Uinput Initialization
events = (
	uinput.BTN_DPAD_RIGHT, uinput.BTN_DPAD_UP, uinput.BTN_DPAD_DOWN, uinput.BTN_DPAD_LEFT,
	uinput.BTN_MODE, uinput.BTN_TL, uinput.BTN_JOYSTICK, uinput.BTN_TL2, uinput.BTN_TR2, uinput.BTN_TR,
	uinput.BTN_Z, uinput.BTN_C, uinput.BTN_Y, uinput.BTN_B, uinput.BTN_X, uinput.BTN_A,
	uinput.BTN_START, uinput.BTN_SELECT, uinput.ABS_X + (0,1023,0,0), uinput.ABS_Y + (0,1023,0,0)
	)

eventsMask = [
        uinput.BTN_DPAD_RIGHT, uinput.BTN_DPAD_UP, uinput.BTN_DPAD_DOWN, uinput.BTN_DPAD_LEFT,
	0, 0, 0, 0, 0, 0, 0, 0, uinput.BTN_TR2, uinput.BTN_TR,
        uinput.BTN_MODE, uinput.BTN_TL, uinput.BTN_JOYSTICK, uinput.BTN_TL2, 0, 0,
        uinput.BTN_Z, 0, uinput.BTN_Y, uinput.BTN_B, uinput.BTN_X, uinput.BTN_A,
        uinput.BTN_START, uinput.BTN_SELECT,
        0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, uinput.BTN_C
        ]

buttonStatus = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

device = uinput.Device(events)

#Supporting Functions
def batteryStatus(channel):
	if (not battIndicator[channel]) and (not GPIO.input(channel)):
		battIndicator[channel] = 1
		print("battery status lower")
	if (battIndicator[channel]) and GPIO.input(channel):
		battIndicator[channel] = 0
		print("battery status higher")

def joystickValue(channel, axis):
	joystickBuffer = spi.xfer(channel, 1000000, 10, 8)
	joystickValue = int((((joystickBuffer[0] & 0x0F) * 256) + joystickBuffer[1]) / 4)
	if axis == 0: #X axis
		if (joystickValue > (512 + deadZone)):
			joystickValue = int(((512/(calValues[1]-511)) * joystickValue) - ((1023-calValues[1])*(512/(calValues[1]-511))))
			if joystickValue > 1023:
				device.emit(uinput.ABS_X, 1023)
			else:
				device.emit(uinput.ABS_X, joystickValue)
		elif (joystickValue < (512 - deadZone)):
			joystickValue = int(((512/(512-calValues[0])) * joystickValue) - (512/(512-calValues[0])*calValues[0]))
			if joystickValue < 0:
				device.emit(uinput.ABS_X, 0)
			else:
				device.emit(uinput.ABS_X, joystickValue)
		else:
			device.emit(uinput.ABS_X, 512)
	else:	#Y axis
		if (joystickValue > (512 + deadZone)):
			joystickValue = int(((512/(calValues[3]-511)) * joystickValue) - ((1023-calValues[3])*(512/(calValues[3]-511))))
			if joystickValue > 1023:
				device.emit(uinput.ABS_Y, 1023)
			else:
				device.emit(uinput.ABS_Y, joystickValue)
		elif (joystickValue < (512 - deadZone)):
			joystickValue = int((512/(512-calValues[2]) * joystickValue) - (512/(512-calValues[2])*calValues[2]))
			if joystickValue < 0:
				device.emit(uinput.ABS_Y, 0)
			else:
				device.emit(uinput.ABS_Y, joystickValue)
		else:
			device.emit(uinput.ABS_Y, 512)
#Setup Code

#fan.ChangeDutyCycle(100)
GPIO.output(fanPWM, 0)

#Looping Code
while True:
	time.sleep(0.01)
	buttonPress2(option)
	buttonPress2(leftShoulder)
	buttonPress2(leftTrigger)
	buttonPress2(rightTrigger)
	buttonPress2(rightShoulder)
	joystickValue([0x00, 0x00], 0)
	joystickValue([0x08, 0x00], 1)
	if not GPIO.input(enPI):
		os.system("sudo fbi -T 1 -a -noverbose /home/A4Scripts/shutdown.png")
		os.system("sudo /home/A4Scripts/multi_switch.sh --es-closeemu")
		time.sleep(1)
		os.system("sudo /home/A4Scripts/multi_switch.sh --es-systemd")
		time.sleep(2)
		GPIO.output(keepAlive, 0)
		time.sleep(1)
