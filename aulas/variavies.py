#Python Variaveis
n1 = 5

#Variavel Names 

#3myvar = 3 

#Assinando/Criando Multiplas Variaveis
x, y, z = 2, 4, 1

#Assinando/Criando Multiplas Variáveis com o mesmo valor
k = l = m = '1'

#Output Variaveis

print(x)

print(x, y, z)

print(x - y)

# Global Variaveis 

x = "awesome"

def myfunc():
  x = "fantastic"
  print("Python is " + x) 

myfunc() # "Python is fantastic"

print("Python is " + x) # "Python is awesome"


#################################################
 
 
def myfunc():
  x = "fantastic"
  print("Python is " + x) 

myfunc() # "Python is fantastic"

print("Python is " + x) # Error

#################################################

 
def myfunc():
  global x 
  x = "fantastic"
  print("Python is " + x) 

myfunc() # "Python is fantastic"

print("Python is " + x) # "Python is fantastic"