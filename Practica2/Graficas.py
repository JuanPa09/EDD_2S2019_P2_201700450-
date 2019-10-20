import os
from Estructuras import Arbol
class Diagramas():

    def graphtree(self,inicio,f):
        f.write(str(inicio.carne)+"[label=\""+str(inicio.carne)+"\"]\n")
        if (inicio!=None):
            if(inicio.left!=None):
                f.write(str(inicio.carne)+"->"+str(inicio.left.carne)+"\n")
                self.graphtree(inicio.left,f)
            else:
                f.write(str(inicio.carne)+"1[label=\"NULL\"]\n")
                f.write(str(inicio.carne)+"->"+str(inicio.carne)+"1\n")

            if(inicio.right!=None):
                f.write(str(inicio.carne)+"->"+str(inicio.right.carne)+"\n")
                self.graphtree(inicio.right,f)
            else:
                f.write(str(inicio.carne)+"0[label=\"NULL\"]\n")
                f.write(str(inicio.carne)+"->"+str(inicio.carne)+"0\n")



    def Darbol(self,inicio):

        
        f=open('nuevo.txt',"w")
        f.write("digraph G{\n")
        self.graphtree(inicio,f)
        f.write("}")
        f.close

    def Graficar(self):
        os.system("dot -Tjpg nuevo.txt -o imagen.jpg")
        os.system("imagen.jpg")


#arbol=Arbol()
#diagramar=Diagramas()
#arbol.insertar(201403525,"Nery")
#arbol.insertar(201212963,"Andres")
#arbol.insertar(201005878,"Estudiante1")
#arbol.insertar(201313526,"Alan")
#arbol.insertar(201403819,"Anne")
#arbol.insertar(201403624,"Fernando")
#arbol.insertar(201602255,"Estudiante2")
#arbol.crearArbol()
#diagramar.Darbol(arbol.arbol.raiz)
#diagramar.Graficar()
