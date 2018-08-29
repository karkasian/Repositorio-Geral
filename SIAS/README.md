```
Em andamento
```

# SIAS 

SIAS � a abrevia��o para Simulador do IAS. O IAS foi previamente discutido em meu outro projeto [J](https://github.com/SapoGitHub/Repositorio-Geral/tree/master/J).

Apesar do nome, realizemos algumas adapta��es conforme pareceram necess�rias ou nosso conhecimento for limitado acerca dos detalhes de algum processo. O conte�do � totalmente baseado no livro de Arquitetura e Organiza��o de Computadores do  William Stallings, 8� edi��o.

Primeiramente, foi implementado um ciclo de busca baseado no seguinte fluxograma:

![Ciclo de Instru��o](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/SIAS/imagens/ciclo.png)

Ent�o come�amos a implementar as 21 instru��es originais:

![Instru��es do IAS](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/SIAS/imagens/instrucoes.png)

Sempre respeitando a estrutura do computador proposta em:

![Estrutura expandida](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/SIAS/imagens/estrutura.png)

Para a opera��o de adi��o, nos baseamos no seguinte diagrama:

![Diagrama em blocos do Hardware](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/SIAS/imagens/adicao.png)

Isso implica por exemplo, em 2 registradores e um FLAG (um registrador que indica o estado da CPU) dentro do m�dulo. Da mesma forma, para multiplica��o utilizamos o Algoritmo de Booth, o que exige 4 registradores.

![Algoritmo de Booth](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/SIAS/imagens/multiplicacao.png)

Essa abordagem foi utilizada pensando na did�tica de tais algoritmos.

E por fim, utilizamos a divis�o inspirado no seguinte fluxograma:
![Algoritmo da divis�o](imagens/div.png)

Mas com as seguinte adapta��es:
1. Guardamos os bits mais significativos de Q e M em um registrador QM.
2. Se o divisor ou dividendo for negativo, pegamos o complemento.
3. Realizamos toda a divis�o normalmente.
4. Atribuimos os sinais do quociente e resto de acordo com a seguinte regra:
	- sinal(resto)=sinal(dividendo)
	- sinal(quociente)=sinal(dividendo) x sinal(divisor)

## Observa��es

- Foi considerado que o registrador PC possui acesso um hardware pr�prio que lhe fornece capacidade de realizar uma soma bin�ria do tipo <code>+1</code> sem acessar a ULA.
- Da mesma forma dentro do complementador no m�dulo de adi��o e subtra��o, ele possui a mesma capacidade de realizar a soma <code>+1</code>.
- O circuito da ULA desloca o bin�rio em AC sem utilizar nenhum outro registrador.
- Os detalhes de como funciona a conex�o entre as estruturas foi ignorado.
- Estamos interpretando "Pr�xima instru��o est� no IBR?" como "O conte�do no IBR � diferente de 00000000000000000000?". Por isso quando o IBR passa os valores pro IR e MAR, estamos zerando ele.
	- Uma op��o � comparar se os valores atuais do IBR, IR e MAR s�o diferentes, nesse caso nossa condi��o poderia ser reescrita como "Os valores do IR e MAR s�o diferentes do IBR?".
	- Essa abordagem � mais pr�xima da utilizada no [IAS Simulator](http://www.ic.unicamp.br/~edson/disciplinas/mc404/2017-2s/abef/IAS-sim/)

## Melhorias poss�veis:
- Tratar o argumento das fun��es aritm�ticas dentro da fun��o, e n�o antes/depois.
- Tratar todas as instru��es como fun��es.
	- Muitos trechos podem ser reaproveitados.
- Adicionar fluxogramas para as outras fun��es.
- Melhorar a conex�o entre as imagens secund�rias.
- Desenhar novas imagens para as outras instru��es.
- Destacar quando algum circuito est� sendo usado na imagem principal.
- Fechar quando clicar no x.
	- Atualmente sai usando a tecla ESC.
- Detalhar o tipo de instru��o quando soma ou subtrai (ex.: ADD M(X) ou ADD |M(X)|).
- Explicitar como o componente para pegar a nega��o dentro da opera��o de adi��o, pode ser usado em outras opera��es e sua sa�da al�m de ir pro somador, pode ir para o AC.
- Da mesma forma que o item anterior, o componente que realiza o deslocamento para a multiplica��o, pode ser reutilizado para as fun��es LSH e RSH.
- A parte de divis�o foi implementado somente na interface gr�fica.