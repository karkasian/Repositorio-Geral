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

## Teste qui-quadrado

Qui Quadrado é um teste não paramétrico, isto é, não depende de parâmetros populacionais como média e variância, que serve para avaliar quantitativamente a relação entre o resultado de um experimento e a distribuição esperada para o fenômeno.

Trabalhamos com duas hipóteses:
- Hipótese nula (H0): as frequências observadas não são diferentes das frequências esperadas.
- Hipótese alternativa: as frequências observadas são diferentes das frequências esperadas.

É simbolizado pela letra grega qui (chi) elevada ao quadrado, pela semelhança com X iremos adotar X. Karl Pearson propôs que para medir as possíveis discrepâncias entre as proporções observadas e esperadas, deviamos fazer o somatório do quadrado da diferença entre a frequência observada e a esperada para classe, dividida pela esperada. Ou seja, chamando de <code>o</code> de frequência observada e <code>e</code> de frequência esperada: <code>X²=Σ[(o-e)²/e]</code>. Em 1900 Person mostrou que em um limite com suficientes observações, X² segue uma distribuição qui-quadrado com um grau de liberdade igual a <code>quantidade de classes - 1</code>.

Chamamos de classe os  valores que podem ser assumidos. Por exemplo se lidarmos com as probabilidades relacionadas a jogar uma moeda, podemos ter cara ou coroa, 2 classes. Se jogarmos 100 vezes a moeda, temos 100 medidas, mas 2 classes.

### Procedimento

O procedimento padrão é primeiro calcular um X² a partir dos dados experimentais e definir um nível de significância. Então a partir de um X² tabelado que depende deste nível significância e do grau de liberdade de nossos dados, tomamos a decisão comporando os dois valores de X²:

- Se o X² é maior ou igual ao X² tabelado, rejeitamos a hipótese nula.
- Se X² é menor que o X² tabelado, aceitamos H0.

Aqui é importante entendermos o que é consultar o valor tabelado. Quando consultamos a tabela, observamos a probabilidade de ocorrência daquele acontecimento. Portanto rejeitamos a hipótese quando a máxima probabilidade de erro ao rejeitar aquela hipótese for baixa.
Por sua vez, o nível de significância (normalmente representado pela letra grega alfa), representa a máxima probabilidade de erro que se tem ao rejeitar uma hipótese.

Portanto a distribuição X² que correponde aos nossos valores tabelados, corresponde a hipótese nula. Se o valor de X² calculado, apresentar uma baixa probabilidade de ocorrência pra distribuição da hipótese nula, rejeitamos a hipótese nula.

### Distribuição X²

A tabela depende do grau de liberdade e do nível de significância. Primeiro, o grau de liberdade é utilizado para a construção da função probabilidade. Ela determina a probabilidade da função X² retornar um determinado valor, para aquele grau de liberdade. 

A distribuição qui quadrado é uma soma dos quadrados de amostras de uma distribuição normal. Isto é, se pegamos <code>N</code> amostras de uma distribuição normal, a distribuição qui-quadrado é a distribuição da soma desses valores ao quadrado, e os graus de liberdade é sua média (os graus de liberdade também são quantidade de amostras sendo somadas). Para uma distribuição com 1 grau de liberdade, por exemplo, então só precisamos pegar uma amostra aleatória com uma distribuição normal e elevarmos seus valores ao quadrado, a distribuição final, é nossa distribuição X². Se tivessemos dois grausde liberdade, somariamos um elemento elevado ao quadrado de cada uma das duas amostras, então calcularíamos o X², e a distribuição destes valores finais calculados seriam nossa distribuição.

O nível de significância nos indica onde está nosso ponto crítico. Um nível de significância comum de a=0.05, significa que o ponto está em uma posição em que que tem 5% de chance da função assumir um valor igual ou maior que aquele. 

### Projeto

A análise do qui quadrado, serve para comparar frequências. Então vamos imaginar que antes de começar a Overwatch League, eu tivesse expectivas humildes que o Florida Mayhem fosse vencer metade das partidas, isto é 20 vitórias e 20 derrotas. Vamos comparar com a frequência real de 7 vitórias e 33 derrotas.

Como hipóteses temos:

- H0: as frequências observadas não são diferentes das frequências esperadas: Florida teve o desempenho esperado.
- H1: as frequências observadas são diferentes das frequências esperadas: nossa teoria estava errada.

Como nossos valores podem assumir 2 valores (vitória e derrota), temos então 1 grau de liberdade. Vamos definir um nível de significância padrão de 5% (a=0,05). 

Calculando o X² temos um valor de 16,9. O próximo passo, seria consultar a tabela,mas ao invés disso, vamos construir esta tabela.

Para nossa aproximação, vamos simplesmente gerar uma distribuição normal de pontos, agrupar eles em faixas de valores. Teremos então uma quantidade de colunas equivalente a quantidade a quantidade de faixas de valores, onde a área da coluna é dada pelo produto de sua altura(quantidade de pontos dentro da faixa) pela largura (tamanho da faixa). Então só precisamos normalizar para que o total da soma da área de todas as colunas seja igual 1. Então só precisamos ir somando as áreas de todas as colunas da extrema direita em direção a origem, quando tivermos uma probabilidade igual ou maior a somada de a, checamos qual o valor do eixo x (valor X²) correspondente. Com esse método, dependendo dos parâmetros que definirmos (como quantidade de pontos e quantidade de faixas de valores), conseguimos obtee um valor arredondado para 3.84, que é o valor tabelado.

Portanto, rejeitamos nossa hipótese nula a admitimos que nossa teoria inicial que o Mayhem seria um time mediano, estava errada.

Uma leitura interessante sobre o assunto pode ser conferido no texto [Qui Quadrado](http://www.ufpa.br/dicas/biome/biopdf/bioqui.pdf), disponibilizado pela <abbr title="Universidade Federal do Pará">UFPA</abbr>.

## Distribuição F

A distribuição F de Snedecor com <code>d<sub>1</sub></code>  graus de liberdade no numerador e <code>d<sub>2</sub></code> graus de liberdade no denomidador é dado por: <code>F=(Q<sub>1</sub>/d<sub>1</sub>)/(Q<sub>2</sub>/d<sub>2</sub>)</code>, onde <code>Q<sub>i</sub></code> é uma distribuição qui-quadrado com <code>d<sub>i</sub></code> graus de liberdade.

Portanto pegamos duas distribuições qui-quadrado da seção anterior, pegamos então um elemento de cada e dividimos pelo grau de liberdade da distribuição a que pertence, e então fazemos a razão entre os dois valores resultantes, assim temos um valor de F. A distribuição destes valores calculados, nos dá a distribuição F de Snedecor. 

[Neste texto](http://www.de.ufpb.br/~tarciana/Probabilidade2/Aula16.pdf) da <abbr title="Universidade Federal da Paraíba">UFPB</abbr> você encontra mais informações sobre a distribuição F. 

# ANOVA

ANOVA,abreviação em inglês para Análise da Variância (Analysis of variance), é um método para testar a igualdade duas ou mais médias populacionais baseado na análise fas variâncias amostrais. Normalmente citado para testar três ou mais, pois se quisermos testar apenas 2, podemos analisar a viabilidade de utilizar um teste T.

Os dados primeiros devem ser separados em grupos segundo uma característica (também chamado de fator), que nada mais é que  alguma característica que permite distinguir diferentes populações uma das outras. Então cada fator contém dois ou mais grupos (também chamados de classificações).

Foi o estatístico E.P. Box que mostrou que os resultados são confiáveis se cumprido alguns critérios. 

Nós vamos querer descobrir se houve mudanças significativas de desempenho na atuação do New York Excelsior nas últimas 15 partidas (desconsideando os playoff) analisando o saldo de mapas em cada partida. Vamos ter grupos, com um único fator: o período liga.

- Período 1 - Final do terceiro estágio:(1,2,4,4,2).
- Período 2 - Começo do quarto estágio, novo meta: (3,2,4,4,4).
- Período 3 - Final do quarto estágio, já classificado: (-1,-1,1,-2,1).

A fim de descobrirmos se temos diferenças entre nossos três grupos, podemos seguir alguns passos:

## Passo 1: Hipóteses

Primeiro passo, é determinar quais as hipóteses que queremos checar. Para aplicar o método ANOVA com 1 fator, temos as seguintes hipóteses:

- Hipótese nula (H0): não há diferença entre os valores médios dos grupos: o fator não tem efeito. 
- Hipótese alternativa (H1): nem todas as médias são iguais: o fator tem efeito.

Para nós, estas hipóteses podem ser "traduzidas" como:
- H0: Não houve mudança no desempenho do NYE ao longo da liga.
- H1: Houve mudanças de desempenho entre algum período e outro.

Também nessa etapa determinamos o nível de significância, exatamente como pro teste de qui quadrado, vamos adotar a=0.05.

## Passo 2: Estatística de teste

O valor da estatística de teste é usado para decidir se podemos ou não rejeitar a hipótese nula, este é um valor calculado a partir de nossa amostra de dados.

Para o ANOVA, a estatística de teste utilizada é a estatística F: a razão entre a variância entre amostras e a variância dentro das amostras: <code>F=S²<sub>entre</sub>/S²<sub>dentro</sub></code>

## Passo 3: Regras de decisão

Precisamos estabelecer agora as regras que irão determinar se rejeitamos a hipótese nula ou não. Então aqui precisamos calcular o F Crítico (Fc) e então determinamos se nosso valor calculado peça estatística de teste for maior ou igual que o F crítico, rejeitamos nossa hipótese nula.

O valor crítico é obtido pela distribuição F. Para o grau de liberdade do numerador da distribuição, é relacionado com a variância entre os grupos, então vai ser a <code>quantidade de grupos-1</code>, e para o denominador, sob a variância dentro dos grupos, vamos ter então a <code>quantidade de elementos - quantidade de grupos</code>.

No próximo item essa relação vai ficar mais clara, por agora, vamos encontrar nosso Fc. Como temos 3 grupos, temos um grau de liberdade no numerador<code>gl<sub>n</sub>=3-1=2</code>, e como temos 15 valores no total (5 em cada grupo), vamos ter então para o denominador um grau de liberdade de <code>gl<sub>n</sub>=15-3=12</code>. Utilizando o mesmo processo de aproximação do teste anterior, conseguimos atingir um valor arrendado de Fc=3.89, que é o valor tabelado.

## Passo 4: Cálculo

Consideramos que a variação total é a soma entre a variação entre e a variação dentro das amostras. Então agora precisamos calcular de fato a variação entre e dentro dos grupos. Primeiro precisamos calcular o valor médio de cada grupo e a média de todos os elementos de todos os grupos (chamada também de grande média, normalmente é representado por um x com duas barras, pela dificuldade de escrita aqui, utilizaremos a letra grega μ).

Para a variância total, teríamos o padrão visto anteriormente: <code>S²= Σ<sub>i</sub>(x<sub>i</sub>-μ)²/(n-1)</code>, onde <code>μ</code> é a média entre todos os elementos, então também é a grande média. Também podemos escrever como um somatório duplo: <code>S²= Σ<sub>j</sub>Σ<sub>i</sub>(x<sub>ji</sub>-μ)²/(n-1)</code>, onde nosso <code>j</code> indica o grupo e <code>i</code> o elemento dentro do grupo.

Então, para calcular primeiro a variância entre os grupos, nós cálculamos a variância da seguinte forma: <code>S²<sub>entre</sub>= Σ<sub>j</sub>n<sub>j</sub>(x̄<sub>j</sub>-μ)²/(k-1)</code>. Só que agora:

- <code>x̄<sub>j</sub></code> é a média do grupo <code>j</code>;
- <code>μ</code> é a grande média;
- nosso grau de liberdade é dado por <code>(k-1)</code>, onde <code>k</code> é nossa quantidade de grupos, portanto é o grau de liberdade do numerador da nossa distribuição F;
- <code>n<sub>j</sub></code> é a quantidade de valores no grupo <code>j</code>, também dito como a frequência do elemento <code>x̄<sub>j</sub></code>.

Calculamos uma variância entre os grupos de 20.07.

Agora para calcular a variância dentro dos grupos, semelhante ao total temos: <code>S²<sub>dentro</sub>= Σ<sub>j</sub>Σ<sub>i</sub>(x<sub>ji</sub>-x̄)²/(n-k)</code>, como podemos ver as diferenças são que:
- Utilizamos a média do grupo a que pertence a amostra ao invés da média total;
- Nosso grau de liberdade é <code>(n-k)</code>, este é o grau de liberdade do denominador de nossa distribuição F.

Lembrando o que são os graus de liberdade, para nosso caso por exemplo, temos três grupos, aqui estamos lidando as médias dos três grupos. Quando tínhamos só a média total, tínhamos apenas uma média (fixada), então podíamos escolher <code>(n-1)</code> livremente, agora temos três médias, sendo que cada grupo tem  <code>m</code> elementos, em cada um podemos escolher aleatóriamente <code>(m-1)</code> elementos, então no total podemos escolher <code>(m-1)+(m-1)+(m-1)</code>, e sendo <code>n=m+m+m</code> nossa quantidade de elementos totais, temos um grau de liberdade de <code>n-3</code>, para o caso de 3 grupos.
 
Nossa variância dentro dos grupos ficou em 1,47. Então fazendo a divisão entre as duas obtemos um valor para F de 13.68.

## Passo 5: Conclusão

Nosso F calculado (13.68) é  maior que nosso Fc (3.89), portanto rejeitamos nossa hipótese nula. Nossa hipótese alternativa nos diz que há diferenças entre os períodos, isto é, houve mudanças de desempenho ao longo dos períodos. Mas, não sabemos qual período que é diferente, isto nos leva ao último passo: Teste de Scheffe.

Dois textos eu tenho para recomendar sobre o método ANOVA:
- [Análise da Variância (ANOVA)](https://edisciplinas.usp.br/pluginfile.php/3260534/mod_resource/content/1/Tópico_13.pdf): Sobre a ANOVa 1-fator e ANOVA 2-fator, divulgado pela <abbr title="Universidade de São Paulo">USP</abbr>.
- [Hypothesis Testing - Analysis of Variance (ANOVA)](http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_HypothesisTesting-ANOVA/BS704_HypothesisTesting-Anova_print.html): Sobre o método de 5 passos, texto fornecido pela Universidade de Boston.

# Teste de Scheffe

O teste de Scheffe é um teste de comparação de médias. Se não rejeitássemos a hipótese nula no ANOVA nenhum procedimento adicional seria necessário, mas como não rejeitamos, preciamos fazer uma análise para determinar quais médias são diferentes dads outras.

Vamos utilizar o teste de Scheffe, pode ser dividido em três etapas principais:

- Obter as diferenças absultas entre as médias dos grupos;
- Obter os valores nos quais devemos comparar nossas diferenças absolutas, para identificar diferenças estatísticamente significantes;
- Comparar os resultados.

## Passo 0: Resultados do ANOVA

Antes de começarmos o teste de Scheffe de fato, precisamos de alguns resultados obtidos quando aplicamos o método ANOVA:

- Variância dentro dos grupos: 1.47;
- F crítico: 3.89

## Passo 1: Diferenças absolutas

Primeiro passo é obtermos as diferenças absolutas entre as médias dos grupos:
- Entre grupo 1 e 2: 0.8
- Entre grupo 1 e 3: 3
- Entre grupo 2 e 3: 3.8

## Passo 2: 

O próximo passo é então obter os valores com os quais as diferenças absolutas devem ser comparados. Para isso utilizamos uma fórmula: <code>√((k-1).Fc.S²<sub>entre</sub>.(1/m<sub>i</sub>+1/m<sub>j</sub>))</code>, onde:

- <code>(k-1)</code>:grau de liberdade do numerador da função F, ou seja a quantidade de grupos menos um;
- <code>Fc</code>: F crítico calculado com os mesmo os graus de liberdade utilizado no método ANOVA, aqui podemos definir um novo nível de significância para este teste, mas vamos utilizar o mesmo, logo temos exatamente o mesmo valor: 3.89;
- <code>S²<sub>entre</sub></code>: variância entre os grupos;
- <code>(1/m<sub>i</sub>+1/m<sub>j</sub>))</code>: <code>m<sub>i</sub></code> e <code>m<sub>j</sub></code> são as quantidades de elementos em cada um dos dois grupos que estamos comparando.

Com esta fórmula, calculamos os seguintes valores para comaparação:

- Entre grupo 1 e 2: 2.62
- Entre grupo 1 e 3: 2.62
- Entre grupo 2 e 3: 2.62

## Passo 3:

Agora nos resta apenas concluir baseado nos valores calculados, lembrando que se a diferença absoluta entre as médias de dois grupos for maior que o valor para comparação, consideramos que são estatisticamente diferentes. Temos como resultado então que:

- Os grupos 1 e 2: não são estatisticamente diferente
- Os grupos 1 e 3: não são estatisticamente diferente
- Os grupos 2 e 3: são estatisticamente diferente

Então podemos confirmar que não houve mudança de desempenho entre o final do terceiro estágio e começo do último, ou seja, a mudança de meta não causou uma mudança de desempenho. Porém os dois períodos são estatisticamente diferente do último: a última metade do último estágio.

Com isso podemos afirmar estatisticamente que a garantia da vaga causou uma mudança de desempenho no NYE.

Sobre este último teste, eu recomendo um texto do Lycoming College, intitulado [Scheffe’s Pair Wise Comparison of Means ](http://lycofs01.lycoming.edu/~sprgene/M123/Text/UNIT_28.pdf).
