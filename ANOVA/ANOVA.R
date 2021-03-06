#ANOVA: ANOVA
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

#Vamos salvar o valor m�dio de cada grupo e a m�dia das m�dias
m1<-mean(per1)			#M�dia do grupo 1
m2<-mean(per2)			#M�dia do grupo 2
m3<-mean(per3)			#M�dia do grupo 3
m<-c(m1,m2,m3)			#Vetor com as m�dias
gm<-mean(m)			#Grande m�dia

#Calcular a vari�ncia entre os grupos
som<-0				#Somat�rio
for (x in m){
	som<-som+5*(x-gm)^2	#Todos nossos grupos tem o mesmo tamanho: 5
}
entre<-som/2			#2 graus de liberdade

#Calcular a vari�ncia dentro dos  grupos
som<-0				#Somat�rio
#Somat�rio do grupo 1
for (x in per1){
	som<-som+(x-m1)^2
}
#Somat�rio do grupo 2
for (x in per2){
	som<-som+(x-m2)^2
}
#Somat�rio do grupo 2
for (x in per3){
	som<-som+(x-m3)^2
}
dentro<-som/12			#12 graus de liberdade

F<-entre/dentro			#Valor da nossa fun��o

a<-0.05				#N�vel de signific�ncia
Fc<-distribuicao(a)		#F cr�tico


cat("A vari�ncia entre os grupos �:",entre)
cat("\nA vari�ncia dentro dos grupos �:",dentro)
cat("\nEnt�o temos F=",F)
cat("\npara um n�vel de signific�ncia",a,"o F cr�tico �",Fc,"ent�o")
if (F>=Fc){
	cat(" rejeitamos nossa hip�tese nula.")
} else {
	cat(" n�o rejeitamos nossa hip�tese nula.")

}
cat("\n")
