# Gestor Pokémon

## Conjunto de dados

Para utilizarmos o Tableau, precisamos inicialmente de uma fonte de dados. Pesquisando na internet, encontramos um no Kaggle chamado [Pokemon with stats](https://www.kaggle.com/abcsds/pokemon). Porém este conjunto de dados está desatualizado, por exemplo, não contém a última geração de Pokémons, então decidimos montar nosso próprio conjunto.

Para isso vamos utilizar como fonte a Pokedéx do [Pokémon Database](https://pokemondb.net/pokedex/all). Pensando em manter um padrão para quem utilizava a disponibilizada no Kaggle, precisamos de algumas informações extras que não constam em nossa fonte principal:
- Gerações;
- Lendários (e míticos);

Para resolver o primeiro problema podemos consultar os [pokemóns lendários](https://bulbapedia.bulbagarden.net/wiki/Legendary_Pok%C3%A9mon) na página do Bulbapedia e criarmos uma lista com os mesmos:
<pre>
Articuno, Zapdos, Moltres, Mewtwo, Mew,
Raikou, Entei, Suicune, Lugia, Ho-Oh, Celebi,
Regirock, Regice, Registeel, Latias, Latios,
Groudon, Rayquaza, Jirachi, Deoxys,
Uxie, Mesprit, Azelf, Dialga, Palkia, Heatran, Regigigas,
Cresselia, Phione, Manaphy, Darkrai, Shaymin, Arceus,
Victini, Cobalion, Terrakion, Virizion, Tornadus, Thundurus,
Reshiram, Zekrom, Landorus, Kyurem, Keldeo, Meloetta, Genesect,
Xerneas, Yveltal, Zygarde, Diancie, Hoopa, Volcanion,
Type: Null, Silvally, Tapu Koko, Tapu Lele, Tapu Bulu, Tapu Fini, Cosmog,
Cosmoem, Solgaleo, Lunala, Necrozma, Magearna, Marshadow, Zeraora
</pre>
Quanto ao segundo problema, podemos consultar também no Bulbapedia a lista de [pokémons por geração](https://bulbapedia.bulbagarden.net/wiki/List_of_Pok%C3%A9mon_by_National_Pok%C3%A9dex_number), e então vamos guardar a identificação do primeiro pokémon de cada geração:
<pre>
1,
152,
252,
387,
494,
650,
722
</pre>
E como ultima característica importante ainda para mantermos o padrão, manteremos os mesmos títulos das columas:
<pre>
#   Name    Type 1    Type 2    Total   HP    Attack    Defense   Sp. Atk   Sp. Def   Speed   Generation    Legendary   
</pre>

Onde cada coluna indica:
- #: ID de cada pokémon;
- Name: Nome de cada pokémon;
- Type 1: Cada pokémon tem um tipo que determina sua fraqueza/resistência a ataques;
- Type 2: Alguns pokémons possuem dois tipos;
- Total: Soma de todos os próximos atributos, um guia geral de quão forte o pokémon é;
- HP: Abreviatura de _hit points_, é a vida do pokémon, determina quanto dano aguenta;
- Attack: o modificador base para ataques normais;
- Defense: a resistênsia a danos base contra ataques normais;
- Sp Atk: Do inglês _special attack_, é o modificador base para ataques especiais;
- Sp Def: Análogo ao caso anterior, é a resistência base contra ataques especiais;
- Speed: Determina que pokémon ataca primeiro em cada rodada;
- Generation: A geração do pokémon;
- Legendary: Verdadeiro se o pokémon é lendário ou mítico, e falso caso contrário.

E um último ponto a destacar, é que diferentemente de nosso conjunto de dados de referência hospedado no Kaggle, vamos utilizar tab e quebra de linhas para separar as linhas e colunas. Ex:
<pre>
Coluna 1	Coluna 2	Coluna 3
Linha 1		Null		True
Linha 2		Valor		False
</pre>

Para pegarmos os dados de nossa fonte, vamos utilizar o [Selenium](http://selenium-python.readthedocs.io/installation.html)  novamente. Vale lembrar que já utilizamos o mesmo na primeira vez em nosso projeto [WFAPI](https://github.com/SapoGitHub/Repositorio-Geral/tree/master/WFAPI).

Após gerarmos nosso arquivo fonte, publicamos no Kaggle: [Pokémon: estatísticas básicas](https://www.kaggle.com/sapokaggle/pokmon-estatsticas-bsicas)

## Tableau

Uma vez com nosso conjunto de dados gerados, podemos utilizar o Tableau para analisarmos os dados em questão. Também seguindo a proposta do compartilhamento na nuvem, publicamos nosso resultado no Tableau Public, com o nome [Análise Pokémon](https://public.tableau.com/profile/jhordan.silveira.de.borba#!/vizhome/AnalisePokmon/Final).

### Página 1

[página 1]()
Na primeira página de nossa história final, escolhemos abordar os atributos individuais dos pokémons. Os gráficos individualmente relacionam:
- Ataque e defesa;
- Ataque especial e defesa especial;
- Vida e velocidade.

Mas todos eles compartilham características em comuns:
- As cores identificam os tipos de pokémons;
- Podemos filtrar por:
  - Nome;
  - Se é lendário;
  - Tipo 1;
  - Geração.
 
 Nela podemos inferir visualmente algumas coisas como:
 - A maior parte dos pokémons possuem mais velocidade que vida;
 - A maior parte dos pokémons possuem Sp. Atk entre 25 e 150, e Sp. Def entre 25 e 100;
 - A maior parte dos pokémons possuem 100 ou menos de defesa;
 - O pokémon com o ataque mais alto que também possui uma defesa equilibrada é o Groudon em sua forma Primal, com 180 e 160 respectivamente.

### Página 2

[página 2]()

Agora decidimos dar uma olhada em informações coletivas sobre os pokémons, para isso mantivemos os mesmos filtros da página anterior e temos os gráficos relacionado:
- Quantidade de pokémon de cada tipo;
- Quantidade de pokémon de cada geração;
- Quantidade de vezes que temos cada combinação de tipo 1 com tipo 2 possível.

Daqui podemos tirar mais algumas informações, por exemplo:
- Geração 1 foi a maior geração até o momento;
- A maior parte dos pokémons não possui um segundo tipo;
- Flying é o tipo 1 menos popular, enquanto normal e água são os mais populares.
  - Esse gráfico é melhor aproveitado de forma interativa para visualizarmos quais são os pokémons de cada tipo, e/ou geração usando os filtros.

### Página 3

[página 3]()

Para a página 3, estamos preocupados em abordar os pontos totais de cada pokémon. Agora utilizamos como filtros unicamente o tipo 1 e a geração. Os gráficos nos mostram basicamente os pontos totais por:
- Pokémon;
- Geração;
- Tipo 1.

Podemos ver algumas coisas como:
- O máximo total de um pokémon atualmente é 780. 
  - 3 pokémons em sua forma mega atingem essa pontuação: Mewtwo X, Mewtwo Y e Rayquaza;
- Como era de esperar, por possuir a maior quantidade de pokémons, é a geração 1 que possui a maior quantidade total acumulada;
  - Podemos pensar em visualizar a média total por pokémon em cada geração, para compararmos as gerações.
- Análogo ao item anterior, são os tipos água e normal que acumulam a maior quantidade de total.

### Página 4

[página 4]()

Baseado nas sugestões anteriores, construímos uma página bônus, também com os filtros de geração e tipo, ela apresenta os gráficos com:
- A média do total por pokémon de cada geração;
- A média do total por pokémon de cada tipo;

Podemos perceber que:
- Não há diferença significativa entre as gerações.
  - Todo caso, a geração 7 tem uma média levemente maior.
 - O tipo dragão é o tipo que apresenta as maiores médias de total por Pokémon.
 
 ### Página 5
 
 [página 5]()
 
 Como outro bônus ainda, decidimos investigar um pouco a questão levantada pelo conjunto de dados original no Kaggle. Reunimos em uma págiba, basicamente todas as combinações possíveis entre 2 atributos. Como podemos ver, não tem nenhum par de atributos que sozinhos consigam separar os pokémons entre os diversos tipos principais.
 
 Sendo assim, não é possível inferir o tipo do pokémon olhando apenas um par de seus atributos, seja qual for.
