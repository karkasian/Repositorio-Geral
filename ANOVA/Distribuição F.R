#ANOVA: Distribuições - Distribuição F
#Desenvolvido por:     Jhordan Silveira de Borba
#E-mail:               jhordandecacapava@gmail.com
#Website:              https://sapogithub.github.io
#Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/ANOVA
#2018

#Função para gerar uma distribuição qui quadrado
qui<-function(pt,gl){
	#pt	- Quantidade de pontos
	#gl	- Graus de liberdade
	qui<-0	# Onde vamos guardar a distribuição
	
	for (x in 1:gl){			#Vamos somar as amostras retiradas da normal
		qui<-qui+(rnorm(pt)^2)
	}
	return (qui)				#E retornamos a amostra

}

#Função para gerar a distribuição F
distribuicao <-function(a){
	#a			- Nivel de significância

	pt<-1000000	#Quantidade de pontos
	fx<-100000	#Quantidade de faixas de valores
	gln<-2		#Graus de liberdade do numerador
	gld<-12		#Graus de liberdade do numerador

	num<-qui(pt,gln)/gln	#Dividimos a distribuição pelo grau de liberdade do numerador
	den<-qui(pt,gld)/gld	#Dividimos a distribuição pelo grau de liberdade do numerador

	#E salvar então nossa distribuição F final
	F<-num/den

	par(mfrow=c(3,1))			#Para plotar em uma matriz 2x2

	#Vamos plotar os gráficos
	hist(num,breaks=100,xlim=c(0,5),main="Distribuição qui-quadrado do numerador normalizado pelo grau de liberdade",freq=FALSE)
	hist(den,breaks=100,main="Distribuição qui-quadrado do denominador normalizado pelo grau de liberdade",freq=FALSE)
	hist(F,breaks=1000,xlim=c(0,6),main="Distribuição F",freq=FALSE) #Configuramos pra não mostrar a frequência, mas a densidade

	dis<-hist(F,breaks=fx, plot=FALSE)	#Vamos gerar a distribuição de frequências


	delta<-dis$breaks[2]			#Nosso delta
	pa<-0					#Probabilidade acumulada
	for (k in length(dis$density):1){	#Vamos percorrer da extrema direita pra esquerda
		pa<-pa+dis$density[k]*delta	#Salvamos a probabilidade
		if (pa>=a){			#Se tem mais ou igual ao defido
		return (dis$breaks[k])		#Retornamos o valor
		}
	}
}

#crit <-distribuicao(0.05)
#cat("Fc =",crit)
#cat("\n")


