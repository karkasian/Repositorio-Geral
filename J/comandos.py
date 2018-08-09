def atribuicao(a,b,variaveis,lista_com,instrucoes,doc_final,end_fun,de):
    #a          - Variável que vai receber o valor
    #b          - Valor a ser salvo na variável
    #variaveis  - Lista de variáveis
    #lista_com  - Lista de comandos
    #instrucoes - Lista com as instruções do IAS
    #doc_final  - Como esta nosso arquivo de saida
    #end_fun    - Endereço que devemos salvar nossa próxima função
    #de         - Indica se a proxima função e na esquerda [0] ou direita [1]
    
    otro_com=False          #Se a atribuição e por outro comando
    otra_vari=False         #Se a atribuição e outra variável
    for c in lista_com:
        res=b.find(c)       #Vamos ver se estamos invocando algum comando pra 
        if (res!=-1):
            otro_com=True
            print('Atribuição por Comando: '+ a+'='+b)  #Se for um comando
    if (otro_com==False):               #Se não é outro comando
        for vari in variaveis:          #Vamos ver se esta recebendo de outra variável
            res=b.find(vari['nome'])
            if (res!=-1):
                otra_vari=True

                #Primeiro vamos ver de qual variável estamos pegando
                
                print('Atribuição por variável: '+ a+' = '+b)
    if (otro_com==False) and (otra_vari==False):        #Se não, deve estar recebendo um valor direto
        
        #Vamos pegar o valor
        valor=''
        for c in range(len(b)):
            if (b[c]!=''):
                valor=valor+b[c]

        #Vamos descobrir se é um elemento de vetor:
        res=a.find('[')

        if (res==-1):   #Se não é
            #Agora vamos pegar qual variável deve receber o valor
            nome=a.replace(' ', '')
            for var in variaveis:           #Procuramos o nome 
                if (nome==var['nome']):     #Em nossa lista de variáveis
                    break                   #E saimos com nosso var carregando as informações da variável

            #Agora checamos que tipo é nossa variável
            if (var['tipo']=='int'):                              #Se é inteiro
                valor=int(valor.replace(' ',''))                  #Podemos retirar os espaços e salvarmos como inteiro
                pos=str(hex(var['posicao'])).replace('0x', '')    #Removemos os '0x'
                val=str(hex(valor)).replace('0x', '')                  #Removemos os '0x'
                linha=pos +' '+val
                doc_final=doc_final+linha+'\n'
                
        else:                                             #Se é vetor
            pos=res                                       #Pegamos onde começa a indicação do elemento
            #Vamos pegar o nome
            nome=''
            for x in range(pos):                            
                nome=nome+a[x]
            nome=nome.replace(' ','')                     #Retirar os espaços

            #Vamos pegar o elemento
            elem=''
            fim=a.find(']')                             #Onde acaba a declaração do elemento
            for x in range(pos+1,fim):     
                elem=elem+a[x]
            elem=int(elem)                              #Vamos passar pra inteiro
        
            #Agora temos o elemento, a variável e o valor, vamos pegar informações sobre a variável que vai receber
            for var in variaveis:           #Procuramos o nome 
                if (nome==var['nome']):     #Em nossa lista de variáveis
                    break                   #E saimos com nosso var carregando as informações da variável

            #Agora checamos que sub-tipo é nossa variável
            if (var['sub-tipo']=='int'):                          #Se é inteiro
                valor=int(valor.replace(' ',''))                  #Podemos retirar os espaços e salvarmos como inteiro

                #Precisamos pegar nossa posição do elemento do vetor:
                pos=var['posicao']-elem
                
                pos=str(hex(pos)).replace('0x', '')    #Removemos os '0x'
                val=str(hex(valor)).replace('0x', '')                  #Removemos os '0x'
                linha=pos +' '+val
                doc_final=doc_final+linha+'\n'

                #Só pra printar na tela
                nome=nome+'['+str(elem)+']'           

        print('Atribuição por valor:'+nome+'='+str(valor)+'.')

    return (instrucoes,doc_final,end_fun,de)                #Retornamos os documentos que podemos ter modificado
