```
Em andamento
```

# SIAS 

SIAS é a abreviação para Simulador do IAS. O IAS foi previamente discutido em meu outro projeto [J](https://github.com/SapoGitHub/Repositorio-Geral/tree/master/J).

Apesar do nome, realizemos algumas adaptações conforme pareceram necessárias, mas o conteúdo é totalmente baseado no livro de Arquitetura e Organização de Computadores do  William Stallings, 8ª edição.

Primeiramente, foi implementado um ciclo de busca baseado no seguinte fluxograma:

![Ciclo de Instrução](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/SIAS/imagens/ciclo.png)

Então começamos a implementar as 21 instruções originais:

![Instruções do IAS](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/SIAS/imagens/instrucoes.png)

Sempre respeitando a estrutura do computador proposta em:

![Estrutura expandida](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/SIAS/imagens/estrutura.png)

Para a operação de adição, nos baseamos no seguinte diagrama:

![Diagrama em blocos do Hardware](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/SIAS/imagens/adicao.png)

Isso implica por exemplo, em 2 registradores e um FLAG (um registrador que indica o estado da CPU) dentro do módulo. Da mesma forma, para multiplicação utilizamos o Algoritmo de Booth, o que exige 4 registradores.

![Algoritmo de Booth](https://github.com/SapoGitHub/Repositorio-Geral/blob/master/SIAS/imagens/multiplicacao.png)

Essa abordagem foi utilizada pensando na didática de tais algoritmos.

Outras observações:
- Foi considerado que o registrador PC possui acesso um hardware próprio que lhe fornece capacidade de realizar uma soma binária do tipo <code>+1</code> sem acessar a ULA.
- Da mesma forma dentro do complementador no módulo de adição e subtração, ele possui a mesma capacidade de realizar a soma <code>+1</code>.
- O circuito da ULA desloca o binário em AC sem utilizar nenhum outro registrador.
- Os detalhes de como funciona a conexão entre as estruturas foi ignorado.

Melhorias:
- Tratar o argumento das funções aritméticas dentro da função, e não antes/depois.
- Tratar todas as instruções como funções.
	- Muitos trechos podem ser reaproveitados.
- Adicionar fluxogramas para as outras funções.