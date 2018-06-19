/*
PROJETO F�SICA
Desenvolvido por:		Jhordan Silveira de Borba
E-mail:					jhordandecacapava@gmail.com
Website:				https://sapogithub.github.io
Sobre o projeto:		https://github.com/SapoGitHub/Repositorio-Geral/wiki/Projeto-F�sica
2018
*/
#include <stdio.h>		//Biblioteca padr�o para comandos de entrada e sa�da
#include<math.h>		//Biblioteca com fun��es matem�ticas
 
int main ()
{
   FILE * t;													//Declara os arquivos
   FILE * d;													
   FILE * r;													

   float theta,x,dist,conv	;									//Vari�veis que vamos utilizar
   int res;
   
   t = fopen ("theta.txt","w");									//Abre os arquivos
   d = fopen ("distancia.txt","w");
   r = fopen ("resposta.txt","w");
   
   for (dist=0;dist<5;dist+=0.05)								//Vamos gerar dados variando a dist�ncia do inimigo
   {
   		for (theta=0;theta<45;theta+=0.5)						//Variar o �ngulo
   		{
   			conv=(theta/180)*3.14159265359;						//Convertemos o �ngulo para radianos
			x=2*(17.5)*(17.5)*cos(conv)*sin(conv)/(9.81);		//Equa��o que nos d� o posicionamento final
	 	  	if (abs(x-dist)<=2)									//Se a diferen�a � menor que 2
	 	  		{
	 	  		res=1;											//Salvamos que a atingiu
			   }
			else												//Se n�o � menor que 2
				{
				res=0;											//N�o atingiu
				} 	  	
				
			fprintf(t,"%f\n",theta);				//Salvar nos arquivos
			fprintf(d,"%f\n",dist);
			fprintf(r,"%d\n",res);				
		}
	}   
	
   fclose (t);													//Fechar os arquivos
   fclose (d);	
   fclose (r);	

   return 0;
}
