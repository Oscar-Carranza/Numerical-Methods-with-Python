from math import log, pi, exp, cos


def f(x):
    return 9*exp(-1*x)*cos(2*pi*x) - 3

print("Método de la regla falsa para encontrar la raíz de una función\n")
print("1. Tabulación en intervalo [a, b]")

# Tabulación de valores (para encontrar cambios de signo)
while True:
    a = float(input("Ingrese el valor de a: "))
    b = float(input("Ingrese el valor de b: "))
    n = int(input("Ingrese el número de divisiones para tabular: "))

    paso = (b - a) / n # Paso en la tabulación
    print("\n")
    for i in range(n + 1):
        x = a + i * paso # Argumento en la función
        print("x: {:.8f}, f(x): {:.8f}".format(x, f(x)))

    repetir = input("¿Deseas volver a tabular? [S/n] ").lower();
    if(repetir == "n"):
        break

print("\n2. Encontrar la raíz en un intervalo [a, b]")
a = float(input("Ingrese el valor de a: "))
b = float(input("Ingrese el valor de b: "))
tol = float(input("Ingrese el valor de la tolerancia (E abs): "))

if(f(a)*f(b) >= 0):
    print("El intervalo no cumple con las condiciones del método")
    quit()

# El método per se
while True:
    x0 = b - (f(b)*(b - a))/(f(b) - f(a))
    if(abs(f(x0)) <= tol): # Cumple el valor con la tolerancia
        break

    if(f(x0)*f(b) < 0):
        a = x0
    else:
        b = x0

print("\nLa raíz de f(x) es: {:.12f}".format(x0))