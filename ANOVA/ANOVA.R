#ANOVA: Distribui��es - ANOVA
#Desenvolvido por:     Jhordan Silveira de Borba
#E-mail:               jhordandecacapava@gmail.com
#Website:              https://sapogithub.github.io
#Mais informa��es:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/ANOVA
#2018

#Equivalente em R para realizar o teste ANOVA: aov()

source("C:\\wamp64\\www\\GitHub\\Repositorio-Geral\\ANOVA\\Distribui��o F.R")	#Carregamos o c�digo escrito para calcular o F cr�tico

#Vamos salvar os nossos dados a serem analisados:
per1<-c(1,2,4,4,2)		#Per�odo 1
per2<-c(3,2,4,4,4)		#Per�odo 2
per3<-c(-1,-1,1,-2,1)		#Per�odo 3

#EXWMPLO
per1<-c(254,263,241,237,251)		#Per�odo 1
per2<-c(234,218,235,227,216)		#Per�odo 2
per3<-c(200,222,197,206,204)		#Per�odo 3

#Vamos salvar o valor m�dio de cada grupo e a m�dia das m�dias
m1<-mean(per1)			#M�dia do grupo 1
m2<-mean(per2)			#M�dia do grupo 2
m3<-mean(per3)			#M�dia do grupo 3
m<-c(m1,m2,m3)			#Vetor com as m�dias
gm<-mean(m)			#Grande m�dia

som<-0				#Somat�rio
for (x in m){
	som<-som+5*(x-gm)^2	#Todos nossos grupos tem o mesmo tamanho: 5
}
entre=som/2