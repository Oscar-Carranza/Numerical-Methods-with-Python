#Integración numérica usando la Cuadratura de Gauss
#Autor: Oscar Carranza

#La integral definida de 'a' hasta 'b' de una función f(x)
#puede aproximarse (numericamente) como: ((b-a)/2)*(suma desde i=1 hasta n de: wi*f(ti))

#donde: wi es el peso o valor de la cuadratura gaussiana
# ti: (xi*(b-a) +a +b)/2

#Existen tablas para aproximar cada vez más al valor de la integral
#siendo entre más grande 'n' mejor la aproximación, yo voy a proponer que n=6 y me fijo en las wi

w=[0.1713245, 0.3607616, 0.4679139, 0.4679139, 0.3607616, 0.1713245]
x=[-0.93246514, -0.661209386, -0.238619186, 0.238619186, 0.661209386, 0.93246514]

def obtenerTi(xi, a, b):
	#Obtengo el valor ti correspondiente a cada i
	ti=xi*(a-b)+a+b
	ti=ti/2
	return ti

def fun(x):
	#Aquí escribo la función que quiero integrar
	import math as mt
	fx=mt.exp(pow(x, 2)) #Esta función es la que quiero integrar
	return fx


def cuadraturaGaussiana(a, b):
	#'a' y 'b' son los limites de integración
	mult=(b-a)/2
	suma=0
	for i in range(0, 6):
		ti=obtenerTi(x[i], a, b)
		suma+=w[i]*fun(ti)
	intDefinida=mult*suma
	print("La integral definida desde {} hasta {} es: {}".format(a, b, intDefinida))


#INICIO
print("***INTEGRACION POR CUADRATURA GAUSSIANA***")
print("Código desarrollado por Oscar Carranza")
print("Fuente: Chapra, S., Canale, R. (2007). MÉTODOS NUMÉRICOS PARA INGENIEROS. McGrawHill. México.")
print()
a=float(input("Dame el límite de integración 'a': "))
b=float(input("Dame el límite de integración 'b': "))
print()
cuadraturaGaussiana(a, b)
#FIN

#Recordar que este es un método numérico donde consideré n=6
#Si quiero que el error disminuya debo modificar los datos de los vectores 'w' y 'x'
#Consultar en las fuentes correspondientes

#Checando una fuente confiable, considerando n=12 
#w=[0.24914704581, 0.24914704581, 0.23349253653, 0.23349253653, 0.20316742672, 0.20316742672, 0.16007832854, 0.16007832854, 0.10693932599, 0.10693932599, 0.04317533638, 0.04317533638]
#x=[0.1252334085, -0.1252334085, 0.36783149899, -0.36783149899, 0.58731795428, -0.58731795428, 0.76990267419, -0.76990267419, 0.9041172563, -0.9041172563, 0.98156063424, -0.9815606342]