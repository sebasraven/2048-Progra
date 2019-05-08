
#Realiza la suma despues de hacer pushUp
def sumaUp(Array, i, j):
      pushUp(Array, 0, 0, 0)
      if(j == 3):
            if(i == 3):
                  return Array
            else:
                  if(Array[i][j] == Array[i+1][j]):
                        Array[i][j] = Array[i][j] + Array[i+1][j]
                        Array[i+1][j] = 0
                        pushUp(Array, 0, 0, 0)
                        return sumaUp(Array, i+1, j)
                  else:
                        return sumaUp(Array, i+1, j)
      elif(i == 3):
            i = 0
            return sumaUp(Array, i, j+1)
      elif(Array[i][j] == Array[i+1][j] or Array[i+1][j] == 0):
            Array[i][j] = Array[i][j] + Array[i+1][j]
            Array[i+1][j] = 0
            pushUp(Array, 0, 0, 0)
            return sumaUp(Array, i+1, j)
      else:
            return sumaUp(Array, i+1, j)
                       
#Manda los 0s del Array hacia abajo(Para hacer suma hacia arriba)
def pushUp(Array, i, j, x):
      if(x == 3):
            if(j == 3):
                  return Array
            else:
                  x = 0
                  i = 0
                  return pushUp(Array, i, j+1, x)
      elif(i == 3):
            i = 0
            x = x+1
            return pushUp(Array, i, j, x)
      elif(Array[i][j] == 0):
            Array[i][j] = Array[i+1][j]
            Array[i+1][j] = 0
            return pushUp(Array, i+1, j, x)
      else:
            return pushUp(Array, i+1, j, x)




#sumaDown
def sumaDown(Array, i, j):
      pushDown(Array, 0, 0, 0)
      if(j == 3):
            if(i == -3):
                  return Array
            else:
                  if(Array[i+3][j] == Array[i+2][j]):
                        Array[i+3][j] = Array[i+3][j] + Array[i+2][j]
                        Array[i+2][j] = 0
                        pushDown(Array, 0, 0, 0)
                        return sumaDown(Array, i-1, j)
                  else:
                        return sumaDown(Array, i-1, j)
      elif(i == -3):
            i = 0
            return sumaDown(Array, i, j+1)
      elif(Array[i+3][j] == Array[i+2][j] or Array[i+2][j] == 0):
            Array[i+3][j] = Array[i+3][j] + Array[i+2][j]
            Array[i+2][j] = 0
            pushDown(Array, 0, 0, 0)
            return sumaDown(Array, i-1, j)
      else:
            return sumaDown(Array, i-1, j)

            

#pushDown
def pushDown(Array, i, j, x):
      if(x == 3):
            if(j == 3):
                  return Array
            else:
                  x = 0
                  i = 0
                  return pushDown(Array, i, j+1, x)
      if(i == -3):
            i = 0
            x = x+1
            return pushDown(Array, i, j, x)
      if(Array[i+3][j] == 0):
            Array[i+3][j] = Array[i+2][j]
            Array[i+2][j] = 0
            return pushDown(Array, i-1, j, x)
      else:
            return pushDown(Array, i-1, j, x)




#sumaLeft
def sumaLeft(Array, i, j):
      pushLeft(Array, 0, 0, 0)
      if(i == 3):
            if(j == 3):
                  return Array
            else:
                  if(Array[i][j] == Array[i][j+1]):
                        Array[i][j] = Array[i][j] + Array[i][j+1]
                        Array[i][j+1] = 0
                        pushLeft(Array, 0, 0, 0)
                        return sumaLeft(Array, i, j+1)
                  else:
                        return sumaLeft(Array, i, j+1)
      elif(j == 3):
            j = 0
            return sumaLeft(Array, i+1, j)
      elif(Array[i][j] == Array[i][j+1] or Array[i][j+1] == 0):
            Array[i][j] = Array[i][j] + Array[i][j+1]
            Array[i][j+1] = 0
            pushLeft(Array, 0, 0, 0)
            return sumaLeft(Array, i, j+1)
      else:
            return sumaLeft(Array, i, j+1)

            
      
#pushLeft
def pushLeft(Array, i, j, x):
      if(x == 3):
            if(i == 3):
                  return Array
            else:
                  x = 0
                  j = 0
                  return pushLeft(Array, i+1, j, x)
      if(j == 3):
            j = 0
            x = x+1
            return pushLeft(Array, i, j, x)
      if(Array[i][j] == 0):
            Array[i][j] = Array[i][j+1]
            Array[i][j+1] = 0
            return pushLeft(Array, i, j+1, x)
      else:
            return pushLeft(Array, i, j+1, x)

      



#sumaRight
def sumaRight(Array, i, j):
      pushRight(Array, 0, 0, 0)
      if(i == 3):
            if(j == -3):
                  return Array
            else:
                  if(Array[i][j+3] == Array[i][j+2]):
                        Array[i][j+3] = Array[i][j+3] + Array[i][j+2]
                        Array[i][j+2] = 0
                        pushRight(Array, 0, 0, 0)
                        return sumaRight(Array, i, j-1)
                  else:
                        return sumaRight(Array, i, j-1)
      elif(j == -3):
            j = 0
            return sumaRight(Array, i+1, j)
      elif(Array[i][j+3] == Array[i][j+2] or Array[i][j+2] == 0):
            Array[i][j+3] = Array[i][j+3] + Array[i][j+2]
            Array[i][j+2] = 0
            pushRight(Array, 0, 0, 0)
            return sumaRight(Array, i, j-1)
      else:
            return sumaRight(Array, i, j-1)
            


#pushRight
def pushRight(Array, i, j, x):
      if(x == 3):
            if(i == 3):
                  return Array
            else:
                  x = 0
                  j = 0
                  return pushRight(Array, i+1, j, x)
      if(j == -3):
            j = 0
            x = x+1
            return pushRight(Array, i, j, x)
      if(Array[i][j+3] == 0):
            Array[i][j+3] = Array[i][j+2]
            Array[i][j+2] = 0
            return pushRight(Array, i, j-1, x)
      else:
            return pushRight(Array, i, j-1, x)


