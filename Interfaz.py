"""
Interfaz Principal
"""
from email import message
from tkinter import *
from tkinter import messagebox
from pygame import *
import os, pygame, random
from tablero import *


#Esta funcion es para cargar las diferentes imagenes
def cargarImagen(nombre): 
    """
    Esta función se encarga de cargar la imagenes
    Parametros:
    nombre: Es un string con el nombre de la imagen que se desea cargar

    La funcion toma el nombre de la imagen y la buscas dentro de la carpeta Adjuntos

    return
    Retorna la imagen
    """
    ruta = os.path.join('Adjuntos/',nombre) #Se le indica el lugar donde buscar la imagen y el nombre de la imagen
    imagen = PhotoImage(file=ruta) #Se crea la imagen  
    return imagen


def Verifica(BarcosA, BarcosB, BarcosC, Nombre):
    
    if (BarcosA+(BarcosB*2)+(BarcosC*4))<=100 :
        Play(BarcosA, BarcosB, BarcosC, Nombre)
    else: 
        messagebox.showinfo('Saturacion', 'Baje la cantidad de Barcos.')




def Fail():
    pygame.mixer.music.load("")
    pygame.mixer.music.play(1)     

def ayuda():
    Acer=Toplevel(Interfaz)
    Acer.title("Ayuda")
    Acer.minsize(800,533)
    Acer.resizable(width=NO, height=NO)
    canvas2 = Canvas(Acer, width=800, height=533)
    canvas2.place(x=0, y=0)

def Salón_de_la_fama():
    salon=Toplevel(Interfaz)
    salon.title("Salón de la fama")
    salon.minsize(800,533)
    salon.resizable(width=NO, height=NO)
    canvas2 = Canvas(salon, width=800, height=533)
    canvas2.place(x=0, y=0)
    
def Abrir():
    abrir=Toplevel(Interfaz)
    abrir.title("Abrir")
    abrir.minsize(800,533)
    abrir.resizable(width=NO, height=NO)
    canvas2 = Canvas(abrir, width=800, height=533)
    canvas2.place(x=0, y=0)

def registro1():
    regis=Toplevel(Interfaz)
    regis.title("Registro")
    regis.minsize(500,350)
    regis.resizable(width=NO,height=NO)
    vprincipal = Button(regis, text="volver ", height=2, width=20, fg="black", command=lambda: regresarRegis())
    vprincipal.place(x=300, y=280)
  
    def regresarRegis():
        regis.withdraw()  # destruir la ventana regis
        Interfaz.deiconify()  # volver a la ventana principal
    regis.mainloop()

def jugar(BarcosA,BarcosB,BarcosC,Nusuario):
    Play(BarcosA,BarcosB,BarcosC,Nusuario)

#Interfaz
Interfaz=Tk()
Interfaz.title("Barcos vs Aliens la ultima esperanza")
Screenwidth= str(int(Interfaz.winfo_screenwidth()/2)-256)
Screenheight= str(int(Interfaz.winfo_screenheight()/2)-256)
size = "960x540+"+Screenwidth+"+"+Screenheight  #Por definir
Interfaz.geometry(size)
Interfaz.resizable(width= False, height= False)
canvas= Canvas(Interfaz, width= 960, height=540)
Fondo=cargarImagen("Fondo.png")
canvas.create_image(-2, -2, image= Fondo, anchor=NW)
titulo = Label(Interfaz, text="Introduzca su usuario",font=("Arial", 10), bg="grey")  # texto
titulo.place(x=50, y=20)
Nusuario = Entry(Interfaz, width=30, font=("Arial", 10), bg="grey")  # crea una caja para en num, textvariable hace una conexión entre la entry y la variable nombre
Nusuario.place(x=50, y=50)  # lugar
titulo2 = Label(Interfaz, text="Introduzca cantidad de barcos tipo A",font=("Arial", 10), bg="grey")  # texto
titulo2.place(x=50, y=80)
BarcosA= Entry(Interfaz, width=30, font=("Arial", 10), bg="grey")  # crea una caja para en num, textvariable hace una conexión entre la entry y la variable nombre
BarcosA.place(x=50, y=110)  # lugar
titulo3 = Label(Interfaz, text="Introduzca cantidad de barcos tipo B",font=("Arial", 10), bg="grey")  # texto
titulo3.place(x=50, y=140)
BarcosB = Entry(Interfaz, width=30, font=("Arial", 10), bg="grey")  # crea una caja para en num, textvariable hace una conexión entre la entry y la variable nombre
BarcosB.place(x=50, y=170)  # lugar
titulo4 = Label(Interfaz, text="Introduzca cantidad de barcos tipo C",font=("Arial", 10), bg="grey")  # texto
titulo4.place(x=50, y=200)
BarcosC = Entry(Interfaz, width=30, font=("Arial", 10), bg="grey")  # crea una caja para en num, textvariable hace una conexión entre la entry y la variable nombre
BarcosC.place(x=50, y=230)  # lugar
#Jugar= Button(Interfaz, text= "Jugar", command=lambda: TableroEnemigo())
#Jugar.place(x= 50, y= 260)
######################################################################
menubar=Menu(Interfaz)#agrega menu
menubar.add_command(label="ayuda", command= ayuda)#opcion
menubar.add_command(label="Salón de la fama",command= Salón_de_la_fama)
menubar.add_command(label="Abrir",command= Abrir)
Interfaz.config(menu= menubar)#agrega al menu
Jugar= Button(Interfaz, text= "Jugar", command=lambda: Verifica( int(BarcosA.get()), int(BarcosB.get()), int(BarcosC.get()), Nusuario.get()))
Jugar.place(x= 50, y= 260)



Opcioes=Menu(Interfaz)
#Opcioes.add_command(label= "Salon de la Fama", command= Fama)
#Opcioes.add_command(label= "Ayuda", command= ayuda)
#Opcioes.add_command(label= "Acerca de", command= Info)

canvas.grid()

Interfaz.mainloop()


"""
Referencias:
http://programarcadegames.com/python_examples/show_file.php?lang=es&file=array_backed_grid.py
"""
