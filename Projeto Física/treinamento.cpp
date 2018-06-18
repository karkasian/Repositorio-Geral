/*
PROJETO FÍSICA
Desenvolvido por:		Jhordan Silveira de Borba
E-mail:					jhordandecacapava@gmail.com
Website:				https://sapogithub.github.io
Sobre o projeto:		https://github.com/SapoGitHub/Repositorio-Geral/wiki/Projeto-Física
2018
*/

#include <stdio.h>		//Biblioteca padrão para comandos de entrada e saída
#include <stdlib.h>     /* atoi */
int main ()
{
   char arq[10];					//Variável pra ler o arquivo
   int x[100];						//As posições
   int t[100];						//Respectivos tempos
   int c,k;   						//Variáveis auxiliares
   
   //Vamos ler o arquivo com os dados para treinamento
   FILE * f;						//Declara arquivo
   f = fopen ("dados.txt","r");		//Abre arquivo
   c=0;
   k=0;
   while (fgets(arq, 10, f) != NULL){	//Vamos ler linha a linha  até que não tenha mais linha a ler
	   	if (c==0){
	   		x[k]=atoi(arq);				//Salvamos o valor X
	   		c=1;
		   }
		else
		{
			t[k]=atoi(arq);;			//Salvamos o valor T
			c=0;
			k+=1;
		}		
	}
   fclose (f);						//Fechar o arquivo

//for (c=0;c<100;c++)
//{
//	printf("%d\n",x[c]);
//}

   return 0;
}
