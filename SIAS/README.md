```
Em andamento
```

# SIAS 

SIAS � a abrevia��o para Simulador do IAS. O IAS foi previamente discutido em meu outro projeto [J](https://github.com/SapoGitHub/Repositorio-Geral/tree/master/J).

Apesar do nome, realizemos algumas adapta��es conforme pareceram necess�rias, mas o conte�do � totalmente baseado no livro de Arquitetura e Organiza��o de Computadores do  William Stallings, 8� edi��o.

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

Outras observa��es:
- Foi considerado que o registrador PC possui acesso um hardware pr�prio que lhe fornece capacidade de realizar uma soma bin�ria do tipo <code>+1</code> sem acessar a ULA.
- Da mesma forma dentro do complementador no m�dulo de adi��o e subtra��o, ele possui a mesma capacidade de realizar a soma <code>+1</code>.
- O circuito da ULA desloca o bin�rio em AC sem utilizar nenhum outro registrador.
- Os detalhes de como funciona a conex�o entre as estruturas foi ignorado.

Melhorias:
- Tratar o argumento das fun��es aritm�ticas dentro da fun��o, e n�o antes/depois.
- Tratar todas as instru��es como fun��es.
	- Muitos trechos podem ser reaproveitados.
- Adicionar fluxogramas para as outras fun��es.