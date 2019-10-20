import os
import curses

def Principal():
    os.system ("cls")
    print("######################### Menu Principal #########################")
    print("1. Insert block")
    print("2. Select block")
    print("3. Reportes")
    respuesta = input('').split("\\")[0]
    if (respuesta=="1"):
        print("Respuesta fue 1")
        Insertar()
    elif respuesta=="2":
        Select()

def Insertar():
    os.system("cls")
    print("######################### Insert block #########################")
    print("Nombre: ")
    bloque= input('').split("\\")[0]

def Select():
    os.system("cls")
    stdscr = curses.initscr() #initialize console
    window = curses.newwin(20,60,0,0) #create a new curses window
    window.keypad(True)     #enable Keypad mode
    curses.noecho()         #prevent input from displaying in the screen
    curses.curs_set(0)      #cursor invisible (0)
    Seleccionar(window)

def paint_title(win,var):
    win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
    win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
    x_start = round((60-len(var))/2)    #center the new title to be painted
    win.addstr(0,x_start,var)           #paint the title on the screen

def Seleccionar(win):
   
    paint_title(win,' USUARIOS ')      #paint menu


    temp=names.inicio
    name = str(temp.nombre)
    posname = round((60-len(name))/2)
    win.addstr(10,posname,name)

    win.addstr(10,10,'<--')
    win.addstr(10,50,'-->')

    stroke = 1
    
    while(stroke==1):
        stroke = win.getch()

        if stroke==KEY_RIGHT:
            #Mover Derecha
            paint_title(win,' USUARIOS ')
            temp=temp.siguiente
            name = temp.nombre
            posname = round((60-len(str(name)))/2)
            win.addstr(10,posname,name)

            win.addstr(10,10,'<--')
            win.addstr(10,50,'-->')

            stroke=1

        elif stroke == KEY_LEFT:
            #Mover Izquierda
            paint_title(win,' USUARIOS ')
            temp=temp.anterior
            name = temp.nombre
            posname = round((60-len(name))/2)
            win.addstr(10,posname,name)

            win.addstr(10,10,'<--')
            win.addstr(10,50,'-->')
            stroke=1
        elif stroke==32:
            Name=temp.nombre
            win.clear()
            Menu(Name)
        else:
            stroke=1 



Principal()
