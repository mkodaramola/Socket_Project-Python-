import socket

# Set Socket
clientsocket = socket.socket()

host = '127.0.0.1'
port = 1233

print("Waiting for connection")

# Connect
try:
	clientsocket.connect((host,port))
except socket.error as e:
	print(str(e))

resp = clientsocket.recv(1024)
print(resp.decode('utf-8'))

# TransReceive
while True:
	msg = input("Send to Server: ")
	clientsocket.send(str.encode(msg))
	resp=clientsocket.recv(1024)
	print(resp.decode('utf-8'))

clientsocket.close()



