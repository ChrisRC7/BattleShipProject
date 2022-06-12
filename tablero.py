from pygame import *
import os, pygame, random
import time
import threading
from tkinter import messagebox
from tkinter import *

from pyparsing import col

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




def T1(boton):
    t1=threading.Thread(target= CambiaBoton, args= (boton,))
    t1.start()





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



class TableroEnemigo: 

    
    def __init__(self, BarcosA, BarcosB, BarcosC, Nombre):
        pygame.init()
        self.pantalla= pygame.display.set_mode([1595, 655]) #1340, 655
        pygame.display.set_caption("Guerra Naval")

        #Colores
        Fondo= (0, 99, 230)
        CasillasE= (0, 14, 107)
        Acierto= (0, 71, 12)
        Fallo= (82, 20, 48)
        PosicionarBarcos= (28,84,68)
    


        self.Acierto= 0
        self.Fallos= 0
        self.TotalIntentos=0
        self.BarcosA= BarcosA #5
        self.BarcosB= BarcosB #3
        self.BarcosC= BarcosC #2

        Aceptar= pygame.image.load('Adjuntos/aceptar.png')
        Aceptar2= pygame.image.load('Adjuntos/aceptar2.png')
        Vertical= pygame.image.load('Adjuntos/vertical.png')
        Vertical2= pygame.image.load('Adjuntos/vertical2.png')
        Horizontal= pygame.image.load('Adjuntos/horizontal.png')
        Horizontal2= pygame.image.load('Adjuntos/horizontal2.png')
        boton1= Boton(Aceptar, Aceptar2, 1350, 5)
        botonv= Boton(Vertical, Vertical2, 1350, 70)
        botonh= Boton(Horizontal, Horizontal2, 1350, 130)
        cursor1= Cursor()
        

        
        Cuadro= 60 #Tamaño de los cuadros
        Margen= 5 #Distancia entre cuadros

        matrizE= []

        for fila in range(20):
            matrizE.append([])
            for columna in range(20):
                matrizE[fila].append(3)
    
        Posicionate = 0

        while Posicionate < self.BarcosA:
            x=random.randint(0,9)
            y=random.randint(0,9)
            if matrizE[y][x]!=0:
                matrizE[y][x]=0
                Posicionate+= 1
        Posicionate = 0
        
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

        Posicionate= 0


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


        while Posicionate<BarcosA:

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    Posicionate=100
                    pygame.quit()

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    posicion= pygame.mouse.get_pos()
                    columna = (posicion[0]-687.5) // (Cuadro+Margen-0.5)
                    fila= posicion[1] // (Cuadro+Margen)
                    columna+=10
                    print(posicion)
                    print(fila)
                    print(columna)

                    if cursor1.colliderect(botonh.rect):
                        Orientacion= 'H'
                        T1(botonh)
                        
                    
                    if cursor1.colliderect(botonv.rect):
                        Orientacion= 'V'
                        T1(botonv)


                    if cursor1.colliderect(boton1.rect) and confirmar:

                        color= CasillasE
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                        PosX= ((PosX%10)*65)+687.5
                        PosY= ((PosY%10)*65)+7
                        T1(boton1)
                        Posicionate+=1
                        confirmar= False
                        Barco_Nombre= 'BarcosA' + Orientacion
                        BarcoA= pygame.image.load('Adjuntos/'+Barco_Nombre+ '.png')
                        self.pantalla.blit(BarcoA, [PosX, PosY])
                        PosX= -500
                        PosY= -500
               
                    if 20>columna>=10 and fila<10: 
                     
                        color= CasillasE
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                        PosX= columna
                        PosY= fila
                        print("Barco")
                        confirmar= True
                        color= PosicionarBarcos
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                        
                        

            cursor1.update()
            boton1.update(self.pantalla)
            botonh.update(self.pantalla)
            botonv.update(self.pantalla)

            pygame.display.flip()
        Posicionate= 0

        while Posicionate<BarcosB:

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    Posicionate=100
                    pygame.quit()

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    posicion= pygame.mouse.get_pos()
                    columna = (posicion[0]-687.5) // (Cuadro+Margen-0.5)
                    fila= posicion[1] // (Cuadro+Margen)
                    columna+=10
                    print(posicion)
                    print(fila)
                    print(columna)

                    if cursor1.colliderect(botonh.rect):
                        T1(botonh)
                        if Orientacion!= 'H':
                            Orientacion= 'H'
                            color= CasillasE
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                            color= PosicionarBarcos
                            PosX2+=1
                            PosY2= PosY
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                    
                    if cursor1.colliderect(botonv.rect):
                        T1(botonv)
                        if Orientacion!= 'V':
                            Orientacion= 'V'
                            color= CasillasE
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                            color= PosicionarBarcos
                            PosX2= PosX
                            PosY2+= 1
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                        



                    if cursor1.colliderect(boton1.rect) and confirmar:
                        color= CasillasE
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                        PosX= ((PosX%10)*65)+687.5
                        PosY= ((PosY%10)*65)+7
                        Barco_Nombre= 'BarcosB' + Orientacion
                        BarcoA= pygame.image.load('Adjuntos/'+Barco_Nombre+ '.png')
                        self.pantalla.blit(BarcoA, [PosX, PosY])
                        T1(boton1)
                        Posicionate+=1
                        confirmar= False
                        PosX= -500
                        PosX2= -500
                        PosY= -500
                        PosY2= -500
               
                    if 20>columna>=10 and fila<10: 
                     
                        color= CasillasE
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                        PosX= PosX2= columna
                        PosY= PosY2= fila
                        if Orientacion=='H':
                            PosX2+=1
                        else:
                            PosY2+=1
                            
                        print("Barco")
                        confirmar= True
                        color= PosicionarBarcos
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (columna+0.5) + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
    
                           
                        
                        

            cursor1.update()
            boton1.update(self.pantalla)
            botonh.update(self.pantalla)
            botonv.update(self.pantalla)

            pygame.display.flip()
        
        Posicionate= 0

        while Posicionate<BarcosC:

            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    Posicionate=100
                    pygame.quit()

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    posicion= pygame.mouse.get_pos()
                    columna = (posicion[0]-687.5) // (Cuadro+Margen-0.5)
                    fila= posicion[1] // (Cuadro+Margen)
                    columna+=10
                    print(posicion)
                    print(fila)
                    print(columna)

                    if cursor1.colliderect(botonh.rect):
                        T1(botonh)
                        if Orientacion!= 'H':
                            Orientacion= 'H'
                            color= CasillasE
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                            color= PosicionarBarcos
                            PosX2+=1
                            PosX3+=2
                            PosX4+=3
                            PosY2= PosY3= PosY4= PosY
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                    
                    if cursor1.colliderect(botonv.rect):
                        T1(botonv)
                        if Orientacion!= 'V':
                            Orientacion= 'V'
                            color= CasillasE
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                            color= PosicionarBarcos
                            PosY2+= 1
                            PosY3+= 2
                            PosY4+= 3
                            PosX2= PosX3= PosX4= PosX
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                            pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                        



                    if cursor1.colliderect(boton1.rect) and confirmar:
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
                        Posicionate+=1
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
                     
                        color= CasillasE
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX+0.5) + Margen, (Margen+Cuadro)* PosY + Margen, Cuadro, Cuadro ])
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX2+0.5) + Margen, (Margen+Cuadro)* PosY2 + Margen, Cuadro, Cuadro ])
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX3+0.5) + Margen, (Margen+Cuadro)* PosY3 + Margen, Cuadro, Cuadro ])
                        pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* (PosX4+0.5) + Margen, (Margen+Cuadro)* PosY4 + Margen, Cuadro, Cuadro ])
                        
                        PosX= PosX2= PosX3= PosX4= columna
                        PosY= PosY2= PosY3= PosY4= fila
                        if Orientacion=='H':
                            PosX2+=1
                            PosX3+=2
                            PosX4+=3
                        else:
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
    
                           
                        
                        

            cursor1.update()
            boton1.update(self.pantalla)
            botonh.update(self.pantalla)
            botonv.update(self.pantalla)

            pygame.display.flip()

        pygame.draw.rect(self.pantalla, Fondo, [1337, 0, 1595, 655])






        run2=True
        self.timerrr=0
        def tiempoSupremo():
            if run2 == True:
                def timert():
                    self.timerrr+=1
                    time.sleep(1)
                    timert()

                def H_Arbol():
                    h1 = threading.Thread(target=timert, args=())
                    h1.start()
                    
            
                H_Arbol()
        tiempoSupremo()

        
        tiempo= 0
        run= True
        reloj= pygame.time.Clock()
        while run:
            def DespuesPartida():
                if run==False:
                    messagebox.showinfo('Estadisticas', Estadisticas)
                    print(Estadisticas)
         
            for evento in pygame.event.get():
                if evento.type == pygame.QUIT:
                    run= False
                    run2=False
                    DespuesPartida()
                    

                elif evento.type == pygame.MOUSEBUTTONDOWN:
                    

                    #if evento.key == pygame.K_a:
                        posicion = pygame.mouse.get_pos()
                        print(posicion)
                        columna = posicion[0] // (Cuadro+Margen)
                        fila= posicion[1] // (Cuadro+Margen) 
                        print(columna)
                        print(fila)
                       
                        
                        if cursor1.colliderect(boton1.rect):
                            T1(boton1)
                      
                            


                        if columna<10 and fila<10:
                            Cordenada= matrizE[fila][columna]
                            print(Cordenada)
                            if Cordenada== 3:
                                matrizE[fila][columna] = 4
                                #Fail()
                                self.Fallos+=1
                                self.TotalIntentos+=1
                                color= Fallo
                                pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* columna + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                                messagebox.showinfo('Fallo', 'Disparo fallido')
                                Fail()

                            elif Cordenada!= 4:
                                if Cordenada == 0:
                                    print("Barco Tipo A")
                                elif Cordenada == 1:
                                    print("Barco Tipo B")
                                elif Cordenada == 2:
                                    print("Barco Tipo C")

                                matrizE[fila][columna] = 4

                                self.Acierto+=1
                                self.TotalIntentos+=1
                                color= Acierto
                                pygame.draw.rect(self.pantalla, color, [(Margen+Cuadro)* columna + Margen, (Margen+Cuadro)* fila + Margen, Cuadro, Cuadro ])
                                messagebox.showinfo('Acierto', 'Barco golpeado')
                                acierto()

                cursor1.update()
           


                        

            reloj.tick(60)

            pygame.display.flip()

        pygame.quit()

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



Play(4,4,4, "jkdzfhg")
       

