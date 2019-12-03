from sympy import *

x = Symbol('x')

f = 9*exp(-1*x)*cos(2*pi*x) - 3 # Función a encontrar raíz

df = diff(f, x) # Primera derivada
d2f = diff(df, x) # Segunda derivada

print("Método de Newton-Raphson\n")
print("1. Tabulación a partir de un punto 'a'")

# Tabulación de valores para encontrar cambio de signo
while True:
    a = float(input("Ingrese el valor de a: "))
    paso = float(input("Ingrese la cantidad de paso para cada tabulación: "))
    n = int(input("Ingrese el número de pasos: "))

    for i in range(n + 1):
        xi = a + i * paso # Argumento en la función
        print("x: {0:.8f}, f(x): {1}".format(xi, f.subs(x, xi).evalf()))

    repetir = input("¿Deseas volver a tabular? [S/n] ").lower();
    if(repetir == "n"):
        break

print("\n2. Raíz a partir de aproximación")
x0 = float(input("Ingrese el valor de aproximación (x0): "))
tol = float(input("Ingrese el valor de la tolerancia (E abs): "))

# Criterio de convergencia
dg = Abs((f*d2f)/Pow(df, 2))
if(dg.subs(x, x0).evalf() > 1):
    print("El método no converge para x0")
    quit()

# El método per se
while True:
    xn = x0 - (f.subs(x, x0).evalf())/(df.subs(x, x0).evalf())
    x0 = xn

    if(Abs(f.subs(x, xn)).evalf() < tol):
        break

print("\nLa raíz de f(x) es: {0}".format(xn))