# Projeto Física

## Treinamento

### Junkrat e MRUV

A equação de MRUV para o movimento vertical da física para um corpo inicialmente em uma posição <code>(0,0)</code> é <code>y=v.sen(θ)+g.t²/2</code>. Então o tempo que um corpo leva para cair é dado por <code>t=-2.v.sen(θ)/g</code>. Substituindo esse tempo na equação de MRU do movimento horizontal <code>x=v.cos(θ).t</code> temos então a distância em que o corpo atingiu o chão <code> x= -2.v².cos(θ).sen(θ)/g</code>.

De acordo a [Overwatch Wiki](https://overwatch.gamepedia.com/Junkrat) a velocidade do projétil do Junkrat é de <code>17,5m/s</code>. Utilizando um ângulo de <code>45°</code> (máximo alcance para um lançamento oblíquo simples), se utilizarmos um valor real para a gravidade (<code>-9.81m/s²</code>) temos um alcance máximo de <code>31.22m</code>.

### Entradas e saídas

Ainda de acordo com a mesma, a área de efeito da bomba é de <code>2m</code>. Então nossas entradas serão a distância do inimigo e o ângulo, e nossa saída será 1 ou 0, indicando se acertou ou não o inimigo respectivamente. Aqui é importante destacar que acertar o inimigo significa que o projétil caiu a no mínimo <code>2m</code> de distância de nosso inimigo.

### Dados de treinamento

Os dados de treinamento vão ser gerados da seguinte forma então: 
- A distância do inimigo vai variar entre 0 e 5, com uma variação de 0.05, o que gera 100 valores diferentes;
- O ângulo vai variar entre 0 e 45°, com uma variação de 0.5º, o que gera 90 valores;

Então vamos ter 100x90=9000 resultados possíveis. Essa é a quantidade de dados com que vamos alimentar nossa rede.

## Modelo de rede

## Neurônio Sigmoid

Inicialmente, pensei em utilizar o neurônio perceptron, mas ele exige que a saída seja linarmente separável. Isto é, plotando o gráfico Entrada_1 x Entrada_2, precisamos que os pontos que representam uma saída 1 possam ser separados por uma linha dos pontos que representem uma saída 0. No nosso caso, relacionando distância x ângulo, teremos uma faixa de valores que representariam os pontos 1. Ou seja, para funcionar, para uma dada distância, precisariamos que a partir de certo valor do ângulo sempre fosse 1, mas a verdade é que abaixo de um valor o projétil não chega no alvo, e acima de outro valor, o projétil passa do alvo.

Se nosso objetivo fosse ensinar a rede a checar se o projétil ultrapassada um ponto (com ângulo máx de 45°) por exemplo, poderíamos utilizar o perceptron, mas no nosso caso, vamos utilizar o sigmoid. Sua saída é dada pela função <code>1/(1+exp[-SOM<sub>i</sub>(p<sub>i</sub>.e<sub>i</sub>)-l])</code>. Onde <code>p<sub>i</sub></code> é o peso correspondente a entrada <code>e<sub>i</sub></code>, então <code>SOM<sub>i</sub>(p<sub>i</sub>.e<sub>i</sub>)</code> é o somatório dos produtos entre os pesos e entradas o  e <code>l</code> é o limiar do neurônio. Se chamarmos <code>e</code> nosso vetor com todas as entrads do neurônio e <code>p</code> todos os pesos, podemos substituir o somatório como um produto interno entre os vetores e ficar com <code>1/(1+exp[-p.e-l])</code>.

A primeira cada de uma rede neural é considerada as entradas, sendo cada entrada um neurônio, então toda rede tem no mínimo 2 camadas, uma de entrada e uma de saída, podendo ter outras entre elas, chamadas "camadas escondidas". Vamos trabalhar com uma rede de 3 camadas:
- A primeira cada (também chamada de camada de entrada) são as entradas, temos duas entradas (distância e ângulo), então dizemos que ela tem 2 neurônios que tem como saída o próprio valor puro;
- A segunda camada, a do meio, tem 3 neurônios e cada neurônio tem como entrada os 2 neurônios da primeira camada, isto é a própria distância e ângulo;
- Por fim, na terceira camada, chamada de camada de saída, temos um único neurônio, que vai nos dar a saída que diz se atingiu o alvo (1) ou não (0); como entrada, ela tem os três valores gerados pelos 3 neurônios da camada anterior.



