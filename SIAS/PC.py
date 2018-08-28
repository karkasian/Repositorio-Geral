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

            
            if (comando==1 or comando==0):  #Se é soma ou subtração
                print('\nAdição ou subtração:')
                estrutura_ULA.adicao.A=CPU.ULA.AC.replace(' ','')
                estrutura_ULA.adicao.B=conteudo.replace(' ','')
                print('Registrador A: '+  estrutura_ULA.adicao.A)
                print('Registrador B: '+  estrutura_ULA.adicao.B)
                binario=estrutura_ULA.adicao.seletor(comando,estrutura_ULA.adicao.complementador())
                #Vamos montar os números pra somar
                (binario,estrutura_ULA.adicao.OF)=estrutura_ULA.adicao.somador(estrutura_ULA.adicao.A,binario)
                #Vamos remontar o número
                CPU.ULA.AC=''
                for x in range (40):
                    if (x==8 or x==20 or x==28):
                        CPU.ULA.AC=CPU.ULA.AC+' '
                    CPU.ULA.AC=CPU.ULA.AC+binario[x]
                print('OF: '+str(estrutura_ULA.adicao.OF))
                regs('Somador')
            elif (comando==2):          #Se é Multiplicação
                #INÍCIO
                print('\nINÍCIO DO ALGORITMO DE BOOTH.')
                        
                #VALORES INICIAIS
                contador=40                     #Inicializar o contador
                estrutura_ULA.multiplicacao.A='0000000000000000000000000000000000000000'
                estrutura_ULA.multiplicacao.Q=CPU.ULA.MBR.replace(' ','')
                estrutura_ULA.multiplicacao.C='0'
                estrutura_ULA.multiplicacao.M=CPU.ULA.MQ.replace(' ','')
            
                booth('Valores iniciais')

                #ESTRUTURA ITERATIVA
                n=contador                                      #Variável para nos ajudar a printar o ciclo na tela 
                while (True):               #Iteração
                    print('\nCiclo '+str(41-contador))

                    #ESTRUTURA CONDICIONAL 1
                    est=estrutura_ULA.multiplicacao.Q[n-1]+estrutura_ULA.multiplicacao.C
                    print('Testa a condição de operação: '+str(est))

                    if (est=='10'): #Vamos realizar a subtração

                        estrutura_ULA.adicao.A=estrutura_ULA.multiplicacao.A
                        estrutura_ULA.adicao.B=estrutura_ULA.multiplicacao.M
                        binario=estrutura_ULA.adicao.seletor(0,estrutura_ULA.adicao.complementador())
                        (binario,estrutura_ULA.adicao.OF)=estrutura_ULA.adicao.somador(estrutura_ULA.adicao.A,binario)
                        estrutura_ULA.multiplicacao.A=binario

                        booth('A<- A-M')

                    elif (est=='01'): #Vamos realizar a adição
                        estrutura_ULA.adicao.A=estrutura_ULA.multiplicacao.A
                        estrutura_ULA.adicao.B=estrutura_ULA.multiplicacao.M
                        binario=estrutura_ULA.adicao.seletor(1,estrutura_ULA.adicao.complementador())
                        (binario,estrutura_ULA.adicao.OF)=estrutura_ULA.adicao.somador(estrutura_ULA.adicao.A,binario)
                        estrutura_ULA.multiplicacao.A=binario

                        booth('A<- A+M')
                        
                    else:
                        print('...	')

                    #DESLOCAMENTO
                    (estrutura_ULA.multiplicacao.A,estrutura_ULA.multiplicacao.Q,estrutura_ULA.multiplicacao.C)=funcao_ULA.deslocamento(estrutura_ULA.multiplicacao.A,estrutura_ULA.multiplicacao.Q,estrutura_ULA.multiplicacao.C)  #Vamos realizar o deslocamento
                    contador=contador-1
                    booth ('Deslocamento')

                    #ESTRUTURA CONDICIONAL 2
                    print('Testa a condição de encerramento: '+str(contador))
                    
                    if(contador==0):
                        #FIM
                        print('FIM: ')
                        resultado=str(estrutura_ULA.multiplicacao.A)+str(estrutura_ULA.multiplicacao.Q)       #Resultado
                        print('O Resultado é: '+resultado)
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
                regs('Resultados em AC e MQ')

    #UNIDADE DE CONTROLE
    class UC:
        IBR='00000000 000000000000'     #Registrador de Buffer da instrução: próxima instrução a ser executada
        PC= '000000000000'              #Contador de programa: endereço do próximo par de instruções
        IR= '00000000'                  #Registrador de instrução: opcode da instrução sendo executada
        MAR='000000000000'              #Registrador de endereço da memória: endereço da memória da palavra a ser escrita/lida no MBR

        #Função do ciclo de instrução
        def ciclo_instrucao():
            
            #Ciclo de instrução
            print('Ciclo de instrução iniciada')
            while(True):
                funcao_UC.busca()       #Ciclo de busca
                funcao_UC.instrucao()   #Ciclo de instrução                
                #break

#MEMÓRIA PRINCIPAL
class memoria:
    #             [  Opcode    Endereço  |  Opcode  Endereço    ]
    conteudo=1024*['00000000 000000000000 00000000 000000000000']   #Conteudo       

#ENTRADA/SAÍDA:
class ES:
    memoria.conteudo[0]= '00001001 000000010000 00001011 000000001000'
    memoria.conteudo[8]= '00000000 000000000000 00000000 000000000011'
    memoria.conteudo[16]='00000000 000000000000 00000000 000000000111'

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
            print('Complemento de B: '+res)
            return (res)                #Retornamos a soma

        #Função para selecionar
        def seletor (operacao,complementado):
            #operacao       - Seleciona o tipo de operação
            #binario        - Número enviado
            #complementado  - Número binário negado

            if (operacao==0):
                print('Operação: subtração')
                return complementado
            else:
                print('Operação: adição')
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
        print('\nCICLO DE BUSCA')
        regs('Próxima instrução está no IBR?')
        if(CPU.UC.IBR!='00000000 000000000000'):                                    #Sim
            CPU.UC.IR=CPU.UC.IBR.split(' ')[0]                                      #IR <- IBR(0:7)
            CPU.UC.MAR=CPU.UC.IBR.split(' ')[1]                                     #MAR <- IBR(8:19)
            regs('Está: \nIR <- IBR (0:7) \nIBR <- MBR(8:19)')

            (CPU.UC.PC,OF)=estrutura_ULA.adicao.somador(CPU.UC.PC.replace(' ',''),'000000000001')   #PC <- PC+1 
            CPU.UC.IBR='00000000 000000000000'     #Vamos zerar o IBR
            regs('PC <- PC+1')
            
        else:                                                                       #Não
            CPU.UC.MAR=CPU.UC.PC                                                    #MAR <- PC
            regs('Não está: MAR <- PC')
            
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  #MBR <- M(MAR)
            regs('MBR <- M(MAR)\nA instrução à esquerda é requisitada?')

            if(funcao_UC.esquerda(CPU.ULA.MBR)):                                    #Sim
                CPU.UC.IBR=CPU.ULA.MBR.split(' ')[2]+' '+CPU.ULA.MBR.split(' ')[3]  #IBR <- MBR(20:39)
                CPU.UC.IR=CPU.ULA.MBR.split(' ')[0]                                 #IR <- MBR(0:7)
                CPU.UC.MAR=CPU.ULA.MBR.split(' ')[1]                                #MAR <- MBR(8:19)
                regs('É: \nIBR <- MBR (20:39) \nIR <- MBR(0:7)\nMAR <- MBR(8:19)')
            else:                                                                   #Não                        
                CPU.UC.IR=CPU.ULA.MBR.split(' ')[2]                                 #IR <- MBR (20:27)
                CPU.UC.MAR=CPU.ULA.MBR.split(' ')[3]                                #MAR <- MBR (28:39)
                regs('Não é: \nIR <- MBR (20:27) \nMAR <- MBR(28:39)')

                (CPU.UC.PC,OF)=estrutura_ULA.adicao.somador(CPU.UC.PC.replace(' ',''),'000000000001')               #PC<-PC+1
                regs('PC <- PC+1')

    #Ciclo de instrução
    def instrucao():

        print('\nCICLO DE EXECUÇÃO')
        #Se não temos instrução
        if (CPU.UC.IR=='00000000'):
            print('Nenhuma instrução')
            parar()

        #LOAD M(X)  Transfere M(X) para AC
        elif(CPU.UC.IR=='00000001'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR <- M(MAR)')

            CPU.ULA.AC=CPU.ULA.MBR                                                  #AC <- MBR
            regs('AC<-MBR')

        #ADD M(X) Soma M(X) a AC e coloca o resultado em AC
        elif(CPU.UC.IR=='00000101'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR<-M(MAR)')
 
            CPU.ULA.circuito(CPU.ULA.MBR,1)

        #SUB M(X) Subtrai M(X) a AC e coloca o resultado em AC
        elif(CPU.UC.IR=='00000110'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR<-M(MAR)')
            
            CPU.ULA.circuito(CPU.ULA.MBR,0)

        #STOR M(X) Transfere o conteudo de AC parao local de memória X
        elif(CPU.UC.IR=='00100001'):
            CPU.ULA.MBR=CPU.ULA.AC                                  #MBR<-AC
            regs('MBR<-AC')

            func_memoria.stor(CPU.UC.MAR,CPU.ULA.MBR)               #M(MAR) <- MBR
            regs('M(MAR) <- MBR')
        #LOAD MQ Transfere o conteudo de MQ para AC
        elif(CPU.UC.IR=='00001010'):
            CPU.ULA.AC=CPU.ULA.MQ                                   #AC<-MQ
            regs('AC <- MQ')

         #LOAD MQ M(X) Transfere o conteudo de X para MQ
        elif(CPU.UC.IR=='00001001'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR <- M(MAR)')

            CPU.ULA.MQ=CPU.ULA.MBR                                                  #MQ <- MBR
            regs('MQ<-MBR')

        #LOAD -M(X) Transfere -M(X) para o AC
        elif(CPU.UC.IR=='00000010'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR <- M(MAR)')

            estrutura_ULA.adicao.B=CPU.ULA.MBR.replace(' ','')                      #B<- MBR
            print('Registrador B: '+ estrutura_ULA.adicao.B)

            binario=estrutura_ULA.adicao.complementador()                       #MBR <- -B
            CPU.ULA.MBR=''
            #Vamos remontar o número
            for x in range (40):
                    if (x==8 or x==20 or x==28):
                        CPU.ULA.MBR=CPU.ULA.MBR+' '
                    CPU.ULA.MBR=CPU.ULA.MBR+binario[x]
            regs('MBR <- -B')           

            CPU.ULA.AC=CPU.ULA.MBR                                                  #AC <- MBR
            regs('AC<-MBR')

        #LOAD M|(X)| Transfere o valor absoluta de M(X) para AC
        elif(CPU.UC.IR=='00000011'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR <- M(MAR)')

            if(CPU.ULA.MBR[0]=='0'):        #Vamos checar se o número já é positivo
                CPU.ULA.AC=CPU.ULA.MBR      #Se é positivo so salvamos              #AC <- MBR
                regs('O número é positivo? Sim.\nAC<- MBR ')
            else:                           #Se é negativo pegamos o complemento
                estrutura_ULA.adicao.B=CPU.ULA.MBR.replace(' ','')                      #B<- MBR
                print('O número é positivo? Não.\nRegistrador B: '+ estrutura_ULA.adicao.B)

                binario=estrutura_ULA.adicao.complementador()                       #MBR <- -B
                CPU.ULA.MBR=''
                #Vamos remontar o número
                for x in range (40):
                    if (x==8 or x==20 or x==28):
                        CPU.ULA.MBR=CPU.ULA.MBR+' '
                    CPU.ULA.MBR=CPU.ULA.MBR+binario[x]
                regs('MBR <- -B')           

                CPU.ULA.AC=CPU.ULA.MBR                                                  #AC <- MBR
                regs('AC<-MBR')

        #LOAD -M|(X)| Transfere o valor  de -|M(X)| para AC
        elif(CPU.UC.IR=='00000100'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR <- M(MAR)')

            if(CPU.ULA.MBR[0]=='1'):        #Vamos checar se o número já é positivo
                CPU.ULA.AC=CPU.ULA.MBR      #Se é positivo so salvamos              #AC <- MBR
                regs('O número é negativo? Sim.\nAC<- MBR ')
            else:                           #Se é negativo pegamos o complemento
                estrutura_ULA.adicao.B=CPU.ULA.MBR.replace(' ','')                      #B<- MBR
                print('O número é negativo? Não.\nRegistrador B: '+ estrutura_ULA.adicao.B)

                binario=estrutura_ULA.adicao.complementador()                       #MBR <- -B
                CPU.ULA.MBR=''
                #Vamos remontar o número
                for x in range (40):
                    if (x==8 or x==20 or x==28):
                        CPU.ULA.MBR=CPU.ULA.MBR+' '
                    CPU.ULA.MBR=CPU.ULA.MBR+binario[x]
                regs('MBR <- -B')           

                CPU.ULA.AC=CPU.ULA.MBR                                                  #AC <- MBR
                regs('AC<-MBR')

        #JUMP M(X,0:19) Apanha a proxima instrução da metade esquerda de m(X)
        elif(CPU.UC.IR=='00001101'):
            CPU.UC.PC=CPU.UC.MAR                                  # MBR<-M(MAR)
            regs('PC <- MAR')

        #JUMP M(X,20:39) Apanha a proxima instrução da metade direita de m(X)
        elif(CPU.UC.IR=='00001110'):
            CPU.UC.PC=CPU.UC.MAR                                  # PC<-MAR
            regs('PC <- MAR')

            (CPU.UC.PC,OF)=estrutura_ULA.adicao.somador(CPU.UC.PC.replace(' ',''),'000000000001')   #PC <- PC+1 
            regs('PC <- PC+1')

            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR <- M(MAR)')

            CPU.UC.IBR=CPU.ULA.MBR.split(' ')[2]+' '+CPU.ULA.MBR.split(' ')[3]      #IBR <- MBR(20:39)
            regs('IBR <- MBR(20:39)')

        #JUMP+ M(X,0:19) Se o número no AC for não negativo, apanha a proxima instrução da metade esquerda
        elif(CPU.UC.IR=='00001111'):
        
            if(CPU.ULA.AC[0]=='0'):        #Vamos checar se o número é positivo
                CPU.UC.PC=CPU.UC.MAR                                  # PC<-MAR
                regs('O número é positivo? Sim.\nPC <- MAR')
            else:
                regs('O número é positivo? Não.')

        #JUMP+ M(X,20:39) Se o número no AC for não negativo, apanha a proxima instrução da metade direita
        elif(CPU.UC.IR=='00010000'):
        
            if(CPU.ULA.AC[0]=='0'):        #Vamos checar se o número já é positivo
                CPU.UC.PC=CPU.UC.MAR                                  # PC<-MAR
                regs('PC <- MAR')

                (CPU.UC.PC,OF)=estrutura_ULA.adicao.somador(CPU.UC.PC.replace(' ',''),'000000000001')   #PC <- PC+1 
                regs('PC <- PC+1')

                CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
                regs('MBR <- M(MAR)')

                CPU.UC.IBR=CPU.ULA.MBR.split(' ')[2]+' '+CPU.ULA.MBR.split(' ')[3]      #IBR <- MBR(20:39)
                regs('IBR <- MBR(20:39)')
            else:
                regs('O número é positivo? Não.')

        #STOR M(X,8:19) Substitui o campo de endereço da esquerda em M(X) por 12 bits mais a direita de AC
        elif(CPU.UC.IR=='00010010'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR <- M(MAR)')

            CPU.ULA.MBR=CPU.ULA.MBR.split(' ')[0]+' '+CPU.ULA.AC.split(' ')[3]+' '+CPU.ULA.MBR.split(' ')[2]+' '+CPU.ULA.MBR.split(' ')[3]     #Passamos os 12 bits
            regs('MBR (8:19) <- AC (8:19)')

            func_memoria.stor(CPU.UC.MAR,CPU.ULA.MBR)               #M(MAR) <- MBR
            regs('M(MAR) <- MBR')
            
        #STOR M(X,28:39) Substitui o campo de endereço da direita em M(X) por 12 bits mais a direita de AC
        elif(CPU.UC.IR=='00010011'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR <- M(MAR)')

            CPU.ULA.MBR=CPU.ULA.MBR.split(' ')[0]+' '+CPU.ULA.MBR.split(' ')[1]+' '+CPU.ULA.MBR.split(' ')[2]+' '+CPU.ULA.AC.split(' ')[3]     #Passamos os 12 bits
            regs('MBR (8:19) <- AC (8:19)')

            func_memoria.stor(CPU.UC.MAR,CPU.ULA.MBR)               #M(MAR) <- MBR
            regs('M(MAR) <- MBR')

        #ADD |M(X)| Soma |M(X)| a AC e coloca o resultado em AC
        elif(CPU.UC.IR=='00000111'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR <- M(MAR)')

            if(CPU.ULA.MBR[0]=='0'):        #Vamos checar se o número já é positivo
                regs('O número é positivo? Sim')
            else:                           #Se é negativo pegamos o complemento
                estrutura_ULA.adicao.B=CPU.ULA.MBR.replace(' ','')                      #B<- MBR
                print('O número é positivo? Não.\nRegistrador B: '+ estrutura_ULA.adicao.B)

                binario=estrutura_ULA.adicao.complementador()                       #MBR <- -B
                CPU.ULA.MBR=''
                #Vamos remontar o número
                for x in range (40):
                    if (x==8 or x==20 or x==28):
                        CPU.ULA.MBR=CPU.ULA.MBR+' '
                    CPU.ULA.MBR=CPU.ULA.MBR+binario[x]
                regs('MBR <- -B')           

            CPU.ULA.circuito(CPU.ULA.MBR,1)

        #SUB|M(X)| subtrai |M(X)| de AC e coloca o resultado em AC
        elif(CPU.UC.IR=='00001000'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR <- M(MAR)')

            if(CPU.ULA.MBR[0]=='0'):        #Vamos checar se o número já é positivo
                regs('O número é positivo? Sim.')
            else:                           #Se é negativo pegamos o complemento
                estrutura_ULA.adicao.B=CPU.ULA.MBR.replace(' ','')                      #B<- MBR
                print('O número é positivo? Não.\nRegistrador B: '+ estrutura_ULA.adicao.B)

                binario=estrutura_ULA.adicao.complementador()                       #MBR <- -B
                CPU.ULA.MBR=''
                #Vamos remontar o número
                for x in range (40):
                    if (x==8 or x==20 or x==28):
                        CPU.ULA.MBR=CPU.ULA.MBR+' '
                    CPU.ULA.MBR=CPU.ULA.MBR+binario[x]
                regs('MBR <- -B')           

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
            regs('AC * 2')

        #RSH  divide AC por 2 desloca a esquerda uma posição de bit
        elif(CPU.UC.IR=='00010101'):
            binario=CPU.ULA.AC.replace(' ','')
            CPU.ULA.AC='0'
            for x in range(0,39):
                if (x==7 or x==19 or x==27):
                        CPU.ULA.AC=CPU.ULA.AC+' '
                CPU.ULA.AC=CPU.ULA.AC+binario[x]
            regs('AC / 2')

        #MUL(X) multiplica M(X) por MQ e coloca os bits mais significativos do resultado em AC
        elif(CPU.UC.IR=='00001011'):
            CPU.ULA.MBR=func_memoria.M(CPU.UC.MAR)                                  # MBR<-M(MAR)
            regs('MBR<-M(MAR)')
 
            CPU.ULA.circuito(CPU.ULA.MBR,2)
            
        else:
            print('Op code inválido.')
            parar()
        
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

#Printar os valores dos registradores e uma mensagem extra
def regs(msg):
    #msg    - Mensagem extra
    
    print('\n'+msg)
    print('AC:  '+CPU.ULA.AC)
    print('MQ:  '+CPU.ULA.MQ)
    print('MBR: '+CPU.ULA.MBR)
    print('IBR: '+CPU.UC.IBR)
    print('PC:  '+CPU.UC.PC)
    print('IR:  '+CPU.UC.IR)
    print('MAR: '+CPU.UC.MAR)

#Printar a memória
def mmria(inicial,final):
    #inicial    - Primeiro endereço a ser exibido
    #final      - Último endereço
    
    for x in range(inicial,final+1):
        num=str(x)
        if(x<10):
            num='000'+num
        elif(x<100):
            num='00'+num
        elif(x<1000):
            num='0'+num
        print('['+num+'] '+memoria.conteudo[x])

#Printa os valores dos registrado da multiplicação e uma mensagem extra
def booth(msg):
    #msg    - Mensagame extra
    print('\n'+msg)
    print('A  : '+estrutura_ULA.multiplicacao.A)
    print('Q  : '+estrutura_ULA.multiplicacao.Q)
    print('Q-1: '+estrutura_ULA.multiplicacao.C)
    print('M  : '+estrutura_ULA.multiplicacao.M)
    
#Iniciamos o PC
def start():
    CPU.UC.ciclo_instrucao()

#Vetores pra animação
est=[]  #Estrutura expandida
reg=[]  #Registradores principais

deta=[] #Detalhes da execução em específico
msg=[]  #Textos da execução em específico

start()
