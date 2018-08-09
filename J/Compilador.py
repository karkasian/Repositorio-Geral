
#Lista de palavras reservadas
reservadas=['int','vet','float','if','else','while','var','start']

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

arquivo = open("codigo.j","r")  #Vamos abrir o código
codigo=arquivo.read()           #Ler o arquivo
arquivo.close()                 #Fechar o arquivo
codigo=codigo.replace('\n', ' ')#Vamos trocar as quebras de linha por espaço


objeto = open('objeto.obj','w')  
objeto.write('Hello World') 
objeto.close() 
#hex()print()
