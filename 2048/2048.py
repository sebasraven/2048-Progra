from Logic import *
import time
import random
from threading import Thread
print('Ingrese Iniciar(0) para comenzar a jugar')
Array = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[0,0,0,0]]
randArray2 = [0, 10, 10]
randArray8 = [0, 2, 2]
randArray10 = [0, 2, 2]
randArray16 = [0, 2, 2]
Leaderboard = []
segundos = 5
randArrayMove = [0,2,2,2,2,4]



#Agrega # random al tablero
def randAgregar(Array, i, j):
      if(j == 3):
            if(i == 3):
                  if(Array[i][j] == 0):
                        Array[i][j] = random.choice(randArrayMove)
            else:
                  if(Array[i][j] == 0):
                        Array[i][j] = random.choice(randArrayMove)
                  else:
                        return randAgregar(Array, i+1, j)
      elif(Array[i][j] == 0):
            Array[i][j] = random.choice(randArrayMove)
      else:
            return randAgregar(Array, i, j+1)

#Revisar si perdio
def gameOver(Array, i, j):
      if(j == 3):
            if(i == 3):
                  if(Array[i][j] == Array[i][j+1]):
                        return False
                  else:
                        return True                  
            else:
                  j = 0
                  return gameOver(Array, i+1, j)            
      if(Array[i][j] == Array[i][j+1]):
            return False
      else:
            return gameOver(Array, i, j+1)

     
#Funcion que revisa si el tablero esta lleno  
def fullArray(Array, i, j):
      if(i != len(Array)-1):
            if(j == len(Array[i])-1):
                  if(Array[i][j] != 0):
                        return fullArray(Array, i+1,j-j)
                  else:
                        return False
            else:
                  if(Array[i][j] != 0):
                        return fullArray(Array, i, j+1)
                  else:
                        return False
      else:
            if(j == len(Array[i])-1):
                  if(Array[i][j] != 0):
                        return gameOver(Array, 0, 0)
                  else:
                        return False
            else:
                  if(Array[i][j] != 0):
                        return fullArray(Array, i, j+1)
                  else:
                        return False
                        
                   
                     
#Up
def Up(Array):
      fullArray(Array, 0, 0)
      if(gameOver ==  True):
            return 'Fin del juego'
      else:
            sumaUp(Array, 0, 0)
#Down
def Down(Array):
      fullArray(Array, 0, 0)
      if(gameOver ==  True):
            return 'Fin del juego'
      else:
            sumaDown(Array, 0, 0)
#Left
def Left(Array):
      fullArray(Array, 0, 0)
      if(gameOver ==  True):
            return 'Fin del juego'
      else:
            sumaLeft(Array, 0, 0)
#Right
def Right(Array):
      fullArray(Array, 0, 0)
      if(gameOver ==  True):
            return 'Fin del juego'
      else:
            sumaRight(Array, 0, 0)
            
            
 
      
                           
#El usuario elige el siguiente movimiento
def move(Array, Dir):
      if(Dir == 'w'):
            Up(Array)
            randAgregar(Array, 0, 0)
            print(Array[0][0], '\t',Array[0][1], '\t',Array[0][2], '\t',Array[0][3], '\n', Array[1][0], '\t',Array[1][1], '\t',Array[1][2], '\t',Array[1][3], '\n', Array[2][0], '\t',Array[2][1], '\t',Array[2][2], '\t',Array[2][3], '\n', Array[3][0], '\t',Array[3][1], '\t',Array[3][2], '\t',Array[3][3], '\n')
            Dir = input('Ingrese su siguiente movimiento(w,s,a,d):')
            return move (Array, Dir)
      if(Dir == 's'):
            Down(Array)
            randAgregar(Array, 0, 0)
            print(Array[0][0], '\t',Array[0][1], '\t',Array[0][2], '\t',Array[0][3], '\n', Array[1][0], '\t',Array[1][1], '\t',Array[1][2], '\t',Array[1][3], '\n', Array[2][0], '\t',Array[2][1], '\t',Array[2][2], '\t',Array[2][3], '\n', Array[3][0], '\t',Array[3][1], '\t',Array[3][2], '\t',Array[3][3], '\n')
            Dir = input('Ingrese su siguiente movimiento(w,s,a,d):')
            return move (Array, Dir)
      if(Dir == 'a'):
            Left(Array)
            randAgregar(Array, 0, 0)
            print(Array[0][0], '\t',Array[0][1], '\t',Array[0][2], '\t',Array[0][3], '\n', Array[1][0], '\t',Array[1][1], '\t',Array[1][2], '\t',Array[1][3], '\n', Array[2][0], '\t',Array[2][1], '\t',Array[2][2], '\t',Array[2][3], '\n', Array[3][0], '\t',Array[3][1], '\t',Array[3][2], '\t',Array[3][3], '\n')
            Dir = input('Ingrese su siguiente movimiento(w,s,a,d):')
            return move (Array, Dir)
      if(Dir == 'd'):
            Right(Array)
            randAgregar(Array, 0, 0)
            print(Array[0][0], '\t',Array[0][1], '\t',Array[0][2], '\t',Array[0][3], '\n', Array[1][0], '\t',Array[1][1], '\t',Array[1][2], '\t',Array[1][3], '\n', Array[2][0], '\t',Array[2][1], '\t',Array[2][2], '\t',Array[2][3], '\n', Array[3][0], '\t',Array[3][1], '\t',Array[3][2], '\t',Array[3][3], '\n')
            Dir = input('Ingrese su siguiente movimiento(w,s,a,d):')
            return move (Array, Dir)
      else:
            Error = input('Ingrese un movimiento valido (w,s,a,d):')
            return move(Array, Error)


#Contador de 5 mins
def Timer(segundos):
      for i in range(segundos):
            time.sleep(1)
      print('Fin del juego')

#baseStart
def baseStart(Base):
      if(Base == '2'):
            return randStart2(Array, 0, 0)      
      if(Base == '8'):
            return randStart8(Array, 0, 0)
      if(Base == '10'):
            return randStart10(Array, 0, 0)
      if(Base == '16'):
            return randStart16(Array, 0, 0)



#Comenzar el juego      
def randStart10(Array, i, j):
      while i < 4:
            Array[i][j] =  random.choice(randArray10)
            return randStart10(Array, i+1, j+1)
      print(Array[0][0], '\t',Array[0][1], '\t',Array[0][2], '\t',Array[0][3], '\n', Array[1][0], '\t',Array[1][1], '\t',Array[1][2], '\t',Array[1][3], '\n', Array[2][0], '\t',Array[2][1], '\t',Array[2][2], '\t',Array[2][3], '\n', Array[3][0], '\t',Array[3][1], '\t',Array[3][2], '\t',Array[3][3], '\n')
      Dir = input('Ingrese su siguiente movimiento(w,s,a,d):')            
      return move (Array, Dir)



#Inicializar la 'main screen'
def Iniciar(Start):
      if(Start == int(0)):
            Base = input('Ingrese la base numerica con la que desea jugar(2,8,10,16):' '\n' 'NOTA: SOLO FUNCIONA EN BASE 10, NO LOGRE HACERLO PARA OTRAS BASES, SORRY PROFE:')
            return baseStart(Base)
      if(Start == int(1)):
            print('Leaderboard')
            Next = input('Para comenzar a jugar ingrese 0, Para ver la leaderboard ingrese 1:')
            Iniciar(Next)
      else:
            Error = input('Ingrese un digito valido:')
            return Iniciar(Error)                  



            



      
                        
     


      
            


            
                        
                  
                  
