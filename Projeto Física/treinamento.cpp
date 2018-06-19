/*
PROJETO FÍSICA
Desenvolvido por:		Jhordan Silveira de Borba
E-mail:					jhordandecacapava@gmail.com
Website:				https://sapogithub.github.io
Sobre o projeto:		https://github.com/SapoGitHub/Repositorio-Geral/wiki/Projeto-Física
2018
*/

#include <stdio.h>		//Biblioteca padrão para comandos de entrada e saída
#include <stdlib.h>     //Propósito geral
#include<math.h>		//Funções matemáticas

//Função do nosso neurônio sigmoidal
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

//Função principal
int main ()
{
   char arq[20];					//Variável pra ler os arquivos
   int res[9000];					//Os resultados
   int c;   						//Variáveis auxiliares
   
   //VETOR DOS RESULTADOS ESPERADOS
   //Vamos montar nosso vetor dos resultados esperados
   FILE * r;	
   r = fopen ("resposta.txt","r");  				//Abre os arquivos
   c=0;												//Declara os arquivos 
   while (fgets(arq, 100, r) != NULL){				//Vamos ler linha a linha  até que não tenha mais linha a ler
	   	res[c]=atoi(arq);							//Salvamos o valor
	   	c+=1;
	}
   fclose (r);										//Fechar os arquivos

   //PRIMEIRA CADAMADA----------------------------------------------------------------------------------------------------------------------
   //A primeira camada consiste nas entradas, cada entrada é um neurônio, então temos uma camada com 2 neurônios

   float dist[9000];				//As distâncias dos inimigos
   float theta[9000];				//As variações de ângulos

   //THETA   
   FILE * t;	
   t = fopen ("theta.txt","r");						//Abre os arquivos
   c=0;												//Declara os arquivos
   
   while (fgets(arq, 100, t) != NULL){				//Vamos ler linha a linha  até que não tenha mais linha a ler
	   	theta[c]=atof(arq);							//Salvamos o valor
	   	c+=1;
	}
   fclose (t);										//Fechar os arquivos
   
   //DISTÂNCIA
   FILE * d;	
   d = fopen ("distancia.txt","r");					//Abre os arquivos
   c=0;												//Declara os arquivos
   
   while (fgets(arq, 100, d) != NULL){				//Vamos ler linha a linha  até que não tenha mais linha a ler
	   	dist[c]=atof(arq);							//Salvamos o valor
	   	c+=1;
	}
   fclose (d);										//Fechar os arquivos
   								
  //Configuração da Segunda camada--------------------------------------------------------------------------------------------------------------------
  //Vamos colocar 3 neurônios na segunda camada
  																				//São 3  porque tem 3 neurônios nessa camada
  float p12[2];    //Pesos das entradas do primeiro neurônio da segunda camada  // 2 Devido a ter 2 neurônios na primeira camada
  float p22[2];    //Pesos das entradas do segundo neurônio da segunda camada  // 2 Devido a ter 2 neurônios na primeira camada
  float p32[2];    //Pesos das entradas do terceiro neurônio da segunda camada // 2 Devido a ter 2 neurônios na primeira camada
  
  float ent2[2];   //Valores de entrada na segunda camada						 // 2 Devido a ter 2 neurônios na primeira camada
  
  float l2[3];   //Limiares dos neurônios da segunda camda						// 3 devido a ter 3 nessa camada
  
  //Vamos definir os pesos iniciais de cada neurônio
  for (c=0;c<2;c++)
  	{
	 p12[c]=1;
	 p22[c]=1;
	 p32[c]=1;
  	}
  	
  //E vamos definir os limiares dos neurônios desta camda
  for (c=0;c<1;c++)
  	{
	l2[c]=1;
  	}
  
  //Configuração da Terceira camada-------------------------------------------------------------------------------------------------------------------
  //Vamos ter um neurônio de saida nessa camada
  																				//São 1  porque tem 1 neurônios nessa camada
  float p13[3];    //Pesos das entradas do primeiro neurônio da terceira camada  // 3 Devido a ter 3 neurônios na segunda camada
 
  float ent3[3];   //Valores de entrada na terceira camada						 // 3 Devido a ter 3 neurônios na segunda camada
  
  float l3[1];   //Limiares dos neurônios da terceira camda						// 1 devido a ter 1 nessa camada
  
  //Vamos definir os pesos iniciais de cada neurônio
  for (c=0;c<3;c++)
  	{
	 p13[c]=1;
  	}
  	
  //E vamos definir os limiares dos neurônios desta camda
  for (c=0;c<1;c++)
  	{
	l3[c]=1;
  	}
  
  //RODANDO AS CAMADAS###############################################################################################################################
  //SEGUNDA CAMADA
    sigmoid (p12, ent2,l2[0],2);			//Primeiro neurônio
  	sigmoid (p22, ent2,l2[1],2);			//Segundo neurônio
  	
 //TERCEIRA CAMADA
 	sigmoid (p13, ent3,l3[0],3);			//Segundo neurônio
   
   
   return 0;
}
