add-apt-repository ppa:nginx/stable
apt-get update

echo "Installing packages"
apt-get install -y python-pip python-dev libpq-dev build-essential git python-software-properties nmap curl vsftpd supervisor nginx postgresql python-psycopg2 xclip python-virtualenv supervisor

cd /opt

echo "Installing Node \n"
wget http://nodejs.org/dist/v0.10.25/node-v0.10.25.tar.gz
tar -xf node-v0.10.25.tar.gz && cd node-v0.10.25 && ./configure && make && make install
curl -L https://get.rvm.io | bash -s stable

echo "Installing Ruby \n"

source /usr/local/rvm/scripts/rvm
sudo rvm requirements
sudo rvm install ruby

echo "Installing grunt command line"
sudo npm -g install grunt-cli bower

#sudo pip install virutalenvwrapper

#supervisor conf https://gist.github.com/tsabat/1528270
#continous integration
wget -q -O - https://jenkins-ci.org/debian/jenkins-ci.org.key | sudo apt-key add -
sudo sh -c 'echo deb http://pkg.jenkins-ci.org/debian binary/ > /etc/apt/sources.list.d/jenkins.list'
sudo apt-get update
sudo apt-get install jenkins
