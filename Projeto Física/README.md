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

