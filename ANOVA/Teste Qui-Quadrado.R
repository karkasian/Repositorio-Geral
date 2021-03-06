#ANOVA: Distribui��es - Teste Qui-Quadrado
#Desenvolvido por:     Jhordan Silveira de Borba
#E-mail:               jhordandecacapava@gmail.com
#Website:              https://sapogithub.github.io
#Mais informa��es:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/ANOVA
#2018

#Equivalente em R para realizar o teste qui-quadrado: chisq.test()

#Fun��o para gerar a distribui��o X� para 1 grau de liberdade
distribuicao<-function(a){
	#a	- Nivel de signific�ncia
	#Podemos confirar algumas coisas pra definir a exatid�o
	pt<-100000	#Quantidade de pontos gerados
	fx<-1000	#Quantidade de faixas de valores gerados

	dist<-(rnorm(pt)^2)			#Pegamos uma amostra de distribui��o normal com 1000 elementos elevados ao quadrado
	hist<-hist(dist,breaks=fx, plot=FALSE)#Mais importante que plotar, isso cria uma classe em R com os pontos. 
	#Em hist cont�m a largura, altura,ponto m�dio e densidade das colunas
	hist(dist,breaks=1000,xlim=c(0,4))	#Mas tamb�m podemos plotar
	delta<-hist$breaks[2]			#Nosso delta
	pa<-0					#Probabilidade acumulada
	for (k in length(hist$density):1){	#Vamos percorrer da extrema direita pra esquerda
		pa<-pa+hist$density[k]*delta	#Salvamos a probabilidade
		if (pa>=a){			#Se tem mais ou igual ao defido
		crit<-hist$breaks[k]		#Retornamos o valor
		break
		}
	}

	return(crit)
}

#Fun��o para retornar X� das amostras
qui<-function(e,o){
	#e	- Vetor com as frequ�ncias esperadas
	#o	- Vetor com as frequ�ncias observadas
	som<-0	# Somat�rio
	for (x in 1:length(e)){
		som<-som+((o[x]-e[x])^2/e[x])	#Realiza o somat�rio
	}
	return (som)
}

esp<-c(20,20)				#Vetor as frequ�ncias de Vit�rias/Derrotas esperadas
obs<-c(7,33)				#Vetor com as frequ�ncias de Vit�rias/Derrotas esperadas

meu<-qui(esp,obs)			#Retornamos o valor X� de nossa fun��o
cat("X� da minha aposta: ",meu)
tab<-distribuicao(0.05)			#Retornamos o valor tabelado
cat("\nX� cr�tico: ",tab)
if(meu>=tab){				#Se o valor da nossa fun��o � maior ou igual
	cat("\nH0 rejeitada.")		#Rejeitamos a hip�tese nula
} else {
	cat("\nH1 Validada.")		#N�o rejeitamos a hip�tese nula
}

cat("\n")
