# Gestor Pokémon

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
- Legendary: Verdadeiro se o pokémon é lendário ou mítico, e falso caso contrário.

E um último ponto a destacar, é que diferentemente de nosso conjunto de dados de referência hospedado no Kaggle, vamos utilizar tab e quebra de linhas para separar as linhas e colunas. Ex:
<pre>
Coluna 1	Coluna 2	Coluna 3
Linha 1		Null		True
Linha 2		Valor		False
</pre>

Para pegarmos os dados de nossa fonte, vamos utilizar o [Selenium](http://selenium-python.readthedocs.io/installation.html)  novamente. Vale lembrar que já utilizamos o mesmo na primeira vez em nosso projeto [WFAPI](https://github.com/SapoGitHub/Repositorio-Geral/tree/master/WFAPI).