def atribuicao(a,b,variaveis,lista_com):
    #a          - Variável que vai receber o valor
    #b          - Valor a ser salvo na variável
    #variaveis  - Lista de variáveis
    #lista_com  - Lista de comandos
    otro_com=False
    otra_vari=False
    for c in lista_com:
        res=b.find(c)       #Vamos ver se estamos invocando algum comando pra 
        if (res!=-1):
            otro_com=True
            print('Atribuição por Comando: '+ a+'='+b)            #Se for um comando
    if (otro_com==False):               #Se não é outro comando
        for vari in variaveis:          #Vamos ver se esta recebendo de outra variável
            res=b.find(vari['nome'])
            if (res!=-1):
                otra_vari=True
                print('Atribuição por variável: '+ a+' = '+b)
    if (otro_com==False) and (otra_vari==False): #Se não, deve estar recebendo um valor
        print('Atribuição por valor: '+ a+'= '+b)
