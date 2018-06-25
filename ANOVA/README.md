# Estatística Básica

<<<<<<< HEAD
#
=======
A fim de descobrirmos se temos diferenças entre nossos três grupos devido a algum fator que controlamos, podemos seguir alguns passos:

## Passo 1: Hipóteses

Primeiro passo, é determinar quais as hipóteses que queremos checar. Para aplicar o método ANOVA com 1 fator, temos as seguintes hipóteses:

- Hipótese nula (H0): não há diferença entre os valores médios dos grupos: o fator não tem efeito.
- Hipótese alternativa (H1): nem todas as médias são iguais: o fator tem efeito.


## Passo 2: Estatística de teste

O valor da estatística de teste é usado para decidir se podemos ou não rejeitar a hipótese nula, este é um valor calculado a partir de nossa amostra de dados.

Para o ANOVA, a estatística de teste utilizada é o teste f: a razão entre a variância entre amostras e a variância dentro das amostras: <code>F=S²<sub>entre</sub>/S²<sub>dentro</sub></code>

## Passo 3: Regras de decisão

Precisamos estabelecer agora as regras que irão determinar se rejeitamos a hipótese nula ou não. Então aqui precisamos calcular o F Crítico (Fc) e então determinamos se nosso valor calculado peça estatística de teste for maior ou igual que o F crítico, rejeitamos nossa hipótese nula.

O valor crítico é obtido pela distribuição F.

### Distribuição F

Uma variável aleatória de uma distribuição F surge como uma razão entre duas distribuições qui-quadradas divididas por seus graus de liberdade: <code>X=(U<sub>1</sub>/d<sub>1</sub>)/(U<sub>2</sub>/d<sub>2</sub>)</code>, onde <code>U<sub>i</sub></code> é uma distribuição qui-quadrado com <code>n<sub>i</sub></code> graus de liberdade.

A sua função densidade de probabilidade (<abbr title="probability density function">PDF</abbr>) descreve a probabilidade de uma variável tomar um valor dado. 

Se uma variável aleatória X tem uma função distribuição F, a função densidade de probabilidade dada para X é dado por:

![PDF de uma distribuição F](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/ANOVA/imagens/PDF.png)

Onde B é uma função beta, para valores inteiros toma a forma:

![Função beta para inteiros](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/ANOVA/imagens/beta.png)

A função de distribuição cumulativa  (<abbr title="cumulative distribution function">CDF</abbr>) avalia a probabilidade de uma variável aleatória assumir um valor igual ou menor a X. Ela pode ser expressada como uma a integral da função densidade de probabilidade de infinito negativo a X.

A distribuição F surge como a distribuição nula da estatística de um teste. Nessa etapa determinamos o nível de significância que vamos aceitar, um valor típico é a=0.05. Então se definimos um a=0.05, significa que definimos um intervalo de 5% no extremo direito da função de distribuição em que se o nosso valor F cair dentro desta faixa, rejeitamos a hipótese 0.

Isto se deve quanto mais a direita de nossa função de distribuição, menor a probabilidade que uma variável aleatória assuma esse valor para uma distribuição nula, então maior a probabilidade que nossa função F calculada a partir de nossos dados, não pertence a uma distribuição nula, consequentemente, maior a segurança para rejeitar nossa hipótese nula.

Então se nossa CDF nos retorna a probabilidade obtermos um valor X ou menor, <code>(1-CDF)</code> vai nos retornar a probabilidade de obtermos um valor X ou maior. Portanto se definimos a=0.05, queremos que o valor de nossa função F nos retorne um valor maior ou igual a 99.5% na CDF, ou então menor que 5% se utilizarmos <code>(1-CDF)</code>.

## Passo 4: Cálculo

## Passo 5: Conclusão

ANOVA 1 fator: https://edisciplinas.usp.br/pluginfile.php/3260534/mod_resource/content/1/T%C3%B3pico_13.pdf
Passo a passo: http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_HypothesisTesting-ANOVA/BS704_HypothesisTesting-Anova_print.html
>>>>>>> 81e62f90f0a46f71138d4d6e7682e091a6e8acfa
