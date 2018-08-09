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

- As variáveis devem ser declaradas sem valor, informando o tipo e com ponto e vírgula.
- Se for vetor, ainda incluir os tipos de dados que o vetor deve conter e o tamanho.
- Pode ser informado um valor inicial na declaração utilizando igualdade, caso contrário, será atribuído o valor 0.
- Preferência pela utilização do espaço entre cada elemento da declaração.

Atualmente é suportado:
- Inteiros: int *nome* = *valor* ;
- Vetor de inteiros: vet *tipo* [*tamanho*] *nome* = [*valor#1*,*valor#2*,...] ;

Ex.:
```
var {
int inteiro ;
vet int [5] vetor ;
int A=10 ;
vet int [3] outro = [1,2,3] ;
}
```

## start

- Cada valor deve sempre estar atribuído a alguma variável em operações e funções. Ex.:
Errado:
```
a = b + 1 ;
if (a>1){...}
```
Certo:
```
c = 1 ;
a= b + c ;
if (a>c) {....}
```
### Atribuições:

- Valor direto:
  - Ocupa meio espaço na memória.
  - Vetores iniciam no 0;
  - Vetores devem ter os valores atribuídos elemento por elemento;
```
a = 1 ;
b [0] = 1 ;
b [1] = 2 ;
```
- Outra variável:

- Operações:
  - Soma:
  - Subtração:
  - Multiplicação:
  - Divisão:

# Condição:
- Usamos apenas o IF;
- Múltiplos IFs não podem ser aninhados;
- Cada IF comporta uma única condição;
- Else é necessário (pode estar vazio);
  - Maior:
  - Menor:
  - Igual:
  - Diferente
Exemplo:
```
if (a>b)
{
  código
}
else { }

```

#Repetição:
- Usamos apenas o while;
- Mesmas estruturas condicionais do IF:
  - Maior:
  - Menor:
  - Igual:
  - Diferente:
Exemplo:
```
while(a<b){
  código
}
```

## Memória

Além das limitações óbvias quanto as instruções que podem ser rodadas nas máquina IAS, uma limitação extra nos diz respeito a sua memória. Ela possui 1024 espaços na memória:
- Uma variável inteira ocupa um espaço na memória;
- Um vetor de inteiros, ocupa uma quantidade de espaço armazenadas correspondente ao tamanho do vetor.
- Uma instrução básica do processador ocupa meia memória, mas nossas funções ocupam mais, conforme a documentação de cada.


# Compilador

- As variáveis são armazenadas do final para o começo da memória do IAS;
- As instruções são armazenadas do começo pra o final do IAS;
- Sem sinalizações de erros.
- Máximo de 756 variáveis.
