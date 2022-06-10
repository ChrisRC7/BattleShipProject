from tkinter import PhotoImage
from pygame import *
import os, pygame, random
import time
import threading

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

def Hilos(BarcosA, BarcosB, BarcosC, Nombre):
    t1= threading.Thread(target= Play, args=(BarcosA, BarcosB, BarcosC, Nombre))
    t1.start()
    #time.sleep(5)
    #t2= threading.Thread(target= Jugador)
    #t2.start()





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

def Play(BarcosA, BarcosB, BarcosC, Nombre):
    TableroIA= TableroEnemigo(BarcosA, BarcosB, BarcosC, Nombre)

def Jugador():
    TableroP= TableroJugador()

class TableroEnemigo: 

    
    def __init__(self, BarcosA, BarcosB, BarcosC, Nombre):
        pygame.init()
        self.pantalla= pygame.display.set_mode([1320, 655])
        pygame.display.set_caption("Guerra Naval")

        #Colores
        Fondo= (0, 99, 230)
        Casillas= (0, 14, 107)
        Acierto= (0, 71, 12)
        Fallo= (82, 20, 48)

        self.Acierto= 0
        self.Fallos= 0
        self.BarcosA= BarcosA #5
        self.BarcosB= BarcosB #3
        self.BarcosC= BarcosC #2

        
        Cuadro= 60 #Tamaño de los cuadros
        Margen= 5 #Distancia entre cuadros

        matriz= []


        for fila in range(10):
            matriz.append([])
            for columna in range(10):
                matriz[fila].append(3)
        


        
        Posicionate = 0

        while Posicionate < self.BarcosA:
            x=random.randint(0,9)
            y=random.randint(0,9)
            if matriz[y][x]!=0:
                matriz[y][x]=0
                Posicionate+= 1
        Posicionate = 0
        
        while Posicionate < self.BarcosB:
            x=random.randint(0,8)
            y=random.randint(0,8)
            Posicion= random.choice(["Vertical", "Horinzontal"])
            Cordenada1= matriz[y][x]
            if Posicion == "Vertical":
                Cordenada2= matriz[y+1][x]
                if Cordenada1!= 0 and Cordenada1 != 1 and Cordenada2 != 0 and Cordenada2 !=1:
                    matriz[y][x]= 1
                    matriz[y+1][x]= 1
                    Posicionate+=1
            else:

                Cordenada2= matriz[y][x+1]
                if Cordenada1!= 0 and Cordenada1 != 1 and Cordenada2 != 0 and Cordenada2 !=1:
                    matriz[y][x]= 1
                    matriz[y][x+1]= 1
                    Posicionate+=1

        Posicionate= 0
        
        while Posicionate < self.BarcosC:
            x=random.randint(0,6)
            y=random.randint(0,6)
            Posicion= random.choice(["Vertical", "Horinzontal"])
            Cordenada1= matriz[y][x]
            if Posicion == "Vertical":
                Cordenada2= matriz[y+1][x]
                Cordenada3= matriz[y+2][x]
                Cordenada4= matriz[y+3][x]
                if Cordenada1!= 0 and Cordenada1 != 1 and Cordenada1!= 2 and Cordenada2 != 0 and Cordenada2 !=1\
                    and Cordenada2 != 2 and Cordenada3 !=0 and Cordenada3 !=1 and Cordenada3 !=2 and Cordenada4 !=0 \
                    and Cordenada4 !=1 and Cordenada4 != 2:
                    matriz[y][x]= 2
                    matriz[y+1][x]= 2
                    matriz[y+2][x]= 2
                    matriz[y+3][x]= 2
                    Posicionate+=1
            else:

                Cordenada2= matriz[y][x+1]
                Cordenada3= matriz[y][x+2]
                Cordenada4= matriz[y][x+3]

                if Cordenada1!= 0 and Cordenada1 != 1 and Cordenada1!= 2 and Cordenada2 != 0 and Cordenada2 !=1\
                    and Cordenada2 != 2 and Cordenada3 !=0 and Cordenada3 !=1 and Cordenada3 !=2 and Cordenada4 !=0 \
                    and Cordenada4 !=1 and Cordenada4 != 2:
                    matriz[y][x]= 2
                    matriz[y][x+1]= 2
                    matriz[y][x+2]= 2
                    matriz[y][x+3]= 2
                    Posicionate+=1



        self.pantalla.fill(Fondo)

        for fila in range(10):
            for columna in range(0, 20):
                color= Casillas
                pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* columna + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])

                pygame.display.flip()
            
        for fila in range(10):
            for columna in range(10, 20):
                color= Acierto
                pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* columna + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])

                pygame.display.flip()

        
        run= True
        reloj= pygame.time.Clock()
        while run:
         
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    run= False
        
                elif evento.type == pygame.MOUSEBUTTONDOWN:

                    #if evento.key == pygame.K_a:
                        posicion = pygame.mouse.get_pos()
                        print(posicion)
                        columna = posicion[0] // (Cuadro+Margen)
                        fila= posicion[1] // (Cuadro+Margen)
                        if columna>=10:
                            columna=9
                        if fila>=10:
                            fila=9    
                        print(columna)
                        print(fila)
                        Cordenada= matriz[fila][columna]
                        print(Cordenada)
                        
                        if Cordenada== 3:
                            matriz[fila][columna] = 4
                            print("Fallo")
                            #Fail()
                            self.Fallos+=1
                            color= Fallo
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* columna + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])

                        elif Cordenada!= 4:
                            if Cordenada == 0:
                                print("Barco Tipo A")
                            elif Cordenada == 1:
                                print("Barco Tipo B")
                            elif Cordenada == 2:
                                print("Barco Tipo C")

                            matriz[fila][columna] = 4

                            self.Acierto+=1
                            color= Acierto
                            print("sexo")
                            acierto()
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* columna + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])


                        

            reloj.tick(60)

            pygame.display.flip()

        pygame.quit()
        


class TableroJugador:


     def __init__(self):
        pygame.init()
        self.pantallaJugador= pygame.display.set_mode([655, 655])
        pygame.display.set_caption("Jugador")

        #Colores
        Fondo= (137,59,176)
        Casillas= (103,46,138)
        aliado=(115,88,38)
        self.BarcosA= 5 #5
        self.BarcosB= 3 #3
        self.BarcosC= 2 #2


        self.Acierto= 0
        self.Fallos= 0

        Cuadro= 60 #Tamaño de los cuadros
        Margen= 5 #Distancia entre cuadros

        matriz=[]
        for fila in range(10):
            matriz.append([])
            for columna in range(10):
                matriz[fila].append(3)

        self.pantallaJugador.fill(Fondo)
        for fila in range(10):
            for columna in range(10):
                color= Casillas
                pygame.draw.rect(self.pantallaJugador, color, [(Margen+Cuadro)* columna + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])

                pygame.display.flip()
        """
        run= True
        reloj= pygame.time.Clock()
        Posicionate=0
        while run:
         
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    run= False
        
                elif evento.type == pygame.MOUSEBUTTONDOWN:

                    #if evento.key == pygame.K_a:
                        posicion = pygame.mouse.get_pos()
                        print(posicion)
                        columna = posicion[0] // (Cuadro+Margen)
                        fila= posicion[1] // (Cuadro+Margen)
                        #print(columna)
                        #print(fila)
                        Cordenada= matriz[fila][columna]
                        
                        if Posicionate < self.BarcosA:
                            matriz[fila][columna] = 0
                            print("ya se ocupo")
                            color= aliado
                            pygame.draw.rect(self.pantallaJugador, color, [(Margen+Cuadro)* columna + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                            Posicionate+=1



                            


            reloj.tick(60)

            pygame.display.flip()

        pygame.quit()
    """


Hilos(1, 2 ,3, "dsfdg")