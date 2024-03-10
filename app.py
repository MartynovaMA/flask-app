from flask import Flask, request, render_template ,json
import socket
from ipaddress import *

app=Flask(__name__)
#app=Flask(__name__, template_folder="templates")

@app.route("/")
def index():
	return "Welcome!"

@app.route("/login",methods=['POST','GET'])
def login():
	if request.method == 'POST':
		username=request.form.get('username')
		password=request.form.get('password')
		#проверка логина и пароля
		if username and password:
			ipAddr=get_local_ip()
			for ip in ip_network('192.168.32.160/255.255.255.240'):
			#for ip in ip_network('127.0.0.1/255.255.255.240'):
				print(ip)

			return render_template('list.html',ip=ipAddr,adressa=ip)
			#return 'Вы вошли в систему!'
	else:
		return render_template('login.html')	
		
def get_local_ip():
	hostname=socket.gethostname()
	local_ip=socket.gethostbyname(hostname)
	return local_ip
	
if __name__=="__main__":
	from waitress import serve
	serve(app, host="0.0.0.0", port=8080)	
