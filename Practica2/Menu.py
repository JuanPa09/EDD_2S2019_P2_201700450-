import os
import curses
from curses import KEY_RIGHT, KEY_LEFT, KEY_UP, KEY_DOWN
from CargaMasiva import CargaMasiva
from Estructuras import Arbol
import json



class Menu():

    def __init__(self):
        self.index=0
        self.json_seleccionado=None
        self.json_entrada=None #Cadena Json
        self.phash="0000" #Hash
        self.cm=CargaMasiva()
        self.arbol=Arbol() #Arbol AVL


    def Principal(self,listajson,json):
        os.system ("cls")
        print("######################### Menu Principal #########################")
        print("1. Insert block")
        print("2. Select block")
        print("3. Reportes")
        respuesta = input('').split("\\")[0]
        if (respuesta=="1"):
            self.Insertar(listajson,json)
        elif respuesta=="2":
            self.Select(listajson,json)
        elif respuesta=="3":
            self.Reportes()
        else:
            self.Principal(listajson,json)

    def Insertar(self,listajson,json):
        os.system("cls")
        print("######################### Insert block #########################")
        print("Nombre: ")
        bloque= input('').split("\\")[0]
        listajson.insertarjson(json.cargarjson(bloque,str(self.index),self.phash)) #METODO QUE INSERTA LA CADENA EN LA LISTA DOBLEMENTE ENLAZADA
        self.Principal(listajson,json)


    def Reportes(self):
        os.system("cls")
        print("######################### Reportes #########################")
        print("1. BlockChain Report")
        print("2. Tree Report")
        respuesta = input('').split("\\")[0]
        if (respuesta=="1"):
            print("BlockChain Report")

        elif respuesta=="2":
            self.TreeReport()

    def TreeReport(self):
        os.system("cls")
        print("######################### TreeReport #########################")
        print("1. Tree")
        print("2. Preorden")
        print("4. Inorden")
        print("2. Postorden")
        respuesta = input('').split("\\")[0]
        if (respuesta=="1"):
            print("Tree")
            self.cm.ArbolBinario(self.json_seleccionado,self.arbol)
        elif respuesta=="2":
            print("Preorden")
        elif respuesta=="3":
            print("Inorden")
        elif respuesta=="4":
            print("Postorden")


    def Select(self,listadoble,json):
        os.system("cls")
        stdscr = curses.initscr() #initialize console
        window = curses.newwin(30,100,0,0) #create a new curses window
        window.keypad(True)     #enable Keypad mode
        curses.noecho()         #prevent input from displaying in the screen
        curses.curs_set(0)      #cursor invisible (0)
        self.Seleccionar(window,listadoble,json)

    def paint_title(self,win,var):
        win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
        win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
        x_start = round((60-len(var))/2)    #center the new title to be painted
        win.addstr(0,x_start,var)           #paint the title on the screen

    def Seleccionar(self,win,listadoble,json):
    
        self.paint_title(win,'Select Block')      #paint menu


        temp=listadoble.inicio
        name = temp.json
        datos=self.cm.Arreglar(name)
        posnamex = 22
        posnamey = 5
        for line in datos.splitlines():
            win.addstr(posnamey,posnamex,line)
            posnamey=posnamey+1



        win.addstr(15,5,'<--')
        win.addstr(15,95,'-->')

        stroke = 1
        
        while(stroke==1):
            stroke = win.getch()

            if stroke==54:
                #Mover Derecha
                self.paint_title(win,' Select Block ')
                temp=temp.siguiente
                name = str(temp.json)
                posnamex = 20
                posnamey = 5
                for line in name.splitlines():
                    win.addstr(posnamey,posnamex,line)
                    posnamey=posnamey+1

                win.addstr(10,5,'<--')
                win.addstr(10,55,'-->')

                stroke=1

            elif stroke == 52:
                #Mover Izquierda
                self.paint_title(win,' Select Block ')
                temp=temp.anterior
                name = str(temp.json)
                posnamex = 20
                posnamey = 5
                for line in name.splitlines():
                    win.addstr(posnamey,posnamex,line)
                    posnamey=posnamey+1

                win.addstr(10,5,'<--')
                win.addstr(10,55,'-->')
                stroke=1
            elif stroke==32:
                #Name=temp.nombre
                self.json_seleccionado=temp.json
                win.clear()
                curses.endwin()
                self.Principal(listadoble,json)
            else:
                curses.endwin()
                self.Principal(listadoble,json) 

