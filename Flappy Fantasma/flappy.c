/*
Flappy Fantasma
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informa��es:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Flappy-Fantasma
##2018
*/

#include <stdio.h>		//Biblioteca padr�o de entradas e sa�das
#include <stdlib.h>     //Biblioteca gen�rica, utilizada para srand, rand
#include <time.h>       //Biblioteca relacionada a data, utilizada para time
#include <math.h>		//Biblioteca com fun��es matem�ticas
#include <locale.h>		//Biblioteca relacionada a localiza��o

//Nosso neur�nio
int perceptron(float *peso,float limiar,float entradaA,float entradaB){
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

//Fun��o custo
float custo_nand (int *saida, int *atu){
	//saida		- Array com as saidas corretas
	//peso		- Array com os pesos das entradas do neur�nio
	//limiar 	- Limiar de sa�da do neur�nio
	//entradaA	- Primeira entrada
	//entradaB	- Segunda entrada

	int c;			//Vari�vei auxiliar
	float custo;	//Onde vamos armazenar o resultado da fun��o custo
	
	custo=0;
	
	for (c=0;c<100;c++){custo=custo+pow(atu[c]-saida[c], 2);	}	//Fun��o custo
	
	return custo;	//Retornamos o resultado
}

float treinamento_nand(float *peso, float limiar){	//Fun��o para treinar a rede
	//peso		- Array com os pesos das entradas do neur�nio
	//limiar 	- Limiar de sa�da do neur�nio

	int c,k,n;				//Vari�velis int auxiliares
	float cf,kf;			//Vari�veis float auxiliares
	float taxa;				//Nossa taxa de aprendizado
	float cust;				//Vamos guardar o custo
	
	//Vamos gerar os dados de treinamento
	float entradaA[100];		//Altura do fantasma
	float entradaB[100];		//Altura do obst�culo
	int saida[100];				//Saida esperada
	int atu[100];				//Saidas atuais
	
	n=0;								//Contador
	for (cf=0;cf<1;cf+=0.1){			//Vamos variar a altura do fantasma de 0 a 1, com intervalos de 0.1
		for (kf=0;kf<1;kf+=0.1){		//Vamos variar a altura do obst�culo de 0 a 1, com intervalos de 0.1
			entradaA[n]=cf;				//Salvamos a entrada A
			entradaB[n]=kf;				//Salvamos a entrada B
			if (cf<kf){saida[n]=1;}		//Se o fantasma est� abaixo do obst�culo, voa (1)
			else {saida[n]=-1;}			//Se n�o, n�o (-1)
		n++;							//Aumentamos o contador
		}
	}

	//Colocamos valores iniciais
	peso[0]=20;
	peso[1]=20;
	limiar=3;
	taxa=0.01;
	
	//Rodamos uma vez a rede para todas entradas para ver como est� com os valores atuais
	for (c=0;c<100;c++){
	atu[c]=perceptron(peso,limiar,entradaA[c],entradaB[c]);
	}
	
    srand(time(NULL)); //  Gera uma semente para os n�meros aleat�rios (srand) baseados no s segundos passados desde 01/01/1970 (time(NULL))
	
	//Declaramos os arquivos
	FILE *p1;
	FILE *p2;
	FILE *L;					
	//Abrimos os arquivos		
    p1 = fopen("Peso1.txt", "w");
    p2 = fopen("Peso2.txt", "w");
    L = fopen("Limiar.txt", "w");

	
	//E ent�o 																//Contador
	for (c=0;c<5000;c++){												//Vamos adicionar uma contagem
		k =rand() % 100;												//Sorteio um n�mero entre 0 e 99
		atu[k]=perceptron(peso,limiar,entradaA[k],entradaB[k]);			//Recebemos o valor de sa�da atual	
		if(atu[k]-saida[k]!=0){											//Checamos se a sa�da est� errada											
			peso[0]=peso[0]+taxa*saida[k]*entradaA[k];					//Se estiver atualizamos o primeiro peso
			peso[1]=peso[1]+taxa*saida[k]*entradaB[k];					//O segundo peso
			limiar=limiar+taxa*saida[k];								//E o limiar
		}
		
		if (c==4000){													//A  cada 4000 c�lculos
			//Salvamos nos arquivos
			fprintf(p1, "%f\n",peso[0]);
			fprintf(p2, "%f\n",peso[1]);
			fprintf(L, "%f\n",limiar);									
			cust = custo_nand (saida,atu);								//Calculamos o custo
			if (cust<0.1){break;}										//Se temos um erro abaixo de um valor, sa�mos do loop
			c=0;														//Zeramos novamente c
		}																//Adicionamos valor ao contador			
	}
	//Fechamos os arquivos
	fclose(p1);
	fclose(p2);
	fclose(L);
	return limiar;														//Retornamos apenas o limiar, o peso � um ponteiro, j� foi alterado
}


int main (){								//Fun��o principal
	 setlocale(LC_ALL, "Portuguese");		//Define o idioma como portugu�s para funcionar a acentua��o
	float peso[2];							//Peso das duas entradas 
	float limiar;							//Limiar do neur�nio
	float ent[2],res[2];					//entradas
	float peso_ale[2];						//Os pesos rede do Alexandre
	float limiar_ale;						//Limiar da rede do Alexandre
	
	//Pesos e limiares informados pelo Alexandre
	peso_ale[0]=-1;						
	peso_ale[1]=0.9316424;
	limiar_ale= -0.7005109;
		
	limiar = treinamento_nand(peso,limiar);		//Vamos primeiro treinar a rede do NAND
	
	//Exibir os pesos e limiares calculados
	printf("NEUR�NIO\n\n");
	printf("Peso A: %f\n",peso[0]);
	printf("Peso B: %f\n",peso[1]);
	printf("Limiar: %f\n",limiar);
	printf("\n\n");
	printf("Pressione qualquer tecla para continuar");
	getchar();											//Aguarda o pressionamento de uma tecla para continuar
	
	//Intera��o	
	while(1){	
	system("cls");										//Limpamos a tela
	printf( "FLAPPY FANTASMA\n\n");
    printf( "Altura do fantasma:");
    scanf("%f",&ent[0]);								//Recebemos a entrada A
    printf( "Altura do obst�culo:");					//Recebemos a entrada B
    scanf("%f",&ent[1]);
    res[0]=perceptron(peso,limiar,ent[0],ent[1]); 					//Calculamos ent�o a sa�da de nossa rede
    if (res[0]==-1){printf("Saida desta rede: N�o voa\n");}			
    else {printf("Saida desta rede: Voa\n")	;}
    res[1]=perceptron(peso_ale,limiar_ale,ent[0],ent[1]); 			//Calculamos ent�o a sa�da da outra rede
    if (res[0]==-1){printf("Saida da outra rede: N�o voa\n\n");}			
    else {printf("Saida da outra rede: Voa\n\n")	;}
	printf("Pressione qualquer tecla para continuar");
	getchar();											//Consome a quebra de linha que sobrou do scanf
	getchar();											//Aguarda o pressionamento de uma tecla para continnuar
	}	
}
