//Método numérico: Método de la bisección
//Autor: Oscar Eduardo Carranza Salazar

#include <stdio.h>
#include <math.h>

void Biseccion(double a, double b, double toleranciaAbs);
double Funcion(double num);

int main() {
	Biseccion(0, 5, 0.007);
	return 0;
}


void Biseccion(double a, double b, double toleranciaAbs){
	//Método de Bisección
	double funcA= Funcion(a); //obtengo el valor de la función valuada en "a"
	double funcB= Funcion(b); ////obtengo el valor de la función valuada en "b"
	if(funcA>0){
		//Dado que F(a)*F(b)<0    donde F(a) es negativo y F(b) es positivo
		//Si no coincide este orden, entonces solo los intercambio y sigo normal
		double aux=funcA;
		funcA=funcB;
		funcA=aux;
	}
	
	double raizValuada=0;
	double errAbs=1000; //Error absoluto
	double nuevaRaiz=0;
	int banderaA=0; //inicializada en FALSE, me indica si se cambio límite "a"

	//primera iteración
	//No compararé con nada, pues apenas es mi primer iteración
	nuevaRaiz=(a+b)/2;
	raizValuada=Funcion(nuevaRaiz);
	if(raizValuada<0){
		a=nuevaRaiz;
		banderaA=1; //TRUE
	}
	else{
		b=nuevaRaiz;
		banderaA=0; //FALSE
	}
	while(toleranciaAbs<errAbs){
		nuevaRaiz=(a+b)/2;	
		raizValuada=Funcion(nuevaRaiz);
		if(raizValuada<0){				
			a=nuevaRaiz;
			banderaA=1; //TRUE
		}	
		else{
			b=nuevaRaiz;
			banderaA=0; //FALSE
		}
		if(banderaA){
			//se cambio valor de "a"
			errAbs=fabs(nuevaRaiz-b);
		}
		else{
			//se cambio valor de "b"
			errAbs=fabs(nuevaRaiz-a);
		}
	}
	double raiz=nuevaRaiz;
	printf("la raíz de tu función es: %f", raiz);
}



double Funcion(double x){
	//la función f(x) es valuada en el número "num"
	//debo declarar aquí la función cuya raíz quiero determinar
	return ((x*exp(x))-1);
}

