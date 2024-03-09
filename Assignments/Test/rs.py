import sys
import socket

entries = []

def PopulateEntries():
    inFile = open("PROJI-DNSRS.txt", "r")
    
    i =0
    for line in inFile:
        tokens = line.split()
        entries.append(DNSEntry(tokens[0], tokens[1], tokens[2]))
        i += 1
    inFile.close()
    
def DNS_RS():
    try:
        rs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("RS: Server socket created")
    except socket.error as err:
        print("RS: socket open error: {}".format(err))
        exit()
        
    server_binding = ('', listenPort)
    rs.bind(server_binding)
    
    rs.listen(1)
    print("RS: Now accepting connections on port {}".format(str(listenPort)))
    
    while True:
        conn, addr = rs.accept()
        print("RS: Got a connection request from a client at {}".format(addr))
        msg = "!empty"
        while msg != "":
            msg = conn.recv(200).decode("utf-8")
            
            if msg != "":
                print("RS: Message from client: " + msg)
                reply = findByHostNameRS(msg).toString()
                print("RS: Replying to client with {}".format(reply)) 
                conn.send(reply.encode("utf-8"))          
    rs.close()
    
def findByHostNameRS(name):
    for entry in entries:
        if entry.hostname.lower() == name.lower():
            return entry
    return entry

class DNSEntry:
    def __init__(self, hostname, ip, flag):
        self.hostname = hostname
        self.ip = ip
        self.flag = flag
    
    def toString(self):
        return "{} {} {}".format(self.hostname, self.ip, self.flag)
    
if __name__ == "__main__":
    try:
        listenPort = int(sys.argv[1])
    except:
        listenPort = 50001
        
    PopulateEntries()
    DNS_RS()