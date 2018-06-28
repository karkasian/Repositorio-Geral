#ANOVA: Distribuições - Teste Qui-Quadrado
#Desenvolvido por:     Jhordan Silveira de Borba
#E-mail:               jhordandecacapava@gmail.com
#Website:              https://sapogithub.github.io
#Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/ANOVA
#2018

#Função para gerar a distribuição X² para 1 grau de liberdade
distribuicao<-function(a){
	#a	- Nivel de significância


	dist<-(rnorm(100000)^2)			#Pegamos uma amostra de distribuição normal com 1000 elementos elevados ao quadrado
	hist<-hist(dist,breaks=1000, plot=FALSE)		#Mais importante que plotar, isso cria uma classe em R com os pontos. 
	#Em hist contém a largura, altura,ponto médio e densidade das colunas
	hist(dist,breaks=1000,xlim=c(0,4))	#Mas também podemos plotar
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


#Equivalente: chisq.test()
qui<-function(e,o){
	#e	- Vetor com as frequências esperadas
	#o	- Vetor com as frequências observadas
	som<-0	# Somatório
	for (x in 1:length(e)){
		som<-som+((o[x]-e[x])^2/e[x])	#Realiza o somatório
	}
	return (som)
}

esp<-c(20,20)				#Vetor as frequências de Vitórias/Derrotas esperadas
obs<-c(7,33)				#Vetor com as frequências de Vitórias/Derrotas esperadas

meu<-qui(esp,obs)			#Retornamos o valor X² de nossa função
cat("X² da minha aposta: ",meu)
tab<-distribuicao(0.05)			#Retornamos o valor tabelado
cat("\nX² crítico: ",tab)
if(meu>=tab){				#Se o valor da nossa função é maior ou igual
	cat("\nH0 rejeitada.")		#Rejeitamos a hipótese nula
} else {
	cat("\nH1 Validada.")		#Não rejeitamos a hipótese nula
}

cat("\n")
