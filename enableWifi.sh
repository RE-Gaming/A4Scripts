#This script disables the wifi on boot to make boot times faster
#Use enableWifi.sh to re-enable wifi on boot when needed

sudo systemctl enable dhcpcd.service
sudo systemctl enable networking.service
sudo systemctl enable ntp.service
sudo systemctl enable nmbd.service
sudo systemctl enable smbd.service
sudo systemctl enable wpa_supplicant.service
sudo systemctl enable avahi-daemon.service

