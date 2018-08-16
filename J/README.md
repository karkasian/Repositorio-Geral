#  Arquitetura de computadores

Especificamente sobre a programação do computador IAS o professor Edson Borin disponibiliza um excelente material:
- Apostila intitulada [Programando o IAS](http://www.ic.unicamp.br/~edson/disciplinas/mc404/2017-2s/abef/anexos/programando_o_IAS.pdf);
- Um simulador para rodar o código de máquina: [IAS Simulator](http://www.ic.unicamp.br/~edson/disciplinas/mc404/2017-2s/abef/IAS-sim/);
- Um assembler para rodarmos o código de montagem: [IAS - Assembler](http://www.ic.unicamp.br/~edson/disciplinas/mc404/2017-2s/abef/IAS-Assembler/assembler.html).

## Introdução

- *Arquitetura de computador*: atributos de um sistema visíveis a um programador;
  - Atributos arquiteturais: conjunto de instruções, número de bits usados para representar os tipos de dados, mecanismos de E/S e técnicas para endereçamento de memória.
- *Organização de computador*: unidades operacionais e suas interconexões que realizam as especificações arquiteturais.
 - Atributos organizacionais: detalhes do hardware transparentes ao programador.

 Ex.:
 - Questão da arquitetura: se o computador terá uma instrução de multiplicação.
 - Questão da organização: se a instrução será implementada por uma unidade de multiplicação especial ou por um mecanismo que faça uso repetido da unidade de adição do sistema.

## Estrutura e função

- **Estrutura**: o modo como os componentes são inter-relacionados.
- **Função**: a operação individual de cada componente como parte da estrutura.

### Função

- Processamento de dados;
- Armazenamento de dados;
- Movimentação de dados;
- Controle.

### Estrutura

- **Unidade central de processamento (CPU)**: controla a operação do computador e realiza suas funç~eos de processadmento de dados.
- **Memória principal**: armazena dados.
- **E/S**: move os dados entre o computador e seu ambiente externo.
- **Interconexão do sistema**: mecanismo que oferece comunicação entre CPU, memória principal e E/S. Ex.: *barramento do sistema*.

Estrutura da CPU:
- **Unidade de controle**: controla a operação da CPU (e do computador).
- **Unidade aritmética e lógica (ALU)**: funções de processamento de dados.
- **Registradores**: armazenamento interno à CPU.
- **Interconexão da CPU**: comunicação entre a unidade de controle, ALU e registradores.

## IAS

- Construção de 1946 a 1952;
- Protótipo de todos os computadores de uso geral;
- Estrutura geral de um computador IAS:
  - Uma memória principal: armazena dados e instruções.
  - Uma unidade lógica e aritmética (ALU): opera sobre dados binários.
  - Uma unidade de controle: interpreta as instruções na memória e faz com que sejam executadas.
  - Um equipamento de entrada e saída (E/S): opera pela unidade de controle.

Memória do IAS:
- 1.000 locais de armazenamento (*words*) de 40 dígitos bináris (bits) cada.
- Dados e instruções são armazenados.
- Número são representados em código binário.
  - Cada número é representador por 1 bit de sinal e um valor de 39 bits.
- Instrução é um código binário.
  - Uma palavra pode conter duas instruções de 20 bits;
  - 8 bits (*opcode*) especifica a operação a ser realizada;
  - 12 bits (endereçamento): especificando uma das palavras da memória (0 a 999).

A unidade de controle opera o IAS buscando instruções da memória e executando-as uma de cada vez. A unidade de controle e a ALU contém locais de armazenamento chamados *registradores*:
- **Registrador de buffer de memória (MBR)**: Recebe uma palavra da memória ou E/S ou tem uma palavra pra ser enviada pra memória ou E/S.
- **Registrador de endereço de memória(MAR)**: especifica o endereço na memória da palavra a ser escrita ou lida no MBR.
- **Registrador de instrução (IR)**: contém o opcode (8bits) da instrução que está sendo executada.
- **Registrador de buffer da instrução (IBR)**: mantém temporariamente a próxima instrução a ser executada.
- **Contador de programa (PC)**: contém o endereço do próximo par de instruções a ser apanhado na memória.
- **Acumulador (AC) e quociente multiplicador(MQ)**: empregado para manter temporariamente operandos e resultados de operações da ALU.

O IAS opera realizando repetidamente um ciclo de instrução, e cada ciclo possui dois sub-ciclos:
- Ciclo de busca (fetch cycle): Pode ser retirada do IBR, ou carregando uma palavra no MBR e depois para o IBR.
  - O opcode da próxima instrução é carregador no IR;
  - O endereço é carregado no MAR;
- Ciclo de execução.

![ciclo do processador](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/J/imagens/ciclo.png)

O IAS tinha 21 instruções agrupadas da seguinte forma?
- **Transferencia de dados**: movem dados entre memórias e registradores da ALU;
- **Desvio inional**: a sequência a partir da memória pode ser alterada, facilitando operações repetitivas;
- **Desvio condicional**: o desvio pode depender de uma condição;
- **Aritméticas**: operações realizadas na ALU;
- **Modificação de endereço**: permite que os endereços sejam calculados na ALU e depois inseridos em instruções armazenadas na memória.

![instruções do IAS](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/J/imagens/instrucoes.png)

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

### Condição:
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

### Repetição:
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
