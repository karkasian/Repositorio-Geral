# Estatística Básica

## Medidas de tendência central

Estas medidas verificam uma tendência dos dados observados a se agruparem em torno dos valores centrais.

### Média aritmética (x̄)

A média aritmética é calculada como a divisão entre a soma dos valores dos conjuntos e o número total de valores somados. Se nosso conjunto é por exemplo (1,3), nossa média é entao <code>x̄=(1+3)/2</code>.

Vamos utilizar para nossa série de análises, como conjunto de dados o saldo dos mapas do NYE em cada estágio: (21,25,22,15).

Então obtemos uma média de saldo de 20,75  por estágio.

### Mediana (Md)

Mediana é o valor que separa um conjunto ordenado segundo uma ordem (crescente ou decrescente) em dois subconjuntos com o mesmo número de elementos.

Se temos uma quantidade <code>n</code> ímpar de elementos, vai ser o elemento <code>N=(n+1)/2</code>, se for par vai ser a média entre os elementos <code>n/2</code> e <code>n/2+1</code>.

Obtemos uma mediana de 21,5.

### Moda (Mo)

É o valor que ocorre com maior frequência. Podendo ser amodal se nenhum valor aparece mais vezes que os outros, ou bimodal se houver dois valores de contração. Ainda pode haver mais valores.

No nosso caso, não temos uma moda.

## Medidas de dipersão

Através das medidas de dispersão avaliamos a dispersão dos dados em tornod os valores centrais.

### Amplitude total (A)

É simplesmente a diferença entre o maior e o menor dos valores da série.

Nós temos uma amplitude total de 10.

### Variância (S²)

Variância  baseia-se nos desvios em torno da média aritmética, é portanto um indicador de variabilidade. Ela considera o quadrado de cada desvio individual para calcularmos a média do desvio sobre os graus de liberdade.

Sua fórmula é então o somatório dos desvios individuais divido pelos graus de liberdade: <code>S²= Σ<sub>i</sub>(x<sub>i</sub>-x̄)²/(n-1)</code>.

Então, temos que <code>(n-1)</code> é o grau de liberdade da amostra. Graus de liberdade indicam os espaços entre os dados, portanto para <code>n</code> amostras, temos <code>(n-1)</code> graus de liberdade. Uma forma de interpretar os graus de liberdade, é tendo então um conjunto de <code>n</code> observações, e tendo ua média fixa, podeos escolher os valores numéricos de <code>(n-1)</code> observações, e o valor da última observação é determinado pelo valor da média fixada, ou seja, é o necessário para que tenhamos a média definida.

Mais informações sobre estatística básica pode ser lida no [Minicurso de Estatística Básica: Minicurso de Estatística Básica:
Introdução ao software R](http://www.uft.edu.br/engambiental/prof/catalunha/arquivos/r/r_bruno.pdf), oferecido pela <abbr title="Universidade Federal de Santa Maria">UFSM</abbr>.
