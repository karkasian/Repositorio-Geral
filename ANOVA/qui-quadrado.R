#ANOVA: Distribuições - Qui-Quadrado
#Desenvolvido por:     Jhordan Silveira de Borba
#E-mail:               jhordandecacapava@gmail.com
#Website:              https://sapogithub.github.io
#Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/ANOVA
#2018

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

apo<-c(-1,1,1,-1,-1,1,-1,1,1,-1)	#Vetor com minhas apostas
res<-c(1,1,1,1,1,-1,-1,1,-1,1)	

cat("X² da minha aposta: ",qui(res,apo))

#Vamos gerar a distribuição X

vet<-c()				#Vetor onde vamos guardar os X
for (x in 1:10000){
	num1<-sample(2:20,1)		#Tamanho do vetore de resultados esperados
	num2<-sample(2:20,1)		#Tamanho do vetore de resultados observados	
	num3<-sample(1:2, num1, replace=T)	#Resultados esperados
	num4<-sample(1:2, num2, replace=T)	#Resultados observados
	vet<-c(vet,qui(num3,num4))
}
fin <-vet [! vet %in% NA]			#Retira os NA (Eles surgem porque se nos dados esperados obtermos só um tipo de valor, teremos uma divisão por 0
div<-100					#Tamanho que vamos dividir os dados
#hist(fin,breaks=div,xlim=c(0,20))		#Histograma dividindo em 100 partes
cort<-cut(fin, div)				#Dividimos em 100 partes
maxi<-max(fin)					#O valor máximo
mini<-min(fin)					#O valor mínimo
delta<-(maxi-mini)/div				#A variação
freq<-table(cort)				#A tabela de frequências		
y<-as.vector(freq)				#A frequência de cada valor
x<-c()						#Onde vamos guardar os X²
k<-0						#Nosso x inicial
for (k in 1:div){
	k<-k+delta				#Variamso x de acordo com o delta
	x<-c(x,k)				#Salvamos
}
#plot(x,y,type="l")				#Plotamos como linha

#Vamos normalizar o resultado
