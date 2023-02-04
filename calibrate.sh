#used to calibrate the joystick minimum and maximum values

sudo pkill -f /home/A4Scripts/userInterface.py
sudo python3 /home/A4Scripts/findValues.py
sudo python3 /home/A4Scripts/userInterface.py &
