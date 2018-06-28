# Estatística Básica

## Medidas de tendência central

Estas medidas verificam uma tendência dos dados observados a se agruparem em torno dos valores centrais.

### Média aritmética (x̄)

A média aritmética é calculada como a divisão entre a soma dos valores dos conjuntos e o número total de valores somados. Se nosso conjunto é por exemplo (1,3), nossa média é entao <code>x̄=(1+3)/2</code>.

Vamos utilizar para nossa série de análises, como conjunto de dados o saldo dos mapas do NYE em cada jogo desde o incídio da liga: 
- (2,-2,2,2,3,4,-1,1,4,2,3,1,-1,2,-1,4,4,2,4,1,4,1,4,1,4,4,-1,1,1,1,2,4,4,2,3,3,3,2,4,4,4,-1,-1,1,-2,1,1,-2)

Então obtemos uma média de 1.83 mapa por jogo, isso significa o NYE é mais propenso a vencer com 2 mapas de diferença, do que perder.

### Mediana (Md)

Mediana é o valor que separa um conjunto ordenado segundo uma ordem (crescente ou decrescente) em dois subconjuntos com o mesmo número de elementos.

Se temos uma quantidade <code>n</code> ímpar de elementos, vai ser o elemento <code>N=(n+1)/2</code>, se for par vai ser a média entre os elementos <code>n/2</code> e <code>n/2+1</code>.

Obtemos uma mediana de 2.

### Moda (Mo)

É o valor que ocorre com maior frequência. Podendo ser amodal se nenhum valor aparece mais vezes que os outros, ou bimodal se houver dois valores de contração. Ainda pode haver mais valores.

No nosso caso, a moda apresentada foi 4. Significa que o placar que mais se repetiu foi com saldo positivo de 4 mapas para o NYE, ou seja. 4x0.

## Medidas de dipersão

Através das medidas de dispersão avaliamos a dispersão dos dados em tornod os valores centrais.

### Amplitude total (A)

É simplesmente a diferença entre o maior e o menor dos valores da série.

Nós temos uma amplitude total de 6. Como o a diferença máxima em uma partida é de 4 mapas, e o NYE teve vitórias de 4x0, significa que a maior derrota que teve, foi por 2 mapas de diferença.

### Variância (S²)

Variância  baseia-se nos desvios em torno da média aritmética, é portanto um indicador de variabilidade. Ela considera o quadrado de cada desvio individual para calcularmos a média do desvio sobre os graus de liberdade.

Sua fórmula é então o somatório dos desvios individuais divido pelos graus de liberdade: <code>S²= Σ<sub>i</sub>(x<sub>i</sub>-x̄)²/(n-1)</code>.

Então, temos que <code>(n-1)</code> é o grau de liberdade da amostra. Graus de liberdade indicam os espaços entre os dados, portanto para <code>n</code> amostras, temos <code>(n-1)</code> graus de liberdade. Uma forma de interpretar os graus de liberdade, é tendo então um conjunto de <code>n</code> observações, e tendo ua média fixa, podeos escolher os valores numéricos de <code>(n-1)</code> observações, e o valor da última observação é determinado pelo valor da média fixada, ou seja, é o necessário para que tenhamos a média definida.

Calculamos uma variância de 3,674.

### Desvio-padrão (S)

Para aproximar a variância da medida da variável original, tiramos a raiz quadrada da variância. Temos então que <code>S=√(S²)</code>.

No nosso caso, temos um desvio padrão de 1,917.

### Coeficiente de variação

É uma medida relativa da dispersão, fazemos a razão entre o desvio padrão e a média, e multiplicalmos por 100: <code>CV=(S/x̄).100%</code>

O coeficiente de variação apresentado foi de 104.5%. Então sabemos que teve resultados bem variados durante a liga.

Mais informações sobre estatística básica podem ser obtidas no [Minicurso de Estatística Básica: Minicurso de Estatística Básica:
Introdução ao software R](http://www.uft.edu.br/engambiental/prof/catalunha/arquivos/r/r_bruno.pdf), oferecido pela <abbr title="Universidade Federal de Santa Maria">UFSM</abbr>.

# Distribuições

## Distribuição qui-quadrado

Qui Quadrado é um teste não paramétrico, isto é, não depende de parâmetros populacionais como média e variância, que serve para avaliar quantitativamente a relação entre o resultado de um experimento e a distribuição esperada para o fenômeno.

Trabalhamos com duas hipóteses:
- Hipótese nula (H0): as frequências observadas não são diferentes das frequências esperadas.
- Hipótese alternativa: as frequências observadas são diferentes das frequências esperadas.

É simbolizado pela letra grega qui elevada ao quadrado, pela semelhança com X iremos adotar X. Karl Pearson propôs que para medir as possíveis discrepâncias entre as proporções observadas e esperadas, deviamos fazer o somatório do quadrado da diferença entre a frequência observada e a esperada para classe, dividida pela esperada. Ou seja, chamando de <code>o</code> de frequência observada e <code>e</code> de frequência esperada: <code>X²=Σ[(o-e)²/e]</code>. 

Chamamos de classe os  valores que podem ser assumidos. Por exemplo se lidarmos com as probabilidades relacionadas a jogar uma moeda, podemos ter cara ou coroa, 2 classes. Se jogarmos 100 vezes a moeda, temos 100 medidas, mas 2 classes.

### Procedimento

O procedimento padrão é primeiro calcular um X² a partir dos dados experimentais e definir um nível de significância. Então a partir de um X² tabelado que depende deste nível significância e do grau de liberdade de nossos dados, tomamos a decisão comporando os dois valores de X²:

- Se o X² é maior ou igual ao X² tabelado, rejeitamos a hipótese nula.
- Se X² é menor que o X² tabelado, aceitamos H0.

Aqui é importante entendermos o que é consultar o valor tabelado. Quando consultamos a tabela, observamos a probabilidade de ocorrência daquele acontecimento. Portanto rejeitamos a hipótese quando a máxima probabilidade de erro ao rejeitar aquela hipótese for baixa.
Por sua vez, o nível de significância (normalmente representado pela letra grega alfa), representa a máxima probabilidade de erro que se tem ao rejeitar uma hipótese.

Portanto a distribuição X² que correponde aos nossos valores tabelados, corresponde a hipótese nula. Se o valor de X² calculado, apresentar uma baixa probabilidade de ocorrência pra distribuição da hipótese nula, rejeitamos a hipótese nula.

### Projeto

Vamos descobrir se eu sei exatamente o que vai acontecer nos jogos do NYE. Para isso, vamos comparar os meus palpites no bolão com os resultados verdadeiros. Para simplificar vamos denotar 1 para uma vitória do NYE, e -1 para uma derrota, e vamos utilizar apenas os jogos do último estágio da liga deste ano (2018).

Então minhas apostas foram: (-1,1,1,-1,-1,1,-1,1,1,-1) e o resultado na verdade foi (1,1,1,1,1,-1,-1,1,-1,1). 

Como hipóteses temos:

- H0: as frequências observadas não são diferentes das frequências esperadas, eu sou um bom apostador.
- H1: as frequências observadas são diferentes das frequências esperadas, eu errei as apostas.

Como nossos valores podem assumir 2 valores, temos então 1 grau de liberdade. Vamos definir um nível de significância de 10% (a=0,1). 

Calculando o X² temos um valor de 0.5261. O próximo passo, seria consultar a tabela,mas ao invés disso, vamos construir esta tabela.

A tabela depende do grau de liberdade e do nível de significância. Primeiro, o grau de liberdade é utilizado para a construção da função probabilidade. Ela determina a probabilidade da função X² retornar um determinado valor, para aquele grau de liberdade. Ao invés de utilizarmos a função probabilidade, vamos calcular.

A distribuição qui quadrado é uma soma dos quadrados de amostras de uma distribuição normal. Isto é, se pegamos amostras de uma distribuição normal, a distribuição qui-quadrado é a distribuição soma desses valores ao quadrado, e os graus de liberdade é sua média, e também a quantidade de amostras sendo somadas. Por exemplo, no nosso caso, queremos uma distribuição com 1 grau de liberdade, então só precisamos pegar uma amostra aleatória com uma distribuição normal e elevarmos seus valores ao quadrado, a distribuição final, é nossa distribuição X². Se tivessemos dois grausde liberdade, somariamos um elemento elevado ao quadrado de cada amostra para termos cada X², e esses valores seriam nossa distribuição.

O nível de significância nos indica onde está nosso ponto crítico. Um nível de significância comum de a=0.05, significa que ele é o ponto em que tem 95% de chance de termos um valor menor, isto é, a probabilidade acumulada até imediatamente antes a aquele ponto é de 95%. Então há apenas 5% de chance da função assumir aquele valor, ou mesmo, algum valor maior.

Uma leitura interessante sobre o assunto pode ser conferido no texto [Qui Quadrado](http://www.ufpa.br/dicas/biome/biopdf/bioqui.pdf), disponibilizado pela <abbr title="Universidade Federal do Pará">UFPA</abbr>.

