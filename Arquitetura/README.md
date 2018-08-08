#  Arquitetura de computadores

## Introdução

- *Arquitetura de computador*: atributos de um sistema visíveis a um programador;
  - Atributos arquiteturais: conjunto de instruções, número de bits usados para representar os tipos de dados, mecanismos de E/S e técnicas para endereçamento de memória.
- *Organização de computador*: unidades operacionais e suas interconexões que realizam as especificações arquiteturais.
 - Atributos organizacionais: detalhes do hardware transparentes ao programador.

 Ex.:
 - Questão da arquitetura: se o computador terá uma instrução de multiplicação.
 - Questão da organização: se a instrução será implementada por uma unidade de multiplicação especial ou por um mecanismo que faça uso repetido da unidade de adição do sistema.

Família de modelos de computador: mesma arquitetura, mas diferentes organizações.

## Estrutura e função

Sistema hierárquico: um conjunto de subsistemas inter-relacionados e cada um destes hierárquico,

Em cada nível o projetista está interessado em:
- **Estrutura**: o modo como os componentes são inter-relacionados.
- **Função**: a operação individual de cada componente como parte da estrutura.

Abordagem *top-down*: começamos de cima e decompomos o sistema em suas subpartes.

### Função

Funções básicas de um computador:
- Processamento de dados;
- Armazenamento de dados;
- Movimentação de dados;
- Controle.

- *Periférico*: dispositivo conectado diretamente ao computador que recebe ou entrega dado.

### Estrutura

Estruturas principais:
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

O IAS opera com um ciclo de instrução, e cada ciclo possui dois sub-ciclos:
- Ciclo de busca (fetch cycle): Pode ser retirada do IBR, ou carregando uma palavra no MBR e depois para o IBR.
  - O opcode da próxima instrução é carregador no IR;
  - O endereço é carregado no MAR;

O IAS tinha 21 instruções agrupadas da seguinte forma?
- **Transferencia de dados**: movem dados entre memórias e registradores da ALU;
- **Desvio incondicional**: a sequência a partir da memória pode ser alterada, facilitando operações repetitivas;
- **Desvio condicionao**: o desvio pode depender de uma condição;
- **Aritméticas**: operações realizadas na ALU;
- **Modificação de endereço**: permite que os endereços sejam calculados na ALU e depois inseridos em instruções armazenadas na memória.

![imagem]()