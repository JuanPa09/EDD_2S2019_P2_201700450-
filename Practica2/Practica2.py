import Estructuras
import Menu
import pandas as pd
import select
import socket
#import Conexion

from Estructuras import ArbolBinario
from Estructuras import ListaDoble
from CargaMasiva import CargaMasiva
from Menu import Menu
from Conexion import Conectar


import threading
import time,sys


    
class Hilos():
    
    tiempo=0

    def pross1 (self):
        time.sleep(1)
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
                        #insertar a la lista
                    elif mensaje=="false":
                        print("Es un false")
                        #no hacer nada
                    else:
                        menu.json_entrada=message
                        
                        #print("Es un json")
                        #Obtener el json
                        #Crear Hash y comprobar
                        
                    
                #else:
                    #Enviar Datos
                    #message=sys.stdin.readline()
                    #server.send(message.encode('utf-8'))
                    #sys.stdout.write('<YOU>')
                    #sys.stdout.write(message)
                    #sys.stdout.flush()
        server.close()
         

    def pross2 (self):
        time.sleep(10)
        #CON ESTO GENERO EL HASH
        datos=pd.read_csv('data.csv',header=None)
        #tam=len(datos)
        df=pd.DataFrame(data=datos)
        archivojson=df.iloc[1,1]
        menu.listajson.insertarjson(archivojson)
        #print("Termino")
    
    def pross3(self):
        time.sleep(2)
        menu.Principal(cm)

        
tree=ArbolBinario()
listajson=ListaDoble()#Lista que contiene los json
lista=ListaDoble()#Lista que contiene los atributos
#lista=ListaDoble()
server=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
menu=Menu(lista,server)
cm=CargaMasiva()

    
    

hilo=Hilos()


#t2 = threading.Thread(name="hilo2",target=hilo.pross2)
t1 = threading.Thread(name="hilo1",target=hilo.pross1)
t3 = threading.Thread(name="hilo3",target=hilo.pross3)

t1.start()
t3.start()
#t2.start()
t3.join()
#menu.Principal(cm)
t1.join()
#t2.join()

def comprobar(json):
    
    print("hola")



























        

