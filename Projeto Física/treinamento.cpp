/*
PROJETO F�SICA
Desenvolvido por:		Jhordan Silveira de Borba
E-mail:					jhordandecacapava@gmail.com
Website:				https://sapogithub.github.io
Sobre o projeto:		https://github.com/SapoGitHub/Repositorio-Geral/wiki/Projeto-F�sica
2018
*/

#include <stdio.h>		//Biblioteca padr�o para comandos de entrada e sa�da
#include <stdlib.h>     /* atoi */
int main ()
{
   char arq[10];					//Vari�vel pra ler o arquivo
   int x[100];						//As posi��es
   int t[100];						//Respectivos tempos
   int c,k;   						//Vari�veis auxiliares
   
   //Vamos ler o arquivo com os dados para treinamento
   FILE * f;						//Declara arquivo
   f = fopen ("dados.txt","r");		//Abre arquivo
   c=0;
   k=0;
   while (fgets(arq, 10, f) != NULL){	//Vamos ler linha a linha  at� que n�o tenha mais linha a ler
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
