import sys
import socket as soc
import threading


def server_listening(argv):
	# create a socket with the Client
	try:
		sc = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
		print(f"[S] Connected successfully")
	except soc.error as err:
		print("Error connecting to client.")

	# get the local host gethostname
	try: 
		host = soc.gethostname()
		client_ip = soc.gethostbyname(host)
		server_address = (client_ip, int(argv))
		sc.bind(server_address)
		sc.listen(1)
		print(f"[S] Open port: {int(argv)}")
	except soc.error as err:
		print("Error getting the hostname and port number.")

	print("Dns table ready")
	file = ''
	dns_table = []
	try:
		file = open("PROJI-DNSTS.txt", "r")
		for tokens in file:
			strings = tokens.strip().split(' ')
			dns_table.append(strings)
			# print(dns_table)  
	except soc.error as err:
		print(f"Error opening file: {err}")
		if not file:
			print(f"File {file} does not exist.")

	while True:
		conn, address = sc.accept()
		client_host = ''
		n = 0
		client_host = conn.recv(1024).decode('ascii')
		n += 1
		print(f"[C] Client looking for: {client_host}")
		# if not client_host:
		# 	break; 
		print(f"Client packet {n}, {client_host}")
		for tokens in dns_table:
			
			if str(client_host).strip(' \n') == "www.google.com":
				print("exists")

			if str(tokens[0]).strip(' \n') == str(client_host).strip(' \n'):
				# print(tokens[0])
				full_string = (' '.join(tokens))
				print(full_string)
				conn.send(full_string.encode('ascii'))
			if tokens[0] == 'localhost':
				# print(tokens[0])
				# print("TS token")
				tell_client_ask_ts = (' '.join(tokens))
				print(tell_client_ask_ts)
				conn.send(tell_client_ask_ts.encode('ascii'))

				
if __name__ == '__main__':
	argv = sys.argv[1]
	t2 = threading.Thread(name='server_listening', target=server_listening(argv))
	t2.start()




