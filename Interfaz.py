"""
Interfaz Principal
"""
from tkinter import *
from tkinter import messagebox
from pygame import *
import os, pygame, random, sys
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
    suma= (BarcosA+(BarcosB*2)+(BarcosC*4))
    if suma <=100 :
        Play(BarcosA, BarcosB, BarcosC, 0, 0, 0, Nombre, 0, 0, [], [], [], suma, suma, 0)
    else: 
        messagebox.showwarning('Saturacion', 'Baje la cantidad de Barcos.')

def Transformar(Matriz):
    NuevaMatriz=[]
    Provicional=[]

    for elemento in Matriz:
        if elemento!=',' and elemento!='[' and elemento!=']' and elemento!=' ':
            Provicional+= [int(elemento)]
        elif elemento==']':
            if Provicional!=[]:
                NuevaMatriz+= [Provicional]
                Provicional=[]
    return NuevaMatriz


def Cargar(Nombre):
    partida= (Nombre + '.txt')
    for archivo in os.listdir():
        if archivo == (partida):
            archivo=open(partida)
            Contenido=archivo.readlines()
            archivo.close()
            Datos= Contenido[0].split('/')
            BarcosA= int(Datos[0])
            BarcosB= int(Datos[1])
            BarcosC= int(Datos[2])
            ColocadosA= int(Datos[3])
            ColocadosB= int(Datos[4])
            ColocadosC= int(Datos[5])
            Jugador_Nombre= Datos[6]
            Aciertos= int(Datos[7])
            Fallos= int(Datos[8])
            matrizJ= Transformar(Datos[9])
            matrizJ2= Transformar(Datos[10])
            matrizE= Transformar(Datos[11])
            RestantesA= int(Datos[12])
            RestantesE= int(Datos[13])
            Tiempo= int(Datos[14])
    Play(BarcosA, BarcosB, BarcosC, ColocadosA, ColocadosB, ColocadosC, Jugador_Nombre, Aciertos, Fallos, matrizJ, matrizJ2, matrizE, RestantesA, RestantesE, Tiempo)

pygame.mixer.init()

def Fail():
    pygame.mixer.init() # Inicializar todos los módulos Pygame importados
    pygame.mixer.music.load("Adjuntos/fallo.wav")  # pone la cancion
    pygame.mixer.music.play(1)  # reproduce la cancion
    pygame.mixer.music.set_volume(0.5)  # el volumen de la musica

def acierto():
    pygame.mixer.init()# Inicializar todos los módulos Pygame importados
    pygame.mixer.music.load("Adjuntos/explosion.wav")  # pone la cancion
    pygame.mixer.music.play(1)  # reproduce la cancion
    pygame.mixer.music.set_volume(0.5)  # el volumen de la musica


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










#Interfaz
Interfaz=Tk()
Interfaz.title("Barcos vs Aliens la ultima esperanza")
Screenwidth= str(int(Interfaz.winfo_screenwidth()/2)-256)
Screenheight= str(int(Interfaz.winfo_screenheight()/2)-256)
size = "960x540+"+Screenwidth+"+"+Screenheight  #Por definir
Interfaz.geometry(size)
Interfaz.resizable(width= False, height= False)
canvas= Canvas(Interfaz, width= 960, height=540)
Fondo=cargarImagen("fondo.png")
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
titulo5= Label(Interfaz, text="Cargar Partida",font=("Arial", 10), bg="grey")
titulo5.place(x= 350, y= 20)
Cargar_Partida=  Entry(Interfaz, width=30, font=("Arial", 10), bg="grey")
Cargar_Partida.place(x= 350, y= 50)
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
Boton_Cargar= Button(Interfaz, text="Cargar", command= lambda: Cargar(Cargar_Partida.get()))
Boton_Cargar.place(x=350, y= 80)




Opcioes=Menu(Interfaz)
#Opcioes.add_command(label= "Salon de la Fama", command= Fama)
#Opcioes.add_command(label= "Ayuda", command= ayuda)
#Opcioes.add_command(label= "Acerca de", command= Info)

canvas.grid()

Interfaz.mainloop()


"""
Referencias:
https://www.youtube.com/watch?v=Zvrj1b9Mguk&list=PL46E99FE946C1C946&index=45&ab_channel=ChelinTutorials
http://programarcadegames.com/python_examples/show_file.php?lang=es&file=array_backed_grid.py
"""
