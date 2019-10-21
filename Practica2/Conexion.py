import select
import socket
import sys
import pandas as pd
class Conectar():
    def connect(self):
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
                    server.send(message.encode('utf-8'))
                    #sys.stdout.write('<YOU>')
                    #sys.stdout.write(message)
                    sys.stdout.flush()
        server.close()

    def prueba(self,menu):
        #CON ESTO GENERO EL HASH
        datos=pd.read_csv('data.csv',header=None)
        tam=len(datos)
        df=pd.DataFrame(data=datos)
        archivojson=df.iloc[1,1]
        menu.listajson.insertarjson(archivojson)
        print("Termino")