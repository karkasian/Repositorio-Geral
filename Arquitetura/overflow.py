##ARQUITETURA: Algoritmo de Booth
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/tree/master/Introdu%C3%A7%C3%A3o%20ao%20Hacking%20e%20Pentest
##2018


#Vamos definir os registradores
class registradores:
    Q=0     #Multiplicador
    M=0     #Multiplicando
    A=0     #Registrador
    C=0     #Multiplicador de 1 bit

#Algoritmos relacionados a adição
class adicao:
    
    #Checar se ouve overflow
    def overflow(um,dois,res):
        #um     - Primeiro número somado
        #dois   - Segundo número somado
        #res    - Resultado da soma
        
        if (um[0]!=dois[0]):    #Se os sinais são diferentes
            return res          #Não houve overflow
        else:                   #Se são iguais
            if (um[0]==res[0]): #Se a resposta tem o mesmo sinal dos números
                return res      #Não houve overflow
            else:               #Se o sinal é diferente
                return 'overflow'#Houve
    
    #Regras da adição
    def regras(um,dois):
        #um     - Primeiro bit
        #dois   - Segundo bit

        #Vamos trabalhar com os casos:
        if (um==0 and dois ==0):    #0+0
            return (0,0)
        elif (um==0 and dois ==1):  #0+1
            return (1,0)
        elif (um==1 and dois==0):     #1+0
            return (1,0)
        else:
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
                (res,elev)=adicao.regras(e,dois)    #Somamos ao segundo
            elif(dois==0):  #Se não mas o segundo é:
                (res,elev)=adicao.regras(e,um)      #Somamos ao primeiro
            else:           #Se nenhum é zero
                (res,elev1)=adicao.regras(e,um)      #Somamos ao primeiro
                (res,elev2)=adicao.regras(res,dois)   #E somamos o resultado ao segundo
                (elev,des)=adicao.regras(elev1,elev2)#E retornamos a soma dos elevados
        return (res,elev)
        
    
    #Operação de fato
    def operacao (um,dois):
        #um     - Primeiro número
        #dois   - Segundo número
        
        tam=len(um)                     #Vamos pegar o tamanho
        res=[]                          #Vamos guardar o resultado
        elev=0                          #Vamos guardar o valor elevado
        for bit in range(tam-1,-1,-1):  #Vamos percorrer bit a bit o número
            (r,elev)=adicao.bit(int(um[bit]),int(dois[bit]),elev)    #Vamos somar todos os bits
            res.append(r)               #Salvamos o resultado
        #Agora vamos montar o resultado
        resposta=''                     #Onde vamos guardar a resposta
        for bit in range (tam-1,-1,-1):
            resposta=resposta+str(res[bit])

        #Checamos o overflow
        resposta=adicao.overflow(um,dois,resposta)
        #Retornamos a resposta
        return (resposta)

        

resposta=adicao.operacao('0011','0100')
print(resposta)
