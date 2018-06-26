#ANOVA
#Desenvolvido por:     Jhordan Silveira de Borba
#E-mail:               jhordandecacapava@gmail.com
#Website:              https://sapogithub.github.io
#Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/ANOVA
#2018

#Função para criar uma com a distribuição de frequencias
#Equivalente: table(), acessa os valores por as.vector() e os nomes por names()
freq <- function(v){
	#v	- Conjunto de dados
	ord <- sort(v)			#Primeiro ordenamos o vetor
	tab <- c()			#Vamos criar nosso vetor
	tam<-length(v)			#Quantidade de valores
	ant <- 0			#Variável pra guardar o valor anterior
	con<-1				#Variável pra contar quantes vezes o valor se repetiu
	prim<-TRUE			#Variável pra indicar que estamos no primeiro valor
	for (k in 1:(tam+1)){		
		if (prim==TRUE){	#Se é o primeiro loop
			ant<-ord[k]	#Salvamos o valor
			prim<-FALSE	#E anotamos que vamos pro segundo valor
		}	
		else if(ord[k]==ant && k<(tam+1)){	#Se não é, e não é o último valor, verificamos se o valor é igual ao anterior
			con<-con+1			#Se é igual, aumentamos a contagem
		}
		else
		{			#Se é um novo valor
			tab<-c(tab,ord[k-1])		#Adicionamos o valor
			tab<-c(tab,con)			#Quantas vezes se repetiu o valor
			con<-1				#E retornamos a contagem para 1
			ant<-ord[k]			#E salvamos o novo valor pra recomeçar
		}
	}
	#Então vamos retornar uma matriz
	return (matrix( tab,  nrow=2,  ncol=length(tab)/2))

}

#Função para ordenar um vetor
#Equivalente: sort()
ord <- function(v){
	#v	- Conjunto de dados
	
	orde<-c()		#Vetor ordenado
	tam<-length(v)		#Tamanho do vetor
	add<-c()		#Elementos já adicionados
	for (k in 1:tam){
	menor<-NULL		#Menor valor que vamos adicionar no loop
	pos<-NULL		#Posição que vamos adicionar no loop
		for (x in 1:tam){
			pode=TRUE				#Variável pra checar se pode adicionar este valor
			if (length(add)>0){			#Se já adicionamos alguns valores
				for (kk in add){		#Vamos percorrer os valores adicionados
					if (kk==x){pode=FALSE}	#Se o valor atual é um adicionado
				}
			}

			if (pode==TRUE){
				if (length(menor)==0){		#Se é o primeiro valor
					menor<-v[x]		#Salvamos como o menor
					pos=x			#Anotamos a posição
					}	
				else if (v[x]<menor){		#Se o valor atual é menor que o menor
					menor<-v[x]		#Salvamos como menor
					pos=x			#E salvamos a posição
					}		
			}

		}
		orde<-c(orde,menor)		#Adicionamos no vetor ordenado
		add<-c(add,pos)			#Salvamos que adicionamos esse vetor
	}
	return (orde)
}

#Função para calcular a média aritmética
#Equivalente: mean()
media_arit <- function(v){
	#v	- Conjunto de dados

	som<-0	#Variável pra guardar o somatório
	for (x in 1:length(v)){som<-(som+v[x])}			#Somamos
	return (som/length(v))					#Retornamos o somatório dividido pela quantidade de elementos
	}

#Função para calcular a mediana
#Equivalente: median()
medi <- function(v){
	#v	- Conjunto de dados

	ordenado<- sort(v)	#Ordenamos nosso vetor
	#Checamos se tem tamanho par, ou ímpar
	tam<-length(v)			#Quantidade de valores
	if (tam%%2!=0){			#Se o resto é diferente de 0, é ímpar
	
		return (ordenado[(tam)/2+1])	
	}
	else {
		return((ordenado[(tam)/2]+ordenado[(tam)/2+1])/2)
	}

}

#Função para calcular a moda
#Equivalente: subset(table(y),table(y)==max(table(y)))
moda <- function(v){

	m= table(v)		#Retornamos uma matriz com a frequência de distribuição
	maior<-0		#Para indicar o maior valor até agora
	moda<-c()		#Para indicar nossas modas
	tam<-length(m)		#Quantidade de elementos que temos
	val=as.vector(m)	#Valores
	nom=names(m)
	#Agora precisamos
	for (k in 1:tam){
		if (val[k]>maior){		#Se nosso atual valor é maior que o que temos salvo
			moda<-nom[k]		#Salvamos o valor
			maior<-val[k]		#Salvamos o novo valor maior
		}
		else if (val[k]==maior){#Se é igual, adicionamos na moda
			moda<-c(moda,nom[k])
		}
	}

	if (length(moda)==tam){return (NULL)}	#Checamos se todos os valores tem a mesma distribuição
	else{ return (moda)}
}

#Vamos definir nosso vetor com as vitórias por estágio do NYE
ve<-c(21,25,22,15)

#Printamos a media
cat("Media: ",media_arit(ve))

cat("\nOrdenado: ",ord(ve))

#Printamos a mediana
cat("\nMediana: ",medi(ve))

#Printamos as frequências
cat("\nFrequencias:\n")
print(freq(ve))

#Printamos as modas:
cat("\nModa: ")
print(moda(ve))
cat("\n")
