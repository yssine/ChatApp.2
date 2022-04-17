import socket
import threading
from matplotlib import image
from requests import get
from netifaces import interfaces, ifaddresses, AF_INET
import pickle
from dep.cls import User, Message





HEADER=128
FORMAT='utf-8'
PORT=6969
# ip = get('https://api.ipify.org').text
# SERVER = ip
SERVER = socket.gethostbyname(socket.gethostname())
#SERVER = ifaddresses('wlan0').setdefault(AF_INET)[0]['addr']
ADDR=(SERVER, PORT)
DISCONNECT = "!CACTUS IS LOVE!"
CONNECTED =[]
Online=""
# print(ip)

server=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)




def receive(conn):
	msg_l = conn.recv(HEADER).decode(FORMAT)
	if msg_l:
		msg_l = int(msg_l)
		msg = pickle.loads(conn.recv(msg_l))
	return msg

def brodcast(msg):
	global CONNECTED

	message = pickle.dumps(msg)
	msg_l = str(len(message)).encode(FORMAT)
	msg_l += b' ' * (HEADER - len(msg_l))
	for client in CONNECTED:
		client.send(msg_l)
		client.send(message)





def handle_client(mycl):
	print(f'[New connection]: {mycl.addr} has connected.')
	CONNECTED.append(mycl.conn)
	print(f'[CONNECTED]: {len(CONNECTED)} ')
	global Online
	connected = True
	while connected:
		message=receive(mycl.conn)
		if message.typ == 'Hello':
			mycl.usn =message.usr.usn
			Online+='|'+message.usr.usn+':'+str(message.usr.pdp)
			# print(Online)
			brodcast(Message(User('server'),msg=Online,typ='Onl'))

		if message.typ == 'disconnect':
			print(f'[Dicsconnected]: {mycl.usn} has disconnected.')
			connected = False
			CONNECTED.remove(mycl.conn)
			# Online.remove([message.usr.usn,message.usr.pdp])
			Online=Online.replace('|'+message.usr.usn+':'+str(message.usr.pdp),'')
			brodcast(Message(User('server'),msg=Online,typ='Onl'))
			# print(Online)
			print(f'[CONNECTED]: {len(CONNECTED)} ')

		else:

			if message.typ=='text':
				print(f'[{message.usr.usn}]:  {message.msg}')
				# data2p={"user":usr,"text":msg,"file":None,"image":None}
				brodcast(message)
		# 	if im:
		# 		# image=open(f'src/{usr}.png', 'wb')
		# 		print(f'[{usr}]:  {im}')
		# 	if fi:
		# 		print(f'[{usr}]:  {fi}')
		# # 	# print(msg)


def start():
	server.listen()
	print(f'[Listening]: The server is listening at {SERVER}')
	while True:
		conn, addr = server.accept()
		mycl = User(conn=conn,addr=addr)
		thread = threading.Thread(target=handle_client, args=(mycl,))
		thread.start()


print('[Starting]: The server is starting...')
start()
