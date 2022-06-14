from pygame import *
import os, pygame, random
import time
import threading
from tkinter import messagebox
from tkinter import *


def T1(boton):
    t1=threading.Thread(target= CambiaBoton, args= (boton,))
    t1.start()

def Fail():
    """
    Esta función se encarga de reproducir el audio de Fallo
    Parametros:
    ninguno
    La funcion inicializar todos los módulos Pygame importados, pone la cancion, reproduce la cancion y controla el volumen

    return
    Retorna el sonido de Fallo
    """
    pygame.mixer.init() # Inicializar todos los módulos Pygame importados
    pygame.mixer.music.load("Adjuntos/fallo.wav")  # pone la cancion
    pygame.mixer.music.play(1)  # reproduce la cancion
    pygame.mixer.music.set_volume(0.5)  # el volumen de la musica

def acierto():
    """
    Esta función se encarga de reproducir el audio de explocion
    Parametros:
    ninguno
    La funcion inicializar todos los módulos Pygame importados, pone la cancion, reproduce la cancion y controla el volumen

    return
    Retorna el sonido de explocion
    """
    pygame.mixer.init()# Inicializar todos los módulos Pygame importados
    pygame.mixer.music.load("Adjuntos/explosion.wav")  # pone la cancion
    pygame.mixer.music.play(1)  # reproduce la cancion
    pygame.mixer.music.set_volume(0.5)  # el volumen de la musica



class Tablero: 

    
    def __init__(self, BarcosA, BarcosB, BarcosC, ColocadosA, ColocadosB, ColocadosC, Nombre, Aciertos, Fallos, matrizJ, matrizJ2, matrizE, RestantesA, RestantesE, Tiempo):
        pygame.init()
        self.pantalla= pygame.display.set_mode([1595, 655]) #1340, 655
        pygame.display.set_caption("Guerra Naval")

        #Colores
        Fondo= (0, 99, 230)
        CasillasE= (0, 14, 107)
        Acierto= (0, 71, 12)
        Fallo= (82, 20, 48)
        PosicionarBarcos= (28,84,68)
        self.timerrr= Tiempo

    
        self.Aciertos= Aciertos
        self.Fallos= Fallos
        self.BarcosA= BarcosA #5
        self.BarcosB= BarcosB #3
        self.BarcosC= BarcosC #2
        self.ColocadosA= ColocadosA
        self.ColocadosB= ColocadosB
        self.ColocadosC= ColocadosC

        self.RestantesA= RestantesA
        self.RestantesE= RestantesE

        
        self.matrizJ= matrizJ
        self.matrizJ2= matrizJ2
        self.matrizE= matrizE
        
        Aceptar= pygame.image.load('Adjuntos/aceptar.png')
        Aceptar2= pygame.image.load('Adjuntos/aceptar2.png')
        Vertical= pygame.image.load('Adjuntos/vertical.png')
        Vertical2= pygame.image.load('Adjuntos/vertical2.png')
        Horizontal= pygame.image.load('Adjuntos/horizontal.png')
        Horizontal2= pygame.image.load('Adjuntos/horizontal2.png')
        guardar= pygame.image.load('Adjuntos/guardar.png')
        guardar2= pygame.image.load('Adjuntos/guardar2.png')
        boton1= Boton(Aceptar, Aceptar2, 1350, 35)
        botonv= Boton(Vertical, Vertical2, 1350, 100)
        botonh= Boton(Horizontal, Horizontal2, 1350, 160)
        BotonGuardar= Boton(guardar, guardar2, 1350, 590 )
        cursor1= Cursor()
        

        
        Cuadro= 60 #Tamaño de los cuadros
        Margen= 5 #Distancia entre cuadros

        Fuente= pygame.font.Font(None, 30)
        Nombre_Texto= Fuente.render(Nombre, 0, (0,0,0))

        def Guardar_Partida():
            archivo=open(Nombre+'.txt','w')
            archivo.write(str(self.BarcosA) + '/' + str(self.BarcosB) + '/' + str(self.BarcosC) + '/' + str(self.ColocadosA) + '/' + str(self.ColocadosB) + '/' + str(self.ColocadosC) + '/' + Nombre + '/' + str(self.Aciertos) + '/' + str(self.Fallos) + '/' + str(self.matrizJ) + '/' + str(self.matrizJ2) + '/'  + str(matrizE) + '/' + str(self.RestantesA) + '/' + str(self.RestantesE) + '/' + str(self.timerrr))
            archivo.close

        if self.ColocadosC<BarcosC:
            
            if self.matrizJ==[]:

                for fila in range(10):
                    self.matrizE.append([])
                    self.matrizJ.append([])
                    self.matrizJ2.append([])
                    for columna in range(10):
                        self.matrizE[fila].append(3)
                        self.matrizJ[fila].append(3)
                        self.matrizJ2[fila].append(3)

                Posicionate = 0
                """
                Esta función se encarga de colocar barco tipo a en una posicion aleatoria 
                Parametros:
                ninguno
                La funcion agarra un numero random para la x,y y coloca un barco en la posicion de la matriz donde esten la x,y escogidas y verifica que no haya un otro barco en esa posicion

                return
                Retorna un barco tipo a en una posicion aleatoria 
                """
                while Posicionate < self.BarcosA:
                    x=random.randint(0,9)
                    y=random.randint(0,9)
                    if matrizE[y][x]!=0:
                        matrizE[y][x]=0
                        Posicionate+= 1
                Posicionate = 0
                """
                Esta función se encarga de colocar barco tipo b en una posicion aleatoria 
                Parametros:
                ninguno
                La funcion agarra un numero random para la x,y y escoge de forma random si es vertical o horizontal, coloca un barco en la posicion de la matriz donde esten la x,y escogidas y verifica que no haya un otro barco en esa posicion
                si es vertical, a cordenada2 le suma un 1 a la y, y si es horizontal a cordenada2 le suma un 1 a la x

                return
                Retorna un barco tipo b en una posicion aleatoria 
                """
                while Posicionate < self.BarcosB:
                    x=random.randint(0,8)
                    y=random.randint(0,8)
                    Posicion= random.choice(["Vertical", "Horinzontal"])
                    Cordenada1= matrizE[y][x]
                    if Posicion == "Vertical":
                        Cordenada2= matrizE[y+1][x]
                        if Cordenada1!= 0 and Cordenada1 != 1 and Cordenada2 != 0 and Cordenada2 !=1:
                            matrizE[y][x]= 1
                            matrizE[y+1][x]= 1
                            Posicionate+=1
                    else:

                        Cordenada2= matrizE[y][x+1]
                        if Cordenada1!= 0 and Cordenada1 != 1 and Cordenada2 != 0 and Cordenada2 !=1:
                            matrizE[y][x]= 1
                            matrizE[y][x+1]= 1
                            Posicionate+=1

                Posicionate= 0
                """
                Esta función se encarga de colocar barco tipo c en una posicion aleatoria 
                Parametros:
                ninguno
                La funcion agarra un numero random para la x,y y escoge de forma random si es vertical o horizontal, coloca un barco en la posicion de la matriz donde esten la x,y escogidas y verifica que no haya un otro barco en esa posicion
                si es vertical, a cordenada2 le suma un 1 a la y,  a cordenada3 le suma un 2 a la y,  a cordenada4 le suma un 3 a la y,y si es horizontal, a cordenada2 le suma un 1 a la x, a cordenada3 le suma un 2 a la x,  a cordenada4 le suma un 3 a la x

                return
                Retorna un barco tipo c en una posicion aleatoria 
                """
                while Posicionate < self.BarcosC:
                    x=random.randint(0,6)
                    y=random.randint(0,6)
                    Posicion= random.choice(["Vertical", "Horinzontal"])
                    Cordenada1= matrizE[y][x]
                    if Posicion == "Vertical":
                        Cordenada2= matrizE[y+1][x]
                        Cordenada3= matrizE[y+2][x]
                        Cordenada4= matrizE[y+3][x]
                        if Cordenada1!= 0 and Cordenada1 != 1 and Cordenada1!= 2 and Cordenada2 != 0 and Cordenada2 !=1\
                            and Cordenada2 != 2 and Cordenada3 !=0 and Cordenada3 !=1 and Cordenada3 !=2 and Cordenada4 !=0 \
                            and Cordenada4 !=1 and Cordenada4 != 2:
                            matrizE[y][x]= 2
                            matrizE[y+1][x]= 2
                            matrizE[y+2][x]= 2
                            matrizE[y+3][x]= 2
                            Posicionate+=1
                    else:

                        Cordenada2= matrizE[y][x+1]
                        Cordenada3= matrizE[y][x+2]
                        Cordenada4= matrizE[y][x+3]

                        if Cordenada1!= 0 and Cordenada1 != 1 and Cordenada1!= 2 and Cordenada2 != 0 and Cordenada2 !=1\
                            and Cordenada2 != 2 and Cordenada3 !=0 and Cordenada3 !=1 and Cordenada3 !=2 and Cordenada4 !=0 \
                            and Cordenada4 !=1 and Cordenada4 != 2:
                            matrizE[y][x]= 2
                            matrizE[y][x+1]= 2
                            matrizE[y][x+2]= 2
                            matrizE[y][x+3]= 2
                            Posicionate+=1

            self.pantalla.fill(Fondo)

            for fila in range(10):
                for columna in range(10):
                    color= CasillasE
                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* columna + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
            
            for fila in range(10):
                for columna in range(10, 20):
                    color= CasillasE
                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])

            pygame.display.flip()

            for fila in range(10):
                for columna in range(10):
                    Valor= self.matrizJ[fila][columna]
                    if Valor==0:
                        PosX= ((columna%10)*65)+687.5
                        PosY= ((fila%10)*65)+7
                        BarcoA= pygame.image.load('Adjuntos/BarcosAH.png')
                        print('Se coloco BarcoA')
                        self.pantalla.blit(BarcoA, [PosX, PosY])

                    elif Valor==1 and columna<=8:
                        if self.matrizJ[fila][columna+1]==1:
                            self.matrizJ[fila][columna+1]=6
                            PosX= ((columna%10)*65)+687.5
                            PosY= ((fila%10)*65)+7
                            BarcoB= pygame.image.load('Adjuntos/BarcosBH.png')
                            print('Se coloco BarcoBH')
                            self.pantalla.blit(BarcoB, [PosX, PosY])

                    elif Valor==1 and fila<=8:
                        if self.matrizJ[fila+1][columna]==1:
                            self.matrizJ[fila+1][columna]= 6
                            PosX= ((columna%10)*65)+687.5
                            PosY= ((fila%10)*65)+7
                            BarcoB= pygame.image.load('Adjuntos/BarcosBV.png')
                            print('Se coloco BarcoBV')
                            self.pantalla.blit(BarcoB, [PosX, PosY])

                    elif Valor==2 and columna<=6:
                        if self.matrizJ[fila][columna+1]==2 and self.matrizJ[fila][columna+2]==2 and self.matrizJ[fila][columna+3]==2:
                            self.matrizJ[fila][columna+1]= 7
                            self.matrizJ[fila][columna+2]= 7
                            self.matrizJ[fila][columna+3]= 7
                            PosX= ((columna%10)*65)+687.5
                            PosY= ((fila%10)*65)+7
                            BarcoC= pygame.image.load('Adjuntos/BarcosCH.png')
                            self.pantalla.blit(BarcoC, [PosX, PosY])
                            print('Se coloco BarcoCH')

                    elif Valor==2 and fila<=6:
                        if self.matrizJ[fila+1][columna]==2 and self.matrizJ[fila+2][columna]==2 and self.matrizJ[fila+2][columna]==2:
                            self.matrizJ[fila+1][columna]= 7
                            self.matrizJ[fila+2][columna]= 7
                            self.matrizJ[fila+3][columna]= 7
                            PosX= ((columna%10)*65)+687.5
                            PosY= ((fila%10)*65)+7
                            BarcoC= pygame.image.load('Adjuntos/BarcosCV.png')
                            print('Se coloco BarcoCV')
                            self.pantalla.blit(BarcoC, [PosX, PosY])




            confirmar= False
            PosX= -500
            PosX2= -500
            PosX3= -500
            PosX4= -500
            PosY= -500
            PosY2= -500
            PosY3= -500
            PosY4= -500
            Orientacion= 'H'


            while self.ColocadosA<BarcosA:

                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        Posicionate=100
                        pygame.quit()

                    elif evento.type == pygame.MOUSEBUTTONDOWN:
                        posicion= pygame.mouse.get_pos()
                        columna = int((posicion[0]-687.5) // (Cuadro+Margen-0.5))
                        fila= posicion[1] // (Cuadro+Margen)
                        columna+=10
                        print(posicion)
                        print(fila)
                        print(columna)

                        if cursor1.colliderect(BotonGuardar.rect):
                            T1(BotonGuardar)
                            Guardar_Partida()

                        if cursor1.colliderect(botonh.rect):
                            Orientacion= 'H'
                            T1(botonh)
                                
                            
                        if cursor1.colliderect(botonv.rect):
                            Orientacion= 'V'
                            T1(botonv)


                        if cursor1.colliderect(boton1.rect) and confirmar:
                            self.matrizJ[PosY][PosX-10]= 0
                            self.matrizJ2[PosY][PosX-10]= 0
                            print("Posicion en Y: ", PosY)
                            print("Posicion en X: ", PosX)
                            color= CasillasE
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                            PosX= ((PosX%10)*65)+687.5
                            PosY= ((PosY%10)*65)+7
                            T1(boton1)
                            self.ColocadosA+=1
                            confirmar= False
                            Barco_Nombre= 'BarcosA' + Orientacion
                            BarcoA= pygame.image.load('Adjuntos/'+Barco_Nombre+ '.png')
                            self.pantalla.blit(BarcoA, [PosX, PosY])
                            PosX= -500
                            PosY= -500
                    
                        if 20>columna>=10 and fila<10: 
                            Posicion1= self.matrizJ[fila][columna-10]
                            print('Esta es la posicion: ', Posicion1)
                            if Posicion1 == 3:
                                color= CasillasE
                                pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                PosX= columna
                                PosY= fila
                                print("Barco")
                                confirmar= True
                                color= PosicionarBarcos
                                pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                            else:
                                messagebox.showwarning('Conflicto', 'Ya hay un barco en esta posicion')
                                
                                

                cursor1.update()
                boton1.update(self.pantalla)
                botonh.update(self.pantalla)
                botonv.update(self.pantalla)
                BotonGuardar.update(self.pantalla)

                pygame.display.flip()
         

            while self.ColocadosB<BarcosB:

                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        Posicionate=100
                        pygame.quit()

                    elif evento.type == pygame.MOUSEBUTTONDOWN:
                        posicion= pygame.mouse.get_pos()
                        columna = int((posicion[0]-687.5) // (Cuadro+Margen-0.5))
                        fila= posicion[1] // (Cuadro+Margen)
                        columna+=10

                        if cursor1.colliderect(BotonGuardar.rect):
                            T1(BotonGuardar)
                            Guardar_Partida()
                        
                        if cursor1.colliderect(botonh.rect) and confirmar:
                            T1(botonh)
                            if Orientacion!= 'H':
                                if PosX==19:
                                    Posicion1= self.matrizJ[PosY][8]
                                    Posicion2= self.matrizJ[PosY][9]
                                else:
                                    Posicion1= self.matrizJ[PosY][PosX-10]
                                    Posicion2= self.matrizJ[PosY][PosX-9]
                                if Posicion1==3 and Posicion2==3:
                                    Orientacion= 'H'
                                    color= CasillasE
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                    if PosX==19:
                                        PosX= PosX2= 18
                                    color= PosicionarBarcos
                                    PosX2+=1
                                    PosY2= PosY
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                else:
                                    messagebox.showwarning('Conflicto', 'Ya hay un barco en esta posicion')
                        
                        if cursor1.colliderect(botonv.rect) and confirmar:
                            T1(botonv)
                            if Orientacion!= 'V':
                                if PosY==9:
                                    Posicion1= self.matrizJ[8][PosX-10]
                                    Posicion2= self.matrizJ[9][PosX-10]
                                else:
                                    Posicion1= self.matrizJ[PosY][PosX-10]
                                    Posicion2= self.matrizJ[PosY+1][PosX-10]

                                if Posicion1==3 and Posicion2==3:
                                    Orientacion= 'V'
                                    color= CasillasE
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                    if PosY==9:
                                        PosY= PosY2= 8
                                    color= PosicionarBarcos
                                    PosX2= PosX
                                    PosY2+= 1
                                    print('PosX: ', PosX, PosX2)
                                    print('PosY: ', PosY, PosY2)
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                else:
                                    messagebox.showwarning('Conflicto', 'Ya hay un barco en esta posicion')
                            


                        if cursor1.colliderect(boton1.rect) and confirmar:
                            self.matrizJ[PosY][PosX-10]= 1
                            self.matrizJ[PosY2][PosX2-10]= 1
                            self.matrizJ2[PosY][PosX-10]= 1
                            self.matrizJ2[PosY2][PosX2-10]= 1
                            color= CasillasE
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                            PosX= ((PosX%10)*65)+687.5
                            PosY= ((PosY%10)*65)+7
                            Barco_Nombre= 'BarcosB' + Orientacion
                            BarcoA= pygame.image.load('Adjuntos/'+Barco_Nombre+ '.png')
                            self.pantalla.blit(BarcoA, [PosX, PosY])
                            T1(boton1)
                            self.ColocadosB+=1
                            confirmar= False
                            PosX= -500
                            PosX2= -500
                            PosY= -500
                            PosY2= -500
                
                        if 20>columna>=10 and fila<10: 
                            
                            if Orientacion=='H':
                                if columna==19:
                                    columna=18
                                Posicion1= self.matrizJ[fila][columna-10]
                                Posicion2= self.matrizJ[fila][columna-9]
                                if Posicion1==3 and Posicion2==3:
                                    color= CasillasE
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                    PosX= PosX2= columna
                                    PosY= PosY2= fila
                                    PosX2+=1
                                    confirmar= True
                                    color= PosicionarBarcos
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                else:
                                    messagebox.showwarning('Conflicto', 'Ya hay un barco en esta posicion')

                            elif Orientacion=='V':
                                if fila==9:
                                    fila=8
                                Posicion1= self.matrizJ[fila][columna-10]
                                Posicion2= self.matrizJ[fila+1][columna-10]
                                if Posicion1==3 and Posicion2==3:
                                    color= CasillasE
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                    PosX= PosX2= columna
                                    PosY= PosY2= fila
                                    PosY2+=1
                                    print("Barco")
                                    print('PosX: ', PosX, PosX2)
                                    print('PosY: ', PosY, PosY2)
                                    confirmar= True
                                    color= PosicionarBarcos
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                else:
                                    messagebox.showwarning('Conflicto', 'Ya hay un barco en esta posicion')  



                    
                                
                            
                cursor1.update()
                boton1.update(self.pantalla)
                botonh.update(self.pantalla)
                botonv.update(self.pantalla)
                BotonGuardar.update(self.pantalla)

                pygame.display.flip()
            

            while self.ColocadosC<BarcosC:

                for evento in pygame.event.get():
                    if evento.type == pygame.QUIT:
                        Posicionate=100
                        pygame.quit()

                    elif evento.type == pygame.MOUSEBUTTONDOWN:
                        posicion= pygame.mouse.get_pos()
                        columna = int((posicion[0]-687.5) // (Cuadro+Margen-0.5))
                        fila= posicion[1] // (Cuadro+Margen)
                        columna+=10
                        print(posicion)
                        print(fila)
                        print(columna)

                        if cursor1.colliderect(BotonGuardar.rect):
                            T1(BotonGuardar)
                            Guardar_Partida()

                        if cursor1.colliderect(botonh.rect) and confirmar:
                            T1(botonh)
                            if Orientacion!= 'H':
                                if PosX>=17:
                                    Posicion1= self.matrizJ[PosY][6]
                                    Posicion2= self.matrizJ[PosY][7]
                                    Posicion3= self.matrizJ[PosY][8]
                                    Posicion4= self.matrizJ[PosY][9]
                                else:
                                    Posicion1= self.matrizJ[PosY][PosX-10]
                                    Posicion2= self.matrizJ[PosY][PosX-9]
                                    Posicion3= self.matrizJ[PosY][PosX-8]
                                    Posicion4= self.matrizJ[PosY][PosX-7]
                                if Posicion1==3 and Posicion2==3 and Posicion3==3 and Posicion4==3:
                                    Orientacion= 'H'
                                    color= CasillasE
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                                    if PosX>=17:
                                        PosX= PosX2= PosX3= PosX4= 16
                                    color= PosicionarBarcos
                                    PosX2+=1
                                    PosX3+=2
                                    PosX4+=3
                                    PosY2= PosY3= PosY4= PosY
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                                else:
                                    messagebox.showwarning('Conflicto', 'Ya hay un barco en esta posicion')
                        
                        if cursor1.colliderect(botonv.rect) and confirmar:
                            T1(botonv)
                            if Orientacion!= 'V':
                                if PosY>=7:
                                    Posicion1= self.matrizJ[6][PosX-10]
                                    Posicion2= self.matrizJ[7][PosX-10]
                                    Posicion3= self.matrizJ[8][PosX-10]
                                    Posicion4= self.matrizJ[9][PosX-10]
                                else:
                                    Posicion1= self.matrizJ[PosY][PosX-10]
                                    Posicion2= self.matrizJ[PosY+1][PosX-10]
                                    Posicion3= self.matrizJ[PosY+2][PosX-10]
                                    Posicion4= self.matrizJ[PosY+3][PosX-10]
                                if Posicion1==3 and Posicion2==3 and Posicion3==3 and Posicion4==3:
                                    Orientacion= 'V'
                                    color= CasillasE
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                                    if PosY>=7:
                                        PosY= PosY2= PosY3= PosY4= 6
                                    color= PosicionarBarcos
                                    PosY2+= 1
                                    PosY3+= 2
                                    PosY4+= 3
                                    PosX2= PosX3= PosX4= PosX
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                                else:
                                    messagebox.showwarning('Conflicto', 'Ya hay un barco en esta posicion')
                            



                        if cursor1.colliderect(boton1.rect) and confirmar:
                            self.matrizJ[PosY][PosX-10]= 2
                            self.matrizJ[PosY2][PosX2-10]= 2
                            self.matrizJ[PosY3][PosX3-10]= 2
                            self.matrizJ[PosY4][PosX4-10]= 2
                            self.matrizJ2[PosY][PosX-10]= 2
                            self.matrizJ2[PosY2][PosX2-10]= 2
                            self.matrizJ2[PosY3][PosX3-10]= 2
                            self.matrizJ2[PosY4][PosX4-10]= 2
                            color= CasillasE
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                            PosX= ((PosX%10)*65)+687.5
                            PosY= ((PosY%10)*65)+7
                            Barco_Nombre= 'BarcosC' + Orientacion
                            BarcoA= pygame.image.load('Adjuntos/'+Barco_Nombre+ '.png')
                            self.pantalla.blit(BarcoA, [PosX, PosY])
                            T1(boton1)
                            self.ColocadosC+=1
                            confirmar= False
                            PosX= -500
                            PosX2= -500
                            PosX3= -500
                            PosX4= -500
                            PosY= -500
                            PosY2= -500
                            PosY3= -500
                            PosY4= -500
                        
                
                        if 20>columna>=10 and fila<10: 

                            if Orientacion=='H':
                                if columna>=17:
                                    columna=16
                                Posicion1= self.matrizJ[fila][columna-10]
                                Posicion2= self.matrizJ[fila][columna-9]
                                Posicion3= self.matrizJ[fila][columna-8]
                                Posicion4= self.matrizJ[fila][columna-7]
                                if Posicion1==3 and Posicion2==3 and Posicion3==3 and Posicion4==3:
                        
                                    color= CasillasE
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                                    PosX= PosX2= PosX3= PosX4= columna
                                    PosY= PosY2= PosY3= PosY4= fila
                                    PosX2+=1
                                    PosX3+=2
                                    PosX4+=3
                                    print("Barco")
                                    confirmar= True
                                    color= PosicionarBarcos
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                                else:
                                    messagebox.showwarning('Conflicto', 'Ya hay un barco en esta posicion')

                            elif Orientacion=='V':
                                if fila>=7:
                                    fila=6
                                Posicion1= self.matrizJ[fila][columna-10]
                                Posicion2= self.matrizJ[fila+1][columna-10]
                                Posicion3= self.matrizJ[fila+2][columna-10]
                                Posicion4= self.matrizJ[fila+3][columna-10]
                                if Posicion1==3 and Posicion2==3 and Posicion3==3 and Posicion4==3:
                        
                                    color= CasillasE
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                                    PosX= PosX2= PosX3= PosX4= columna
                                    PosY= PosY2= PosY3= PosY4= fila
                                    PosY2+=1
                                    PosY3+=2
                                    PosY4+=3
                                    print("Barco")
                                    confirmar= True
                                    color= PosicionarBarcos
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                                else:
                                    messagebox.showwarning('Conflicto', 'Ya hay un barco en esta posicion')
                                
                cursor1.update()
                boton1.update(self.pantalla)
                botonh.update(self.pantalla)
                botonv.update(self.pantalla)
                BotonGuardar.update(self.pantalla)

                pygame.display.flip()
        else:
            
            self.pantalla.fill(Fondo)
            for fila in range(10):
                for columna in range(10):
                    Valor= self.matrizE[fila][columna]
                    if Valor==5:
                        color= Fallo
                    elif Valor==4:
                        color= Acierto
                    else:
                        color= CasillasE
                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* columna + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
            
            for fila in range(10):
                for columna in range(10, 20):
                    color= CasillasE
                    pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
            
            for fila in range(10):
                for columna in range(10):
                    Valor= self.matrizJ[fila][columna]
                    if Valor==0:
                        PosX= ((columna%10)*65)+687.5
                        PosY= ((fila%10)*65)+7
                        BarcoA= pygame.image.load('Adjuntos/BarcosAH.png')
                        print('Se coloco BarcoA')
                        self.pantalla.blit(BarcoA, [PosX, PosY])

                    elif Valor==1 and columna<=8:
                        if self.matrizJ[fila][columna+1]==1:
                            self.matrizJ[fila][columna+1]=6
                            PosX= ((columna%10)*65)+687.5
                            PosY= ((fila%10)*65)+7
                            BarcoB= pygame.image.load('Adjuntos/BarcosBH.png')
                            print('Se coloco BarcoBH')
                            self.pantalla.blit(BarcoB, [PosX, PosY])

                    elif Valor==1 and fila<=8:
                        if self.matrizJ[fila+1][columna]==1:
                            self.matrizJ[fila+1][columna]= 6
                            PosX= ((columna%10)*65)+687.5
                            PosY= ((fila%10)*65)+7
                            BarcoB= pygame.image.load('Adjuntos/BarcosBV.png')
                            print('Se coloco BarcoBV')
                            self.pantalla.blit(BarcoB, [PosX, PosY])

                    elif Valor==2 and columna<=6:
                        if self.matrizJ[fila][columna+1]==2 and self.matrizJ[fila][columna+2]==2 and self.matrizJ[fila][columna+3]==2:
                            self.matrizJ[fila][columna+1]= 7
                            self.matrizJ[fila][columna+2]= 7
                            self.matrizJ[fila][columna+3]= 7
                            PosX= ((columna%10)*65)+687.5
                            PosY= ((fila%10)*65)+7
                            BarcoC= pygame.image.load('Adjuntos/BarcosCH.png')
                            self.pantalla.blit(BarcoC, [PosX, PosY])
                            print('Se coloco BarcoCH')

                    elif Valor==2 and fila<=6:
                        if self.matrizJ[fila+1][columna]==2 and self.matrizJ[fila+2][columna]==2 and self.matrizJ[fila+2][columna]==2:
                            self.matrizJ[fila+1][columna]= 7
                            self.matrizJ[fila+2][columna]= 7
                            self.matrizJ[fila+3][columna]= 7
                            PosX= ((columna%10)*65)+687.5
                            PosY= ((fila%10)*65)+7
                            BarcoC= pygame.image.load('Adjuntos/BarcosCV.png')
                            print('Se coloco BarcoCV')
                            self.pantalla.blit(BarcoC, [PosX, PosY])
                
            for fila in range(10):
                for columna in range(10):
                    valor= self.matrizJ[fila][columna]
                    if valor==6:
                        self.matrizJ[fila][columna]= 1
                    elif valor==7:
                        self.matrizJ[fila][columna]=2

            for fila in range(10):
                for columna in range(10, 20):
                    Valor= self.matrizJ2[fila][columna-10]
                    if Valor==5:
                        color= Fallo
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                    elif Valor==4:
                        color= Acierto
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])

                    

                        

        pygame.draw.rect(self.pantalla, Fondo, [1337, 0, 1595, 655])
        self.pantalla.blit(Nombre_Texto,(1350, 5))
        self.Turno= False
        def Ataque():
            """
            Esta función se encarga de que el barco enemigo ataque
            Parametros:
            ninguno
            La funcion seleciona una x,y de forma random donde no haya atacado anteriormente,si la matrizJ[y][x]==3 la convierte en un 4 , reproduce la funcion Fail y hace un cuadrado en la posicion selecionada,
            de caso contrario  convierte la matrizJ[y][x] en 4, redroduce la funcion acierto y hace un cuadrado en la posicion selecionada

            return
            Si la ia falla, retorna un cuadrado en la posicion selecionada de color Fallo (rojo), Si la ia acierta, retorna un cuadrado en la posicion selecionada de color acierto (verde)
            """
            while self.Turno:
                x=random.randint(0,9)
                y=random.randint(0,9)
                Valor= self.matrizJ2[y][x]
                if Valor!=4 and Valor!=5:
                    columna= x+10
                    fila= y
                    if Valor== 3:
                        self.matrizJ2[y][x]= 5
                        time.sleep(1)
                        Fail()
                        print('La ia fallo')
                        color= Fallo
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                        time.sleep(1)
                        self.Turno= False
                    else:
                        self.matrizJ2[y][x]= 4
                        acierto()
                        print('La ia acerto')
                        color= Acierto
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                        pygame.display.flip()
                        self.RestantesA-= 1
                        time.sleep(1)
        
        
        run= True
        def tiempoSupremo():
            """
            Esta función se encarga de mostrar el timepo
            Parametros:
            ninguno
            La funcion crea un espacio donde se muestra una variable que se le va sumando 1 cada segundo

            return
            Retorna el timepo en partida  
            """
            while run == True:
                Tiempo= Fuente.render(str(self.timerrr) + ' segundos', 0, (0,0,0))
                pygame.draw.rect(self.pantalla, Fondo, [1350, 50, 1500, 80])
                self.pantalla.blit(Tiempo, (1350,50))
                self.timerrr+=1
                time.sleep(1)

        def T2():
            t2 = threading.Thread(target=tiempoSupremo)
            t2.start()      
        T2()
        self.Ganar= False
        Estado= 'Inconcluso'
        reloj= pygame.time.Clock()
        while run:
            if self.RestantesE== 0:
                self.Ganar= True
                Estado= 'de Victoria'
                run= False
            elif self.RestantesA== 0:
                Estado= 'de Derrota'
                run= False
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    run= False
                elif evento.type == pygame.MOUSEBUTTONDOWN and self.Turno==False:
                    
                    posicion = pygame.mouse.get_pos()
                    print(posicion)
                    columna = posicion[0] // (Cuadro+Margen)
                    fila= posicion[1] // (Cuadro+Margen) 
        
                    if cursor1.colliderect(BotonGuardar.rect):
                        T1(BotonGuardar)
                        Guardar_Partida()      

                    """
                    Esta función se encarga de que el jugador pueda atacar
                    Parametros:
                    ninguno
                    La funcion verifica si golpeo un barco, si no golpeo ningun barco, marca la zona como lugar atacado luego suma 1 a los ataques fallidos, crea un cuadrado en la zona del disparo para marcar que ya ataco ahi y llama la funcion Fail, nos muestra un mensaje que nos indica que fallamos,turno pasa a ser True, se llama a la funcion ataque,
                    si golpea algun barco, marca de que tipo es, suma 1 a aciertos resta uno a restantes, crea un cuadrado en la zona del disparo para marcar que ya ataco ahi y llama la funcion acierto,os muestra un mensaje que nos indica que acertamos

                    return
                    Retorna el disparo del jugador en la posicion deseada
                    """
                    if columna<10 and fila<10:
                        Cordenada= matrizE[fila][columna]
                        print(Cordenada)
                        if Cordenada== 3:
                            self.matrizE[fila][columna] = 5
                            self.Fallos+=1
                            color= Fallo
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* columna + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                            Fail()
                            messagebox.showinfo('Fallo', 'Disparo fallido')
                            self.Turno= True
                            pygame.display.flip()
                            Ataque()

                        elif Cordenada!= 4:
                            self.matrizE[fila][columna] = 4

                            self.Aciertos+=1
                            self.RestantesE-= 1 
                            color= Acierto
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* columna + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                            acierto()
                            messagebox.showinfo('Acierto', 'Barco golpeado')
                                
                            

                cursor1.update()
                BotonGuardar.update(self.pantalla)

            reloj.tick(60)

            pygame.display.flip()


        Estadisticas=('Usuario: '+ Nombre + '\nTiempo: ' + str(self.timerrr) + ' segundos' + '\nAceiertos: ' + str(self.Aciertos) +'\nFallos: ' + str(self.Fallos) + '\nIntentos: ' + str(self.Aciertos+self.Fallos))
        messagebox.showinfo('Estadisticas ' + Estado, Estadisticas)
        print(Estadisticas)
        pygame.quit()

    def Get_Puntos(self):
        if self.Ganar==True:
            return int(round(100+ 10000%self.timerrr,0))
        else:
            return 0



    
    

class Cursor(pygame.Rect):
    def __init__(self):
        pygame.Rect.__init__(self, 0, 0, 1, 1)
    def update(self):
        self.left, self.top= pygame.mouse.get_pos()


class Boton(pygame.sprite.Sprite): 
    def __init__(self, imagen1, imagen2, x, y):
        self.imagen1= imagen1
        self.imagen2= imagen2
        self.imagen_actual= self.imagen1
        self.rect= self.imagen_actual.get_rect()
        self.rect.left, self.rect.top= (x, y)

    def update(self, pantalla):
        pantalla.blit(self.imagen_actual, self)
        

    def Accion(self):
        self.imagen_actual= self.imagen2
       
        
    
    def Volver(self):
        self.imagen_actual= self.imagen1
    

def CambiaBoton(boton):
    boton.Accion()
    time.sleep(0.05)
    boton.Volver()

"""
a= 4
b= 4
c= 4


Totales= a + b*2 + c*4

Play(a, b, c, 0, 0, 0, "GatitosSupremos", 0, 0, [], [], [], Totales, Totales, 0)
       
"""
