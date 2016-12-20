# project-djangorest-angular
This is own pet project. I want to build backend with Django Rest Framework to make it flexible and modern and in Frontend side I prefere Angular. 

How to install this project?
# SERVER SIDE
1. Copy this project
git clone https://github.com/DesmondJava/project-djangorest-angular.git

2. You need tools defined below
apt get install virtualenvwrapper
apt get install pip

3. Create own vitrual environment, install django
mkvirtualenv taskmanager
pip install django==1.8.5
pip install djangorestframework==3.3.0

4. Make migration of our models
python server/manage.py makemigrations retail
python server/manage.py migrate

# CLIENT SIDE
1. Install nodejs
sudo apt-get install npm

2. Go to the client folder in the project and install requiments to npm
cd client/
npm install

3. Install bower globally
sudo npm install -g grunt-cli
ln -s /usr/bin/nodejs /usr/bin/node
npm install -g bower

4. Install dependencies for bower (angular etc)
bower install --config.interactive=false --allow-root

5. Start our project
node server.js

NOW YOU CAN CHECK FRONTEND SIDE FROM BROWSER
http://127.0.0.1:8081/
