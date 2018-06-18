/*
PROJETO FÍSICA
Desenvolvido por:		Jhordan Silveira de Borba
E-mail:					jhordandecacapava@gmail.com
Website:				https://sapogithub.github.io
Sobre o projeto:		https://github.com/SapoGitHub/Repositorio-Geral/wiki/Projeto-Física
2018
*/

#include <stdio.h>
 
int main ()
{
   FILE * f;						//Declara arquivo
   int vel,x,c;
   long int t,quant;
   vel=10;							//Velocidade
   quant=100000;					//Quantidade de dados a serem gerados
   f = fopen ("dados.txt","w");		//Abre arquivo
	c=0;
   for (t=101;t<101+quant;t++)	//Vamos gerar dados
   {
  	x=vel*t;						//Função do MRU
 	  	fprintf(f,"%d\n%d",x,t);		//Salvar no arquivo
   	if (t!=101+quant-1){
   		fprintf(f,"\n");
	   }
   }
   
   fclose (f);						//Fechar o arquivo
   return 0;
}
