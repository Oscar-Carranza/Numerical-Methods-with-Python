#Codificación del método de Gauss-Seidel para resolver sistemas de ecuaciones lineales nxn
#Autor:Oscar Carranza

import numpy #Se hace uso de numpy para poder modificar vectores y matrices con mayor facilidad
import copy #Se hace uso de copy para hacer una copia del vector x como vector xAuxiliar en el método

# Se resolverá un sistema de ecuaciones lineales de la forma Ax=b, cabe resaltar que n es el orden de la matriz de coeficientes A
print('\n' +"***Solución de sistemas de ecuaciones lineales por el método de Gauss-Seidel***")
n=int(input("Dame el número de incógitas en tu sistema de ecuaciones lineales: "))
tolUsuario = float(input("Ingrese el valor de la tolerancia (E abs): "))

A = numpy.zeros((n,n)) #matriz de coeficientes
x=numpy.zeros((n)) #vector de incógnitas x1, x2, ..., xn
b=numpy.zeros((n)) #vector de términos independientes

#Entrada de coeficientes de matriz A y vector b
print ('\n' +"Ingresa los términos de la matriz de coeficientes, así como los valores del vector de términos independientes")
for i in range(0,n):
    for j in range(0,n):
        A[(i),(j)]=float(input("Elemento a["+str(i+1)+str(j+1)+"] "))
    b[(i)]=float(input("b["+str(i+1)+"]: "))

#Debo asegurarme que la matriz de coeficientes A cumpla con la condición necesaria, esta es que: abs(a ii)>abs(a ij)
    #Es decir: el elemento ubicado en la diagonal principal de cada ecuación sea mayor en valor absoluto que el resto 
    #de los elementos de la misma ecuación.
convergencia=numpy.zeros((n,n))
    #El siguiente ciclo for es para asignar con True a las posiciones ii del arreglo
for i in range(0,n):
    convergencia[(i,i)]=True #En la posición ii no habrá valores que comprobar, entonces se le pone True por defecto
    
#En el siguiente ciclo for se comparan los valores de aii con los de aij
for i in range(0,n):
    for j in range(0,n):
        if i!=j:
            if abs(A[(i),(i)]) > abs(A[(i),(j)]):
                convergencia[(i,j)]=True
            else:
                convergencia[(i,j)]=False

#El siguiente ciclo for se usa para saber si se cumple la condición necesaria
bandera=False #Me va a indicar si debo parar la ejecución del porgrama
for i in range(0,n):
    for j in range(0,n):
        #print(bool(convergencia[(i,j)]))    
        if convergencia[(i,j)]==False:
            print("El metodo no converge a la solución dado el sistema que ingresaste. Error en la ecuación: " +str(i+1))
            bandera=True #Debo finalizar programa
            break
if bandera:
    print("FIN del programa")
    input()
    exit()
    
#Ahora si comenzamos con el método de Gauss-Seidel (si el método convergió)
print('\n' +"El método va a converger a la solución, considerando la tolerancia que ingresaste")
suma=0
for i in range(0,n):
    #Ciclo iterativo para llenat vector x inicial
    for j in range(0,n):
        if i!=j:
            suma=suma+A[i,j]*x[j]
    x[i]=(b[i]-suma)/A[i,i]
    
contador=0 #número de iteraciones
error=1000*numpy.ones((n)) #Lista de los errores tras cada iteracion de las incognitas x1, x2, ..., xn
 #Se asignó 1000 como valores iniciales de error para que se pueda entrar en el siguiente ciclo while

while ((error[0] > tolUsuario) and (error[1] > tolUsuario) and (error[2] > tolUsuario)):
    contador=contador+1 #aumenta en una unidad mi variable contadora
    suma=0
    xAuxiliar=copy.deepcopy(x); #Almacena valores actuales del vector x
    for i in range(0,n):
        suma=0
        for j in range(0,n):
            if i!=j:
                suma=suma+A[i,j]*x[j]
        x[i]=(b[i]-suma)/A[i,i] #valor de las x en cada iteración 
    for k in range(0,n): #ciclo iterativo para llenar valores de lista de errores
        error[k]=abs(x[k]- xAuxiliar[k])
        

print('\n' + "Vector X solución:")
for i in range(0,n):
    print("x[" +str(i+1)+"]: " +str(x[i]))

print('\n' +"Se llegó en un total de "+str(contador)+" iteraciones")       
print('\n' +"Fin del método")
#FIN