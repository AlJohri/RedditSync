sudo apt-get update -y
sudo apt-get install -y git vim make wget curl build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev llvm libncurses5-dev
wget https://www.python.org/ftp/python/3.5.1/Python-3.5.1.tgz
tar -xvf Python-3.5.1.tgz
rm Python-3.5.1.tgz
cd Python-3.5.1
./configure
make
sudo make install
cd ~
git clone https://github.com/AlJohri/RedditBlogger.git
cd RedditBlogger
pip3.5 install --upgrade pip
pip3.5 install -r requirements.txt