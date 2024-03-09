import sys
import socket as soc

def rServer(host, s_argv, t_argv):
	
	# Handle conecting to the host
	try:	
		rc = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
		rshost = soc.gethostname()
		rserver_ip = soc.gethostbyname(host)
		# rport = 10002
		print(f"[C] Requesting connection with {rserver_ip} at port: {int(s_argv)}")
		# print(f"Host tyope: {type(host)}")
	except soc.error as err:
		print(f"Error connecting to {err}")

	try:
		rserver_bind = (rserver_ip, int(s_argv))
		rc.connect(rserver_bind)
		print(f"[C] Connected to {rserver_ip} at port: {int(s_argv)}")
	except soc.error as err:
		print(f" Error connecting to server: {err}")

	# Handle file open and create a dns table
	file = ''
	dns_table = []
	try:
		file = open("PROJI-HNS.txt", "r")
		for tokens in file:
			strings = tokens.strip().split(' ')
			dns_table.append(strings)
			# print(strings)
	except soc.error as err:
		print(f"Error opening file: {err}")
		if not file:
			print(f"File {file} does not exist.")
	
	# Handle creating the 2nd socket	
	try:
		ts = soc.socket(soc.AF_INET, soc.SOCK_STREAM)
		tshost = soc.gethostname()
		tserver_ip = soc.gethostbyname(tshost)
		print(f"[C] Requesting connection with {tserver_ip} at port: {int(t_argv)}")
	except soc.error as err:
		printf(f"Error connecting to {err}")

	try:
		tserver_bind = (tserver_ip, int(t_argv))
		ts.connect(tserver_bind)
	except soc.error as err:
		print(f"Error connecting to {err}")

	# if not dns_table:
 	#    print("No list exists")
	# else:
	# 	for strings in dns_table:
	# 		print(strings)
	# 		print(type(strings))


	with open("PROJI-HNS.txt", "r") as fp:

		with open('HW2out.txt','w') as fw:
			
			for line in fp:
				# print(tokens)
				# tokens = fp.readline().lower()
				# domains = tokens.strip()
				print(line.rstrip())
				# send the tokens	
				rc.send(line.rstrip().lower().encode('utf-8'))
				rc.recv(200).decode('utf-8')

				# response from the ts server 
				# server_response = rc.recv(1024).decode('ascii')
				# print(f"[S] {server_response}")

				# after the server response from rs then run the query for the ts
				# if server_response == 'localhost - NS':
				# 	while True:
				# 		# send the rs the query to check if the dns table has the 
				# 		# domain name systems 
				# 		ts.send(server_response.encode('ascii'))
				# 		t_server_response = ts.recv(1024).decode('ascii')
				# 		fw.write(t_server_response + "\n") 
				# 		if not t_server_response:
				# 			break
				# else:
				# 	fw.write(server_response + "\n")
	fp.close()
	fw.close()
	rc.close()

if __name__ == '__main__':
	host = sys.argv[1]
	rs_argv = sys.argv[2]
	ts_argv = sys.argv[3]
	rServer(host, rs_argv, ts_argv)

