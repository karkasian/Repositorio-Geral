#ANOVA: Distribuições - Qui-Quadrado
#Desenvolvido por:     Jhordan Silveira de Borba
#E-mail:               jhordandecacapava@gmail.com
#Website:              https://sapogithub.github.io
#Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/ANOVA
#2018

#Função para gerar a distribuição X² para 1 grau de liberdade
distribuicao<-function(a){
	#a	- Nivel de significância


	dist<-rnorm(10000000)^2			#Pegamos uma amostra de distribuição normal com 1000 elementos elevados ao quadrado
	hist<-hist(dist,breaks=1000000)		#Mais importante que plotar, isso cria uma classe com os 10.000 pontos, dividido com largura das colunas, altura das colunas, ponto médio das colunas, e densidade
	delta<-hist$breaks[2]			#Nosso delta
	p<-1-a					#Valor que vamos procurar
	pa<-0					#Probabilidade acumulada
	for (k in 1:length(hist$density)){
		pa<-pa+hist$density[k]*delta
		if (pa>p){
		crit<-hist$breaks[k-1]		#Como isso retorna a probabilidade de termos ESSE valor ou menor, e só queremos menor, pegamos o anterior imediatamente
		break
		}
	}

	return(crit)
}


#Equivalente: chisq.test()
qui<-function(e,o){
	#e	- Vetor com os valores esperados
	#o	- Vetor com os valores observados
	ef<-table(e)	#Tabela com frequencias dos valores esperados
	of<-table(o)	#Tabela com frequência dos valores observados
	vef<-as.vector(ef)	#Frequências esperadas
	vof<-as.vector(of)	#Frequências esperadas
	som<-0	# Somatório
	for (x in 1:length(ef)){
		som<-som+((vof[x]-vef[x])^2/vef[x])
	}
	return (som)
}

apo<-c(-1,1,1,-1,-1, 1,-1,1, 1,-1)	#Vetor com minhas apostas
res<-c( 1,1,1, 1, 1,-1,-1,1,-1, 1)	

cat("X² da minha aposta: ",qui(res,apo))

cat("\nX² crítico: ",distribuicao(0.05))
