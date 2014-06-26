
import zmqros
import sys
import socket

if __name__ == "__main__":
    if len(sys.argv) == 3:
        zmqros.run(sys.argv[1], sys.argv[2])
    elif len(sys.argv) == 2:
        ip_addr = socket.gethostbyname(socket.getfqdn())
        zmqros.run(ip_addr, 8000)
    else:
        raise Exception("Correct argument form not supplied")
