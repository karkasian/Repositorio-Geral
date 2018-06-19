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
	float som,final;
	som=0;				//Somatório
	final=0;			//Resultado final
	
	for (c=0;c<n;c++)
		{
		som= som+p[c]*e[c];
		}
	final=1/(1+expf(-som-l));
	return final;
}

//Função rede
float rede(float p3[],float p2[][2],float l2[],float l3,float ent2[],float ent3[],int cam){
	//p3[]		- Pesos dos neurônios na terceira camada 	[entrada]
	//p2[][]	- Pesos dos neurônios na segunda camada 	[neuronio][entrada]
	//l2[]		- Limiar dos neurônios da segunda camada 	[neuronio]
	//l3		- Limiar dos neurônios da terceira camada 
	//ent2[]	- Entrada dos neurônios da segunda camada 	[entrada]
	//ent3[]	- Entrada dos neurônios da terceira camada 	[entrada]
	//cam		- Quantidade de neurônios na segunda camada	[camada]
	
	float final;					
	int c;
		
    //SEGUNDA CAMADA
	for (c=0;c<cam;c++)
	{
   		ent3[c]=sigmoid (p2[c], ent2,l2[c],2);			//c neurônio com 2 entradas
	}
  	
	//TERCEIRA CAMADA

 	final = sigmoid (p3,ent3,l3,cam);					//Neurônio de saída com 'cam' entradas
 	
 	return final;
}

//Função custo
float fcusto (float saida, float p3[],float p2[][2],float l2[],float l3,float ent2[], float ent3[],int cam){
	//saida		- Valores esperados para a saida
	//p3[]	- Pesos dos neurônios na terceira camada 		[entrada]
	//p2[][]	- Pesos dos neurônios na segunda camada 	[neuronio][entrada]
	//l2[]		- Limiar dos neurônios da segunda camada 	[neuronio]
	//l3		- Limiar do neurônios da camada de saída
	//ent2[]	- Entrada dos neurônios da segunda camada 	[entrada]
	//ent3[]	- Entrada dos neurônios da terceira camada 	[entrada]
	//red[]		- Configuração da rede						[camada]

	float custo, atual;							
	atual=rede(p3,p2 ,l2,l3,ent2,ent3,red);			//Valor atual fornecido pela rede
	custo= pow( saida - atual, 2)/2; 			//Função custo
	return custo;
}

//Função principal
int main ()
{
	char arq[20];									//Variável pra ler os arquivos
    int res[9000];									//Os resultados corretos
    int c,k,n,m;   										//Variáveis auxiliares
   
    //VETOR DOS RESULTADOS ESPERADOS
    //Vamos montar nosso vetor dos resultados esperados
    FILE * r;										//Declara os arquivos 
    r = fopen ("resposta.txt","r");  				//Abre o arquivo
     c=0;												
    while (fgets(arq, 100, r) != NULL){				//Vamos ler linha a linha  até que não tenha mais linha a ler
	   	res[c]=atoi(arq);							//Salvamos o valor
	   	c+=1;
	}
    fclose (r);										//Fecha o arquivo

    //PRIMEIRA CADAMADA----------------------------------------------------------------------------------------------------------------------
    //A primeira camada consiste nas entradas, cada entrada é um neurônio, então temos uma camada com 2 neurônios
    float dist[9000];								//As distâncias dos inimigos
    float theta[9000];								//As variações de ângulos

    //THETA   
    FILE * t;										//Declara o arquivo
    t = fopen ("theta.txt","r");						//Abre os arquivos
    c=0;												
   
    while (fgets(arq, 100, t) != NULL)				//Vamos ler linha a linha  até que não tenha mais linha a ler
	   	{
	    theta[c]=atof(arq);							//Salvamos o valor
	   	c+=1;
	    }
    fclose (t);										//Fechar o arquivo
   
    //DISTÂNCIA
    FILE * d;										//Declara o arquivo
    d = fopen ("distancia.txt","r");					//Abre o arquivo
    c=0;												
   
    while (fgets(arq, 100, d) != NULL)				//Vamos ler linha a linha  até que não tenha mais linha a ler
	   	{
		dist[c]=atof(arq);							//Salvamos o valor
	   	c+=1;
		}
 	fclose (d);										//Fechar o arquivo
   								
  	//Configuração da Segunda camada--------------------------------------------------------------------------------------------------------------------
   	//Vamos definir o tamanho da segunda camada
   	int cam;
   	cam=3
  
   	// Chamando a quantidade de neurônios da primeira cmaada de n1 e da segunda camada de n2
   	float p2[cam][2]; 	 //Pesos das entradas do da segunda camada  //  n2 neurônios com n1  valores devido a ter n1 neurônios na primeira camada
   	float ent2[2];  		 //Valores de entrada na segunda camada		// n1 Devido a ter n1 neurônios na primeira camada
   	float l2[cam];  		 //Limiares dos neurônios da segunda camda	// n2 devido a ter n2 nessa camada

   	//Configuração da Terceira camada-------------------------------------------------------------------------------------------------------------------
   	//Vamos ter um neurônio de saida nessa camada
    float p3[cam];	 //Os peses das entradas do neurônio    
    float l3; 		 //O limiar
	float ent3[cam];	//As entradas

    //Valores iniciais
    //Primeira camada
    //Vamos definir os pesos iniciais de cada neurônio
  
    //Segunda camada
	  	for (c=0;c<cam;c++)
	  	{
	  		//Os pesos
	  		for (k=0;k<2;k++)
	  		{
	  		p2[c][k]=1;	
			}
			//Os limiares
			l2[c]=1;
			//E o peso da tareceira camada
			p3[c]=1;	
	  	}
    
  	//E vamos definir os limiares do neurônio da camada de saída
	l3=1;
  
  	//RODANDO AS CAMADAS###############################################################################################################################
  	float saida;
  	m=0;
  	for (n=0;n<9001;n++)
		{
	  	ent2[0]=dist[n];
	  	ent2[1]=theta[n];
	  	saida=res[n];   
	  
 		//Atualizar os valores###############################################################################
	 	float custovelho,custonovo,temp,h,taxa;
	 	h=0.0001;
	 	taxa=0.001;
	  	//precisamos agora aplicar um método numérico para encontrar o gradiente da função custo
  	 	//f'(x)=[f(x+h)-f(x)]/h  
  	  
	  	custovelho=fcusto(saida, p3,p2,l2,l3,ent2,ent3,cam);	  

	 	//Terceira camada
	 	//Pesos
	 	for (c=0;c<cam;c++)
			{
	  		//Terceira camada
	  		temp=p3[c];
	  		p3[c]=p3[c]+h;
	  		custonovo=fcusto(saida, p3,p2,l2,l3,ent2,ent3,cam);
	  		p3[c]=temp;
	  		p3[c]=p3[c]-taxa*(custonovo-custovelho)/h;
	  
	  		//Segunda camada
	  		//Pesos
	  		for (k=0;k<2;k++)
	 			{
	 			temp=p2[c][k];
				p2[c][k]=p2[c][k]+h;
				custonovo=fcusto(saida, p3,p2,l2,l3,ent2,ent3,red);
				p2[c][k]=temp;
				p2[c][k]=p2[c][k]-taxa*(custonovo-custovelho)/h;
		 		}		
		 	//Limiar
	  		temp=l2[c];
	  		l2[c]=l2[c]+h;
	  		custonovo=fcusto(saida, p3,p2,l2,l3,ent2,ent3,red);
	  		l2[c]=temp;
	  		l2[c]=l2[c]-taxa*(custonovo-custovelho)/h;
	 		}	
	  
		//Limiar da terceira camada
	  	temp=l3;
	  	l3=l3+h;
	  	custonovo=fcusto(saida, p3,p2,l2,l3,ent2,ent3,cam);
	  	l3=temp;
	  	l3=l3-taxa*(custonovo-custovelho)/h;

	  	if(n==9000)
	   		{
	   		if (m<10000)
	   			{
	   			n=0;
	   			m=m+1;
	   			printf("%f \n",custovelho);
	   			
	   			//Escrever no arquivo
	   			FILE * s;
				s = fopen ("Treino.txt","w");
				for (c=0;c<red[1];c++)
					{
				 	fprintf(s,"p3[ %d ]: %f\n",c,p3[c]);
				  	fprintf(s,"l2 [ %d ]: %f\n",c,l2[c]);
				  	for (k=0;k<red[0];k++)
				  		{
				  		fprintf(s,"p2[%d][%d]: %f\n",c,k,p2[k][c]);
						}
				  	}		
				fprintf(s,"l3: %f\n",l3);
				fclose (s);		
			   }   	
	   	}	
	}
   	return 0;
}
