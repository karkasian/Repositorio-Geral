##ARQUITETURA: Divisão de inteiros
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/tree/master/Arquitetura
##2018

#Vamos definir os registradores
class registradores:
    #Vamos setar as configurações iniciais
    def __init__(self,divisor,dividendo,A):
        #self           - Referência a própria classe

        #multiplicando  - Multiplicando do cálculo
        #multiplicador  - Multiplicador do cálculo
        #A              - Valor inicial do registrador A
        
        self.Q=dividendo      #Multiplicador
        self.M=divisor    #Multiplicando
        self.A=A                #Registrador

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
class divisao:
    #Função para realizar o deslocamento
    def deslocamento(self, A,Q,n):
        #self           - Referência a própria classe
        #A              - Registrador A
        #Q              - Registrador Q
        #n              - Tamanho dos bits

        nQ=''           #Onde vamos armazenar nosso novo Q
        nA=''           #Onde vamos armazenar nosso novo A
        for x in range (1,n):   #Vamos percorrer até o penúltimo elemento
            nQ=nQ+Q[x]
            nA=nA+A[x]
        nA=nA+Q[0]        
        nQ=nQ+'0'
        return (nA,nQ)       #Retornamos os valores
    
    #Operaçao de fato
    def __init__(self,divisor,dividendo):
        #self           - Referência a própria classe
        #multiplicando  - Multiplicando do cálculo
        #multiplicador  - Multiplicador do cálculo

        manual='p'       #Para definir se o controle e manual


        #INÍCIO
        print('INÍCIO.')
        if(manual==''):
                manual= input()

        print('Vamos converter os números para positivo')
        if (divisor[0]=='0'):
            visor=divisor
        else:
            visor=subtracao.negacao(divisor)

        if (dividendo[0]=='0'):
            dendo=dividendo
        else:
            dendo=subtracao.negacao(dividendo)
                
        #VALORES INICIAIS
        contador=len(divisor)                     #Inicializar o contador
        a=''
        for x in range(contador):                       #Vamos gerar nosso valor inicial de A
            a=a+'0'                                     #De acordo com o tamanho dos nossos bits

        pc=registradores(visor,dendo,a) #Vamos setar nossas configurações iniciais
    
        print('A: '+pc.A+' | Q: '+pc.Q+' | M: '+pc.M+' |	Valores iniciais')
        if(manual==''):
                manual= input()

        #ESTRUTURA ITERATIVA
        n=contador                                      #Variável para nos ajudar a printar o ciclo na tela 
        while (True):               #Iteração
            print('\nCiclo '+str(n-contador+1))

            #DESLOCAMENTO
            (pc.A,pc.Q)=self.deslocamento(pc.A,pc.Q,n)  #Vamos realizar o deslocamento

            print('A: '+pc.A+' | Q: '+pc.Q+' | M: '+pc.M+' |	Deslocamento')
            if(manual==''):
                manual= input()

            pc.A=subtracao.operacao(pc.A,pc.M)      #Vamos realizar a subtração
            print('A: '+pc.A+' | Q: '+pc.Q+' | M: '+pc.M+' |	A<- A-M')
            if(manual==''):
                manual= input()

            #ESTRUTURA CONDICIONAL 1
            print('Testa a condição de operação: A<0')
            if(manual==''):
                manual= input()

            if (pc.A[0]=='1'):
                pc.A=adicao.operacao(pc.A,pc.M)         #Vamos realizar a adição
                antQ=pc.Q
                pc.Q=''
                for x in range(len(antQ)-1):
                    pc.Q=pc.Q+antQ[x]
                pc.Q=pc.Q+'0'
                print('A: '+pc.A+' | Q: '+pc.Q+'  | M: '+pc.M+' |	A<- A+M e Q0 <-0 ' )
                if(manual==''):
                    manual= input()
            else:
                antQ=pc.Q
                pc.Q=''
                for x in range(len(antQ)-1):
                    pc.Q=pc.Q+antQ[x]
                pc.Q=pc.Q+'1'
                print('A: '+pc.A+' | Q: '+pc.Q+'  | M: '+pc.M+' |	Q0 <- 1 ' )
                if(manual==''):
                    manual= input()
                    
            #Contador
            contador=contador-1
            print('Contador: '+str(contador))
            if(manual==''):
                    manual= input()

            #ESTRUTURA CONDICIONAL 2
            print('Testa a condição de encerramento: '+str(contador))
            if(manual==''):
                manual= input()
            
            if(contador==0):
                #FIM
                print('FIM: ')
                break

        #PODEMOS AGORAR CONSIDERAR OS SINAIS
        #A
            
        if (dividendo[0]=='1'):
            pc.A=subtracao.negacao(pc.A)

        if(divisor[0]!=dividendo[0]):
            pc.Q=subtracao.negacao(pc.Q)
            
        print('Quociente: '+pc.Q)
        print('Resto: '+pc.A)
        return None
        

#Variáveis para nossa animação
dividendo=subtracao.negacao('0111')
divisor='0011'
divisao(divisor,dividendo)
