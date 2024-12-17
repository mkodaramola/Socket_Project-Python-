import socket

# Set up Socket
server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Start Server at 127.0.0.1 (port 12345)
server_socket.bind(('127.0.0.1',12345))

# Start listening
server_socket.listen(5)



while True:
	# Wait for Client to join Server
	print("Server waiting for connection")
	client_socket, addr = server_socket.accept()
	
	# After connection print this
	print("New client connection --> ",addr)
	while True:

		#Receive Data
		data= client_socket.recv(1024)
		if not data or data.decode('utf-8')=='END':
			break;
		print("Client:",(data.decode('utf-8')) )

		#Send Data
		try:
			client_socket.send(bytes('Hey client','utf-8'))
		except:
			print("Exited by the user")
	
	client_socket.close()	
