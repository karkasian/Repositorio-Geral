#E vamos exibir na tela
# Importa as bibliotecas utilizadas
import pygame,sys
from pygame.locals import *

##CONFIGURAÇÔES --------------------------------------------------------------------------
# Inicializa a biblioteca
pygame.init()

# Define algumas cores em RGB
PRETO  = (0, 0, 0)
BRANCO = (255, 255, 255)

# Define a largura e altura da janela em pixels 800x600
size = (1200, 600)
screen = pygame.display.set_mode(size)

# Utilizado para controlar a velocidade de quadros (de atualizacoes da tela)
clock = pygame.time.Clock()

# Define um nome para a janela
pygame.display.set_caption("Fantasminha CaArmada")

#Configura as fontes usadas
fonte1 = pygame.font.SysFont(None,24)


##IMAGENS----------------------------------------------------------------------------------------------

##Vamos carregar as imagens
class solidos:
    #Sólidos fixos na tela
    fixos={
        'chao':   {'imagem':pygame.image.load('imagens/chao.png'),'ret':''},
        'parede1':{'imagem':pygame.image.load('imagens/parede.png'),'ret':''},
        'parede2':{'imagem':pygame.image.load('imagens/parede.png'),'ret':''},
        'parede3':{'imagem':pygame.image.load('imagens/parede.png'),'ret':''},
        'andar':  {'imagem':pygame.image.load('imagens/1andar.png'),'ret':''}
        }

class personagens:
    jogador={'imagem':pygame.image.load('imagens/jd.png'),'agacha':pygame.image.load('imagens/agacha.png'),'ret':''}
    jorjao1={'imagem':pygame.image.load('imagens/jorjao.png'),'ret':'','posicao':'esquerda','movendo':False,'vivo':True,'movx':'','movy':'','descendo':False}
    jorjao2={'imagem':pygame.image.load('imagens/jorjao.png'),'ret':'','posicao':'esquerda','movendo':False,'vivo':True,'mov':''}
    paulao={'imagem':pygame.image.load('imagens/paulao.png'),'ret':'','movendo':False,'vivo':True,'mov':'','assistindo':False}
    pedrao1={'imagem':pygame.image.load('imagens/pedrao.png'),'ret':'','atirando':False,'vivo':True,'tiro':''}
    pedrao2={'imagem':pygame.image.load('imagens/pedrao.png'),'ret':'','atirando':False,'vivo':True,'tiro':''}

class objeto:
    escada={'imagem':pygame.image.load('imagens/escada.png'),'ret':''}
    armas={'arma1':{'imagem':pygame.image.load('imagens/arma1.png'),'ret':''},  #Revolver
           'arma2':{'imagem':pygame.image.load('imagens/arma2.png'),'ret':''},  #Morteiro
           'arma3':{'imagem':pygame.image.load('imagens/arma3.png'),'ret':''},  #Taser
           }
    barris={'interior':{'imagem':pygame.image.load('imagens/barril.png'),'explosao':pygame.image.load('imagens/explosão.png'),'ret':'','vivo':True},
            'exterior':{'imagem':pygame.image.load('imagens/barril.png'),'explosao':pygame.image.load('imagens/explosão.png'),'ret':'','vivo':True}
            }
    aviao={'imagem':pygame.image.load('imagens/avião.png'),'ret':'','caindo':False}
    lixo={'imagem':pygame.image.load('imagens/lixo.png'),'ret':'','fogo':pygame.image.load('imagens/chamas.png'),'queimando':False}

class portas:
    porta1={'imagem':pygame.image.load('imagens/porta.png'),'ret':''}
    porta2={'imagem':pygame.image.load('imagens/porta.png'),'ret':''}
    eletrica={'imagem':pygame.image.load('imagens/eletrica.png'),'ret':'','fechada':True}
    
#Fundo
fundo={'imagem':pygame.image.load('imagens/fundo.png'),'ret':''}
#Explosão

#Condição de início
inicio=True

# Loop principal do jogo
while True:

    ##CONFIGURAÇÃO INICIAL
    if (inicio==True):

        #Configura o estado do personagem principal
        estado={'esquerda': False,
                'direita':  False,
                'agacha':   False,
                'sobe':     False,
                'arma1':    False,
                'arma2':    False,
                'arma3':    False,
                'equipado': 0,
                'lado':     'direita',
                'atirando': False}

        #Os projéteis no ar
        projeteis=[]
        
        #Vamos configurar as posições das imagens
        solidos.fixos['chao']['ret']=solidos.fixos['chao']['imagem'].get_rect()
        solidos.fixos['chao']['ret'].topleft=(0,489)
        solidos.fixos['parede1']['ret']=solidos.fixos['parede1']['imagem'].get_rect()
        solidos.fixos['parede1']['ret'].topleft=(364,0)
        solidos.fixos['parede2']['ret']=solidos.fixos['parede2']['imagem'].get_rect()
        solidos.fixos['parede2']['ret'].topleft=(747,0)
        solidos.fixos['parede3']['ret']=solidos.fixos['parede3']['imagem'].get_rect()
        solidos.fixos['parede3']['ret'].bottomleft=(1171,533)
        solidos.fixos['andar']['ret']=solidos.fixos['andar']['imagem'].get_rect()
        solidos.fixos['andar']['ret'].topright=(673,165)

        personagens.jogador['ret']=personagens.jogador['imagem'].get_rect()
        personagens.jogador['ret'].bottomleft=(600,160)

        personagens.jorjao1['posicao']='direita'
        personagens.jorjao1['movendo']=False
        personagens.jorjao1['vivo']=True
        personagens.jorjao1['ret']=personagens.jorjao1['imagem'].get_rect()
        personagens.jorjao1['ret'].bottomleft=(660,160)
        personagens.jorjao1['movx']=''
        personagens.jorjao1['movy']=''
        personagens.jorjao1['descendo']=False
        
        personagens.jorjao2['posicao']='direita'
        personagens.jorjao2['movendo']=False
        personagens.jorjao2['vivo']=True
        personagens.jorjao2['ret']=personagens.jorjao2['imagem'].get_rect()
        personagens.jorjao2['ret'].bottomleft=(660,490)
        personagens.jorjao2['mov']=''

        personagens.paulao['movendo']=False
        personagens.paulao['vivo']=True
        personagens.paulao['assistindo']=False
        personagens.paulao['mov']=''
        personagens.paulao['ret']= personagens.paulao['imagem'].get_rect()
        personagens.paulao['ret'].bottomright=(355,485)

        personagens.pedrao1['vivo']=True
        personagens.pedrao1['ret']= personagens.pedrao1['imagem'].get_rect()
        personagens.pedrao1['ret'].bottomright=(970,490)
        personagens.pedrao1['atirando']=False
        personagens.pedrao1['tiro']=''

        personagens.pedrao2['vivo']=True
        personagens.pedrao2['ret']= personagens.pedrao2['imagem'].get_rect()
        personagens.pedrao2['ret'].bottomleft=(970,490)
        personagens.pedrao2['atirando']=False
        personagens.pedrao2['tiro']=''

        objeto.escada['ret']=objeto.escada['imagem'].get_rect()
        objeto.escada['ret'].topleft=(674,170)
        objeto.armas['arma1']['ret']=objeto.armas['arma1']['imagem'].get_rect()
        objeto.armas['arma1']['ret'].topleft=(480,132)
        objeto.armas['arma2']['ret']=objeto.armas['arma2']['imagem'].get_rect()
        objeto.armas['arma2']['ret'].topleft=(900,460)
        objeto.armas['arma3']['ret']=objeto.armas['arma3']['imagem'].get_rect()
        objeto.armas['arma3']['ret'].right=0

        objeto.barris['interior']['vivo']=True
        objeto.barris['interior']['ret']=objeto.barris['interior']['imagem'].get_rect()
        objeto.barris['interior']['ret'].bottomleft=(620,490)
        objeto.barris['exterior']['vivo']=True
        objeto.barris['exterior']['ret']=objeto.barris['exterior']['imagem'].get_rect()
        objeto.barris['exterior']['ret'].bottomleft=(170,490)
        objeto.aviao['caindo']=False
        objeto.aviao['ret']=objeto.aviao['imagem'].get_rect()
        objeto.aviao['ret'].topleft=(410,195)
        objeto.lixo['queimando']=False
        objeto.lixo['ret']=objeto.lixo['imagem'].get_rect()
        objeto.lixo['ret'].bottomright=(130,327)

        fundo['ret']=fundo['imagem'].get_rect()

        portas.porta1['ret']=portas.porta1['imagem'].get_rect()
        portas.porta1['ret'].bottomleft=(365,490)
        portas.porta2['ret']=portas.porta2['imagem'].get_rect()
        portas.porta2['ret'].bottomleft=(750,490)
        portas.eletrica['ret']=portas.eletrica['imagem'].get_rect()
        portas.eletrica['ret'].bottomleft=(970,490)
        portas.eletrica['fechada']=True

        inicio=False        #Desativamos a condição de inicio

        contador=0

    ##DETECÇÃO DE EVENTOS-------------------------------------------------------------------------

    #Detectamos os tipos de evento
    for event in pygame.event.get():
        #Tecla pressionada
        if event.type==KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                sys.exit()
            if event.key==K_r:
                inicio=True
            if event.key == K_LEFT:
                estado['esquerda']=True
                estado['lado']='esquerda'
            if event.key == K_RIGHT:
                estado['direita']=True
                estado['lado']='direita'
            if event.key == K_DOWN:
                estado['agacha']=True
            if event.key == K_UP:
                estado['sobe']=True
            if event.key == K_1:
                if (estado['arma1']==True):
                    estado['equipado']=1
            if event.key == K_2:
                if (estado['arma2']==True):
                    estado['equipado']=2
            if event.key == K_3:
                if (estado['arma3']==True):
                    estado['equipado']=3
            if event.key == K_SPACE:
                estado['atirando']=True
                    
        #Tecla solta
        if event.type==KEYUP:
            if event.key == K_LEFT:
                estado['esquerda']=False
            if event.key == K_RIGHT:
                estado['direita']=False
            if event.key == K_DOWN:
                estado['agacha']=False
            if event.key == K_UP:
                estado['sobe']=False
                
        #Clicar no X para sair
        if event.type == QUIT:
                    pygame.quit()
                    sys.exit()

    ##MOVIMENTAÇÕES------------------------------------------------------------------------------
    #DO JOGADOR
    personagens.jogador['ret'].move_ip(0,5)    #Desce devido a gravidade

    if (estado['esquerda']==True):               #Se movimenta para a esquerda
        personagens.jogador['ret'].move_ip(-5,0)
    if (estado['direita']==True):               #Se movimenta para a direita
        personagens.jogador['ret'].move_ip(5,0)

    #Detecta colisões    
    if (personagens.jogador['ret'].colliderect(solidos.fixos['chao']['ret'])):      #Com o chão
        personagens.jogador['ret'].bottom=solidos.fixos['chao']['ret'].top
    if (personagens.jogador['ret'].colliderect(solidos.fixos['andar']['ret'])):     #Com o piso do primeiro andar
        #Se o jogador está a esquerda
        if (personagens.jogador['ret'].bottom-10>solidos.fixos['andar']['ret'].top):
            personagens.jogador['ret'].left=solidos.fixos['andar']['ret'].right
        else:                                                                       #Se não esta acima
            personagens.jogador['ret'].bottom=solidos.fixos['andar']['ret'].top 
    if (personagens.jogador['ret'].colliderect(solidos.fixos['parede1']['ret'])):   #Com parede mais a esquerda
        personagens.jogador['ret'].left=solidos.fixos['parede1']['ret'].right
    if (personagens.jogador['ret'].colliderect(solidos.fixos['parede2']['ret'])):   #Com a parede do meio
        personagens.jogador['ret'].right=solidos.fixos['parede2']['ret'].left
    if (personagens.jogador['ret'].colliderect(solidos.fixos['parede3']['ret'])):   #Com a parede mais a direita
        personagens.jogador['ret'].right=solidos.fixos['parede3']['ret'].left

    if (personagens.jogador['ret'].colliderect(objeto.escada['ret'])):              #Com a escada
        personagens.jogador['ret'].move_ip(0,-5)    #Anula a gravidade
        if (estado['agacha']==True):
            personagens.jogador['ret'].move_ip(0,5)
        if (estado['sobe']==True):
            personagens.jogador['ret'].move_ip(0,-5)

    #Portas internas
    if(personagens.jorjao1['vivo']==True or personagens.jorjao1['vivo']==True):
        if(personagens.jogador['ret'].colliderect(portas.porta1['ret'])):
            personagens.jogador['ret'].left=portas.porta1['ret'].right
        if(personagens.jogador['ret'].colliderect(portas.porta2['ret'])):
            personagens.jogador['ret'].right=portas.porta2['ret'].left
    if(portas.eletrica['fechada']==True):
        if(personagens.jogador['ret'].colliderect(portas.eletrica['ret'])):
            personagens.jogador['ret'].right=portas.eletrica['ret'].left

    #Coleta de armas
    #ARMA 1
    if (estado['arma1']==False):
        if (personagens.jogador['ret'].colliderect(objeto.armas['arma1']['ret'])):
            estado['arma1']=True
    #ARMA 2
    if (estado['arma2']==False):
        if (personagens.jogador['ret'].colliderect(objeto.armas['arma2']['ret'])):
            estado['arma2']=True

    #ARMA 3
    if (estado['arma3']==False):
        if (personagens.jogador['ret'].colliderect(objeto.armas['arma3']['ret'])):
            estado['arma3']=True

    #DOS PROJETEIS
    if (len(projeteis)>0):      #Se temos projeteis
        tam=len(projeteis)      #Quantos temos
        elim=[]                 #Onde vamos guardar os que vamos eliminar
        for n in range(tam):    #Vamos percorrer todos
            if (projeteis[n]['arma']=='arma1'):
                projeteis[n]['ret']=projeteis[n]['img'].get_rect()                  #Pegamos o rect
                projeteis[n]['ret'].topleft=(projeteis[n]['x'][0],projeteis[n]['y'])#Ajustamos a posição
                projeteis[n]['x'].pop(0)        #Eliminamos a posição atual
                if (len(projeteis[n]['x'])==0): #Se já não temos mais posições, eliminamos
                    elim.append(projeteis[n])
                elif (projeteis[n]['ret'].colliderect(objeto.armas['arma3']['ret']) or #Se não foi eliminado, checamos a colisão
                    projeteis[n]['ret'].colliderect(solidos.fixos['andar']['ret']) or
                    projeteis[n]['ret'].colliderect(solidos.fixos['parede1']['ret']) or
                    projeteis[n]['ret'].colliderect(solidos.fixos['parede2']['ret']) or
                    projeteis[n]['ret'].colliderect(solidos.fixos['parede3']['ret'])):
                    elim.append(projeteis[n])

                #Vamos detectar se explodiu o barril do interior
                elif (projeteis[n]['ret'].colliderect(objeto.barris['interior']['ret']) and objeto.barris['interior']['vivo']==True):
                     objeto.barris['interior']['vivo']=False
                     elim.append(projeteis[n])
                     personagens.jorjao1['descendo']=True
                     if (objeto.barris['interior']['ret'].colliderect(personagens.jorjao2['ret'])):
                         personagens.jorjao2['vivo']=False
                     if (objeto.barris['interior']['ret'].colliderect(personagens.jorjao1['ret'])):
                         personagens.jorjao1['vivo']=False
                     objeto.barris['interior']['ret'].bottom=objeto.barris['interior']['ret'].bottom-50
                     objeto.barris['interior']['ret'].left=objeto.barris['interior']['ret'].left-40
                #Vamos detectar se explodiu o barril do exterior
                elif (projeteis[n]['ret'].colliderect(objeto.barris['exterior']['ret']) and objeto.barris['exterior']['vivo']==True):
                     objeto.barris['exterior']['vivo']=False
                     elim.append(projeteis[n])
                     if (objeto.barris['exterior']['ret'].colliderect(personagens.paulao['ret'])):
                        personagens.paulao['vivo']=False
                        objeto.armas['arma3']['ret']=objeto.armas['arma3']['imagem'].get_rect()
                        objeto.armas['arma3']['ret'].bottomleft=personagens.paulao['ret'].bottomleft
                     objeto.barris['exterior']['ret'].bottom=objeto.barris['exterior']['ret'].bottom-50
                     objeto.barris['exterior']['ret'].left=objeto.barris['exterior']['ret'].left-40


                #Se derrubou o avião
                elif (projeteis[n]['ret'].colliderect(objeto.aviao['ret']) and objeto.aviao['caindo']==False):
                     objeto.aviao['caindo']=True
                     elim.append(projeteis[n])
                #Portas internas
                elif(personagens.jorjao1['vivo']==True or personagens.jorjao1['vivo']==True):
                    if(projeteis[n]['ret'].colliderect(portas.porta1['ret'])):
                       elim.append(projeteis[n])
                    if(projeteis[n]['ret'].colliderect(portas.porta2['ret'])):
                       elim.append(projeteis[n])
                #Elétrica
                elif(portas.eletrica['fechada']==True):
                    if(projeteis[n]['ret'].colliderect(portas.eletrica['ret'])):
                       elim.append(projeteis[n])
                    
                     
            elif (projeteis[n]['arma']=='arma2'):
                projeteis[n]['ret']=projeteis[n]['img'].get_rect()                  #Pegamos o rect
                projeteis[n]['ret'].topleft=(projeteis[n]['x'][0],projeteis[n]['y'][0])#Ajustamos a posição
                projeteis[n]['x'].pop(0)        #Eliminamos as posições atuais
                projeteis[n]['y'].pop(0)        #Eliminamos as posições
                if (len(projeteis[n]['x'])==0): #Se já não temos mais posições, eliminamos
                    elim.append(projeteis[n])
                elif (projeteis[n]['ret'].colliderect(objeto.armas['arma3']['ret']) or #Se não foi eliminado, checamos a colisão
                    projeteis[n]['ret'].colliderect(solidos.fixos['andar']['ret']) or
                    projeteis[n]['ret'].colliderect(solidos.fixos['parede1']['ret']) or
                    projeteis[n]['ret'].colliderect(solidos.fixos['parede2']['ret']) or
                    projeteis[n]['ret'].colliderect(solidos.fixos['parede3']['ret'])):
                    elim.append(projeteis[n])
                elif (projeteis[n]['ret'].colliderect(objeto.lixo['ret']) and objeto.lixo['queimando']==False):   #Se acertou o lixo
                    objeto.lixo['ret'].bottom=objeto.lixo['ret'].bottom-17
                    objeto.lixo['ret'].left=objeto.lixo['ret'].left+15
                    objeto.lixo['queimando']=True
                    elim.append(projeteis[n])
                                #Portas internas
                elif(personagens.jorjao1['vivo']==True or personagens.jorjao1['vivo']==True):
                    if(projeteis[n]['ret'].colliderect(portas.porta1['ret'])):
                       elim.append(projeteis[n])
                    if(projeteis[n]['ret'].colliderect(portas.porta2['ret'])):
                       elim.append(projeteis[n])
                elif(portas.eletrica['fechada']==True):
                    if(projeteis[n]['ret'].colliderect(portas.eletrica['ret'])):
                       elim.append(projeteis[n])
                    
            elif (projeteis[n]['arma']=='arma3'):
                projeteis[n]['ret']=projeteis[n]['img'].get_rect()                  #Pegamos o rect
                projeteis[n]['ret'].topleft=(projeteis[n]['x'][0],projeteis[n]['y'])#Ajustamos a posição
                projeteis[n]['x'].pop(0)        #Eliminamos a posição atual
                if (len(projeteis[n]['x'])==0): #Se já não temos mais posições, eliminamos
                    elim.append(projeteis[n])
                elif (projeteis[n]['ret'].colliderect(objeto.armas['arma3']['ret']) or #Se não foi eliminado, checamos a colisão
                    projeteis[n]['ret'].colliderect(solidos.fixos['andar']['ret']) or
                    projeteis[n]['ret'].colliderect(solidos.fixos['parede1']['ret']) or
                    projeteis[n]['ret'].colliderect(solidos.fixos['parede2']['ret']) or
                    projeteis[n]['ret'].colliderect(solidos.fixos['parede3']['ret'])):
                    elim.append(projeteis[n])
                #Portas internas
                elif(personagens.jorjao1['vivo']==True or personagens.jorjao1['vivo']==True):
                    if(projeteis[n]['ret'].colliderect(portas.porta1['ret'])):
                       elim.append(projeteis[n])
                    if(projeteis[n]['ret'].colliderect(portas.porta2['ret'])):
                       elim.append(projeteis[n])
                elif(portas.eletrica['fechada']==True):
                    if(projeteis[n]['ret'].colliderect(portas.eletrica['ret'])):
                       elim.append(projeteis[n])
                       portas.eletrica['fechada']=False


        for item in elim:
            projeteis.remove(item)
    #Do avião
    if(objeto.aviao['caindo']==True):
        objeto.aviao['ret'].move_ip(0,50)    #Desce devido a gravidade
        if (objeto.aviao['ret'].colliderect(personagens.jorjao2['ret'])):
                         personagens.jorjao2['vivo']=False
        if (objeto.aviao['ret'].colliderect(personagens.jorjao1['ret'])):
                         personagens.jorjao1['vivo']=False
        if (objeto.aviao['ret'].colliderect(solidos.fixos['chao']['ret'])):      #Com o chão
            objeto.aviao['ret'].bottom=solidos.fixos['chao']['ret'].top
            objeto.aviao['caindo']=None
            

    if(personagens.jorjao1['vivo']==True):
        if  (personagens.jorjao1['descendo']==False):
            if (personagens.jorjao1['movendo']==False):
                if(personagens.jorjao1['ret'].colliderect(personagens.jogador['ret'])):
                    personagens.jorjao1['movendo']=True
                    
                    if(personagens.jorjao1['posicao']=='esquerda'):
                        inicial=personagens.jorjao1['ret'].right
                        final=inicial+200
                        pos=[]
                        for x in range(inicial,final,10):
                            pos.append(x)
                        personagens.jorjao1['movx']=pos
                        personagens.jorjao1['posicao']='direita'
                        
                    else:
                        inicial=personagens.jorjao1['ret'].left
                        final=inicial-200
                        pos=[]
                        for x in range(inicial,final,-10):
                            pos.append(x)
                        personagens.jorjao1['movx']=pos
                        personagens.jorjao1['posicao']='esquerda'

                    personagens.jorjao1['movendo']=True
                    
            elif (personagens.jorjao1['movendo']==True):
                if (personagens.jorjao1['posicao']=='esquerda'):
                    personagens.jorjao1['ret'].left=personagens.jorjao1['movx'][0]
                else:
                    personagens.jorjao1['ret'].right=personagens.jorjao1['movx'][0]
                personagens.jorjao1['movx'].pop(0)
                if(len(personagens.jorjao1['movx'])==0):
                    personagens.jorjao1['movendo']=False
        else:           
            if (personagens.jorjao1['movendo']==False):
                inicio=personagens.jorjao1['ret'].right
                fim=733
                movx=[]
                movy=[]
                
                for x in range(inicio,fim,10):
                    movx.append(x)
                    movy.append(personagens.jorjao1['ret'].bottom)
                    
                inicio=personagens.jorjao1['ret'].bottom
                fim=490
                
                for x in range(inicio,fim,10):
                    movx.append(733)
                    movy.append(x)
                    
                personagens.jorjao1['movx']=movx
                personagens.jorjao1['movy']=movy
                personagens.jorjao1['posicao']='direita'
                personagens.jorjao1['movendo']=True
            else:
                personagens.jorjao1['ret'].bottomright=(personagens.jorjao1['movx'][0],personagens.jorjao1['movy'][0])
                personagens.jorjao1['movx'].pop(0)
                personagens.jorjao1['movy'].pop(0)
                if(len(personagens.jorjao1['movx'])==0):
                    personagens.jorjao1['movendo']=False
                    personagens.jorjao1['descendo']=False

    if(personagens.jorjao2['vivo']==True):
        if (personagens.jorjao2['movendo']==False):
            if(personagens.jorjao2['ret'].colliderect(personagens.jogador['ret'])):
                personagens.jorjao2['movendo']=True
                
                if(personagens.jorjao2['posicao']=='esquerda'):
                    inicial=personagens.jorjao2['ret'].right
                    final=inicial+200
                    pos=[]
                    for x in range(inicial,final,10):
                        pos.append(x)
                    personagens.jorjao2['mov']=pos
                    personagens.jorjao2['posicao']='direita'
                    
                else:
                    inicial=personagens.jorjao2['ret'].left
                    final=inicial-200
                    pos=[]
                    for x in range(inicial,final,-10):
                        pos.append(x)
                    personagens.jorjao2['mov']=pos
                    personagens.jorjao2['posicao']='esquerda'

                personagens.jorjao2['movendo']=True
                
        elif (personagens.jorjao2['movendo']==True):
            if (personagens.jorjao2['posicao']=='esquerda'):
                personagens.jorjao2['ret'].left=personagens.jorjao2['mov'][0]
            else:
                personagens.jorjao2['ret'].right=personagens.jorjao2['mov'][0]
            personagens.jorjao2['mov'].pop(0)
            if(len(personagens.jorjao2['mov'])==0):
                personagens.jorjao2['movendo']=False

    if(personagens.paulao['vivo']==True):
        if (objeto.lixo['queimando']==True):
            if (personagens.paulao['assistindo']==False):
                if(personagens.paulao['movendo']==False):
                    inicio=personagens.paulao['ret'].left
                    fim=170
                    for x in range(inicio,fim,-10):
                        pos.append(x)
                    personagens.paulao['mov']=pos
                    personagens.paulao['movendo']=True
                else:
                    personagens.paulao['ret'].left=personagens.paulao['mov'][0]
                    personagens.paulao['mov'].pop(0)
                    if(len(personagens.paulao['mov'])==0):
                        personagens.paulao['movendo']=False
                        personagens.paulao['assistindo']=True
                        
    if(personagens.pedrao1['vivo']==True):
        if (personagens.pedrao1['atirando']==False):
            if(personagens.pedrao1['ret'].colliderect(personagens.jogador['ret']) and estado['agacha']==False):
                personagens.pedrao1['atirando']=True
                if (personagens.jogador['ret'].left-100<personagens.pedrao1['ret'].left):
                    
                    inicio=personagens.pedrao1['ret'].left+75
                    fim=inicio-300
                    pos=[]
                    for x in range(inicio,fim,-20):
                        pos.append(x)
                    img=pygame.image.load('imagens/tiro_inimigo.png')
                    ret=img.get_rect()
                    ret.top=personagens.pedrao1['ret'].top
                    personagens.pedrao1['tiro']={'img':img,'ret':ret,'x':pos}
                else:
                    inicio=personagens.pedrao1['ret'].right-75
                    fim=inicio+300
                    pos=[]
                    for x in range(inicio,fim,20):
                        pos.append(x)
                    img=pygame.image.load('imagens/tiro_inimigo.png')
                    ret=img.get_rect()
                    ret.top=personagens.pedrao1['ret'].top
                    personagens.pedrao1['tiro']={'img':img,'ret':ret,'x':pos}
                    
    if(personagens.pedrao1['atirando']==True):
        personagens.pedrao1['tiro']['ret'].left=personagens.pedrao1['tiro']['x'][0]
        personagens.pedrao1['tiro']['x'].pop(0)
        if(len(personagens.pedrao1['tiro']['x'])==0):
            personagens.pedrao1['atirando']=False
            
        elif(personagens.pedrao1['tiro']['ret'].colliderect(solidos.fixos['parede3']['ret'])):
            personagens.pedrao1['atirando']=False

        elif (personagens.pedrao1['tiro']['ret'].right>=personagens.pedrao2['ret'].left+75 and personagens.pedrao2['vivo']==True):
            personagens.pedrao2['vivo']=False
            personagens.pedrao1['atirando']=False

        #Elétrica
        elif(portas.eletrica['fechada']==True):
            if(personagens.pedrao1['tiro']['ret'].colliderect(portas.eletrica['ret'])):
                personagens.pedrao1['atirando']=False
                
    if(personagens.pedrao2['vivo']==True):                    
        if (personagens.pedrao2['atirando']==False):
            if(personagens.pedrao2['ret'].colliderect(personagens.jogador['ret']) and estado['agacha']==False):
                personagens.pedrao2['atirando']=True
                if (personagens.jogador['ret'].left-100<personagens.pedrao2['ret'].left):
                    
                    inicio=personagens.pedrao2['ret'].left+75
                    fim=inicio-300
                    pos=[]
                    for x in range(inicio,fim,-10):
                        pos.append(x)
                    img=pygame.image.load('imagens/tiro_inimigo.png')
                    ret=img.get_rect()
                    ret.top=personagens.pedrao2['ret'].top
                    personagens.pedrao2['tiro']={'img':img,'ret':ret,'x':pos}
                else:
                    inicio=personagens.pedrao2['ret'].right-75
                    fim=inicio+300
                    pos=[]
                    for x in range(inicio,fim,10):
                        pos.append(x)
                    img=pygame.image.load('imagens/tiro_inimigo.png')
                    ret=img.get_rect()
                    ret.top=personagens.pedrao2['ret'].top
                    personagens.pedrao2['tiro']={'img':img,'ret':ret,'x':pos}
                    
    if (personagens.pedrao2['atirando']==True):
        personagens.pedrao2['tiro']['ret'].left=personagens.pedrao2['tiro']['x'][0]
        personagens.pedrao2['tiro']['x'].pop(0)
        if(len(personagens.pedrao2['tiro']['x'])==0):
            personagens.pedrao2['atirando']=False
            
        elif(personagens.pedrao2['tiro']['ret'].colliderect(solidos.fixos['parede3']['ret'])):
            personagens.pedrao2['atirando']=False

        elif (personagens.pedrao2['tiro']['ret'].left<=personagens.pedrao1['ret'].right-75 and personagens.pedrao1['vivo']==True):
            personagens.pedrao1['vivo']=False
            personagens.pedrao2['atirando']=False

    #TIRO-----------------------------------------------------------------------------------------

    if (estado['agacha']==True and estado['atirando']==True):
        estado['atirando']=False
        
    if (estado['atirando']==True):
        if (estado['equipado']==1):
            if (estado['lado']=='direita'):
                inicial=personagens.jogador['ret'].right
                final=inicial+300
                pos=[]
                for x in range(inicial,final,10):
                    pos.append(x)
                tiro={'arma':'arma1','x':pos,'y':personagens.jogador['ret'].top+60,'img':pygame.image.load('imagens/tiro_revolver.png'),'ret':''}
                projeteis.append(tiro)
                estado['atirando']=False
            if (estado['lado']=='esquerda'):
                inicial=personagens.jogador['ret'].left-13
                final=inicial-300
                pos=[]
                for x in range(inicial,final,-10):
                    pos.append(x)
                tiro={'arma':'arma1','x':pos,'y':personagens.jogador['ret'].top+60,'img':pygame.image.load('imagens/tiro_revolver.png'),'ret':''}
                projeteis.append(tiro)
                estado['atirando']=False
        if (estado['equipado']==2):
            if (estado['lado']=='direita'):
                #Eixo X
                inicial=personagens.jogador['ret'].right
                final=inicial+200
                posx=[]
                for x in range(inicial,final,2):
                    posx.append(x)
                #EiXO Y
                inicial=personagens.jogador['ret'].top
                meio=inicial-150
                posy=[]
                for x in range(inicial,meio,-3):
                    posy.append(x)
                for x in range(meio,inicial,3):
                    posy.append(x)
                tiro={'arma':'arma2','x':posx,'y':posy,'img':pygame.image.load('imagens/tiro_morteiro.png'),'ret':''}
                projeteis.append(tiro)
                estado['atirando']=False
            if (estado['lado']=='esquerda'):
                #Eixo X
                inicial=personagens.jogador['ret'].left
                final=inicial-200
                posx=[]
                for x in range(inicial,final,-2):
                    posx.append(x)
                #EiXO Y
                inicial=personagens.jogador['ret'].top
                meio=inicial-150
                posy=[]
                for x in range(inicial,meio,-3):
                    posy.append(x)
                for x in range(meio,inicial,3):
                    posy.append(x)
                tiro={'arma':'arma2','x':posx,'y':posy,'img':pygame.image.load('imagens/tiro_morteiro.png'),'ret':''}
                projeteis.append(tiro)
                estado['atirando']=False
        if (estado['equipado']==3):
            if (estado['lado']=='direita'):
                inicial=personagens.jogador['ret'].right
                final=inicial+300
                pos=[]
                for x in range(inicial,final,10):
                    pos.append(x)
                tiro={'arma':'arma3','x':pos,'y':personagens.jogador['ret'].top+25,'img':pygame.image.load('imagens/tiro_taser.png'),'ret':''}
                projeteis.append(tiro)
                estado['atirando']=False
            if (estado['lado']=='esquerda'):
                inicial=personagens.jogador['ret'].left
                final=inicial-300
                pos=[]
                for x in range(inicial,final,-10):
                    pos.append(x)
                tiro={'arma':'arma3','x':pos,'y':personagens.jogador['ret'].top,'img':pygame.image.load('imagens/tiro_taser.png'),'ret':''}
                projeteis.append(tiro)
                estado['atirando']=False
        estado['atirando']=False

    ##DESENHAR NA TELA----------------------------------------------------------------------------

    # Preenche a tela com uma cor, neste caso preto (definido logo apos importar as bibliotecas)
    screen.fill(BRANCO)

    #Desenhar o fundo
    screen.blit(fundo['imagem'],fundo['ret'])

    #Desenha os objetos
    if( objeto.barris['exterior']['vivo']==True):
        screen.blit(objeto.barris['exterior']['imagem'],objeto.barris['exterior']['ret'])
    else:
        screen.blit(objeto.barris['exterior']['explosao'],objeto.barris['exterior']['ret'])
    if( objeto.barris['interior']['vivo']==True):
        screen.blit(objeto.barris['interior']['imagem'],objeto.barris['interior']['ret'])
    else:
        screen.blit(objeto.barris['interior']['explosao'],objeto.barris['interior']['ret'])
    if (objeto.lixo['queimando']==False):
        screen.blit(objeto.lixo['imagem'],objeto.lixo['ret'])
    else:
        screen.blit(objeto.lixo['fogo'],objeto.lixo['ret'])

    screen.blit(objeto.escada['imagem'],objeto.escada['ret'])
    screen.blit(objeto.armas['arma1']['imagem'],objeto.armas['arma1']['ret'])
    screen.blit(objeto.armas['arma2']['imagem'],objeto.armas['arma2']['ret'])
    screen.blit(objeto.armas['arma3']['imagem'],objeto.armas['arma3']['ret'])
    screen.blit(objeto.aviao['imagem'],objeto.aviao['ret'])

    #Desenha os sólidos fixos
    screen.blit(solidos.fixos['parede1']['imagem'],solidos.fixos['parede1']['ret'])
    screen.blit(solidos.fixos['parede2']['imagem'],solidos.fixos['parede2']['ret'])
    screen.blit(solidos.fixos['parede3']['imagem'],solidos.fixos['parede3']['ret'])
    screen.blit(solidos.fixos['andar']['imagem'],solidos.fixos['andar']['ret'])
    screen.blit(solidos.fixos['chao']['imagem'],solidos.fixos['chao']['ret'])


    #Desenhar o jogador
    if (estado['agacha']==False):
        if(estado['lado']=='direita'):
            if(estado['direita']==True):
                if(contador%5==0):
                    if(contador%10==0):
                        personagens.jogador['imagem']=pygame.image.load('imagens/jdc1.png')
                    else:
                        personagens.jogador['imagem']=pygame.image.load('imagens/jdc2.png')
            else:
                personagens.jogador['imagem']=pygame.image.load('imagens/jd.png')
        else:
            if(estado['esquerda']==True):
                if(contador%5==0):
                    if(contador%10==0):
                        personagens.jogador['imagem']=pygame.image.load('imagens/jec1.png')
                    else:
                        personagens.jogador['imagem']=pygame.image.load('imagens/jec2.png')
            else:
                personagens.jogador['imagem']=pygame.image.load('imagens/je.png')
                 
        screen.blit(personagens.jogador['imagem'],personagens.jogador['ret'])
    else:
        if(estado['lado']=='direita'):
            if(estado['direita']==True):
                if(contador%5==0):
                    if(contador%10==0):
                        personagens.jogador['imagem']=pygame.image.load('imagens/jda1.png')
                    else:
                        personagens.jogador['imagem']=pygame.image.load('imagens/jda2.png')
            else:
                personagens.jogador['imagem']=pygame.image.load('imagens/jda1.png')
        else:
            if(estado['esquerda']==True):
                if(contador%5==0):
                    if(contador%10==0):
                        personagens.jogador['imagem']=pygame.image.load('imagens/jea1.png')
                    else:
                        personagens.jogador['imagem']=pygame.image.load('imagens/jea2.png')
            else:
                personagens.jogador['imagem']=pygame.image.load('imagens/jea1.png')
                    
        screen.blit(personagens.jogador['imagem'],personagens.jogador['ret'])

    #O Jorjão1
    if (personagens.jorjao1['vivo']==True):
        screen.blit(personagens.jorjao1['imagem'],personagens.jorjao1['ret'])

    #O Jorjão2
    if (personagens.jorjao2['vivo']==True):
        screen.blit(personagens.jorjao2['imagem'],personagens.jorjao2['ret'])

    #O Paulão
    if (personagens.paulao['vivo']==True):
        screen.blit(personagens.paulao['imagem'],personagens.paulao['ret'])

    #O Pedrão 1
    if (personagens.pedrao1['vivo']==True):
        screen.blit(personagens.pedrao1['imagem'],personagens.pedrao1['ret'])

    #O Pedrão 2
    if (personagens.pedrao2['vivo']==True):
        screen.blit(personagens.pedrao2['imagem'],personagens.pedrao2['ret'])

    #Printar os projeteis
    if (len(projeteis)>0):
        tam=len(projeteis)
        for n in range(tam):
            if (projeteis[n]['ret']!=''):                           #Precisamos pular o primeiro quadro
                screen.blit(projeteis[n]['img'],projeteis[n]['ret'])

    #Tiro do pedrao1
    if (personagens.pedrao1['atirando']==True):
        screen.blit(personagens.pedrao1['tiro']['img'],personagens.pedrao1['tiro']['ret'])

    #Tiro do pedrao2
    if (personagens.pedrao2['atirando']==True):
        screen.blit(personagens.pedrao2['tiro']['img'],personagens.pedrao2['tiro']['ret'])

    #Desenhar as portas:
    if (personagens.jorjao1['vivo']==True or personagens.jorjao1['vivo']==True):
        screen.blit(portas.porta1['imagem'],portas.porta1['ret'])
        screen.blit(portas.porta2['imagem'],portas.porta2['ret'])
    if( portas.eletrica['fechada']==True):
        screen.blit(portas.eletrica['imagem'],portas.eletrica['ret'])

    #Vamos printar as armas que o jogador tem:
    if  (estado['arma1']==True):
        if (estado['equipado']==1):
            texto=fonte1.render("[1: Revólver]",0,PRETO)
        else:
            texto=fonte1.render("1: Revólver",0,PRETO)
        textoret=texto.get_rect()
        textoret.topleft=(10,10)
        screen.blit(texto,textoret)
    if  (estado['arma2']==True):
        if (estado['equipado']==2):
            texto=fonte1.render("[2: Morteiro]",0,PRETO)
        else:
            texto=fonte1.render("2: Morteiro",0,PRETO)
        textoret=texto.get_rect()
        textoret.topleft=(10,30)
        screen.blit(texto,textoret)
    if  (estado['arma3']==True):
        if (estado['equipado']==3):
            texto=fonte1.render("[3: Taser]",0,PRETO)
        else:
            texto=fonte1.render("3: Taser",0,PRETO)
        textoret=texto.get_rect()
        textoret.topleft=(10,50)
        screen.blit(texto,textoret)


    # Atualiza a tela visivel ao usuario
    pygame.display.flip()

    # Limita a taxa de quadros (framerate) a 60 quadros por segundo (60fps)
    clock.tick(30)

    contador=contador+1
