/*
PERCEPTRON: Porta OR
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informa��es:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Perceptron
##2018
*/

#include <stdio.h>		//Biblioteca padr�o de entradas e sa�das
#include <stdlib.h>     //Biblioteca gen�rica, utilizada para srand, rand
#include <time.h>       //Biblioteca relacionada a data, utilizada para time
#include <math.h>		//Biblioteca com fun��es matem�ticas

//Nosso neur�nio
int perceptron(float *peso,float limiar,int entradaA,int entradaB){
	//peso		- Array com os pesos das entradas do neur�nio
	//limiar 	- Limiar de sa�da do neur�nio
	//entradaA	- Primeira entrada
	//entradaB	- Segunda entrada

	float res;	//Resultado parcial
	
	//Fun��o de ativa��o
	res=entradaA*peso[0]+entradaB*peso[1]+limiar;
	
	if (res>0){
		return 1;
	}
	else{
		return -1;
	}
}

//Nossa combina��o de redes
int por(float *peso,float limiar,int entradaA,int entradaB){
	//peso		- Array com os pesos das entradas do neur�nio
	//limiar 	- Limiar de sa�da do neur�nio
	//entradaA	- Primeira entrada
	//entradaB	- Segunda entrada
	
	int temp[2];	//Vari�vel pra guardar as sa�das tempor�rias de nossa rede;
	int saida;		//Sa�da
	
	temp[0]=perceptron(peso,limiar,entradaA,entradaA);		//Entramos duas vezes a entrada A em nosso neur�nio
	if (temp[0]==-1){temp[0]=0;}							//Nosso neur�nio retorna -1, o que equivale a 0 em nossa entrada
	temp[1]=perceptron(peso,limiar,entradaB,entradaB);		//Entramos duas vezes a entrada B em nosso neur�nio
	if (temp[1]==-1){temp[1]=0;}
	saida=perceptron(peso,limiar,temp[0],temp[1]);			//Entramos com os resultados anteriores nosso neur�nio
	if (saida==-1){saida=0;}
	
	return saida;
}

int main (){								//Fun��o principal
	float peso[2];							//Peso das duas entradas 
	float limiar;							//Limiar do neur�nio
	int ent[2],res;							//entradas
	
	//Valores calculados em nosso outro c�digo	
	peso[0]=-0.02036;
	peso[1]=-0.01036;
	limiar= 0.030003;
	
	//Intera��o	
	while(1){					//Para sair basta entrar com 99 em qualquer entrada
	system("cls");										//Limpamos a tela
	printf( "PORTA OR\n\n");
    printf( "Entrada A:");
    scanf("%d",&ent[0]);								//Recebemos a entrada A
    printf( "Entrada B:");								//Recebemos a entrada B
    scanf("%d",&ent[1]);
    res=por(peso,limiar,ent[0],ent[1]); 			//Calculamos ent�o a sa�da de nossa rede
	printf("Saida: %d\n\n",res);
	printf("Pressione qualquer tecla para continuar");
	getchar();											//Consome a quebra de linha que sobrou do scanf
	getchar();											//Aguarda o pressionamento de uma tecla para continnuar
	}	
}
