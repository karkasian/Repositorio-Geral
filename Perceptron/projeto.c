/*
PERCEPTRON: Porta OR
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Perceptron
##2018
*/

#include <stdio.h>		//Biblioteca padrão de entradas e saídas
#include <stdlib.h>     //Biblioteca genérica, utilizada para srand, rand
#include <time.h>       //Biblioteca relacionada a data, utilizada para time
#include <math.h>		//Biblioteca com funções matemáticas

//Nosso neurônio
int perceptron(float *peso,float limiar,int entradaA,int entradaB){
	//peso		- Array com os pesos das entradas do neurônio
	//limiar 	- Limiar de saída do neurônio
	//entradaA	- Primeira entrada
	//entradaB	- Segunda entrada

	float res;	//Resultado parcial
	
	//Função de ativação
	res=entradaA*peso[0]+entradaB*peso[1]+limiar;
	
	if (res>0){
		return 1;
	}
	else{
		return -1;
	}
}

//Nossa redes OR
int rede_or(float *peso,float limiar,int entradaA,int entradaB){
	//peso		- Array com os pesos das entradas do neurônio
	//limiar 	- Limiar de saída do neurônio
	//entradaA	- Primeira entrada
	//entradaB	- Segunda entrada
	
	int temp[2];	//Variável pra guardar as saídas temporárias de nossa rede;
	int saida;		//Saída
	
	temp[0]=perceptron(peso,limiar,entradaA,entradaA);		//Entramos duas vezes a entrada A em nosso neurônio
	if (temp[0]==-1){temp[0]=0;}							//Nosso neurônio retorna -1, o que equivale a 0 em nossa entrada
	temp[1]=perceptron(peso,limiar,entradaB,entradaB);		//Entramos duas vezes a entrada B em nosso neurônio
	if (temp[1]==-1){temp[1]=0;}
	saida=perceptron(peso,limiar,temp[0],temp[1]);			//Entramos com os resultados anteriores nosso neurônio
	if (saida==-1){saida=0;}
	
	return saida;
}

float custo (int saida[2][250],int saida_atu[2][250]){
	//saida		- Array com as saidas corretas
	//peso		- Array com os pesos das entradas do neurônio
	//limiar 	- Limiar de saída do neurônio
	//entradaA	- Primeira entrada
	//entradaB	- Segunda entrada

	float costo;	//Onde vamos armazenar o resultado da função custo
	costo=0;
	int c,k;
	for (c=0;c<250;c++){
		costo=costo+pow(saida[0][c]-saida_atu[0][c], 2)+pow(saida[1][c]-saida_atu[1][c], 2);					//Calculamos todas saídas
	}	
	return costo;	//Retornamos o resultado
	
}



float treinamento(float peso[][2], float *limiar){	//Função para treinar a rede
	//peso		- Matriz com os pesos das entradas do neurônio
	//limiar 	- Limiar de saída do neurônio
	printf("%f",peso[0][0]);
	int c,k,n;				//Variávelis auxiliares
	int res;				//Resultado de saida
	float taxa;				//Nossa taxa de aprendizado
	float cust;				//Vamos guardar o custo
	int s_esp[2][250];		//Saidas esperadas
	int s_atu[2][250];		//Saidas atuais
	float entA[250];		//EntradaA
	float entB[250];		//EntradaB
	
	//Vamos gerar os dados de treinamento
	n=0;							//Contador
	for (c=1;c<100;c+=2){
		for (k=1;k<10;k+=2){
			entA[n]=c;
			entB[n]=k;
			if (c>=50){s_esp[0][n]=1;}
			else {s_esp[0][n]=-1;}
			if (k>=5){s_esp[1][n]=1;}
			else {s_esp[1][n]=-1;}
			n++;
		}	
	}

	//Colocamos valores iniciais
	for (c=0;c<2;c++){
		limiar[c]=1;
		for (k=0;k<2;k++){peso[c][k]=1;}
	}

	taxa=0.1;
	
    srand(time(NULL)); //  Gera uma semente para os números aleatórios (srand) baseados no s segundos passados desde 01/01/1970 (time(NULL))
	
	//Vamos rodar uma vez todos os dados:
	for (c=0;c<250;c++){													//Vamos adicionar uma contagem
		s_atu[0][c]=perceptron(peso[0],limiar[0],entA[c],entB[c]);			//Recebemos o valor de saída atual	
		s_atu[1][c]=perceptron(peso[1],limiar[1],entA[c],entB[c]);			//Recebemos o valor de saída atual	
	}
	
	//E então 
	for (k=0;k<250000;k++){													//Vamos adicionar uma contagem
		c =rand() % 250;													//Sorteio um número entre 0 e 3

		s_atu[0][c]=perceptron(peso[0],limiar[0],entA[c],entB[c]);			//Recebemos o valor de saída atual	
		s_atu[1][c]=perceptron(peso[1],limiar[1],entA[c],entB[c]);			//Recebemos o valor de saída atual	
		
		if(s_atu[0][c]-s_esp[0][c]!=0){											//Checamos se a saída está errada											
			peso[0][0]=peso[0][0]+taxa*s_esp[0][c]*entA[c];					//Se estiver atualizamos o primeiro peso
			peso[0][1]=peso[0][1]+taxa*s_esp[0][c]*entB[c];					//O segundo peso
			limiar[0]=limiar[0]+taxa*s_esp[0][c];								//E o limiar
		}
		
		if(s_atu[1][c]-s_esp[1][c]!=0){											//Checamos se a saída está errada
			peso[1][0]=peso[1][0]+taxa*s_esp[1][c]*entA[c];					//Se estiver atualizamos o primeiro peso
			peso[1][1]=peso[1][1]+taxa*s_esp[1][c]*entB[c];					//O segundo peso
			limiar[1]=limiar[1]+taxa*s_esp[1][c];								//E o limiar
		}
		
		if (k==1000){														//A  cada 10 cálculos
			cust = custo (s_esp,s_atu);	//Calculamos o custo
			printf("custo: %f\n",cust);
			if (abs(cust)<0.1){break;}										//Se temos um erro abaixo de um valor, saímos do loop
			k=0;														//Zeramos novamente c
		}				
	}
	return 0;//limiar;														//Retornamos apenas o limiar, o peso é um ponteiro, já foi alterado
}



int main (){								//Função principal
	float peso_or[2];						//Peso das duas entradas na porta NAND 
	float limiar_or;						//Limiar do neurônio na porta NAND
	float peso[2][2];						//Pesos das duas entradas nos dois neurônios
	float limiar[2];						//Limiar dos dois neurônios
	int ent[2],res[2];							//entradas
	
	//Valores calculados em nosso outro código	
	peso_or[0]=-0.02036;
	peso_or[1]=-0.01036;
	limiar_or= 0.030003;
	peso[0][0]=1;
	treinamento (peso,limiar);
	while(1){

	printf( "\nEntrada A:");
    scanf("%d",&ent[0]);								//Recebemos a entrada A
    printf( "Entrada B:");								//Recebemos a entrada B
    scanf("%d",&ent[1]);

	res[0]=perceptron(peso[0],limiar[0],ent[0],ent[1]);			//Recebemos o valor de saída atual	
	res[1]=perceptron(peso[1],limiar[1],ent[0],ent[1]);			//Recebemos o valor de saída atual	
	printf("Saida: %d %d\n\n",res[0],res[1]);
	}
	
}
