# Arquitetura de computadores

## Problemas

Estes são alguns problemas retirados do livro de Arquitetura e Organização de Computadores (8 edição, William Stallings).

### Problema 2.1

Considere que A = A(1), A(2),... , A(1 000) e B = B(1), B(2),..., B(1 000) sejam dois vetores (arrays unidimensionais) compostos de 3 números em cada um, que são somados para formar um array C tal que C(I) = A(I) + B(I) para I = 1,2,3. Usando o conjunto de instruções do IAS, escreva um programa para esse problema. 

[Código](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/Arquitetura/Problema%202.1.asm) em linguagem de montagem.

## Problema 2.4

Interprete e escreva em linguagem de montagem:
```
08A 010FA210FB
08B 010FA0F08D
08C 020FA210FB
```

Reescrevendo de forma mais legível:
```
08A [01 0FA] [21 0FB]
08B [01 0FA] [0F 08D]
08C [02 0FA] [21 0FB]
```
Então para a primeira linha guarda seu conteúdo no endereço 08A Hex (138 Dec). Seu conteúdo tem 2 palavras:
1. [01 0FA]
2. [21 0FB]

A primeira palavra, traz um opcode e um endereço:
1. 01 Hex (1 Dec, 0000 0001 Bin): Load M(X): transfere o conteúdo de X para o AC
2. 0FA Hex (250 Dec): Endereço de memória.

Podemos reescrever então como [01 0FA]=LOAD M(0FA). De forma análoga, temos para a segunda palavra 21 Hex(33 Dec, 00010 0001 Bin). Esse opcode é STOR M(X), que implica em transferir o conteúdo de AC para X.

Então a primeira linha do código contém de forma descritiva:
- Copia o conteúdo de 0FA para AC, e depois de AC para 0FB.

Então fazendo o mesmo para as outras linhas, temos:
- Copia o conteúdo de 0FA para AC, e depois de AC para 0FB.
- Copia novamente o conteúdo de 0FA para AC e se o número for positivo, apanha a próxima instrução da metade esquerda de 08D.
- Então transferimos o valor de 0FA com o sinal invertido para AC e salvamos em 0FB.

Fizemos algumas mudanças:
- Declaramos um valor em 0FA (25 decimal);
- Substituímos os endereços 08A, 08B e 08C por 000, 001 e 08D respectivamente;
- Adicionamos um comando para pular para um endereço que não existe em 08E.

Então agora nosso código:
- Armazena o número 25 em 0FA;
- Copia 25 para o AC, e depois passa do AC para 0FB;
- Copia 25 novamente para o AC e como é positivo apanha a próxima instrução na metade esquerda de 08D;
- Salvamos 25 com sinal contrário (-25) em AC e do AC guardamos em 0FB;
- Buscamos a próxima instrução em um endereço inexistente (1024 em decimal) causando a interrupção do programa:

Temos o código em [linguagem de máquina](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/Arquitetura/Problema%202.4.obj) e [linguagem de montagem](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/Arquitetura/Problema%202.4.asm).

## Algoritmo de Booth

### Adição

Primeiro precisamos definir como funciona a adição, já que uma multiplicação nada mais é que sucessivas adições.

A adição de inteiros em binário seguem algumas regras simples:
- 0+0=0;
- 0+1=1;
- 1+0=1;
- 1+1=0 (e 'vai 1' para o dígito de ordem superior)
- 1+1+1=1 (e 'vai 1' para o dígito de ordem superior)

### Overflow

E temos uma regra simples para determinar a ocorrência de overflow: se os dois números somados tem o mesmo sinal, ocorre overflow se o resultado possuir o sinal oposto.
Agora 

## Multiplicação de inteiros sem sinal

Escrevemos um [código em python](booth.py) para isso.
