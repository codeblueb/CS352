import sys
import socket

entries = []

def PopulateEntries():
    inFile = open("PROJI-DNSTS.txt", "r")
    
    i =0
    for line in inFile:
        tokens = line.split()
        entries.append(DNSEntry(tokens[0], tokens[1], tokens[2]))
        i += 1
    inFile.close()
    
def DNS_TS():
    try:
        ts = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("TS: Server socket created")
    except socket.error as err:
        print("TS: socket open error: {}".format(err))
        exit()
        
    server_binding = ('', listenPort)
    ts.bind(server_binding)
    
    ts.listen(1)
    print("TS: Now accepting connections on port {}".format(str(listenPort)))
    
    while True:
        conn, addr = ts.accept()
        print("TS: Got a connection request from a client at {}".format(addr))
        msg = conn.recv(200).decode("utf-8")
        print("TS: Message form client: {}".format(msg))
        
        reply = findByHostNameRS(msg)
        
        if reply == False:
            reply = "{} - Error:Host Not Found".format(msg) 
            
        print("TS: Replying to client with {}".format(reply))
        conn.send(reply.encode("utf-8"))         
  
    
def findByHostNameRS(name):
    for entry in entries:
        if entry.hostname.lower() == name.lower():
            return entry.toString()
    return False

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
        listenPort = 50002
        
    PopulateEntries()
    DNS_TS()