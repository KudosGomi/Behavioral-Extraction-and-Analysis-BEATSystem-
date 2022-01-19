sudo apt-get install wget
sudo apt-get install gnupg
wget -qO - https://www.mongodb.org/static/pgp/server-4.2.asc | sudo apt-key add -
echo "deb http://repo.mongodb.org/apt/debian buster/mongodb-org/4.2 main" | sudo tee /etc/apt/sources.list.d/mongodb-org-4.2.list
sudo apt-get install python3-pip
sudo apt-get update
sudo apt-get install -y mongodb-org
sudo apt-get install radare2

mkdir /usr/share/radare2/3.9/www

python3 -m pip install pymongo
python3 -m pip install r2pipe
python3 -m pip install scapy
