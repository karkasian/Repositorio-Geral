# ANOVA

A fim de descobrirmos se temos diferenças entre nossos três grupos devido a algum fator que controlamos, podemos seguir alguns passos:

## Passo 1: Hipóteses

Primeiro passo, é determinar quais as hipóteses que queremos checar. Para aplicar o método ANOVA com 1 fator, temos as seguintes hipóteses:

- Hipótese nula (H0): não há diferença entre os valores médios dos grupos: o fator não tem efeito.
- Hipótese alternativa (H1): nem todas as médias são iguais: o fator tem efeito.

Também nessa etapa determinamos o nível de significância que vamos aceitar, isto é "o quão incerto" vamos aceitar que nossa resposta seja. Um valor típico é utilizar a=0.05, isto é aceitamos uma probabilidade 5% de estar errado.

## Passo 2: Estatística de teste

O valor da estatística de teste é usado para decidir se podemos ou não rejeitar a hipótese nula, este é um valor calculado a partir de nossa amostra de dados.

Para o ANOVA, a estatística de teste utilizada é o teste f: a razão entre a variância entre amostras e a variância dentro das amostras: <code>F=S²<sub>entre</sub>/S²<sub>dentro</sub></code>

## Passo 3: Regras de decisão

Precisamos estabelecer agora as regras que irão determinar se rejeitamos a hipótese nula ou não. Então aqui precisamos calcular o F Crítico (Fc) e então determinamos se nosso valor calculado peça estatística de teste for maior ou igual que o F crítico, rejeitamos nossa hipótese nula.

O valor crítico é obtido pela distribuição F.

### Distribuição F

A função densidade de probabilidade (<abbr title="probability density function">PDF</abbr>) descreve a probabilidade de uma variável tomar um valor dado. 

Se uma variável aleatória X tem uma função distribuição F, a função densidade de probabilidade dada para X é dado por:

![PDF de uma distribuição F](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/ANOVA/imagens/PDF.png)

Onde B é uma função beta, para valores inteiros toma a forma:

![Função beta para inteiros](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/ANOVA/imagens/beta.png)

A função de distribuição cumulativa  (<abbr title="cumulative distribution function">CDF</abbr>) avalia a probabilidade de uma variável aleatória assumir um valor igual ou menor a X. Ela pode ser expressada uma a integral da função densidade de probabilidade.

## Passo 4: Cálculo

## Passo 5: Conclusão


ANOVA 1 fator: https://edisciplinas.usp.br/pluginfile.php/3260534/mod_resource/content/1/T%C3%B3pico_13.pdf
Passo a passo: http://sphweb.bumc.bu.edu/otlt/MPH-Modules/BS/BS704_HypothesisTesting-ANOVA/BS704_HypothesisTesting-Anova_print.html
