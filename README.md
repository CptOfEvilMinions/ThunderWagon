# ThunderWagon
## Install/Setup on Centos 7
0. yum install epel-release git nginx tmux python-pip -y
1. pip install virtualenv
1. useradd webapp
2. su webbapp
2. git clone https://github.com/Benster900/ThunderWagon.git
3. cd ThunderWagon
3. Add Slack webhook token to config.py
4. tmux new -s webapp
4. virtualenv env
5. source env/bin/activate
5. pip install -r requirements.txt
5. python run.py
5. Control + B + D
6. Set nginx as a reverse proxy
7. cp conf/webapp_reverse_proxy.conf /etc/nginx/conf.d/
8. systemctl restart nginx
