# SIAS 

SIAS � a abrevia��o para Simulador do IAS. O IAS foi previamente discutido em meu outro projeto [J](https://github.com/SapoGitHub/Repositorio-Geral/tree/master/J).

Apesar do nome, realizemos algumas adapta��es conforme pareceram necess�rias, mas o conte�do � totalmente baseado no livro de Arquitetura e Organiza��o de Computadores do  William Stallings, 8� edi��o.

Primeiramente, foi implementado um ciclo de busca baseado no seguinte fluxograma:

![Ciclo de Instru��o](/imagens/ciclo.png)

Ent�o come�amos a implementar as 21 instru��es originais:

![Instru��es do IAS](/imagens/instrucoes.png)

Sempre respeitando a estrutura do computador proposta em:

![Estrutura expandida](/imagens/estrutura.png)

Para a opera��o de adi��o, nos baseamos no seguinte diagrama:

[!Diagrama em blocos do Hardware](/imagens/adicao.png)

Isso implica por exemplo, em 2 registradores e um FLAG (um registrador que indica o estado da CPU) dentro do m�dulo. Da mesma forma, para multiplica��o utilizamos o Algoritmo de Booth, o que exige 4 registradores.

[!Algoritmo de Booth](/imagens/multiplicacao)

Essa abordagem foi utilizada pensando na did�tica de tais algoritmos.

Outras observa��es:
- Foi considerado que o registrador PC possui acesso um hardware pr�prio que lhe fornece capacidade de realizar uma soma bin�ria do tipo <code>+1</code> sem acessar a ULA.
- Da mesma forma dentro do complementador no m�dulo de adi��o e subtra��o, ele possui a mesma capacidade de realizar a soma <code>+1</code>.