"""
Interfaz Principal
"""
from tkinter import *
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


def Verifica(BarcosA, BarcosB, BarcosC):
    
    if (BarcosA+(BarcosB*2)+(BarcosC*4)):
        return

def Fail():
    pygame.mixer.music.load("")
    pygame.mixer.music.play(1)     



    
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

Jugar= Button(Interfaz, text= "Jugar", command= Tablero)
Jugar.place(x= 200, y= 100)

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
