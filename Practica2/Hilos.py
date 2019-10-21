import threading
import time,sys


    
class Hilos():
    
    tiempo=0

    def pross1 (self):
        time.sleep(5)
        print("Hilo1")
        if self.tiempo == 0:
            self.pross1()
        else:
            return  

    def pross2 (self):
        time.sleep(3)
        print("Hilo2")
        
        
        if self.tiempo==0:
            self.pross2()
        else:
            return

    def pross3(self):
        time.sleep(10)
        self.tiempo=1
        print("Se termina")
    

hilo=Hilos()

t1 = threading.Thread(name="hilo1",target=hilo.pross1)
t2 = threading.Thread(name="hilo2",target=hilo.pross2)
t3 = threading.Thread(name="hilo3",target=hilo.pross3)

t1.start()
t2.start()
t3.start()
t1.join()
t2.join()
t3.join()

