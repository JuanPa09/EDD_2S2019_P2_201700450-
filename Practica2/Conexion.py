import select
import socket
import sys
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
if len(sys.argv)!=3:
    print("Faltan Parametros, IP adress, port number")
    exit()
IP_address = str(sys.argv[1])
Port = int(sys.argv[2])
server.connect((IP_address,Port))

while True:
    read_sockets = select.select([server], [], [], 1)[0]
    import msvcrt
    if msvcrt.kbhit():read_sockets.append(sys.stdin)

    for socks in read_sockets:
        if socks == server:
            message = socks.recv(2048)
            mensaje=message.decode('utf-8')
            if mensaje=="true":
                print("Es un true")
            elif mensaje=="false":
                print("Es un false")
            else:
                print("Es un json")
            
        else:
            message=sys.stdin.readline()
            server.sendall(message.encode('utf-8'))
            sys.stdout.write('<YOU>')
            sys.stdout.write(message)
            sys.stdout.flush()
server.close()