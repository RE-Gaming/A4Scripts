# Script used to download the lastest config files and replace the current files

cd
git clone https://github.com/RE-Gaming/getUpdate
sudo cp -r getUpdate/configs/* /opt/retropie/configs/
sudo rm -r getUpdate
