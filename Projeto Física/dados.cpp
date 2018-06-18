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
   int t,vel,quant,x;
   vel=10;							//Velocidade
   quant=100;//000					//Quantidade de dados a serem gerados
   f = fopen ("dados.txt","w");		//Abre arquivo
   for (t=100;t<(100+quant);t++)	//Vamos gerar dados
   {
   	x=vel*t;						//Função do MRU
   	fprintf(f,"%d\n%d\n",x,t);		//Salvar no arquivo
   	//printf("%d\n%d\n",x,t);
   }
   fclose (f);						//Fechar o arquivo
   return 0;
}
