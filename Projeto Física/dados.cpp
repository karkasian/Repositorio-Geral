/*
PROJETO FÍSICA
Desenvolvido por:		Jhordan Silveira de Borba
E-mail:					jhordandecacapava@gmail.com
Website:				https://sapogithub.github.io
Sobre o projeto:		https://github.com/SapoGitHub/Repositorio-Geral/wiki/Projeto-Física
2018
*/

#include <stdio.h>		//Biblioteca padrão para comandos de entrada e saída
#include<math.h>		//Biblioteca com funções matemáticas
 
int main ()
{
   FILE * f;						//Declara arquivo
   float theta,v,vx,vy,x;
   f = fopen ("dados.txt","w");		//Abre arquivo
   
   v=10;
   theta=3.14/4;
   vx=v*cos(theta);
   vy=v*sin(theta);

   for (x=0;x<10;x=x+0.1)				//Vamos gerar dados
   {
									//Função do MRU
 	  	fprintf(f,"\n");		//Salvar no arquivo
 	  	printf("%f \n",x);
   	if (x!=10-1)
	   {
   			fprintf(f,"\n");
	   }
   }   
   fclose (f);						//Fechar o arquivo
   return 0;
}
