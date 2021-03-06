#ANOVA: Estat�stica B�sica
#Desenvolvido por:     Jhordan Silveira de Borba
#E-mail:               jhordandecacapava@gmail.com
#Website:              https://sapogithub.github.io
#Mais informa��es:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/ANOVA
#2018

#Fun��o para criar uma com a distribui��o de frequencias
#Equivalente: table(), acessa os valores por as.vector() e os nomes por names()
freq <- function(v){
	#v	- Conjunto de dados
	ord <- sort(v)			#Primeiro ordenamos o vetor
	tab <- c()			#Vamos criar nosso vetor
	tam<-length(v)			#Quantidade de valores
	ant <- 0			#Vari�vel pra guardar o valor anterior
	con<-1				#Vari�vel pra contar quantes vezes o valor se repetiu
	prim<-TRUE			#Vari�vel pra indicar que estamos no primeiro valor
	for (k in 1:(tam+1)){		
		if (prim==TRUE){	#Se � o primeiro loop
			ant<-ord[k]	#Salvamos o valor
			prim<-FALSE	#E anotamos que vamos pro segundo valor
		}	
		else if(ord[k]==ant && k<(tam+1)){	#Se n�o �, e n�o � o �ltimo valor, verificamos se o valor � igual ao anterior
			con<-con+1			#Se � igual, aumentamos a contagem
		}
		else
		{			#Se � um novo valor
			tab<-c(tab,ord[k-1])		#Adicionamos o valor
			tab<-c(tab,con)			#Quantas vezes se repetiu o valor
			con<-1				#E retornamos a contagem para 1
			ant<-ord[k]			#E salvamos o novo valor pra recome�ar
		}
	}
	#Ent�o vamos retornar uma matriz
	return (matrix( tab,  nrow=2,  ncol=length(tab)/2))

}

#Fun��o para ordenar um vetor
#Equivalente: sort()
ord <- function(v){
	#v	- Conjunto de dados
	
	orde<-c()		#Vetor ordenado
	tam<-length(v)		#Tamanho do vetor
	add<-c()		#Elementos j� adicionados
	for (k in 1:tam){
	menor<-NULL		#Menor valor que vamos adicionar no loop
	pos<-NULL		#Posi��o que vamos adicionar no loop
		for (x in 1:tam){
			pode=TRUE				#Vari�vel pra checar se pode adicionar este valor
			if (length(add)>0){			#Se j� adicionamos alguns valores
				for (kk in add){		#Vamos percorrer os valores adicionados
					if (kk==x){pode=FALSE}	#Se o valor atual � um adicionado
				}
			}

			if (pode==TRUE){
				if (length(menor)==0){		#Se � o primeiro valor
					menor<-v[x]		#Salvamos como o menor
					pos=x			#Anotamos a posi��o
					}	
				else if (v[x]<menor){		#Se o valor atual � menor que o menor
					menor<-v[x]		#Salvamos como menor
					pos=x			#E salvamos a posi��o
					}		
			}

		}
		orde<-c(orde,menor)		#Adicionamos no vetor ordenado
		add<-c(add,pos)			#Salvamos que adicionamos esse vetor
	}
	return (orde)
}

#Fun��o para calcular a m�dia aritm�tica
#Equivalente: mean()
media_arit <- function(v){
	#v	- Conjunto de dados

	som<-0	#Vari�vel pra guardar o somat�rio
	for (x in 1:length(v)){som<-(som+v[x])}			#Somamos
	return (som/length(v))					#Retornamos o somat�rio dividido pela quantidade de elementos
	}

#Fun��o para calcular a mediana
#Equivalente: median()
medi <- function(v){
	#v	- Conjunto de dados

	ordenado<- sort(v)	#Ordenamos nosso vetor
	#Checamos se tem tamanho par, ou �mpar
	tam<-length(v)			#Quantidade de valores
	if (tam%%2!=0){			#Se o resto � diferente de 0, � �mpar
	
		return (ordenado[(tam)/2+1])	
	}
	else {
		return((ordenado[(tam)/2]+ordenado[(tam)/2+1])/2)
	}

}

#Fun��o para calcular a moda
#Equivalente: subset(table(y),table(y)==max(table(y)))
moda <- function(v){
	#v	- Conjunto de dados

	m= table(v)		#Retornamos uma matriz com a frequ�ncia de distribui��o
	maior<-0		#Para indicar o maior valor at� agora
	moda<-c()		#Para indicar nossas modas
	tam<-length(m)		#Quantidade de elementos que temos
	val=as.vector(m)	#Valores
	nom=names(m)
	#Agora precisamos
	for (k in 1:tam){
		if (val[k]>maior){		#Se nosso atual valor � maior que o que temos salvo
			moda<-nom[k]		#Salvamos o valor
			maior<-val[k]		#Salvamos o novo valor maior
		}
		else if (val[k]==maior){#Se � igual, adicionamos na moda
			moda<-c(moda,nom[k])
		}
	}

	if (length(moda)==tam){return (NULL)}	#Checamos se todos os valores tem a mesma distribui��o
	else{ return (moda)}
}

#Fun��o para calcular a amplitude
#Equivalente: max()-min()
amp <-function(v){
	#v	- Conjunto de dados
	ord<-sort(v)		#ordenamos o valor
	tam<-length(ord)		#O tamanho do vetor
	return (ord[tam]-ord[1])#Retornamos o maior valor, menos o menor
}

#Fun��o para calcular a vari�ncia
#Equivalente: var()
vari<-function(v){
	#v	- Conjunto de dados
	tam<-length(v)		#Quantidade de dados em nosso vetor
	medi<-mean(v)		#Media de nossa medida
	som<-0			#Somat�rio
	for (x in v){
		som<-som+(x-medi)^2
	}
	return (som/(tam-1))	#Retornamos dividindo (n-1)

}

#Fun��o para calcular o desvio padr�o
#Equivalente: sd()
dv<-function(v){
	va<-var(v)		#Calculamos a vari�ncia
	return (va^(1/2))	#Retornamos a raiz quadrada
}

#Fun��o para calcular o coeficiente de varia��o
cv<-function(v){
	desvio<-sd(v)		#Calculamos o desvio-padr�o
	media<-mean(v)		#Calculamos a m�dia
	return ((desvio/media)*100)	#Retornamos a divis�o multiplicada por 100
}


#Vamos definir nosso vetor com as vit�rias por est�gio do NYE
ve<-c(2,-2,2,2,3,4,-1,1,4,2,3,1,-1,2,-1,4,4,2,4,1,4,1,4,1,4,4,-1,1,1,1,2,4,4,2,3,3,3,2,4,4,4,-1,-1,1,-2,1,1,-2)

Sys.setlocale(category="LC_ALL", locale = "Portuguese")		#Configura o idioma e acentos, o arquivo .R deve ser salvo com a mesma condifica��o

#Vamos printar o vetor:
cat("Vetor: ",(ve))

#Vamos printar o vetor ordenado
cat("\nOrdenado: ",ord(ve))

#Printamos as frequ�ncias
cat("\nFrequ�ncias:\n")
print(freq(ve))

#Printamos a media
cat("Media: ",media_arit(ve))

#Printamos a mediana
cat("\nMediana: ",medi(ve))

#Printamos as modas:
cat("\nModa: ")
cat(moda(ve))

#Printamos a amplitude
cat ("\nAmplitude: ",amp(ve))

#Printamos a vari�ncia
cat ("\nVari�ncia: ",vari(ve))

#Printamos a vari�ncia
cat ("\nDesio-padr�o: ",dv(ve))

#Printamos o coeficiente de varia��o
cat ("\nCoeficiente de varia��o: ",cv(ve),"%")

cat("\n")
