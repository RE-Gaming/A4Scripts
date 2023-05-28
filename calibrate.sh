#used to calibrate the joystick minimum and maximum values

sudo pkill -f /home/pi/A4Scripts/userInterface.py
sudo python3 /home/pi/A4Scripts/findValues.py
sudo python3 /home/pi/A4Scripts/userInterface.py &
