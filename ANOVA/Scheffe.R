#ANOVA: Teste Scheffe
#Desenvolvido por:     Jhordan Silveira de Borba
#E-mail:               jhordandecacapava@gmail.com
#Website:              https://sapogithub.github.io
#Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/ANOVA
#2018

#Valores do teste ANOVA
dentro<-1.47				#Variância dentro do grupo
Fc<-3.89				#F crítico

#Valores
per1<-c(1,2,4,4,2)		#Período 1
per2<-c(3,2,4,4,4)		#Período 2
per3<-c(-1,-1,1,-2,1)		#Período 3


#Médias
m1<-mean(per1)				#Média do grupo 1
m2<-mean(per2)				#Média do grupo 2
m3<-mean(per3)				#Média do grupo 3
m<-c(m1,m2,m3)			#Todas médias

#Diferenças absolutas entre as médias
tam<-length(m)				#Quantidade de médias
absol<-c()				#Vetor com as diferenças absolutas das médias
for (x in 1:(tam-1)){			#Vamos comparar desde o primeiro com grupo, o último já vai ter sido comparado com todos os outros
	for (y in (x+1):tam){		#Vamos comparar o grupo atual com todos os outros, mas não com ele mesmo
	absol<-c(absol,abs(m[x]-m[y]))	#As comaparações serão salvas na seguinte ordem (12,13,23)
	}				#Onde 12 significa comparação entre os grupos significa 1 e 2
}

#Valores para comparação
tam<-length(m)				#Quantidade de médias
tamg<-c(length(per1),length(per2),length(per3))#Tamanho de cada grupo
comp<-c()				#Vetor com as diferenças absolutas das médias
for (x in 1:(tam-1)){			#Vamos comparar desde o primeiro com grupo, o último já vai ter sido comparado com todos os outros
	for (y in (x+1):tam){		#Vamos comparar o grupo atual com todos os outros, mas não com ele mesmo
	form<-((4-1)*Fc*dentro*(1/tamg[x]+1/tamg[y]))^(1/2)		#Fórmula dos valores para comparação
	comp<-c(comp,(form))	#As comaparações serão salvas na seguinte ordem (12,13,23)
	}				#Onde 12 significa comparação entre os grupos significa 1 e 2
}


#Valores printados-------------------------------------------------------------
cat("DADOS DO ANOVA:\n")
cat ("Variância dentro dos grupos: ",dentro)
cat ("\nF crítico: ",Fc,"\n\n")

#Vamos printar as médias:
for (x in 1:tam){
	cat("Media",x,":",m[x]," | ")
}

cat("\n")

con<-1					#Contador
#Printar as diferenças absolutas entre as médias
for (x in 1:(tam-1)){	
	for (y in (x+1):tam){
	cat("Diferenca entre ",x,y,":",absol[con],"\n")
	con<-con+1			#Aumenta o contador
	}
}

cat("\n")

con<-1					#Contador
#Printar os valores de comparação
for (x in 1:(tam-1)){	
	for (y in (x+1):tam){
	cat("Comparação entre ",x,y,":",comp[con],"\n")
	con<-con+1			#Aumenta o contador
	}
}

cat("\n")

con<-1					#Contador
#Printar as diferenças absolutas entre as médias
for (x in 1:(tam-1)){	
	for (y in (x+1):tam){
	cat("A diferença entre os grpos ",x,y)
	if (absol[con]>comp[con]){cat(" é estatisticamente diferente.\n")}
	else {cat(" não é estatisticamente diferente.\n")}
	con<-con+1			#Aumenta o contador
	}
}


#Vamos printar o resultado final

cat("\n")
