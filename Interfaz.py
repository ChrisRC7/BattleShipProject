"""
Interfaz Principal
Este es el codigo del proyecto del juego de Christopher Rodriguez y Javier Mora
para ayuda use el comado de Documentacion()
"""
from tkinter import *
from tkinter import messagebox
from pygame import *
import os, pygame
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
        Interfaz.withdraw()
        tablero= Tablero(BarcosA, BarcosB, BarcosC, 0, 0, 0, Nombre, 0, 0, [], [], [], suma, suma, 0)
        tablero.Accion()
        Interfaz.deiconify()
        Puntos= tablero.Get_Puntos()
        if Puntos!=0:
            Contenido= LeerArchivo()
            Posicion=VerificaPosicion(Contenido,1, Puntos)

            if Posicion<8:
                Borrar=open("Puntos.txt","w")
                Borrar.close()
                NuevaTabla(Posicion,1,Contenido, Puntos, Nombre)
                messagebox.showinfo('Felicidades', 'Has entrado en el salón de la fama:')
                Tabla()

    else: 
        messagebox.showwarning('Saturacion', 'Baje la cantidad de Barcos.')

def VerificaPosicion(Contenido,Contador, Puntos):
    if Contenido==[]:
        return Contador
    
    elif int(Contenido[0].split(",")[2].split("\n")[0])<Puntos:
        return Contador

    else:
        Contador+=1
        return VerificaPosicion(Contenido[1:], Contador, Puntos)

def NuevaTabla(Posicion,Contador,Tabla, Puntos, Nombre):
    if Contador!=8:
        if Posicion==Contador:
            Escribir(str(Contador) + ")" + "," + Nombre + "," + str(Puntos))
            Contador+=1
            return NuevaTabla(Posicion,Contador,Tabla, Puntos, Nombre)
        else:
            Usuario=Tabla[0].split(",")[1]
            Puntaje=Tabla[0].split(",")[2].split("\n")[0]
            Escribir(str(Contador) + ")" + "," + Usuario + "," + Puntaje)
            Contador+=1
            return NuevaTabla(Posicion, Contador, Tabla[1:], Puntos, Nombre)

        

def Escribir(dato):
    archivo=open("Puntos.txt","a")
    archivo.write(dato+"\n")
    archivo.close

def LeerArchivo():
    archivo=open("Puntos.txt")
    Contenido=archivo.readlines()
    archivo.close()
    return Contenido

#Funcion para la tabla
def Tabla():
    Tabla=Toplevel(bg="Blue")#Se define la ventana
    Tabla.title("Salón de la fama")#Se le indica el titulo a la ventana
    Tabla.resizable(width=NO,height=NO)#Se restringe el tamaño
    Puntajes= Transformar(LeerArchivo(),[])
    TablaAux(0,0,8,2,Puntajes, Tabla)
    Tabla.mainloop()

def Transformar(Tabla,Resultado):
    if Tabla==[]:
        return [["Jugadores", "Puntaje"]] + Resultado
    else:
        Resultado= Resultado + [[Tabla[0].split(",")[0] + " " + Tabla[0].split(",")[1], Tabla[0].split(",")[2].split("\n")[0]]]
        return Transformar(Tabla[1:],Resultado)

def TablaAux(fila, columna, filamax, columnamax, Puntajes, Tabla):
    if fila<filamax:
        Celda=Entry(Tabla,width=20,fg="black",bg="sky blue",font=("Arial",15,"bold"))
        Celda.grid(row=fila, column= columna)
        Celda.insert(END, Puntajes[fila][columna])
        columna+=1
        if columna<columnamax:
            TablaAux(fila, columna, filamax, columnamax, Puntajes, Tabla)
        else:
            fila+=1
            columna=0
            TablaAux(fila, columna, filamax, columnamax, Puntajes, Tabla)

def TransformarMatriz(Matriz):
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
            matrizJ= TransformarMatriz(Datos[9])
            matrizJ2= TransformarMatriz(Datos[10])
            matrizE= TransformarMatriz(Datos[11])
            RestantesA= int(Datos[12])
            RestantesE= int(Datos[13])
            Tiempo= int(Datos[14])
            Interfaz.withdraw()
            tablero= Tablero(BarcosA, BarcosB, BarcosC, ColocadosA, ColocadosB, ColocadosC, Jugador_Nombre, Aciertos, Fallos, matrizJ, matrizJ2, matrizE, RestantesA, RestantesE, Tiempo)
            tablero.Accion()
            Interfaz.deiconify()
            Puntos= tablero.Get_Puntos()

            if Puntos!=0:
                Contenido= LeerArchivo()
                Posicion=VerificaPosicion(Contenido,1, Puntos)

                if Posicion<8:
                    Borrar=open("Puntos.txt","w")
                    Borrar.close()
                    NuevaTabla(Posicion,1,Contenido, Puntos, Nombre)
                    messagebox.showinfo('Felicidades', 'Has entrado en el salón de la fama:')
                    Tabla()
            
    else:
        messagebox.showwarning('Error al buscar la partida', 'La partida se guarda con su nombre de usuario.')

    

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
    Acerca=Toplevel()
    Acerca.title("Ayuda")
    Acerca.minsize(800,533)
    Acerca.resizable(width=NO, height=NO)
    Titulo1= Label(Acerca, text= 'Guia para poder jugar:', font=('Arial', 11))
    Titulo1.place(x=10, y= 10)
    Guia= Label(Acerca, text= 'Primero hay que introducir el nombre de usuario y la cantidad de barcos qué quiere de cada tipo, luego colocar\nlos barcos de cada tipo en las posiciones que usted guste, para esto simplemente haga click en la casilla donde\ndesea colocar sus barcos y darle al botón de check sí ahí es donde desea colocar el barco, si desea mover su barco\nde forma  vertical u horizontal haga click en cualquiera de los botones que usted necesite para ello, después dará\n inicio a la partida,haga click donde desee atacar en el tablero enemigo, se le mostrar la información de si acertó o falló,\nen caso de haber acertado puede volver a atacar, en caso contrario espere a que el enemigo ataque, una vez usted o\nel enemigo hayan logrado derribar todos los barcos contrarios, se acabará el juego mostrándole las estadísticas de\nla partida. Si desea puede guardar la partida dándole al botón guardar y en el menú puede volver a cargar la partida\njustamente donde la dejó.', font=('Arial', 11))
    Guia.place(x= 10, y=30)
    Titulo2= Label(Acerca, text= 'Desarrolladores', font=('Arial', 11))
    Titulo2.place(x=10, y=50)
    Desarrolladores= Label(Acerca, text= 'Estudiantes de ingeniería en computadores en el instituto tecnológico de Costa Rica con el profesor\nJason Leiton Jiménez en el curso de taller de programación GR 5, versión 1.0\nJavier Mora Masis y Christopher Rodríguez', font=('Arial',11))
    Desarrolladores.place(x=10, y=200)

def Salón_de_la_fama():
    salon=Toplevel()
    salon.title("Salón de la fama")
    salon.minsize(800,533)
    salon.resizable(width=NO, height=NO)
    canvas2 = Canvas(salon, width=800, height=533)
    canvas2.place(x=0, y=0)
    

def Documentacion():
    tablero= Tablero(0, 0, 0, 0, 0, 0, "Docu", 0, 0, [], [], [], 0, 0, 0)
    help(Fail)
    help(acierto)
    help(tablero.Guardar_Partida)
    help(tablero.PartidaNoEmpezada)
    help(tablero.CrearTablas)
    help(tablero.ColocarBarcos)
    help(tablero.Recrear)
    help(tablero.Ataque)
    help(tablero.tiempoSupremo)
    help(tablero.Battalla)

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
menubar.add_command(label="Salón de la fama",command= lambda: Tabla())
Interfaz.config(menu= menubar)#agrega al menu
Jugar= Button(Interfaz, text= "Jugar", command=lambda: Verifica( int(BarcosA.get()), int(BarcosB.get()), int(BarcosC.get()), Nusuario.get()))
Jugar.place(x= 50, y= 260)
Boton_Cargar= Button(Interfaz, text="Cargar", command= lambda: Cargar(Cargar_Partida.get()))
Boton_Cargar.place(x=350, y= 80)
Opcioes=Menu(Interfaz)
canvas.grid()
Interfaz.mainloop()



"""
Referencias:
https://www.youtube.com/watch?v=Zvrj1b9Mguk&list=PL46E99FE946C1C946&index=45&ab_channel=ChelinTutorials
http://programarcadegames.com/python_examples/show_file.php?lang=es&file=array_backed_grid.py
"""
