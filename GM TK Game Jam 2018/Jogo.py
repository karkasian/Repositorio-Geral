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
    jogador={'imagem':pygame.image.load('imagens/jogador.png'),'agacha':pygame.image.load('imagens/agacha.png'),'ret':''}

class objeto:
    escada={'imagem':pygame.image.load('imagens/escada.png'),'ret':''}
    armas={'arma1':{'imagem':pygame.image.load('imagens/arma1.png'),'ret':''},
           'arma2':{'imagem':pygame.image.load('imagens/arma2.png'),'ret':''},
           'arma3':{'imagem':pygame.image.load('imagens/arma3.png'),'ret':''},
           }
    
#Fundo
fundo={'imagem':pygame.image.load('imagens/fundo.png'),'ret':''}

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
        solidos.fixos['parede1']['ret'].topleft=(365,0)
        solidos.fixos['parede2']['ret']=solidos.fixos['parede2']['imagem'].get_rect()
        solidos.fixos['parede2']['ret'].topleft=(745,0)
        solidos.fixos['parede3']['ret']=solidos.fixos['parede3']['imagem'].get_rect()
        solidos.fixos['parede3']['ret'].bottomleft=(1171,491)
        solidos.fixos['andar']['ret']=solidos.fixos['andar']['imagem'].get_rect()
        solidos.fixos['andar']['ret'].topright=(675,165)

        personagens.jogador['ret']=personagens.jogador['imagem'].get_rect()
        personagens.jogador['ret'].bottomleft=(600,160)

        objeto.escada['ret']=objeto.escada['imagem'].get_rect()
        objeto.escada['ret'].topleft=(674,170)
        objeto.armas['arma1']['ret']=objeto.armas['arma1']['imagem'].get_rect()
        objeto.armas['arma1']['ret'].topleft=(480,120)
        objeto.armas['arma2']['ret']=objeto.armas['arma2']['imagem'].get_rect()
        objeto.armas['arma2']['ret'].topleft=(840,460)
        objeto.armas['arma3']['ret']=objeto.armas['arma3']['imagem'].get_rect()
        
        objeto.armas['arma3']['ret'].topleft=(200,450)

        fundo['ret']=fundo['imagem'].get_rect()

        inicio=False        #Desativamos a condição de inicio

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

        for item in elim:
            projeteis.remove(item)
            
#projeteis.pop(0)
    #TIRO-----------------------------------------------------------------------------------------
    if (estado['atirando']==True):
        if (estado['equipado']==1):
            if (estado['lado']=='direita'):
                inicial=personagens.jogador['ret'].right
                final=inicial+300
                pos=[]
                for x in range(inicial,final,10):
                    pos.append(x)
                tiro={'arma':'arma1','x':pos,'y':personagens.jogador['ret'].top,'img':pygame.image.load('imagens/tiro_revolver.png'),'ret':''}
                projeteis.append(tiro)
                estado['atirando']=False
            if (estado['lado']=='esquerda'):
                inicial=personagens.jogador['ret'].left
                final=inicial-300
                pos=[]
                for x in range(inicial,final,-10):
                    pos.append(x)
                tiro={'arma':'arma1','x':pos,'y':personagens.jogador['ret'].top,'img':pygame.image.load('imagens/tiro_revolver.png'),'ret':''}
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
                tiro={'arma':'arma3','x':pos,'y':personagens.jogador['ret'].top,'img':pygame.image.load('imagens/tiro_taser.png'),'ret':''}
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
    screen.blit(objeto.escada['imagem'],objeto.escada['ret'])
    screen.blit(objeto.armas['arma1']['imagem'],objeto.armas['arma1']['ret'])
    screen.blit(objeto.armas['arma2']['imagem'],objeto.armas['arma2']['ret'])
    screen.blit(objeto.armas['arma3']['imagem'],objeto.armas['arma3']['ret'])

    #Desenha os sólidos fixos
    screen.blit(solidos.fixos['chao']['imagem'],solidos.fixos['chao']['ret'])
    screen.blit(solidos.fixos['parede1']['imagem'],solidos.fixos['parede1']['ret'])
    screen.blit(solidos.fixos['parede2']['imagem'],solidos.fixos['parede2']['ret'])
    screen.blit(solidos.fixos['parede3']['imagem'],solidos.fixos['parede3']['ret'])
    screen.blit(solidos.fixos['andar']['imagem'],solidos.fixos['andar']['ret'])

    #Desenhar o jogador
    if (estado['agacha']==False):
        screen.blit(personagens.jogador['imagem'],personagens.jogador['ret'])
    else:
        screen.blit(personagens.jogador['agacha'],personagens.jogador['ret'])

    #Printar os projeteis
    if (len(projeteis)>0):
        tam=len(projeteis)
        for n in range(tam):
            if (projeteis[n]['ret']!=''):                           #Precisamos pular o primeiro quadro
                screen.blit(projeteis[n]['img'],projeteis[n]['ret'])

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
