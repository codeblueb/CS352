import sys
import socket

def client(rsHostname, rsListenPort, tsListenPort):
    try:
        cs = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        print("[C]: RS Client socket created. ")
    except socket.error as err:
        print("socket open error {}".format(err))
        exit()
    
    port = int(rsListenPort)
    rsAddr = socket.gethostbyname(rsHostname)
    
    server_binding = (rsAddr, port)
    cs.connect(server_binding)
    
    f = open("PROJI-HNS.txt", "r")
    out = open("RESOLVED.txt", "w")
    
    for line in f:
        
        print("[C]: Sending '{}' to RS.".format(line.rstrip()))
        cs.send(line.rstrip().encode("utf-8"))
        
        rsData = cs.recv(256).encode("utf-8")
        print("[C]: Data received from rs {}".format(rsData))
        
        split = rsData.split()
        
        if split[2] == 'A':
            out.write(rsData + '\n')
        else:
            try:
                cs2 = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                print("[C]: TS client socket created")
            except socket.error as err:
                print("socket open error: {}".format(err))
                exit()
            
            tsAddr = socket.gethostbyname(split[0])
            
            cs2.connect((tsAddr, int(tsListenPort)))
            
            print("[C]: Sending '{}' to TS".format(line.rstrip()))
            cs2.send(line.rstrip().encode("utf-8"))
            
            tsData = cs2.recv(200).decode("utf-8")
            print("[C]: Data received from TS: {}".format(tsData))
            print("[C]: Writing " + tsData) 
            out.write(tsData + '\n')
            
            cs2.close()     
    
    cs.close()
    f.close()
    out.close()
    exit()

if __name__ == "__main__":
    client(sys.argv[1], sys.argv[2], sys.argv[3])
    print("Done.")
                    
        