echo This is a script to get google access automatically.
echo Powered by Waldo Tsui.
echo All Rights Reserved.
echo Ver. 1.0.
rm ./hosts_new
rm ./hosts_old
wget https://raw.githubusercontent.com/racaljk/hosts/master/hosts
mv ./hosts ./hosts_new
cp /etc/hosts ./hosts_old
python3 edit_hosts.py
cp /etc/hosts ~/Documents/hosts.bak/hosts.bak
echo Backup Complete.
cp ./hosts_edited /etc/hosts
echo All Complete,Enjoy~
