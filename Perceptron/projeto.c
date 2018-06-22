/*
PERCEPTRON: Projeto final
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
#include <locale.h>		//Biblioteca relacionada a localiza��o



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

//Nossa redes OR
int rede_or(float *peso,float limiar,int entradaA,int entradaB){
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

float custo (int saida[2][250],int saida_atu[2][250]){
	//saida		- Matriz com as saidas corretas
	//saida_atu	- Matriz com as saidas atuais

	float costo;	//Onde vamos armazenar o resultado da fun��o custo
	costo=0;
	int c,k;
	for (c=0;c<250;c++){
		costo=costo+pow(saida[0][c]-saida_atu[0][c], 2)+pow(saida[1][c]-saida_atu[1][c], 2);					//Calculamos todas sa�das
	}	
	return costo;	//Retornamos o resultado
}

//Fun��o para treinar a rede
float treinamento(float peso[][2], float *limiar){	
	//peso		- Matriz com os pesos das entradas dos neur�nios
	//limiar 	- Limiar de sa�da dos neur�nios
	
	int c,k,n;				//Vari�velis auxiliares
	float taxa;				//Nossa taxa de aprendizado
	float cust;				//Vamos guardar o custo
	int s_esp[2][250];		//Saidas esperadas
	int s_atu[2][250];		//Saidas atuais
	float entA[250];		//EntradaA
	float entB[250];		//EntradaB
	
	//Vamos gerar os dados de treinamento
	n=0;									//Contador
	for (c=1;c<100;c+=2){					//Variar a porcentagem de comida de 1 at� 100%, avan�ando de 2 em 2
		for (k=1;k<10;k+=2){				//Variar o n�mero de famintos 1 at� 10, avan�ando de 2 em 2
			entA[n]=c;						//Guardamos a porcentagem atual na entrada A
			entB[n]=k;						//E o n�mero de famintos na entada B
			if (c>=50){s_esp[0][n]=-1;}		//Se a porcentagem for maior ou igual a 50, a sa�da esperada do primeiro neur�nio � -1
			else {s_esp[0][n]=1;}			//Se n�o � 1
			if (k>=5){s_esp[1][n]=1;}		//Se a quantidade de famintos � maior ou igual a 5, a sa�da esperada do segundo neur�nio � 1
			else {s_esp[1][n]=-1;}			//Se n�o � -1
			n++;							//Aumentamos o contador
		}	
	}

	//Colocamos valores iniciais para limiares e pesos
	for (c=0;c<2;c++){
		limiar[c]=1;
		for (k=0;k<2;k++){peso[c][k]=1;}
	}

	taxa=0.1;				//Definimos a taxa de aprendizado
	
    srand(time(NULL)); 		// Gera uma semente para os n�meros aleat�rios (srand) baseados no s segundos passados desde 01/01/1970 (time(NULL))
	
	//Vamos rodar uma vez todos os dados para obtermos a sa�da atual com estas entradas e pesos
	for (c=0;c<250;c++){													//Vamos adicionar uma contagem
		s_atu[0][c]=perceptron(peso[0],limiar[0],entA[c],entB[c]);			//Recebemos o valor de sa�da atual para o primeiro neur�nio	
		s_atu[1][c]=perceptron(peso[1],limiar[1],entA[c],entB[c]);			//Recebemos o valor de sa�da atual para o segundo neur�nio
	}
	
	//E ent�o vamos treinar de fato
	for (k=0;k<250000;k++){													//Vamos adicionar uma contagem
		c =rand() % 250;													//Sorteio um n�mero entre 0 e 249

		s_atu[0][c]=perceptron(peso[0],limiar[0],entA[c],entB[c]);			//Recebemos o valor de sa�da do primeiro neur�nio
		s_atu[1][c]=perceptron(peso[1],limiar[1],entA[c],entB[c]);			//Recebemos o valor de sa�da do segundo neur�nio
		
		if(s_atu[0][c]-s_esp[0][c]!=0){										//Checamos se a sa�da do primeiro neur�nio est� errada											
			peso[0][0]=peso[0][0]+taxa*s_esp[0][c]*entA[c];					//Se estiver atualizamos o primeiro peso
			peso[0][1]=peso[0][1]+taxa*s_esp[0][c]*entB[c];					//O segundo peso
			limiar[0]=limiar[0]+taxa*s_esp[0][c];							//E o limiar
		}
		
		if(s_atu[1][c]-s_esp[1][c]!=0){										//Checamos se a sa�da do segundo neur�nio est� errada	
			peso[1][0]=peso[1][0]+taxa*s_esp[1][c]*entA[c];					//Se estiver atualizamos o primeiro peso
			peso[1][1]=peso[1][1]+taxa*s_esp[1][c]*entB[c];					//O segundo peso
			limiar[1]=limiar[1]+taxa*s_esp[1][c];							//E o limiar
		}
		
		if (k==1000){														//A  cada 1000 c�lculos
			cust = custo (s_esp,s_atu);										//Calculamos o custo
			if (abs(cust)<0.1){break;}										//Se temos um erro abaixo de um valor, sa�mos do loop
			k=0;															//Zeramos novamente k
		}				
	}
	return 0;													
}

//Vamos juntar nossas redes
int rede_final(float peso[][2], float *limiar,float *peso_or,float limiar_or,int entradaA,int entradaB){
	//peso			- Matriz com os pesos das entradas dos neur�nios
	//limiar 		- Limiar de sa�da dos neur�nios
	//peso_or		- Array com os pesos das entradas do neur�nio da rede OR
	//limiar_or 	- Limiar de sa�da do neur�nio da rede OR
	//entradaA		- Primeira entrada
	//entradaB		- Segunda entrada

	
	int temp[3];		//Vari�vel para guardar os resultadods tempor�rios
	temp[0]=perceptron(peso[0],limiar[0],entradaA,entradaB);			//Recebemos o primeiro valor de sa�da atual	da nossa rede 1
	temp[1]=perceptron(peso[1],limiar[1],entradaA,entradaB);			//Recebemos o primeiro valor de sa�da atual	da nossa rede 1
	//Convertemos as sa�das -1 em 0
	if (temp[0]==-1){temp[0]=0;}
	if (temp[1]==-1){temp[1]=0;}
	temp[2]=rede_or(peso_or,limiar_or,temp[0],temp[1]); 				//Calculamos ent�o a sa�da de nossa rede
	
	return temp[2]; 													//Retornamos
	
}

//Fun��o principal
int main (){						
	 setlocale(LC_ALL, "Portuguese");		//Define o idioma como portugu�s para funcionar a acentua��o
	 		
	//Pesos e limiares das portas l�gicas
	float peso_or[2];						//Peso das duas entradas na porta NAND 
	float limiar_or;						//Limiar do neur�nio na porta NAND
	//Pesos e limiares de nossa nova rede
	float peso[2][2];						//Pesos das duas entradas nos dois neur�nios de nossa rede
	float limiar[2];						//Limiar dos dois neur�nios
	
	int ent[2],res[2];						//entradas e sa�das
	
	//Valores calculados em nosso outro c�digo	
	peso_or[0]=-0.02036;
	peso_or[1]=-0.01036;
	limiar_or= 0.030003;
	
	//Vamos treinar nossa nova rede
	treinamento (peso,limiar);
	
	//Exibir os pesos e limiares calculados
	printf("NEUR�NIO 1\n\n");
	printf("Peso A: %f\n",peso[0][0]);
	printf("Peso B: %f\n",peso[0][1]);
	printf("Limiar: %f\n",limiar[0]);
	printf("\n");
	printf("NEUR�NIO 2\n\n");
	printf("Peso A: %f\n",peso[1][0]);
	printf("Peso B: %f\n",peso[1][1]);
	printf("Limiar: %f\n",limiar[1]);
	printf("\n");
	printf("Pressione qualquer tecla para continuar");
	getchar();											//Aguarda o pressionamento de uma tecla para continuar
	
	//Vamos interagir com o resultado de nossa nova rede
	ent[0]=1;
	ent[1]=0;
	while(ent[0]!=999 && ent[1]!=999){
		system("cls");												//Limpamos a tela
		printf( "PROJETO FINAL PT I\n");
		printf("Entre com 999 como entrada para avan�ar\n\n");
		printf( "Porcentagem de aliemnto:");
	    scanf("%d",&ent[0]);										//Recebemos a entrada A
	    printf( "Quantidade de famintos:");								
	    scanf("%d",&ent[1]);										//Recebemos a entrada B
		res[0]=perceptron(peso[0],limiar[0],ent[0],ent[1]);			//Recebemos o primeiro valor de sa�da atual	
		res[1]=perceptron(peso[1],limiar[1],ent[0],ent[1]);			//Recebemos o segundo valor de sa�da atual	
		printf("Saida: %d %d\n\n",res[0],res[1]);
		printf("Pressione qualquer tecla para continuar");
		getchar();													//Consome a quebra de linha que sobrou do scanf
		getchar();													//Aguarda o pressionamento de uma tecla para continnuar
	}
	
	//Ent�o conectamos nossas redes j� treindas
	ent[0]=1;
	ent[1]=0;
	while(ent[0]!=999 && ent[1]!=999){
		system("cls");												//Limpamos a tela
		printf( "PROJETO FINAL PT II\n");
		printf("Entre com 999 como entrada para avan�ar\n\n");
		printf( "Porcentagem de alimento:");
	    scanf("%d",&ent[0]);										//Recebemos a entrada A
	    printf( "Quantidade de famintos:");								
	    scanf("%d",&ent[1]);										//Recebemos a entrada B
		res[0]=rede_final(peso,limiar,peso_or,limiar_or,ent[0],ent[1]);			//Recebemos o valor de sa�da atual	
		if (res[0]==1){printf("Saida: Produza alimento.\n\n");}
		else {printf("Saida: N�o produza alimento.\n\n");}
		printf("Pressione qualquer tecla para continuar");
		getchar();													//Consome a quebra de linha que sobrou do scanf
		getchar();													//Aguarda o pressionamento de uma tecla para continnuar
	}

}
