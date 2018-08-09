from comandos import *          #Vamos importar os comandos

#Lista de palavras reservadas
tipos_var=['vet','int']     #Primeiro precisamos ver se é vetor
lista_com=['=','+']             #Primeiro queremos saber onde salvar o resultado
reservadas=['start','var']

#Lista de instruções
instrucoes={'LOAD MQ':          {'binario':'00001010','hexadecimal':'0A','decimal':'10','Descrição':'Transfere o conteudo de MQ para AC'},
            'LOAD MQ,M(X)':     {'binario':'00001001','hexadecimal':'09','decimal':'09','Descrição':'Transfere o conteudo do local de memória para MQ'},
            'STOR M(X)':        {'binario':'00100001','hexadecimal':'21','decimal':'33','Descrição':'Transfere o conteúdo de AC para o local de memória X'},
            'LOAD M(X)':        {'binario':'00000001','hexadecimal':'01','decimal':'01','Descrição':'Transfere M(X) para o AC'},
            'LOAD -M(X)':       {'binario':'00000010','hexadecimal':'02','decimal':'02','Descrição':'Transfere -M(X) para o AC'},
            'LOAD |M(X)|':      {'binario':'00000011','hexadecimal':'03','decimal':'03','Descrição':'Transfere o valor absoluto de M(X) para o AC'},
            'LOAD -|M(X)|':     {'binario':'00000100','hexadecimal':'04','decimal':'04','Descrição':'Transfere -|M(X)| para o acumulador'},
            'JUMP M(X,0:19)':   {'binario':'00001101','hexadecimal':'0D','decimal':'13','Descrição':'Apanha a próxima instrução da metade esquerda M(X)'},
            'JUMP M(X,20:39)':  {'binario':'00001110','hexadecimal':'0E','decimal':'14','Descrição':'Apanha a próxima instrução da metade direta de M(X)'},
            'JUMP+ M(X:0:19)':  {'binario':'00001111','hexadecimal':'0F','decimal':'15','Descrição':'Se o número no AC for positivo, apanha a próxima instrução da metade esquerda de M(X)'},
            'JUMP+ M(X:20:39)': {'binario':'00010000','hexadecimal':'10','decimal':'16','Descrição':'Se o número no AC for positivo, apanha a proxima instrução da metade direita de M(X)'},
            'ADD M(X)':         {'binario':'00000101','hexadecimal':'05','decimal':'05','Descrição':'Soma M(X) a AC e coloca em AC'},
            'ADD |M(X)|':       {'binario':'00000111','hexadecimal':'07','decimal':'07','Descrição':'Soma |M(X)| a AC e coloca em AC'},
            'SUB M(X)':         {'binario':'00000110','hexadecimal':'06','decimal':'06','Descrição':'Subtrai M(X) de AC e coloca em AC'},
            'SUB |M(X)|':       {'binario':'00001000','hexadecimal':'08','decimal':'08','Descrição':'Subtrai |M(X)| de AC e coloca em AC'},
            'MUL M(X)':         {'binario':'00001011','hexadecimal':'0B','decimal':'11','Descrição':'Multiplica M(X) por MQ, coloca os bits mais significativos em AC e os menos em MQ'},
            'DIV M(X)':         {'binario':'00001100','hexadecimal':'0C','decimal':'12','Descrição':'Divide AC por M(X)  e coloca o quociente em MQ e o resto em AC'},
            'LSH':              {'binario':'00010100','hexadecimal':'14','decimal':'20','Descrição':'Multiplica AC por 2 (deslocando à esquerda uma posição de bit)'},
            'RS':               {'binario':'00010101','hexadecimal':'15','decimal':'21','Descrição':'Divide AC por 2 (deslocando uma posição à direita)'},
            'STOR M(X:8:19)':   {'binario':'00010010','hexadecimal':'12','decimal':'18','Descrição':'Substitui o campo de endereço da esquerda em M(X) por 12 bits mais à direita de AC'},
            'STOR M(X:28:39)':  {'binario':'00010011','hexadecimal':'13','decimal':'19','Descrição':'Substitui o campo de endereço da direita em M(X) por 12 bits mais à direita de AC'}
            }

#Lista de variáveis
variaveis=[]

#Endereço da proxima variável a ser declarada
end_var=1023

#Endereço da proxima função a ser declarada
end_fun=0
de=0            #Indicando se vamos salvar na esquerda (0) ou direita (1)

arquivo = open("codigo.j","r")  #Vamos abrir o código
codigo=arquivo.read()           #Ler o arquivo
arquivo.close()                 #Fechar o arquivo
codigo=codigo.replace('\n', ' ')#Vamos trocar as quebras de linha por espaço

pos=codigo.find('var')          #Primeiro vamos procurar o nosso bloco de variáveis declaradas:
if (pos==-1):                   #Se não foi declarado
    print('Bloco de variáveis não declarado')       #Avisa

#Vamos procurar onde começa o bloco 
for c in range (pos,len(codigo)):
    if (codigo[c]=='{'):
        inicio=c
        break

#Vamos procurar onde termina o bloco 
for c in range (inicio,len(codigo)):
    if (codigo[c]=='}'):
        fim=c
        break

#Podemos extrair esse texto
codigo_var=''
for c in range (inicio+1,fim):
    codigo_var=codigo_var+codigo[c]

#E separarmos para cada variavel
trechos_var=codigo_var.split(';')
for trecho in trechos_var:
    for tipo in tipos_var:      #Vamos descobrir o tipo
        res=trecho.find(tipo)
        if(res!=-1):            #Se é esse tipo
            #Com  tipo, vamos dar tratamentos diferentes dependendo do tipo
            if (tipo=='int'):       #Se é inteiro prosseguimos pegando o nome
                
                pos=res+4           #Vamos começar a pegar o nome
                nome=''
                for c in range(pos,len(trecho)):
                    if (trecho[c]==' '):
                        fim=c
                        break
                    else:
                        nome=nome+trecho[c]
                        
                valor=''
                #Com o nome e o tipo e onde terminou o nome, vamos ver se o proximo item foi o fim, ou atribui valor
                for c in range (fim,len(trecho)):                    
                    if (trecho[c]=='='):#Se atribuiu, vamos lidar com isso
                        inicio=c+1      #Pegamos o primeiro elemento depois da igualdade
                        for k in range (inicio,len(trecho)):
                            if (trecho[k]!=' '):        #Se não for espaço, salvamos
                                valor=valor+trecho[k]
                              
                if (valor==''):         #Se o valor permaneceu vazio
                    valor='0'           #Adicionamos 0
                valor=int(valor)        #Passamos valor pra inteiro
                
                #Com o nome, e o valor, podemos salvar na nossa lista:
                doc={'nome':nome,'valor':valor,'posicao':end_var,'tipo':tipo}
                print('Declara inteiro: '+nome+'='+str(valor))
                end_var=end_var-1       #Próxima variável, adicionamos no elemento da memória anterior
                variaveis.append(doc)
                
            elif (tipo =='vet'):        #Se é vetor
                
                pos=res+4           #Vamos começar a pegar o subtipo
                sub=''
                for c in range(pos,len(trecho)):
                    if (trecho[c]==' '):
                        fim=c
                        break
                    else:
                        sub=sub+trecho[c]

                #agora podemos pegar o tamanho
                #Vamos definir onde começa
                for c in range(fim,len(trecho)):
                    if (trecho[c]=='['):
                        com=c
                        break
                #E onde termina
                for c in range(com,len(trecho)):
                    if (trecho[c]==']'):
                        ter=c
                        break
                #Então podemos pegar o tamanho
                tam=''
                for c in range (com+1,ter):
                    tam=tam+trecho[c]
                tam=int(tam)                #Passamos para inteiro

                # então pegamos o nome:
                nome=''
                for c in range(ter+2,len(trecho)):
                    if (trecho[c]==' '):
                        fim=c
                        break
                    else:
                        nome=nome+trecho[c]

                #podemos conferir se os valores foram declarados:
                decl=trecho.find('=')
                if (decl==-1):      #Se não foi declarado
                    for x in range(tam):    #Vamos salvar tudo 0
                        if (sub=='int'):
                            if (x>0):
                                nome='vet'
                            doc={'nome':nome,'valor':0,'posicao':end_var,'tipo':tipo}
                            print('Declara vetor: '+nome+'['+str(x)+'] =0')
                            end_var=end_var-1       #Próxima variável, adicionamos no elemento da memória anterior
                            variaveis.append(doc)
                else:               #Mas se foi
                    #Vamos pegar onde começa a declaração
                    for c in range(decl+1,len(trecho)):
                        if (trecho[c]=='['):
                            com=c
                            break
                    #E onde termina
                    for c in range(com,len(trecho)):
                        if (trecho[c]==']'):
                            ter=c
                            break
                    #Então podemos pegar a declaração inteira
                    dec=''
                    for c in range (com+1,ter):
                        dec=dec+trecho[c]
                    dec_sep=dec.split(',')      #Separamos os valores
                    
                    for x in range(tam):    #Vamos salvar tudo
                        if (sub=='int'):
                            if (x>0):
                                nome='vet'
                            doc={'nome':nome,'valor':int(dec_sep[x]),'posicao':end_var,'tipo':tipo}
                            print('Declara vetor: '+nome+'['+str(x)+'] ='+dec_sep[x])
                            end_var=end_var-1       #Próxima variável, adicionamos no elemento da memória anterior
                            variaveis.append(doc)

            break

doc_final=''
#Vamos agora registrar as variáveis
for v in variaveis:
    pos=str(hex(v['posicao'])).replace('0x', '')    #Removemos os '0x'
    val=str(hex(v['valor'])).replace('0x', '')      #Removemos os '0x'
    linha=pos +' '+val
    doc_final=doc_final+linha+'\n'


#Próximo passo é procurar os comandos
pos=codigo.find('start')        #Primeiro vamos procurar o nosso bloco de comandos
if (pos==-1):                   #Se não foi declarado
    print('Bloco de variáveis não declarado')       #Avisa

#Vamos procurar onde começa o bloco 
for c in range (pos,len(codigo)):
    if (codigo[c]=='{'):
        inicio=c
        break

#Vamos procurar onde termina o bloco 
for c in range (inicio,len(codigo)):
    if (codigo[c]=='}'):
        fim=c
        break

#Podemos extrair esse texto
codigo_com=''
for c in range (inicio+1,fim):
    codigo_com=codigo_com+codigo[c]

#E separarmos para cada variavel
trechos_com=codigo_com.split(';')

#Vamos analisar linha a linha
for trecho in trechos_com:
    for comando in lista_com:   #Vamos percorrer nossa lista de comandos
        res=trecho.find(comando)    #procurar comandos linha
        if (res!= -1):              #Se encontrouo comando
            pos=res                 #Vamos guardar onde está o comando
            if( comando == '='): #Se o comando é de atribuição
                trecho_dem=trecho.split('=')    #Vamos separar em o valor a ser atribuir, e onde será atribuido
                atribuicao(trecho_dem[0],trecho_dem[1],variaveis, lista_com)
                    
    
objeto = open('objeto.obj','w')  
objeto.write(doc_final) 
objeto.close() 

memoria=end_fun+(1023-end_var)
print ("Foi usado "+ str(memoria)+" espaços na memoria")
#Endereço da proxima função a ser declarada
end_fun=0


#112 - 100
#120 - 100

#   1,12    -   1,2         =   -0,08
#   112/100 -   12/10
#   112/100 -   120/100
#   8/100


#Inteiros
#vetores
#= ,+,*,/
#=while
#if (<,>,==,!=)
