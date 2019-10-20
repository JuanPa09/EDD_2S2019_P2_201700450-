import os
import curses


#os.system ("cls")
#a = input('').split("\\")[0]
#print("Hola "+a)

class Menu():
    
    def principal(self,nombre):
        
        stdscr = curses.initscr() #initialize console
        window = curses.newwin(20,60,0,0) #create a new curses window
        window.keypad(True)     #enable Keypad mode
        curses.noecho()         #prevent input from displaying in the screen
        curses.curs_set(0)      #cursor invisible (0)
        self.paint_principal(window,nombre)      #paint menu
        keystroke = -1
        while(keystroke==-1):
            keystroke = window.getch()  #get current key being pressed
            if(keystroke==49): #1
                
                self.Escribir()
                
            elif(keystroke==50):#2
                print("Op2")
                keystroke=-1
            elif(keystroke==51):#3
                print("Op3")
                keystroke=-1                  
            elif(keystroke==54):#6
                pass
            else:
                keystroke=-1
        
    def Escribir(self):
        os.system ("cls")
        curses.echo()
        a = input('').split("\\")[0]      
        self.principal('Mundo')

          

    def paint_principal(self,win,nombre):
        self.paint_title(win,nombre)          #paint title
        win.addstr(7,21, '1. Insert Block')             #paint option 1
        win.addstr(8,21, '2. Select block')       #paint option 2
        win.addstr(9,21, '3. Reports')   #paint option 3
        
        win.addstr(12,21, '6. Exit')            #paint option 6
        win.timeout(-1)                         #wait for an input thru the getch() function

    def paint_Escritura(self,win):
        self.paint_title(win,'Escribir')
        win.addstr(8,20, 'Bloque : ')
        curses.echo()
        

    def paint_title(self,win,var):
        win.clear()                         #it's important to clear the screen because of new functionality everytime we call this function
        win.border(0)                       #after clearing the screen we need to repaint the border to keep track of our working area
        x_start = round((60-len(var))/2)    #center the new title to be painted
        win.addstr(0,x_start,var)           #paint the title on the screen



Inicio=Menu()
Inicio.principal('MENU PRINCIPAL')