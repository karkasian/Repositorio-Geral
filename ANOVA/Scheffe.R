#ANOVA: Teste Scheffe
#Desenvolvido por:     Jhordan Silveira de Borba
#E-mail:               jhordandecacapava@gmail.com
#Website:              https://sapogithub.github.io
#Mais informa��es:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/ANOVA
#2018

#Valores do teste ANOVA
dentro<-1.47				#Vari�ncia dentro do grupo
Fc<-3.89				#F cr�tico

#Valores
per1<-c(1,2,4,4,2)		#Per�odo 1
per2<-c(3,2,4,4,4)		#Per�odo 2
per3<-c(-1,-1,1,-2,1)		#Per�odo 3


#M�dias
m1<-mean(per1)				#M�dia do grupo 1
m2<-mean(per2)				#M�dia do grupo 2
m3<-mean(per3)				#M�dia do grupo 3
m<-c(m1,m2,m3)			#Todas m�dias

#Diferen�as absolutas entre as m�dias
tam<-length(m)				#Quantidade de m�dias
absol<-c()				#Vetor com as diferen�as absolutas das m�dias
for (x in 1:(tam-1)){			#Vamos comparar desde o primeiro com grupo, o �ltimo j� vai ter sido comparado com todos os outros
	for (y in (x+1):tam){		#Vamos comparar o grupo atual com todos os outros, mas n�o com ele mesmo
	absol<-c(absol,abs(m[x]-m[y]))	#As comapara��es ser�o salvas na seguinte ordem (12,13,23)
	}				#Onde 12 significa compara��o entre os grupos significa 1 e 2
}

#Valores para compara��o
tam<-length(m)				#Quantidade de m�dias
tamg<-c(length(per1),length(per2),length(per3))#Tamanho de cada grupo
comp<-c()				#Vetor com as diferen�as absolutas das m�dias
for (x in 1:(tam-1)){			#Vamos comparar desde o primeiro com grupo, o �ltimo j� vai ter sido comparado com todos os outros
	for (y in (x+1):tam){		#Vamos comparar o grupo atual com todos os outros, mas n�o com ele mesmo
	form<-((4-1)*Fc*dentro*(1/tamg[x]+1/tamg[y]))^(1/2)		#F�rmula dos valores para compara��o
	comp<-c(comp,(form))	#As comapara��es ser�o salvas na seguinte ordem (12,13,23)
	}				#Onde 12 significa compara��o entre os grupos significa 1 e 2
}


#Valores printados-------------------------------------------------------------
cat("DADOS DO ANOVA:\n")
cat ("Vari�ncia dentro dos grupos: ",dentro)
cat ("\nF cr�tico: ",Fc,"\n\n")

#Vamos printar as m�dias:
for (x in 1:tam){
	cat("Media",x,":",m[x]," | ")
}

cat("\n")

con<-1					#Contador
#Printar as diferen�as absolutas entre as m�dias
for (x in 1:(tam-1)){	
	for (y in (x+1):tam){
	cat("Diferenca entre ",x,y,":",absol[con],"\n")
	con<-con+1			#Aumenta o contador
	}
}

cat("\n")

con<-1					#Contador
#Printar os valores de compara��o
for (x in 1:(tam-1)){	
	for (y in (x+1):tam){
	cat("Compara��o entre ",x,y,":",comp[con],"\n")
	con<-con+1			#Aumenta o contador
	}
}

cat("\n")

con<-1					#Contador
#Printar as diferen�as absolutas entre as m�dias
for (x in 1:(tam-1)){	
	for (y in (x+1):tam){
	cat("A diferen�a entre os grpos ",x,y)
	if (absol[con]>comp[con]){cat(" � estatisticamente diferente.\n")}
	else {cat(" n�o � estatisticamente diferente.\n")}
	con<-con+1			#Aumenta o contador
	}
}


#Vamos printar o resultado final

cat("\n")
