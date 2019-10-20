import os
from Estructuras import Arbol
from Estructuras import ListaDoble
class Diagramas():


    lista=ListaDoble()

    def graphtree(self,inicio,f):
        f.write(str(inicio.carne)+"[label=\"Carne: "+str(inicio.carne)+" \\n Nombre: "+str(inicio.nombre)+"\\n Atura: "+str(inicio.altura)+"\\n Fe: "+str(inicio.fe)+"\"]")
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
        f.write("node[shape=rectangle]\n")
        self.graphtree(inicio,f)
        f.write("}")
        f.close

    def graphpre(self,inicio,lista):
        lista.inicio=None
        f=open('nuevo.txt',"w")
        f.write("digraph{\n")
        f.write("graph [rankdir=LR]\n")
        f.write("node[shape=rectangle]\n")
        self.preorder(inicio,lista)
        temp=lista.inicio
        if inicio.left==None and inicio.right==None:
            f.write(str(temp.carne)+"[label=\""+str(temp.carne)+" \\n"+str(temp.nombre)+"\"]")
        else:
            while temp.siguiente!=None:
                f.write(str(temp.carne)+"[label=\""+str(temp.carne)+" \\n"+str(temp.nombre)+"\"]")
                f.write(temp.carne+"->"+temp.siguiente.carne+"\n")
                temp=temp.siguiente
            f.write(str(temp.carne)+"[label=\""+str(temp.carne)+" \\n"+str(temp.nombre)+"\"]")
        f.write("}")
        f.close()

    def preorder(self,inicio,lista):
        if(inicio is not None):
            lista.insertarR(inicio.carne,inicio.nombre)
            self.preorder(inicio.left,lista)
            self.preorder(inicio.right,lista)

    def graphin(self,inicio,lista):
        lista.inicio=None
        f=open('nuevo.txt',"w")
        f.write("digraph{\n")
        f.write("graph [rankdir=LR]\n")
        f.write("node[shape=rectangle]\n")
        self.inorder(inicio,lista)
        temp=lista.inicio
        if inicio.left==None and inicio.right==None:
            f.write(str(temp.carne)+"[label=\""+str(temp.carne)+" \\n"+str(temp.nombre)+"\"]")
        else:
            while temp.siguiente!=None:
                f.write(str(temp.carne)+"[label=\""+str(temp.carne)+" \\n"+str(temp.nombre)+"\"]")
                f.write(temp.carne+"->"+temp.siguiente.carne+"\n")
                temp=temp.siguiente
            f.write(str(temp.carne)+"[label=\""+str(temp.carne)+" \\n"+str(temp.nombre)+"\"]")
        f.write("}")
        f.close()

    def inorder(self,inicio,lista):
        if(inicio is not None):
            self.inorder(inicio.left,lista)
            lista.insertarR(inicio.carne,inicio.nombre)
            self.inorder(inicio.right,lista)

    def graphpost(self,inicio,lista):
        lista.inicio=None
        f=open('nuevo.txt',"w")
        f.write("digraph{\n")
        f.write("graph [rankdir=LR]\n")
        f.write("node[shape=rectangle]\n")
        self.postorder(inicio,lista)
        temp=lista.inicio
        if inicio.left==None and inicio.right==None:
            f.write(str(temp.carne)+"[label=\""+str(temp.carne)+" \\n"+str(temp.nombre)+"\"]")
        else:
            while temp.siguiente!=None:
                f.write(str(temp.carne)+"[label=\""+str(temp.carne)+" \\n"+str(temp.nombre)+"\"]")
                f.write(temp.carne+"->"+temp.siguiente.carne+"\n")
                temp=temp.siguiente
            f.write(str(temp.carne)+"[label=\""+str(temp.carne)+" \\n"+str(temp.nombre)+"\"]")
        f.write("}")
        f.close()

    def postorder(self,inicio,lista):
        if(inicio is not None):
            self.postorder(inicio.left,lista)
            self.postorder(inicio.right,lista)
            lista.insertarR(inicio.carne,inicio.nombre)


    def graphArboles(self,lista):#GRAFICA LOS ARBOLES
        temp=lista.inicio
        f=open('nuevo.txt',"w")
        f.write("digraph{\n")
        f.write("node[shape=rectangle]\n")        
        if temp.siguiente==None:
            f.write("A"+str(temp.hash)+"[label=\" Class= "+str(temp.clase)+" \\n TimeStamp= "+str(temp.timestap)+" \\n PHASH= "+str(temp.phash)+" HASH= "+str(temp.hash)+"\"]\n")
        else:

            while True:
                #print(temp.hash)
                f.write("A"+str(temp.hash)+"[label=\" Class= "+str(temp.clase)+" \\n TimeStamp= "+str(temp.timestap)+" \\n PHASH= "+str(temp.phash)+" HASH= "+str(temp.hash)+"\"]\n")
                f.write("A"+str(temp.hash)+"->"+"A"+str(temp.siguiente.hash)+"\n")
                f.write("A"+str(temp.siguiente.hash)+"->"+"A"+str(temp.hash)+"\n")
                temp=temp.siguiente
                f.write("A"+str(temp.hash)+"[label=\" Class= "+str(temp.clase)+" \\n TimeStamp= "+str(temp.timestap)+" \\n PHASH= "+str(temp.phash)+" HASH= "+str(temp.hash)+"\"]\n")
                temp=temp.siguiente
                if(temp==lista.inicio):
                    break
        f.write("}")
        f.close()
        self.Graficar()
    

    


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
