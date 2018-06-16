# Projeto Difuso

As entradas são a quantidade de comida e a quantidade de colonos com fome e a saída é o nível de prioridade definido para a máquina de produção de alimento.

### Estoque
Por economia de energia, é conveniente manter apenas um reservatório de comida refrigerado, então nossa quantidade de comida vai ser de 0 a 100, correspondendo a vazio e cheio equivalentemente. E vamos definir como:
- Vazio: Máximo (1) quando a quantidade é 0 e mínima (0) quando a quantidade é 50, daí em diante se mantém como 0;
- Médio: Mínimo (0) quando a quantidade é 0, máximo (1) quando a quantidade é 50, e então decai para o mínimo (0) novamente com a comida em 100;
- Cheio: Mínimo (0) desde quando a quantidade é 0 até 50, então máximo (1) quando a quantidade é 100;

### Famintos
Mantenho um máximo de 10 colonos ao mesmo tempo em cada colônio, acredito que esse é um número suficiente para manter todas atividades em operação, então vamos definir a quantidade de colonos famintos como:
- Poucos: Máximo (1) quando a quantidade é 0 e mínima (0) quando a quantidade é 5, daí em diante se mantém como 0;
- Médio: Mínimo (0) quando a quantidade é 0, máximo (1) quando a quantidade é 5, e então decai para o mínimo (0) novamente quando a quantidade de colonos famintos é 10;
- Muitos: Mínimo (0) desde quando a quantidade é 0 até 5, então máximo (1) quando a quantidade é 10;

### Prioridade
A prioridade no jogo é definido em uma escala de níveis entre 1 e 9, vamos classificar como:
- Baixa: Máximo (1) quando o nível é 1 e mínima (0) quando a quantidade é 5, daí em diante se mantém como 0;
- Média: Mínimo (0) quando o nível é 1, máximo (1) quando o nível é 5, e então decai para o mínimo (0) novamente quando o nível de prioridade é 9;
- Muitos: Mínimo (0) desde quando o nível é 1 até 5, então máximo (1) quando a quantidade é 9;

<b> Observação:<b> Todas variações são lineares.
  
  ### Regras Difusas
  Vamos definir relações difusas entre as entradas e saídas:
  1 - Se o estoque é vazio OU os famintos são muitos, então a prioridade é alta;
  2 - Se o estoque é medio então a prioridade é média;
  4 - Se o Estoque é cheio OU os famintos são poucos, então a prioridade é baixa.
