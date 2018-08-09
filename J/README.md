# Linguagem

## Estrutura principal

Nosso propósito aqui é desenvolver uma linguagem simples de alto nível para o IAS.
Nosso código deve ser dividido em duas partes. Uma para a declaração de variáveis:
```
var {
...
}
```
E outro que deve conter os comandos que serão executados:
```
start {
...
}
```
A ordem em que é feito a declaração não importa podemos ter tanto <code>var {...} start {...}</code>, quanto <code>start {...} var {...}</code>.

## var

As variáveis devem ser declaradas sem valor, informando o tipo e com ponto e vírgula. Se for vetor, ainda incluir os tipos de dados que o vetor deve conter e o tamanho.
Pode ser informado um valor inicial na declaração utilizando igualdade, caso contrário, será atribuído o valor 0.
Atualmente é suportado:
- Inteiros: int *nome* = *valor*;
- Vetor de inteiros: vet *tipo* [*tamanho*] *nome* = [*valor#1*,*valor#2*,...];

Ex.:
```
var {
int inteiro;
vet int [5] vetor;
int A=10;
vet int [3] outro=[1,2,3];
}
```

## start

## Memória

Além das limitações óbvias quanto as instruções que podem ser rodadas nas máquina IAS, uma limitação extra nos diz respeito a sua memória. Ela possui 1024 espaços na memória:
- Uma variável inteira ocupa um espaço na memória;
- Um vetor de inteiros, ocupa uma quantidade de espaço armazenadas correspondente ao tamanho do vetor.
- Uma instrução básica do processador ocupa meia memória, mas nossas funções ocupam mais, conforme a documentação de cada.

# Compilador
