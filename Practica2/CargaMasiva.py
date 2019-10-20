import pandas as pd
import json,sys
from datetime import datetime
from Graficas import Diagramas
class CargaMasiva():

    def __init__(self):
        self.diagramar=Diagramas()

    def cargarjson(self,archivo,index,phash): #Crea El archivo que se enviara al servidor
        dateTimeObj = datetime.now()
        timestamp=str(dateTimeObj.day)+"-"+str(dateTimeObj.month)+'-'+str(dateTimeObj.year)+'::'+str(dateTimeObj.hour)+':'+str(dateTimeObj.minute)+':'+str(dateTimeObj.second)

        datos=pd.read_csv(archivo,header=None)
        df=pd.DataFrame(data=datos)
        clase=df.iloc[0,1]
        archivojson=df.iloc[1,1]
        f=open('json.text',"w")
        f.write("{\n")
        f.write("   \"INDEX\": "+index+",\n")
        f.write("   \"TIMESTAMP\": \""+str(timestamp)+"\",\n")
        f.write("   \"CLASE\": \""+clase+"\",\n")
        f.write("   \"DATA\": "+archivojson+",\n")
        f.write("   \"PREVIOUSHASH\": \""+phash+"\",\n")
        f.write("}")
        f.close()
        return str(archivojson)

    def getDataI(self,raiz):
        try:
            if raiz!="None":
                print(raiz['value'])
                self.getDataI(raiz['left'])
                self.getDataI(raizI['right'])
        except:
            self.a=1
    def getDataD(self,raiz):
        try:
            if raiz!="None":
                print(raiz['value'])
                self.getDataD(raiz['left'])
                self.getDataD(raizI['right'])
        except:
            self.a=1

    def getData(self,normal,AVLtree):
        try:
            if normal!="None":
                #print(normal['value'])
                a=normal['value'].split('-')#carne-nombre
                AVLtree.insertar(a[0],a[1])
                #Aca se inserta al Arbol
                if normal['left']!="None":
                    self.getData(normal['left'],AVLtree)
                if normal['right']!="None":
                    self.getData(normal['right'],AVLtree)

        except:
            self.a=1   

        
    def ArbolBinario(self,jsonn,avltree):
        data=json.loads(jsonn)
        #dat=json.dumps(data)
        self.getData(data['DATA'],avltree)
        avltree.crearArbol()
        self.diagramar.Darbol(avltree.arbol.raiz)
        self.diagramar.Graficar()

    def Arreglar(self,name):
        data=json.loads(name)
        index=str(data["INDEX"])
        timestap=data['TIMESTAMP']
        classs=data['CLASS']
        #dat=str(data["DATA"])
        datt=json.dumps(data,indent=0)
        P=datt.split('\n')
        phash=data["PREVIOUSHASH"]
        datos="INDEX: "+index+"\n TIMESTAMP: "+timestap+"\n CLASS: "+classs+"\n DATA: "+P[0:5]+"\n PREVIOUSHASH: "+phash
        return datos


#carga=CargaMasiva()
#data=json.loads(carga.cargarjson('data.csv')
#dat=json.dumps(data)
#print(dat)

#data=json.loads(carga.cargarjson('data.csv'))
#print(data['DATA']['left']['left']['left'])

#carga.getData(data['DATA'])

#carga.getDataI(data['DATA'])
#carga.getDataD(data['DATA']['right'])

