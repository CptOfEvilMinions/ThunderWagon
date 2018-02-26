# ThunderWagon

## Docker setup
0. docker build -t thunderwagon .
0. docker run -d -p 80:5000 thunderwagon

## Install/Setup on Centos 7
0. yum install epel-release git nginx tmux python-pip -y
0. pip install virtualenv 
0. useradd webapp
0. su webbapp
0. git clone https://github.com/Benster900/ThunderWagon.git
0. cd ThunderWagon/webapp
0. Add Slack webhook token to config.py
4. tmux new -s webapp
4. virtualenv env
5. source env/bin/activate
5. pip install -r requirements.txt
5. python run.py
5. Control + B + D
6. Set nginx as a reverse proxy
7. cp conf/webapp_reverse_proxy.conf /etc/nginx/conf.d/
8. systemctl restart nginx
