##Flappy Fantasma
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Flappy-Fantasma
##2018


import matplotlib.pyplot as plt             #Biblioteca para plotar gráficos
import os                                   #Biblioteca relacionada a caminhos
from PIL import Image                       #PIL para trabalhar com as imagens
import matplotlib.animation as animation    #Para fazer animação

#Fundo de todos os gráficos
def fundo():
    #Salvamos os pontos no gráfico
    plt.plot(voax, voay, 'or',label='Voa')
    plt.plot(nvoax, nvoay, 'ob',label='Não Voa')
    plt.title("Aprendizado de um Perceptron")
    plt.xlabel('Altura do fantasma')
    plt.ylabel('Altura do obstáculo')
##    plt.ylim(ymin=-1)
##    plt.xlim(xmin=-1)
##    plt.xlim(xmax=1)
##    plt.ylim(ymax=1)


#Cria o diretorio se não existe
if not os.path.exists("imagens/"):
    os.makedirs("imagens/")

#Vamos ler os dados dos arquivos
with open("Peso1.txt", "r") as arquivo:     #Abrimos o arquivo
    p1 = []                                 #Onde vamos guardar os valores
    for line in arquivo:                    #Percorremos as linhas
        p1.append(line.rstrip('\n').replace(",", "."))        #Salvamos as linhas retirando as quebras

with open("Peso2.txt", "r") as arquivo:     #Abrimos o arquivo
    p2 = []                                 #Onde vamos guardar os valores
    for line in arquivo:                    #Percorremos as linhas
        p2.append(line.rstrip('\n').replace(",", "."))        #Salvamos as linhas retirando as quebras

with open("Limiar.txt", "r") as arquivo:    #Abrimos o arquivo
    L = []                                  #Onde vamos guardar os valores
    for line in arquivo:                    #Percorremos as linhas
        L.append(line.rstrip('\n').replace(",", "."))         #Salvamos as linhas retirando as quebras

#Vamos criar os pontos no grafico:
voax=[]          #Array pra salvar os pontos na coordenada X que o passarinho voa
voay=[]          #Coordenada Y
nvoax=[]         #Array pra guardar os pontos que o passarinho não voa na coordenada X
nvoay=[]         #Coordenada Y

#Geramos os pontos
for x in range(0,50,1):
    for y in range (0,50,1):
        if x>=y:
            nvoax.append(x/10)
            nvoay.append(y/10)
        else:
            voax.append(x/10)
            voay.append(y/10)
n=0                                         #Variável pra indicar qual figura e

fundo()                                      #Plotamos o fundo
plt.legend()
plt.savefig('imagens/fig-'+str(n)+'.png')
plt.show()

#Vamos percorrer nossas matriz agora
for x in range(0,3,1):
    xis=[]
    yp=[]
    y=-(float(p1[x])*0+float(L[x]))/float(p2[x])
    xis.append(0)
    yp.append(y)
    y=-(float(p1[x])*5+float(L[x]))/float(p2[x])
    xis.append(5)
    yp.append(y)
    fundo()                                      #Plotamos o fundo
    plt.plot(xis,yp,'black')
    plt.legend()
    plt.savefig('imagens/fig-'+str(n+1)+'.png')
    #plt.show()
    plt.close();
    n+=1




fig = plt.figure()                          #Cria uma figura
ims = []                                    #Criamos nossa lista de frames
for x in range(4):
    em = Image.open("imagens/fig-"+str(x)+".png") 
    im = plt.imshow(em, animated=True)     #Renderiza a imagem
    ims.append([im])
ani = animation.ArtistAnimation(fig, ims, interval=50, blit=True,repeat_delay=0)
ani.save('imagens/animacao.gif')#,writer = animation.FFMpegWriter())
plt.show(ani)
