/*
PROJETO F�SICA
Desenvolvido por:		Jhordan Silveira de Borba
E-mail:					jhordandecacapava@gmail.com
Website:				https://sapogithub.github.io
Sobre o projeto:		https://github.com/SapoGitHub/Repositorio-Geral/wiki/Projeto-F�sica
2018
*/

#include <stdio.h>		//Biblioteca padr�o para comandos de entrada e sa�da
#include <stdlib.h>     //Prop�sito geral
#include<math.h>		//Fun��es matem�ticas

//Fun��o do nosso neur�nio sigmoidal
float sigmoid (float p[], float e[],float l,int n){
	//p 		- Pesos  	(w)
	//e		 	- Entradas 	(x)
	//l			- Limiar 	(bias)
	//n			- Quantidade entradas
	
	int c;
	float temp1,temp2;
	temp1=0;
	
	for (c=0;c<n;c++)
		{
		temp1= temp1+p[c]*e[c];
		}
	temp2=1/(1+expf(-temp1-l));
	return temp2;
}

//Fun��o principal
int main ()
{
   char arq[20];					//Vari�vel pra ler os arquivos
   int res[9000];					//Os resultados
   int c;   						//Vari�veis auxiliares
   
   //VETOR DOS RESULTADOS ESPERADOS
   //Vamos montar nosso vetor dos resultados esperados
   FILE * r;	
   r = fopen ("resposta.txt","r");  				//Abre os arquivos
   c=0;												//Declara os arquivos 
   while (fgets(arq, 100, r) != NULL){				//Vamos ler linha a linha  at� que n�o tenha mais linha a ler
	   	res[c]=atoi(arq);							//Salvamos o valor
	   	c+=1;
	}
   fclose (r);										//Fechar os arquivos

   //PRIMEIRA CADAMADA----------------------------------------------------------------------------------------------------------------------
   //A primeira camada consiste nas entradas, cada entrada � um neur�nio, ent�o temos uma camada com 2 neur�nios

   float dist[9000];				//As dist�ncias dos inimigos
   float theta[9000];				//As varia��es de �ngulos

   //THETA   
   FILE * t;	
   t = fopen ("theta.txt","r");						//Abre os arquivos
   c=0;												//Declara os arquivos
   
   while (fgets(arq, 100, t) != NULL){				//Vamos ler linha a linha  at� que n�o tenha mais linha a ler
	   	theta[c]=atof(arq);							//Salvamos o valor
	   	c+=1;
	}
   fclose (t);										//Fechar os arquivos
   
   //DIST�NCIA
   FILE * d;	
   d = fopen ("distancia.txt","r");					//Abre os arquivos
   c=0;												//Declara os arquivos
   
   while (fgets(arq, 100, d) != NULL){				//Vamos ler linha a linha  at� que n�o tenha mais linha a ler
	   	dist[c]=atof(arq);							//Salvamos o valor
	   	c+=1;
	}
   fclose (d);										//Fechar os arquivos
   								
  //Configura��o da Segunda camada--------------------------------------------------------------------------------------------------------------------
  //Vamos colocar 3 neur�nios na segunda camada
  																				//S�o 3  porque tem 3 neur�nios nessa camada
  float p12[2];    //Pesos das entradas do primeiro neur�nio da segunda camada  // 2 Devido a ter 2 neur�nios na primeira camada
  float p22[2];    //Pesos das entradas do segundo neur�nio da segunda camada  // 2 Devido a ter 2 neur�nios na primeira camada
  float p32[2];    //Pesos das entradas do terceiro neur�nio da segunda camada // 2 Devido a ter 2 neur�nios na primeira camada
  
  float ent2[2];   //Valores de entrada na segunda camada						 // 2 Devido a ter 2 neur�nios na primeira camada
  
  float l2[3];   //Limiares dos neur�nios da segunda camda						// 3 devido a ter 3 nessa camada
  
  //Vamos definir os pesos iniciais de cada neur�nio
  for (c=0;c<2;c++)
  	{
	 p12[c]=1;
	 p22[c]=1;
	 p32[c]=1;
  	}
  	
  //E vamos definir os limiares dos neur�nios desta camda
  for (c=0;c<1;c++)
  	{
	l2[c]=1;
  	}
  
  //Configura��o da Terceira camada-------------------------------------------------------------------------------------------------------------------
  //Vamos ter um neur�nio de saida nessa camada
  																				//S�o 1  porque tem 1 neur�nios nessa camada
  float p13[3];    //Pesos das entradas do primeiro neur�nio da terceira camada  // 3 Devido a ter 3 neur�nios na segunda camada
 
  float ent3[3];   //Valores de entrada na terceira camada						 // 3 Devido a ter 3 neur�nios na segunda camada
  
  float l3[1];   //Limiares dos neur�nios da terceira camda						// 1 devido a ter 1 nessa camada
  
  //Vamos definir os pesos iniciais de cada neur�nio
  for (c=0;c<3;c++)
  	{
	 p13[c]=1;
  	}
  	
  //E vamos definir os limiares dos neur�nios desta camda
  for (c=0;c<1;c++)
  	{
	l3[c]=1;
  	}
  
  //RODANDO AS CAMADAS###############################################################################################################################
  //SEGUNDA CAMADA
    sigmoid (p12, ent2,l2[0],2);			//Primeiro neur�nio
  	sigmoid (p22, ent2,l2[1],2);			//Segundo neur�nio
  	
 //TERCEIRA CAMADA
 	sigmoid (p13, ent3,l3[0],3);			//Segundo neur�nio
   
   
   return 0;
}
