# Perceptron

## Porta NAND

Uma porta lógica é uma porta que para uma par de entradas binárias (0 ou 1) retorna sempre 1 exceto se o par for (1,1), ou seja, possui a seguinte tabela verdade:

Entrada A	Entrada B	Saída
0		0		1
0		1		1
1		0		1
1		1		0

Esse é o conjunto de dados que vamos utilizar para treinar nossa rede.

A função de ativação de um perceptron é a soma do produto do somatório entre as entradas e seus respectivos pesos, e seu limiar. Isto é, por exemplo,para duas entradas: <code>y=e<sub>1</sub>*p<sub>1</sub>+e<sub>2</sub>*p<sub>2</sub>+l</code>
