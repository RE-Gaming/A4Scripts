# A4Scripts - Files for the REG A4

Github: https://www.github.com/RE-Gaming <br />
Website: https://www.re-gaming.com <br />
Kickstarter: TBD <br />
<br />
File Descriptions <br />
- **calibrate.sh**: Script used to calibrate the joystick
- **disableWifi.sh**: Script used to disable Wifi/Ethernet related programs that occur at boot, reduces boot time ~12 seconds
- **enableWifi.sh**: Script used to enable the programs that are disabled by disableWifi.sh
- **findValues.py**: Python script called by calibrate.sh, determines minimum and maximum values for joystick on X adn Y axis. Exports values to joystickCalibration.txt
- **joystickCalibration.txt**: Text file to store the calibration outputs from findValues.py, imported into userInterface.py
- **userInterface.py**: Python script run from autostart.sh. Handles all button mapping, joystick inputs, and software shutdown when power switch is turned to off position
- **config.txt**: Updated config.txt file for the REG A4 specifically, configures the RPi CM4 to handle the screen, audio, USB, SPI, and external HDMI port 
- **cmdline.txt**: Updated cmdline.txt file for the REG A4 specifically, hides all boot code from the user for cleaner startup experience
- **multi_switch.sh**: Scripted used to close out the emulator and emulationstation during shutdown
- **batteryCrit.png** and **batteryLow.png** are used to display battery status
- **fastboot.png**, **fullboot.png**, and **joystick.png** are used as icons in the RetroPie menu
