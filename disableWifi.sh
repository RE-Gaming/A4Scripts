#This script disables the wifi on boot to make boot times faster
#Use enableWifi.sh to re-enable wifi on boot when needed

sudo systemctl disable dhcpcd.service
sudo systemctl disable networking.service
sudo systemctl disable ntp.service
sudo systemctl disable nmbd.service
sudo systemctl disable smbd.service
sudo systemctl disable wpa_supplicant.service
sudo systemctl disable avahi-daemon.service

