##ARQUITETURA: Algoritmo de Booth
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/tree/master/Arquitetura
##2018

#Vamos definir os registradores
class registradores:
    #Vamos setar as configurações iniciais
    def __init__(self,multiplicando,multiplicador,A):
        #self           - Referência a própria classe
        #multiplicando  - Multiplicando do cálculo
        #multiplicador  - Multiplicador do cálculo
        #A              - Valor inicial do registrador A
        
        self.Q=multiplicador    #Multiplicador
        self.M=multiplicando    #Multiplicando
        self.A=A                #Registrador
        self.C='0'              #Registrador de 1 bit

        return None

#Algoritmos relacionados a adição
class adicao:
    
    #Checar se houve overflow
    def overflow(um,dois,res):
        #um     - Primeiro número somado
        #dois   - Segundo número somado
        #res    - Resultado da soma
        
        if (um[0]!=dois[0]):        #Se os sinais são diferentes
            return res              #Não houve overflow
        else:                       #Se são iguais
            if (um[0]==res[0]):     #Se a resposta tem o mesmo sinal dos números
                return res          #Não houve overflow
            else:                   #Se o sinal é diferente
                return 'overflow'   #Houve
    
    #Regras da adição
    def regras(um,dois):
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
    def bit (um, dois, e):
        #um     - Primeiro bit
        #dois   - Segundo bit
        #e      - Bit resultado de soma anterior

        if(e==0):   #Se não temos de um anterior, apenas somamos:
            (res,elev)=adicao.regras(um,dois)
        else:       #Se temos
            if (um==0):      #E o primeiro é zero
                (res,elev)=adicao.regras(e,dois)        #Somamos ao segundo
            elif(dois==0):  #Se não mas o segundo é:
                (res,elev)=adicao.regras(e,um)          #Somamos ao primeiro
            else:           #Se nenhum é zero
                (res,elev1)=adicao.regras(e,um)         #Somamos ao primeiro
                (res,elev2)=adicao.regras(res,dois)     #E somamos o resultado ao segundo
                (elev,des)=adicao.regras(elev1,elev2)   #E retornamos a soma dos elevados
        return (res,elev)
    
    #Operação de fato
    def operacao (um,dois):
        #um     - Primeiro número
        #dois   - Segundo número
        
        tam=len(um)                     #Vamos pegar o tamanho
        res=[]                          #Vamos guardar o resultado
        elev=0                          #Vamos guardar o valor elevado
        for bit in range(tam-1,-1,-1):  #Vamos percorrer bit a bit o número
            (r,elev)=adicao.bit(int(um[bit]),int(dois[bit]),elev)   #Vamos somar todos os bits
            res.append(r)               #Salvamos o resultado
        #Agora vamos montar o resultado
        resposta=''                     #Onde vamos guardar a resposta
        
        for bit in range (tam-1,-1,-1): #Montamos nossa resposta
            resposta=resposta+str(res[bit])

        resposta=adicao.overflow(um,dois,resposta)                  #Checamos o overflow
        return (resposta)                                           #Retornamos a resposta

#Algoritmos relacionados a subtração
class subtracao:

    #Função para realizar a negação
    def negacao(n):
        #n  - Número em que faremos o complemento

        res=''      #Onde vamos guardar o resultado
        som=''      #Onde vamos guardar o 1 que vamos somar
        tam=len(n)  #Tamanho do binário
        for bit in range(tam):      #Vamos percorrer bit a bit o número
            if (n[bit]=='0'):       #Se é 0
                res=res+'1'         #Guardamos 1
            else:                   #Se não
                res=res+'0'         #Guardamos 0
            if(bit==tam-1):         #Se é o último bit
                som=som+'1'         #Guardamos o 1
            else:                   #Se não
                som=som+'0'         #Adicionamos outro 0
        res=adicao.operacao(res,som)
        return (res)                #Retornamos a soma
    
    #Função para fazer a operação de fato
    def operacao(minuendo,subtraendo):
        #subtraendo     - Subtraendo da operação
        #minuendo       - Minuendo da operação

        sub=subtracao.negacao(subtraendo)       #Vamos pegar a negação
        res=adicao.operacao(minuendo,sub)       #E somamos ao minuendo
        return (res)

#Algoritmos relacionados a multiplicação
class multiplicacao:
    #Função para realizar o deslocamento
    def deslocamento(self, A,Q,C,n):
        #self           - Referência a própria classe
        #A              - Registrador A
        #Q              - Registrador Q
        #C              - Registrador C
        #n              - Tamanho dos bits

        nC=Q[n-1]       #Nosso novo C
        nQ=''           #Onde vamos armazenar nosso novo Q
        nA=''           #Onde vamos armazenar nosso novo A
        nQ=nQ+A[n-1]    #Primeiro elemento do Q
        nA=A[0]         #Nosso novo A
        for x in range (n-1):   #Vamos percorrer até o penúltimo elemento
            nQ=nQ+Q[x]
            nA=nA+A[x]

        return (nA,nQ,nC)       #Retornamos os valores
    
    #Operaçao de fato
    def __init__(self,multiplicando,multiplicador):
        #self           - Referência a própria classe
        #multiplicando  - Multiplicando do cálculo
        #multiplicador  - Multiplicador do cálculo

        manual=''       #Para definir se o controle e manual

        #INÍCIO
        print('INÍCIO.')
        if(manual==''):
                manual= input()
                
        #VALORES INICIAIS
        contador=len(multiplicando)                     #Inicializar o contador
        a=''
        for x in range(contador):                       #Vamos gerar nosso valor inicial de A
            a=a+'0'                                     #De acordo com o tamanho dos nossos bits
        pc=registradores(multiplicando,multiplicador,a) #Vamos setar nossas configurações iniciais
    
        print('A: '+pc.A+' | Q: '+pc.Q+' | Q-1: '+pc.C+' | M: '+pc.M+' |	Valores iniciais')
        if(manual==''):
                manual= input()

        #ESTRUTURA ITERATIVA
        n=contador                                      #Variável para nos ajudar a printar o ciclo na tela 
        while (True):               #Iteração
            print('Ciclo '+str(n-x))

            #ESTRUTURA CONDICIONAL 1
            est=pc.Q[n-1]+pc.C
            print('Testa a condição de operação: '+str(est))
            if(manual==''):
                manual= input()

            if (est=='10'):
                pc.A=subtracao.operacao(pc.A,pc.M)      #Vamos realizar a subtração
                print('A: '+pc.A+' | Q: '+pc.Q+' | Q-1: '+pc.C+' | M: '+pc.M+' |	A<- A-M')
                if(manual==''):
                    manual= input()

            elif (est=='01'):
                pc.A=adicao.operacao(pc.A,pc.M)         #Vamos realizar a adição
                print('A: '+pc.A+' | Q: '+pc.Q+' | Q-1: '+pc.C+' | M: '+pc.M+' |	A<- A+M')
                if(manual==''):
                    manual= input()
            else:
                print('A: '+pc.A+' | Q: '+pc.Q+' | Q-1: '+pc.C+' | M: '+pc.M+' |	')

            #DESLOCAMENTO
            (pc.A,pc.Q,pc.C)=self.deslocamento(pc.A,pc.Q,pc.C,n)  #Vamos realizar o deslocamento
            contador=contador-1
            print('A: '+pc.A+' | Q: '+pc.Q+' | Q-1: '+pc.C+' | M: '+pc.M+' |	Deslocamento')
            if(manual==''):
                manual= input()

            #ESTRUTURA CONDICIONAL 2
            print('Testa a condição de encerramento: '+str(contador))
            if(manual==''):
                manual= input()
            
            if(contador==0):
                #FIM
                print('FIM: ')
                resultado=str(pc.A)+str(pc.Q)       #Resultado
                print('O Resultado é: '+resultado)
                break
            
        return None
        

#Variáveis para nossa animação
multiplicando='0111'
multiplicador='0011'
multiplicacao(multiplicando,multiplicador)
