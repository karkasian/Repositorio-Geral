##SIAS com interface gráfica para o usuário
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/tree/master/SIAS
##2018

import sys                      #Módulo para controlar a taxa de quadro por segundo(QPS)
import pygame,sys               #Módulo para interface gráfica
from pygame.locals import *     #Códigos para as teclas

#ESTRUTURAS PRINCIPAIS ---------------------------------------------------------------------

class CPU:

    #ESTRUTURA DA CPU------------------------------------------------------------
    
    #UNIDADE LÓGICA E ARITMÉTICA
    class ULA:
        AC= '00000000 000000000000 00000000 000000000000'   #Acumulador: manter operandos e resultados das operações
        MQ= '00000000 000000000000 00000000 000000000000'   #Multiplicador: manter operandos e resultados das operações
        MBR='00000000 000000000000'     #Registrador de buffer da memória: recebe/envia palavra para memória/Entrada/Saida

        def circuito(conteudo,comando):
            #conteudo   - Coneúdo da memória que devemos trabalhar
            #Comando    - Comando definindo a operação que faremos

            global est
            global reg
            global deta
            global msg

            
            if (comando==1 or comando==0):  #Se é soma ou subtração
                estrutura_ULA.adicao.A=CPU.ULA.AC.replace(' ','')
                estrutura_ULA.adicao.B=conteudo.replace(' ','')
                estrutura_ULA.adicao.OF='0'
                est.append('imagens/Estrutura/mbr e ac - ula.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Adição/entrada.png')
                msg.append(['A <- AC e B <- MBR','A  : '+estrutura_ULA.adicao.A,'B  : '+estrutura_ULA.adicao.B,'OF: ' +'OF: 0'])
                memor.append(memoria.conteudo.copy())


                saida_complementador=estrutura_ULA.adicao.complementador()
                est.append('imagens/Estrutura/estrutura.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Adição/complementador.png')
                msg.append(['Saida do complemento: '+saida_complementador,'A  : '+estrutura_ULA.adicao.A,'B  : '+estrutura_ULA.adicao.B,'OF: 0'])
                memor.append(memoria.conteudo.copy())

                binario=estrutura_ULA.adicao.seletor(comando,saida_complementador)
                est.append('imagens/Estrutura/estrutura.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Adição/seletor.png')
                msg.append(['Operação: '+str(comando),'A  : '+estrutura_ULA.adicao.A,'B  : '+estrutura_ULA.adicao.B,'OF: 0'])
                memor.append(memoria.conteudo.copy())
                
                #Vamos montar os números pra somar
                (binario,estrutura_ULA.adicao.OF)=estrutura_ULA.adicao.somador(estrutura_ULA.adicao.A,binario)
                est.append('imagens/Estrutura/estrutura.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Adição/somador.png')
                msg.append(['Registrador A + '+binario,'A  : '+estrutura_ULA.adicao.A,'B  : '+estrutura_ULA.adicao.B,'OF: 0'])
                memor.append(memoria.conteudo.copy())
                
                #Vamos remontar o número
                CPU.ULA.AC=''
                for x in range (40):
                    if (x==8 or x==20 or x==28):
                        CPU.ULA.AC=CPU.ULA.AC+' '
                    CPU.ULA.AC=CPU.ULA.AC+binario[x]
                est.append('imagens/Estrutura/ula - ac.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Adição/saida.png')
                msg.append(['AC <- Resultado','A  : '+estrutura_ULA.adicao.A,'B  : '+estrutura_ULA.adicao.B,'OF: ' +str(estrutura_ULA.adicao.OF)])
                memor.append(memoria.conteudo.copy())
                
            elif (comando==2):          #Se é Multiplicação
                #INÍCIO
                        
                #VALORES INICIAIS
                contador=40                     #Inicializar o contador
                estrutura_ULA.multiplicacao.A='0000000000000000000000000000000000000000'
    
                estrutura_ULA.multiplicacao.Q=CPU.ULA.MBR.replace(' ','')
                estrutura_ULA.multiplicacao.C='0'
                estrutura_ULA.multiplicacao.M=CPU.ULA.MQ.replace(' ','')
            
                #booth('Valores iniciais')
                est.append('imagens/Estrutura/mbr e mq - ula.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Multiplicação/2.png')
                msg.append(['Q <- MBR e M <- MQ | Contador: '+str(contador),'A  : '+estrutura_ULA.multiplicacao.A,'Q  : '+estrutura_ULA.multiplicacao.Q,'Q-1: '+estrutura_ULA.multiplicacao.C,'M  : '+estrutura_ULA.multiplicacao.M])
                memor.append(memoria.conteudo.copy())
                
                #ESTRUTURA ITERATIVA
                n=contador                                      #Variável para nos ajudar a printar o ciclo na tela 
                while (True):               #Iteração
    
                    #ESTRUTURA CONDICIONAL 1
                    estr=estrutura_ULA.multiplicacao.Q[n-1]+estrutura_ULA.multiplicacao.C
                    est.append('imagens/Estrutura/estrutura.png')
                    reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                    deta.append('imagens/Multiplicação/3.png')
                    msg.append(['Q0,Q-1: '+estr,'A  : '+estrutura_ULA.multiplicacao.A,'Q  : '+estrutura_ULA.multiplicacao.Q,'Q-1: '+estrutura_ULA.multiplicacao.C,'M  : '+estrutura_ULA.multiplicacao.M])
                    memor.append(memoria.conteudo.copy())
                    
                    if (estr=='10'): #Vamos realizar a subtração
                        estrutura_ULA.adicao.A=estrutura_ULA.multiplicacao.A
                        estrutura_ULA.adicao.B=estrutura_ULA.multiplicacao.M
                        binario=estrutura_ULA.adicao.seletor(0,estrutura_ULA.adicao.complementador())
                        (binario,estrutura_ULA.adicao.OF)=estrutura_ULA.adicao.somador(estrutura_ULA.adicao.A,binario)
                        estrutura_ULA.multiplicacao.A=binario

                        est.append('imagens/Estrutura/estrutura.png')
                        reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                        deta.append('imagens/Multiplicação/4a.png')
                        msg.append([' ','A  : '+estrutura_ULA.multiplicacao.A,'Q  : '+estrutura_ULA.multiplicacao.Q,'Q-1: '+estrutura_ULA.multiplicacao.C,'M  : '+estrutura_ULA.multiplicacao.M])
                        memor.append(memoria.conteudo.copy())
                        
                    elif (estr=='01'): #Vamos realizar a adição
                        estrutura_ULA.adicao.A=estrutura_ULA.multiplicacao.A
                        estrutura_ULA.adicao.B=estrutura_ULA.multiplicacao.M
                        binario=estrutura_ULA.adicao.seletor(1,estrutura_ULA.adicao.complementador())
                        (binario,estrutura_ULA.adicao.OF)=estrutura_ULA.adicao.somador(estrutura_ULA.adicao.A,binario)
                        estrutura_ULA.multiplicacao.A=binario

                        est.append('imagens/Estrutura/estrutura.png')
                        reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                        deta.append('imagens/Multiplicação/4b.png')
                        msg.append([' ','A  : '+estrutura_ULA.multiplicacao.A,'Q  : '+estrutura_ULA.multiplicacao.Q,'Q-1: '+estrutura_ULA.multiplicacao.C,'M  : '+estrutura_ULA.multiplicacao.M])
                        memor.append(memoria.conteudo.copy())
                        
                    #DESLOCAMENTO
                    (estrutura_ULA.multiplicacao.A,estrutura_ULA.multiplicacao.Q,estrutura_ULA.multiplicacao.C)=funcao_ULA.deslocamento(estrutura_ULA.multiplicacao.A,estrutura_ULA.multiplicacao.Q,estrutura_ULA.multiplicacao.C)  #Vamos realizar o deslocamento
                    contador=contador-1

                    est.append('imagens/Estrutura/estrutura.png')
                    reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                    deta.append('imagens/Multiplicação/5.png')
                    msg.append(['Contador: '+str(contador) ,'A  : '+estrutura_ULA.multiplicacao.A,'Q  : '+estrutura_ULA.multiplicacao.Q,'Q-1: '+estrutura_ULA.multiplicacao.C,'M  : '+estrutura_ULA.multiplicacao.M])
                    memor.append(memoria.conteudo.copy())
                    
                    #ESTRUTURA CONDICIONAL 2
                    est.append('imagens/Estrutura/estrutura.png')
                    reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                    deta.append('imagens/Multiplicação/6.png')
                    msg.append(['Contador: '+str(contador) ,'A  : '+estrutura_ULA.multiplicacao.A,'Q  : '+estrutura_ULA.multiplicacao.Q,'Q-1: '+estrutura_ULA.multiplicacao.C,'M  : '+estrutura_ULA.multiplicacao.M])
                    memor.append(memoria.conteudo.copy())
                    
                    if(contador==0):
                        break

                #Agora precisamos montar os números
                CPU.ULA.AC=''
                CPU.ULA.MQ=''
                for x in range (40):
                    if (x==8 or x==20 or x==28):
                        CPU.ULA.AC=CPU.ULA.AC+' '
                        CPU.ULA.MQ=CPU.ULA.MQ+' '
                    CPU.ULA.AC=CPU.ULA.AC+estrutura_ULA.multiplicacao.A[x]
                    CPU.ULA.MQ=CPU.ULA.MQ+estrutura_ULA.multiplicacao.Q[x]

                est.append('imagens/Estrutura/ula - ac e mq.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Multiplicação/7.png')
                msg.append([' AC <- A e MQ <- Q ','A  : '+estrutura_ULA.multiplicacao.A,'Q  : '+estrutura_ULA.multiplicacao.Q,'Q-1: '+estrutura_ULA.multiplicacao.C,'M  : '+estrutura_ULA.multiplicacao.M])
                memor.append(memoria.conteudo.copy())
                
    #UNIDADE DE CONTROLE
    class UC:
        IBR='00000000 000000000000'     #Registrador de Buffer da instrução: próxima instrução a ser executada
        PC= '000000000000'              #Contador de programa: endereço do próximo par de instruções
        IR= '00000000'                  #Registrador de instrução: opcode da instrução sendo executada
        MAR='000000000000'              #Registrador de endereço da memória: endereço da memória da palavra a ser escrita/lida no MBR

        #Função do ciclo de instrução
        def ciclo_instrucao():
            
            #Ciclo de instrução
            while(True):
                funcao_UC.busca()       #Ciclo de busca
                funcao_UC.execucao()    #Ciclo de execucao               
                #break

#MEMÓRIA PRINCIPAL
class memoria:
    #             [  Opcode    Endereço  |  Opcode  Endereço    ]
    conteudo=1024*['00000000 000000000000 00000000 000000000000']   #Conteudo       

#ENTRADA/SAÍDA:
class ES:
    memoria.conteudo[0]=  '00000000 000000000000 00000001 000000010100'
    memoria.conteudo[1]=  '00000101 000000010101 00000110 000000010101'
    memoria.conteudo[2]=  '00100001 000000010110 00001001 000000010101'
    memoria.conteudo[3]=  '00001010 000000000000 00000010 000000010100'
    memoria.conteudo[4]=  '00000011 000000010100 00000001 000000010100'
    memoria.conteudo[5]=  '00001101 000000000111 00000000 000000000000'
    memoria.conteudo[7]=  '00001110 000000001001 00000000 000000000000'
    memoria.conteudo[9]=  '00000000 000000000000 00001111 000000001011'
    memoria.conteudo[11]= '00000000 000000000000 00010000 000000001101'
    memoria.conteudo[13]= '00000000 000000000000 00010010 000000010100'
    memoria.conteudo[14]= '00000000 000000000000 00010010 000000010100'
#    memoria.conteudo[11]= '00010100 000000010101 00010101 000000010101'
#    memoria.conteudo[20]= '11111111 111111111111 11111111 111111111111'
    memoria.conteudo[21]= '00000000 000000000000 00000000 000000000011'
##    #FALTA MUL, ADD e SUB ||

#ESTRUTURAS INTERNAS------------------------------------------------------------

#Estrutura ULA
class estrutura_ULA:

    #Adição e subtração
    class adicao:
        A='0000000000000000000000000000000000000000'    #Registrador A
        B='0000000000000000000000000000000000000000'    #Registrador B
        OF=0                                            #Bit de overflow

        #Função para pegar a negação do número
        def complementador (*conteudo):
            #binario    - Número binário que vamos pegar a negacao
            res=''      #Onde vamos guardar o resultado
            som=''      #Onde vamos guardar o 1 que vamos somar
            for bit in range(40):      #Vamos percorrer bit a bit o número
                if (estrutura_ULA.adicao.B[bit]=='0'):       #Se é 0
                    res=res+'1'         #Guardamos 1
                else:                   #Se não
                    res=res+'0'         #Guardamos 0
                if(bit==39):         #Se é o último bit
                    som=som+'1'         #Guardamos o 1
                else:                   #Se não
                    som=som+'0'         #Adicionamos outro 0

            (res,OF)=estrutura_ULA.adicao.somador(res,som)
            return (res)                #Retornamos a soma

        #Função para selecionar
        def seletor (operacao,complementado):
            #operacao       - Seleciona o tipo de operação
            #binario        - Número enviado
            #complementado  - Número binário negado

            if (operacao==0):
                return complementado
            else:
                return estrutura_ULA.adicao.B

        #Estrutura para somar
        def somador (um,dois):
            #um     - Primeiro número a ser somado
            #dois   - Segundo número a ser somado         
            
            tam=len(um)                     #Vamos pegar o tamanho
            res=[]                          #Vamos guardar o resultado
            elev=0                          #Vamos guardar o valor elevado
            for bit in range(tam-1,-1,-1):  #Vamos percorrer bit a bit o número
                (r,elev)=funcao_ULA.bit_a_bit(int(um[bit]),int(dois[bit]),elev)   #Vamos somar todos os bits
                res.append(r)               #Salvamos o resultado
                
            #Agora vamos montar o resultado
            resposta=''                     #Onde vamos guardar a resposta
            
            for bit in range (tam-1,-1,-1): #Montamos nossa resposta
                resposta=resposta+str(res[bit])

            #Vamos checar se houve overflow
            of=funcao_ULA.overflow(um,dois,resposta)
            return (resposta,of)                                           #Retornamos a resposta

    #Multiplicação
    class multiplicacao:
        Q='0000000000000000000000000000000000000000'    #Multiplicador
        M='0000000000000000000000000000000000000000'    #Multiplicando
        A='0000000000000000000000000000000000000000'    #Registrador A
        C='0'    #Registrador de um bit


#FUNÇÕES ESPECÍFICAS------------------------------------------------------------

#Funções relacionadas a ULA
class funcao_ULA:
    #Checar se houve overflow
    def overflow(um,dois,res):
        #um     - Primeiro número somado
        #dois   - Segundo número somado
        #res    - Resultado da soma
        
        if (um[0]!=dois[0]):        #Se os sinais são diferentes
            return 0              #Não houve overflow
        else:                       #Se são iguais
            if (um[0]==res[0]):     #Se a resposta tem o mesmo sinal dos números
                return (0)            #Não houve overflow
            else:                   #Se o sinal é diferente
                return (1)            #Houve
    
    #Regras da adição
    def regras_adicao(um,dois):
        #um     - Primeiro bit
        #dois   - Segundo bit

        #Vamos trabalhar com os casos:
        if (um==0 and dois ==0):    #0+0
            return (0,0)
        elif (um==0 and dois ==1):  #0+1
            return (1,0)
        elif (um==1 and dois==0):   #1+0
            return (1,0)
        else:                       #1+1
            return (0,1)
        
    #Para obtermos um bit da soma
    def bit_a_bit (um, dois, e):
        #um     - Primeiro bit
        #dois   - Segundo bit
        #e      - Bit resultado de soma anterior

        if(e==0):   #Se não temos de um anterior, apenas somamos:
            (res,elev)=funcao_ULA.regras_adicao(um,dois)
        else:       #Se temos
            if (um==0):      #E o primeiro é zero
                (res,elev)=funcao_ULA.regras_adicao(e,dois)        #Somamos ao segundo
            elif(dois==0):  #Se não mas o segundo é:
                (res,elev)=funcao_ULA.regras_adicao(e,um)          #Somamos ao primeiro
            else:           #Se nenhum é zero
                (res,elev1)=funcao_ULA.regras_adicao(e,um)         #Somamos ao primeiro
                (res,elev2)=funcao_ULA.regras_adicao(res,dois)     #E somamos o resultado ao segundo
                (elev,des)=funcao_ULA.regras_adicao(elev1,elev2)   #E retornamos a soma dos elevados
        return (res,elev)

    #Para realizarmos o deslocamento da multiplicação:
    def deslocamento(A,Q,C):
        #A              - Registrador A
        #Q              - Registrador Q
        #C              - Registrador C

        nC=Q[39]       #Nosso novo C
        nQ=''           #Onde vamos armazenar nosso novo Q
        nA=''           #Onde vamos armazenar nosso novo A
        nQ=nQ+A[39]    #Primeiro elemento do Q
        nA=A[0]         #Primeiro elemento do A
        for x in range (39):   #Vamos percorrer até o penúltimo elemento
            nQ=nQ+Q[x]
            nA=nA+A[x]

        return (nA,nQ,nC)       #Retornamos os valores

#Funções relacionadas a UC
class funcao_UC:
    #Função para checar se tem instrução a esquerda do conteúdo
    def esquerda(conteudo):
        #conteudo   - Conteúdo que vamos analisar
        
        quebrado=conteudo.split(' ')
        if (quebrado[0]=='00000000'):
            return False
        else:
            return True

    #Ciclo de busca
    def busca():

        global est
        global reg
        global deta
        global msg

        est.append('imagens/Estrutura/estrutura.png')
        reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
        deta.append('imagens/Ciclo/c2.png')
        msg.append(None)
        memor.append(memoria.conteudo.copy())
        
        if(CPU.UC.IBR!='00000000 000000000000'):                                    #Sim
            CPU.UC.IR=CPU.UC.IBR.split(' ')[0]                                      #IR <- IBR(0:7)
            CPU.UC.MAR=CPU.UC.IBR.split(' ')[1]                                     #MAR <- IBR(8:19)
            CPU.UC.IBR='00000000 000000000000'     #Vamos zerar o IBR

            est.append('imagens/Estrutura/ibr - ir e mar.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Ciclo/c3b.png')
            msg.append(None)
            memor.append(memoria.conteudo.copy())

            (CPU.UC.PC,OF)=estrutura_ULA.adicao.somador(CPU.UC.PC.replace(' ',''),'000000000001')   #PC <- PC+1 

            est.append('imagens/Estrutura/estrutura.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Ciclo/c7.png')
            msg.append(None)
            memor.append(memoria.conteudo.copy())
            
        else:                                                                       #Não
            CPU.UC.MAR=CPU.UC.PC                                                    #MAR <- PC

            est.append('imagens/Estrutura/pc - mar.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Ciclo/c3a.png')
            msg.append(None)
            memor.append(memoria.conteudo.copy())
            
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  #MBR <- M(MAR)

            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Ciclo/c4.png')
            msg.append(None)
            memor.append(memoria.conteudo.copy())

            est.append('imagens/Estrutura/estrutura.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Ciclo/c5.png')
            msg.append(None)
            memor.append(memoria.conteudo.copy())
            
            if(funcao_UC.esquerda(CPU.ULA.MBR)):                                    #Sim
                CPU.UC.IBR=CPU.ULA.MBR.split(' ')[2]+' '+CPU.ULA.MBR.split(' ')[3]  #IBR <- MBR(20:39)
                CPU.UC.IR=CPU.ULA.MBR.split(' ')[0]                                 #IR <- MBR(0:7)
                CPU.UC.MAR=CPU.ULA.MBR.split(' ')[1]                                #MAR <- MBR(8:19)

                est.append('imagens/Estrutura/mbr - ir mar e ibr.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Ciclo/c6b.png')
                msg.append(None)
                memor.append(memoria.conteudo.copy())
            else:                                                                   #Não                        
                CPU.UC.IR=CPU.ULA.MBR.split(' ')[2]                                 #IR <- MBR (20:27)
                CPU.UC.MAR=CPU.ULA.MBR.split(' ')[3]                                #MAR <- MBR (28:39)

                est.append('imagens/Estrutura/mbr - ir e mar.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Ciclo/c6a.png')
                msg.append(None)
                memor.append(memoria.conteudo.copy())

                (CPU.UC.PC,OF)=estrutura_ULA.adicao.somador(CPU.UC.PC.replace(' ',''),'000000000001')               #PC<-PC+1

                est.append('imagens/Estrutura/estrutura.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Ciclo/c7.png')
                msg.append(None)
                memor.append(memoria.conteudo.copy())

    #Ciclo de execução
    def execucao():

        #Se não temos instrução
        if (CPU.UC.IR=='00000000'):
            print('Nenhuma instrução')
            GUI()

        #LOAD M(X)  Transfere M(X) para AC
        elif(CPU.UC.IR=='00000001'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['LOAD M(X)','MBR <- M(MAR)'])
            memor.append(memoria.conteudo.copy())

            CPU.ULA.AC=CPU.ULA.MBR                                                  #AC <- MBR
            est.append('imagens/Estrutura/mbr - ac.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['LOAD M(X)','AC<-MBR'])
            memor.append(memoria.conteudo.copy())

        #ADD M(X) Soma M(X) a AC e coloca o resultado em AC
        elif(CPU.UC.IR=='00000101'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Adição/adicao.png')
            msg.append(['ADD(X)','MBR <- M(MAR)','A  : 0000000000000000000000000000000000000000','B  : 0000000000000000000000000000000000000000','OF: 0'])
            memor.append(memoria.conteudo.copy())
            
            CPU.ULA.circuito(CPU.ULA.MBR,1)

        #SUB M(X) Subtrai M(X) a AC e coloca o resultado em AC
        elif(CPU.UC.IR=='00000110'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Adição/adicao.png')
            msg.append(['SUB(X)','MBR <- M(MAR)','A  : 0000000000000000000000000000000000000000','B  : 0000000000000000000000000000000000000000','OF: 0'])
            memor.append(memoria.conteudo.copy())
            
            CPU.ULA.circuito(CPU.ULA.MBR,0)

        #STOR M(X) Transfere o conteudo de AC parao local de memória X
        elif(CPU.UC.IR=='00100001'):
            CPU.ULA.MBR=CPU.ULA.AC                                  #MBR<-AC
            est.append('imagens/Estrutura/ac - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['STOR(X)','MBR <- AC'])
            memor.append(memoria.conteudo.copy())

            func_memoria.stor(CPU.UC.MAR,CPU.ULA.MBR)               #M(MAR) <- MBR           
            est.append('imagens/Estrutura/mbr - mmar.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['STOR(X)','M(MAR) <- MBR'])
            memor.append(memoria.conteudo.copy())
            
        #LOAD MQ Transfere o conteudo de MQ para AC
        elif(CPU.UC.IR=='00001010'):
            CPU.ULA.AC=CPU.ULA.MQ                                   #AC<-MQ
            est.append('imagens/Estrutura/mq - ac.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['LOAD MQ','AC <- MQ'])
            memor.append(memoria.conteudo.copy())

         #LOAD MQ M(X) Transfere o conteudo de X para MQ
        elif(CPU.UC.IR=='00001001'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['LOAD MQ,M(X)','MBR <- M(MAR)'])
            memor.append(memoria.conteudo.copy())
            
            CPU.ULA.MQ=CPU.ULA.MBR                                                  #MQ <- MBR
            est.append('imagens/Estrutura/mbr - mq.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['LOAD MQ,M(X)','MQ <- MBR'])
            memor.append(memoria.conteudo.copy())

        #LOAD -M(X) Transfere -M(X) para o AC
        elif(CPU.UC.IR=='00000010'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['LOAD -M(X)','MBR <- M(MAR)'])
            memor.append(memoria.conteudo.copy())
            
            estrutura_ULA.adicao.B=CPU.ULA.MBR.replace(' ','')                      #B<- MBR
            binario=estrutura_ULA.adicao.complementador()                       #MBR <- -B
            bina=''
            #Vamos remontar o número
            for x in range (40):
                    if (x==8 or x==20 or x==28):
                        bina=bina+' '
                    bina=bina+binario[x]
            est.append('imagens/Estrutura/mbr - ula.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['LOAD -M(X)','ULA <- MBR'])
            memor.append(memoria.conteudo.copy())

            CPU.ULA.AC=bina                                                  #AC <- MBR
            est.append('imagens/Estrutura/ula - ac.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['LOAD -M(X)','AC <- ULA'])
            memor.append(memoria.conteudo.copy())

        #LOAD M|(X)| Transfere o valor absoluta de M(X) para AC
        elif(CPU.UC.IR=='00000011'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['LOAD M|(X)|','MBR <- M(MAR)'])
            memor.append(memoria.conteudo.copy())

            if(CPU.ULA.MBR[0]=='0'):        #Vamos checar se o número já é positivo
                CPU.ULA.AC=CPU.ULA.MBR      #Se é positivo so salvamos              #AC <- MBR
                est.append('imagens/Estrutura/mbr - ac.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['LOAD M|(X)|','É Positivo? Sim.','AC < - mbr'])
                memor.append(memoria.conteudo.copy())
            else:                           #Se é negativo pegamos o complemento
                estrutura_ULA.adicao.B=CPU.ULA.MBR.replace(' ','')                      #B<- MBR
                est.append('imagens/Estrutura/mbr - ula.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['LOAD M|(X)|','É Positivo? Não.','ULA <- MBR'])
                memor.append(memoria.conteudo.copy())

                binario=estrutura_ULA.adicao.complementador()                       #MBR <- -B
                bina=''
                #Vamos remontar o número
                for x in range (40):
                    if (x==8 or x==20 or x==28):
                        bina=bina+' '
                    bina=bina+binario[x]
                CPU.ULA.AC=bina                                                 #AC <- MBR
                est.append('imagens/Estrutura/ula - AC.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['LOAD M|(X)|','AC <- ULA'])
                memor.append(memoria.conteudo.copy())
                
        #LOAD -M|(X)| Transfere o valor  de -|M(X)| para AC
        elif(CPU.UC.IR=='00000100'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['LOAD -M|(X)|','MBR <- M(MAR)'])
            memor.append(memoria.conteudo.copy())
            
            if(CPU.ULA.MBR[0]=='1'):        #Vamos checar se o número já é negativo
                CPU.ULA.AC=CPU.ULA.MBR      #Se é positivo so salvamos              #AC <- MBR
                est.append('imagens/Estrutura/mbr - ac.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['LOAD -M|(X)|','É negativo? Sim.','AC < - mbr'])
                memor.append(memoria.conteudo.copy())
                
            else:                           #Se é negativo pegamos o complemento
                estrutura_ULA.adicao.B=CPU.ULA.MBR.replace(' ','')                      #B<- MBR
                binario=estrutura_ULA.adicao.complementador()                       #MBR <- -B
                bina=''
                #Vamos remontar o número
                for x in range (40):
                    if (x==8 or x==20 or x==28):
                        bina=bina+' '
                    bina=bina+binario[x]
                est.append('imagens/Estrutura/mbr - ula.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['LOAD -M|(X)|','É Positivo? Não.','ULA <- MBR'])         
                memor.append(memoria.conteudo.copy())
                
                CPU.ULA.AC=bina                                                  #AC <- MBR
                est.append('imagens/Estrutura/ula - AC.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['LOAD -M|(X)|','AC <- ULA'])
                memor.append(memoria.conteudo.copy())
                
        #JUMP M(X,0:19) Apanha a proxima instrução da metade esquerda de m(X)
        elif(CPU.UC.IR=='00001101'):
            CPU.UC.PC=CPU.UC.MAR                                  # PC <- MAR           
            est.append('imagens/Estrutura/mar - pc.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['JUMP M(X,0:19)','PC <- MAR'])
            memor.append(memoria.conteudo.copy())

        #JUMP M(X,20:39) Apanha a proxima instrução da metade direita de m(X)
        elif(CPU.UC.IR=='00001110'):
            CPU.UC.PC=CPU.UC.MAR                                  # PC<-MAR
            est.append('imagens/Estrutura/mar - pc.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['JUMP M(X,20:39)','PC <- MAR'])
            memor.append(memoria.conteudo.copy())
            
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['JUMP M(X,20:39)','MBR<-M(MAR)'])
            memor.append(memoria.conteudo.copy())

            CPU.UC.IBR=CPU.ULA.MBR.split(' ')[2]+' '+CPU.ULA.MBR.split(' ')[3]      #IBR <- MBR(20:39)
            est.append('imagens/Estrutura/mbr - ibr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['JUMP M(X,20:39)','IBR <- MBR(20:39)'])
            memor.append(memoria.conteudo.copy())

        #JUMP+ M(X,0:19) Se o número no AC for não negativo, apanha a proxima instrução da metade esquerda
        elif(CPU.UC.IR=='00001111'):
        
            if(CPU.ULA.AC[0]=='0'):        #Vamos checar se o número é positivo
                CPU.UC.PC=CPU.UC.MAR                                  # PC<-MAR
                est.append('imagens/Estrutura/pc - mar.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['JUMP+ M(X,0:19)','O Número é positivo? Sim.','PC <- MAR'])
                memor.append(memoria.conteudo.copy())
            else:
                est.append('imagens/Estrutura/estrutura.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['JUMP+ M(X,0:19)','O Número é positivo? Não.'])
                memor.append(memoria.conteudo.copy())

        #JUMP+ M(X,20:39) Se o número no AC for não negativo, apanha a proxima instrução da metade direita
        elif(CPU.UC.IR=='00010000'):
        
            if(CPU.ULA.AC[0]=='0'):        #Vamos checar se o número já é positivo
                CPU.UC.PC=CPU.UC.MAR                                  # PC<-MAR
                est.append('imagens/Estrutura/mar - pc.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['JUMP+ M(X,20:39)','O Número é positivo? SIM.','PC <- MAR'])
                memor.append(memoria.conteudo.copy())

                CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
                est.append('imagens/Estrutura/mmar - mbr.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['JUMP+ M(X,20:39)','MBR<-M(MAR)'])
                memor.append(memoria.conteudo.copy())

                CPU.UC.IBR=CPU.ULA.MBR.split(' ')[2]+' '+CPU.ULA.MBR.split(' ')[3]      #IBR <- MBR(20:39)
                est.append('imagens/Estrutura/mbr - ibr.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['JUMP+ M(X,20:39)','IBR <- MBR(20:39)'])
                memor.append(memoria.conteudo.copy())

            else:
                est.append('imagens/Estrutura/estrutura.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['JUMP+ M(X,20:39)','O Número é positivo? Não.'])
                memor.append(memoria.conteudo.copy())

        #STOR M(X,8:19) Substitui o campo de endereço da esquerda em M(X) por 12 bits mais a direita de AC
        elif(CPU.UC.IR=='00010010'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['STOR M(X,8:19)','MBR <- M(MAR)'])
            memor.append(memoria.conteudo.copy())          

            CPU.ULA.MBR=CPU.ULA.MBR.split(' ')[0]+' '+CPU.ULA.AC.split(' ')[3]+' '+CPU.ULA.MBR.split(' ')[2]+' '+CPU.ULA.MBR.split(' ')[3]     #Passamos os 12 bits
            est.append('imagens/Estrutura/ac - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['STOR M(X,8:19)','MBR (8:19) <- AC (8:19)'])
            memor.append(memoria.conteudo.copy())          

            func_memoria.stor(CPU.UC.MAR,CPU.ULA.MBR)               #M(MAR) <- MBR
            est.append('imagens/Estrutura/mbr - mmar.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['STOR M(X,8:19)','M(MAR) <- MBR'])
            memor.append(memoria.conteudo.copy())
            
        #STOR M(X,28:39) Substitui o campo de endereço da direita em M(X) por 12 bits mais a direita de AC
        elif(CPU.UC.IR=='00010011'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['STOR M(X,28:39)','MBR <- M(MAR)'])
            memor.append(memoria.conteudo.copy())
                           
            CPU.ULA.MBR=CPU.ULA.MBR.split(' ')[0]+' '+CPU.ULA.MBR.split(' ')[1]+' '+CPU.ULA.MBR.split(' ')[2]+' '+CPU.ULA.AC.split(' ')[3]     #Passamos os 12 bits
            est.append('imagens/Estrutura/ac - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['STOR M(X,28:39)','MBR (8:19) <- AC (28:39)'])
            memor.append(memoria.conteudo.copy())          

            func_memoria.stor(CPU.UC.MAR,CPU.ULA.MBR)               #M(MAR) <- MBR
            est.append('imagens/Estrutura/mbr - mmar.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['STOR M(X,28:39)','M(MAR) <- MBR'])
            memor.append(memoria.conteudo.copy())          

        #ADD |M(X)| Soma |M(X)| a AC e coloca o resultado em AC
        elif(CPU.UC.IR=='00000111'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['ADD |M(X)|','MBR <- M(MAR)'])
            memor.append(memoria.conteudo.copy())          

            if(CPU.ULA.MBR[0]!='0'):        #Vamos checar se o número já é positivo
                #Se é negativo pegamos o complemento
                estrutura_ULA.adicao.B=CPU.ULA.MBR.replace(' ','')                      #B<- MBR
                est.append('imagens/Estrutura/mbr - ula.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['ADD |M(X)|','O Número é negativo','ULA <- MBR'])
                memor.append(memoria.conteudo.copy())          

                binario=estrutura_ULA.adicao.complementador()                       #MBR <- -B
                CPU.ULA.MBR=''
                #Vamos remontar o número
                for x in range (40):
                    if (x==8 or x==20 or x==28):
                        CPU.ULA.MBR=CPU.ULA.MBR+' '
                    CPU.ULA.MBR=CPU.ULA.MBR+binario[x]
                est.append('imagens/Estrutura/ula - mbr.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['ADD |M(X)|','Negação do número','MBR <- ULA'])
                memor.append(memoria.conteudo.copy())          

            CPU.ULA.circuito(CPU.ULA.MBR,1)

        #SUB|M(X)| subtrai |M(X)| de AC e coloca o resultado em AC
        elif(CPU.UC.IR=='00001000'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['SUB |M(X)|','MBR <- M(MAR)'])
            memor.append(memoria.conteudo.copy())

            if(CPU.ULA.MBR[0]!='0'):        #Vamos checar se o número já é positivo
                estrutura_ULA.adicao.B=CPU.ULA.MBR.replace(' ','')                      #B<- MBR
                est.append('imagens/Estrutura/mbr - ula.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['SUB |M(X)|','O Número é negativo','ULA <- MBR'])
                memor.append(memoria.conteudo.copy())
                           
                binario=estrutura_ULA.adicao.complementador()                       #MBR <- -B
                CPU.ULA.MBR=''
                #Vamos remontar o número
                for x in range (40):
                    if (x==8 or x==20 or x==28):
                        CPU.ULA.MBR=CPU.ULA.MBR+' '
                    CPU.ULA.MBR=CPU.ULA.MBR+binario[x]
                est.append('imagens/Estrutura/ula - mbr.png')
                reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
                deta.append('imagens/Outros/branco.png')
                msg.append(['SUB |M(X)|','Negação do número','MBR <- ULA'])
                memor.append(memoria.conteudo.copy())

            CPU.ULA.circuito(CPU.ULA.MBR,0)

        #LSH  multiplca AC por 2 desloca a esquerda uma posição de bit
        elif(CPU.UC.IR=='00010100'):
            binario=CPU.ULA.AC.replace(' ','')
            CPU.ULA.AC=''
            for x in range(1,40):
                if (x==9 or x==21 or x==29):
                        CPU.ULA.AC=CPU.ULA.AC+' '
                CPU.ULA.AC=CPU.ULA.AC+binario[x]
                
            CPU.ULA.AC=CPU.ULA.AC+'0'
            est.append('imagens/Estrutura/estrutura.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['LSH','AC * 2 | Desloca um bit a esquerda'])
            memor.append(memoria.conteudo.copy())

        #RSH  divide AC por 2 desloca a esquerda uma posição de bit
        elif(CPU.UC.IR=='00010101'):
            binario=CPU.ULA.AC.replace(' ','')
            CPU.ULA.AC='0'
            for x in range(0,39):
                if (x==7 or x==19 or x==27):
                        CPU.ULA.AC=CPU.ULA.AC+' '
                CPU.ULA.AC=CPU.ULA.AC+binario[x]
            est.append('imagens/Estrutura/estrutura.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Outros/branco.png')
            msg.append(['RSH','AC / 2 | Desloca um bit a direita'])
            memor.append(memoria.conteudo.copy())

        #MUL(X) multiplica M(X) por MQ e coloca os bits mais significativos do resultado em AC
        elif(CPU.UC.IR=='00001011'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            est.append('imagens/Estrutura/mmar - mbr.png')
            reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
            deta.append('imagens/Multiplicação/1.png')
            msg.append(['MUL(X)','MBR<-M(MAR)','A  : 0000000000000000000000000000000000000000','Q  : 0000000000000000000000000000000000000000','Q-1: 0','M  : 0000000000000000000000000000000000000000'])
            memor.append(memoria.conteudo.copy())
             
            CPU.ULA.circuito(CPU.ULA.MBR,2)
            
        else:
            print('Op code inválido.')
            GUI()
        
#Funções relacionadas a memória memória
class func_memoria:
    endereco=[]                             #Endereços
    for i in range (1024):
        binario=bin(i).split('0b')[1]       #Convertemos o decimal para binário
        while (len(binario)<12):            #Se é menor que 12                        
                binario='0'+binario         #Adicionamos um 
        endereco.append(binario)            #E retornamos

    #Função para associar o endereço ao conteudo
    def M(end):
        #end    - Endereço do conteúdo que buscamos
        for i in range (1024):
            if (end==func_memoria.endereco[i]):     #Se estamos no endereço correspondente ao argumento
                return memoria.conteudo[i]          #Retornamos o conteudo equivalente

    #Função para passaro conteudo para determinado endereço
    def stor(endereco, conteudo):
        #endereco   - Onde vamos guardar o conteudo
        #conteudi   - Conteudo que vamos guardar
        for i in range (1024):
            if (endereco==func_memoria.endereco[i]):    #Se estamos no endereço correspondente ao argumento
                memoria.conteudo[i]=conteudo            #Retornamos o conteudo equivalente
 

#SIMULADOR----------------------------------------------------------------------

#Iniciamos o PC
def start():
    global est
    global reg
    global deta
    global msg

    est.append('imagens/Estrutura/estrutura.png')
    reg.append([CPU.ULA.AC,CPU.ULA.MQ,CPU.ULA.MBR,CPU.UC.IBR,CPU.UC.PC,CPU.UC.IR,CPU.UC.MAR])
    deta.append('imagens/Ciclo/c1.png')
    msg.append(None)
    memor.append(memoria.conteudo.copy())

    CPU.UC.ciclo_instrucao()

#Vetores pra animação
est=[]  #Estrutura expandida
reg=[]  #Registradores principais
deta=[] #Detalhes da execução em específico
msg=[]  #Textos da execução em específico
memor=[]#Para guardar a memória
memor.append(memoria.conteudo.copy())
#Interface gráfica
def GUI():
    # Define algumas cores em RGB
    PRETO  = (0, 0, 0)
    BRANCO = (255, 255, 255)

    # Inicializa a biblioteca
    pygame.init()

    # Define a largura e altura da janela em pixels 800x600
    size = (1366, 690)
    screen = pygame.display.set_mode(size)

    # Utilizado para controlar a velocidade de quadros (de atualizacoes da tela)
    clock = pygame.time.Clock()

    # Define um nome para a janela
    pygame.display.set_caption("SIAS")

    #Variável de controle
    c=0

    #Configura a fonte
    fonte = pygame.font.SysFont(None,21)

    #Configura as imagens
    vet_imgsp=[]     #Vetor que vamos guardar as imagens principais
    vet_retp=[]      #Vetor que vamos guardar as posições destas imagens
    vet_imgss=[]     #Vetor que vamos guardar as imagens secundárias
    vet_rets=[]      #Vetor que vamos guardar as posições destas imagens



    for x in range(len(est)):
        i=pygame.image.load(est[x])
        r= i.get_rect()
        ii=pygame.image.load(deta[x])
        rr= ii.get_rect()
        rr.topright=(1366,0)
        
        vet_imgsp.append(i)
        vet_retp.append(r)
        vet_imgss.append(ii)
        vet_rets.append(rr)

    #Define se vamos automático e variável auxiliar
    aut=False
    con=0
    # Loop principal do jogo
    while True:

        if (aut==False):
            for event in pygame.event.get():
                if event.type==KEYDOWN:
                    if event.key == K_RIGHT:
                        c=c+1
                    if event.key == K_LEFT:
                        c=c-1
                    if event.key == K_UP:
                        aut=True
                    if event.key == K_DOWN:
                        aut=None
                    if event.key == K_ESCAPE:
                        pygame.quit()
                        sys.exit()
                        
        elif (aut==True):
            if(con==1):
                c=c+1
                con=0
            con=con+1
        else:
            if(con==1):
                c=c-1
                con=0
            con=con+1

        
                    
        if (c==len(est)):
            c=len(est)-1
            aut=False
            con=0
            
        elif(c<0):
            c=0
            aut=False
            con=0

        # Preenche a tela com uma cor, neste caso preto (definido logo apos importar as bibliotecas)
        screen.fill(BRANCO)

        #Desenha o fluxograma principal
        screen.blit(vet_imgsp[c],vet_retp[c])
        #Desenha o fluxograma secundário
        screen.blit(vet_imgss[c],vet_rets[c])

        #Vamos desenhar os registradores principais:
        texto=fonte.render("REGISTRADORES",1,PRETO)
        textoret=texto.get_rect()
        textoret.topleft=(5,475)
        screen.blit(texto,textoret)
        
        texto=fonte.render("AC : "+reg[c][0],1,PRETO)
        textoret=texto.get_rect()
        textoret.topleft=(5,500)
        screen.blit(texto,textoret)

        texto=fonte.render("MQ : "+reg[c][1],1,PRETO)
        textoret=texto.get_rect()
        textoret.topleft=(5,525)
        screen.blit(texto,textoret)

        texto=fonte.render("MBR: "+reg[c][2],1,PRETO)
        textoret=texto.get_rect()
        textoret.topleft=(5,550)
        screen.blit(texto,textoret)

        texto=fonte.render("IBR : "+reg[c][3],1,PRETO)
        textoret=texto.get_rect()
        textoret.topleft=(5,575)
        screen.blit(texto,textoret)

        texto=fonte.render("PC : "+reg[c][4],1,PRETO)
        textoret=texto.get_rect()
        textoret.topleft=(5,600)
        screen.blit(texto,textoret)

        texto=fonte.render("IR : "+reg[c][5],1,PRETO)
        textoret=texto.get_rect()
        textoret.topleft=(5,625)
        screen.blit(texto,textoret)

        texto=fonte.render("MAR: "+reg[c][6],1,PRETO)
        textoret=texto.get_rect()
        textoret.topleft=(5,650)
        screen.blit(texto,textoret)

        texto=fonte.render("MEMÓRIA PRINCIPAL",1,PRETO)
        textoret=texto.get_rect()
        textoret.topleft=(400,0)
        screen.blit(texto,textoret)

        #Vamos printar parte da memória principal
        for x in range(33):
            num=str(x)
            if(x<10):
                num='000'+num
            elif(x<100):
                num='00'+num
            elif(x<1000):
                num='0'+num
            msgm='['+num+']: '+memor[c][x]
            
            texto=fonte.render(msgm,1,PRETO)
            textoret=texto.get_rect()
            textoret.topleft=(400,25+x*20)
            screen.blit(texto,textoret)

        if (msg[c]!=None):
            for x in range(len(msg[c])):
                texto=fonte.render(msg[c][x],1,PRETO)
                textoret=texto.get_rect()
                textoret.topleft=(800,400+x*20)
                screen.blit(texto,textoret)

        
        # Atualiza a tela visivel ao usuario
        pygame.display.flip()

        # Limita a taxa de quadros (framerate) a 60 quadros por segundo (60fps)
        clock.tick(30)
start()
