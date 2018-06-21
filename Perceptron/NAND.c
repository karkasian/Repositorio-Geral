/*
PERCEPTRON: Porta NAND
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informa��es:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Perceptron
##2018
*/

#include <stdio.h>		//Biblioteca padr�o de entradas e sa�das
int perceptron(float *peso,float limiar,int entradaA,int entradaB){
	//peso		- Array com os pesos das entradas do neur�nio
	//limiar 	- Limiar de sa�da do neur�nio
	//entradaA	- Primeira entrada
	//entradaB	- Segunda entrada

	float res;		//Resultado parcial
	
	//Fun��o de ativa��o
	res=entradaA*peso[0]+entradaB*peso[1]+limiar;
	
	if (res>0){
		return 1;
	}
	else{
		return 0;
	}
	
	
}

float treinamento(float *peso, float limiar){	//Fun��o para treinar a rede
	//peso		- Array com os pesos das entradas do neur�nio
	//limiar 	- Limiar de sa�da do neur�nio

	int c,k;				//Vari�velis auxiliares
	int res;				//Resultado de saida
	
	//Vamos gerar os dados de treinamento
	int entradaA[4];		//Entrada A
	int entradaB[4];		//Entrada B
	int saida[4];			//Saida
	
	//TABELA VERDADE	
	entradaA[0]=0;	entradaB[0]=0;	saida[0]=1;
	entradaA[1]=0;	entradaB[1]=1;	saida[1]=1;
	entradaA[2]=1;	entradaB[2]=0;	saida[2]=1;
	entradaA[3]=1;	entradaB[2]=1;	saida[3]=0;
	
	//Colocamos valores iniciais
	peso[0]=1;
	peso[1]=1;
	limiar=1;
	
	for (c=0;c<1000;c++){														//Vamos treinar o conjunto de dados por c vezes
		for (k=0;k<4;k++){														//O conjunto tem 4 dados
			res=perceptron(peso,limiar,entradaA[k],entradaB[k]);				//Recebemos o valor de sa�da atual
			
		}

	}
	
	return limiar;
}


int main (){				//Fun��o principal
	float peso[2];			//Peso das duas entradas 
	float limiar;			//Limiar do neur�nio
	limiar = treinamento(peso,limiar);		//Vamos primeiro treinar a rede
	
	printf("Peso A: %f\n",peso[0]);
	printf("Peso B: %f\n",peso[1]);
	printf("Limiar: %f\n",limiar);
	
}
