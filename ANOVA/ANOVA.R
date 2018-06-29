#ANOVA: Distribuições - ANOVA
#Desenvolvido por:     Jhordan Silveira de Borba
#E-mail:               jhordandecacapava@gmail.com
#Website:              https://sapogithub.github.io
#Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/ANOVA
#2018

#Equivalente em R para realizar o teste ANOVA: aov()

source("C:\\wamp64\\www\\GitHub\\Repositorio-Geral\\ANOVA\\Distribuição F.R")	#Carregamos o código escrito para calcular o F crítico

#Vamos salvar os nossos dados a serem analisados:
per1<-c(1,2,4,4,2)		#Período 1
per2<-c(3,2,4,4,4)		#Período 2
per3<-c(-1,-1,1,-2,1)		#Período 3

#EXWMPLO
per1<-c(254,263,241,237,251)		#Período 1
per2<-c(234,218,235,227,216)		#Período 2
per3<-c(200,222,197,206,204)		#Período 3

#Vamos salvar o valor médio de cada grupo e a média das médias
m1<-mean(per1)			#Média do grupo 1
m2<-mean(per2)			#Média do grupo 2
m3<-mean(per3)			#Média do grupo 3
m<-c(m1,m2,m3)			#Vetor com as médias
gm<-mean(m)			#Grande média

#Calcular o valor entre os grupos
som<-0				#Somatório
for (x in m){
	som<-som+5*(x-gm)^2	#Todos nossos grupos tem o mesmo tamanho: 5
}
entre=som/2


