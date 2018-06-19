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
   FILE * t;													//Declara os arquivos
   FILE * d;													
   FILE * r;													

   float theta,x,dist,conv	;									//Variáveis que vamos utilizar
   int res;
   
   t = fopen ("theta.txt","w");									//Abre os arquivos
   d = fopen ("distancia.txt","w");
   r = fopen ("resposta.txt","w");
   
   for (dist=0;dist<5;dist+=0.05)								//Vamos gerar dados variando a distância do inimigo
   {
   		for (theta=0;theta<45;theta+=0.5)						//Variar o ângulo
   		{
   			conv=(theta/180)*3.14159265359;						//Convertemos o ângulo para radianos
			x=2*(17.5)*(17.5)*cos(conv)*sin(conv)/(9.81);		//Equação que nos dá o posicionamento final
	 	  	if (abs(x-dist)<=2)									//Se a diferença é menor que 2
	 	  		{
	 	  		res=1;											//Salvamos que a atingiu
			   }
			else												//Se não é menor que 2
				{
				res=0;											//Não atingiu
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
