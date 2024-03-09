import sys
import socket as soc
import threading
# import select


def server_listening(argv):
    	# create a socket with the Client
	try:
		sc = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
		# sc.setblocking(0)
		print(f"[S] Connected successfully")
	except soc.error as err:
		print("Error connecting to client.")

	# get the local host gethostname
	try: 
		host = soc.gethostname()
		client_ip = soc.gethostbyname(host)
		server_address = ('', int(argv))
		sc.bind(server_address)
		sc.listen(5)
		print(f"[S] Open port: {int(argv)} and connecting to {client_ip}")
	except soc.error as err:
		print("Error getting the hostname and port number.")


	file = ''
	dns_table = []
	try:
		file = open("PROJI-DNSRS.txt", "r")
		for tokens in file:
			strings = tokens.strip().split()
			dns_table.append(strings)
			# print(dns_table)  
	except soc.error as err:
		print(f"Error opening file: {err}")
		if not file:
			print(f"File {file} does not exist.")
	print("Dns table ready")

	while True:
		conn, address = sc.accept()
		client_host = ' '
		while client_host != "":
			client_host = conn.recv(200).decode('utf-8')
			if not client_host:
				break; 
			print(f"[C] Client looking for: {client_host}")
			# for tokens in dns_table:
			# 	# print(f"\"kill.cs.rutgers.edu\" == \"{client_host}\" ? : {"kill.cs.rutgers.edu" == client_host}")
			# 	# print("\"kill.cs.rutgers.edu\" == \"{}\" ? : {}".format(client_host, "kill.cs.rutgers.edu" == client_host))
			# 	if "kill.cs.rutgers.edu" == str(client_host):
			# 		print(f"found: {client_host}")
			# 	if "www.google.com" == str(client_host):
			# 		print(f"found: {client_host}")

			# 	if str(tokens[0]) == str(client_host):
			# 		full_string = (' '.join(tokens))
			# 		print(full_string)
			# 		conn.send(full_string.encode('utf-8'))
			# 	if tokens[0] == 'localhost':
			# 		tell_client_ask_ts = (' '.join(tokens))
			# 		print(tell_client_ask_ts)
			# 		conn.send(tell_client_ask_ts.encode('utf-8'))

					
if __name__ == '__main__':
	argv = sys.argv[1]
	t2 = threading.Thread(name='server_listening', target=server_listening(argv))
	t2.start()




