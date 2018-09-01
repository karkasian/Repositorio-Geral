# GDD

A estrutura desse GDD é feita baseado no [GDD Maker](http://www.gddmaker.com/), e o jogo por sua vez, foi feito para uma [game jam](https://itch.io/jam/gmtk-2018) de 48h.

## Título e descrição

**Nome**:
Fantasminha CaArmado

**Descrição curta**:
Jogo desenvolvido para a game jam GM TK Game Jam 2018.

**Versão**: 1

## Visão geral

**Conceito**:
O jogo se baseia no desafio de produzir um jogo de um determinado gênero, sem uma das principais mecânicas deste tipo de gênero. Nesse caso foi escolhido um jogo de "tiro de plataforma", mas os tiros não acertam os inimigos. A ideia é que você é um fantasma armado que assombra uma instalação militar, mas não consegue interagir diretamente com os militares, portanto você precisa fazer uso do ambiente para eliminá-los. E essa interação por sua vez, é feita somente através de suas armas, pois você carrega os traumas de um veterano de guerra morto.

**Audiência**:
Jogadores casuais, e principalmente, participantes da Game Jam em questão.

**Resumo do fluxo**: A princípio, o jogo todo vai ter somente uma tela, um único ambiente. Quando você morre, esta tela e todos os elementos do jogo são simplesmente reiniciados.

**Aparência e clima**:
O visual todo do jogo é construído em cima de uma mistura de visual pixelado como terraria e Metal Slug.

## Gameplay

**Progressão**: Como o jogo todo é baseado em um único ambiente, não há uma progressão significativa que mereça destaque. A única medida que pode ser feita diretamente, é a quantidade de inimigos ainda vivos e proporção do mapa explorado.

**Missões**: A missão colocada é a de eliminar as forças militares que ocupam a base para reestabelecer a paz na região.

**Estrutura dos desafios**: Conforme o jogador avança, a ideia é que consiga eliminar os inimigos em que isso seja possível no momento, e colocar outros que não são possíveis no momento em uma situação mais favorável a você.

**Objetivos**: O objetivo do jogador, como previamente discutido é a de eliminar todos os indivíduos na base. Em poucas palavras: mate todos.

**Fluxo de jogo**: Para o jogador, temos apenas uma tela inicial, um único ambiente, onde conforme ele progride, vai conseguindo acesso a mais e mais partes do mapa para eliminar todos os militares.

## Mecânica

**Física**: A física na maior parte do tempo não existe. Não vai ser desenvolvido nenhum motor de física, na maior parte dos movimentos não vai seguir nenhuma física, apenas quando julgar necessário se baseará na física para realizar algum movimento de forma mais realista.

**Movimento no jogo**: O jogador se desloca pelo mapa do jogo através de seu personagem principal, isto é, controlando o seu avatar.


**Objetos**: Os únicos objetos que o jogador pode pegar são as armas, e elas são coletadas apenas passando por elas.

**Ações**: Toda a ação e a interação entre o jogador e qualquer outro componente no cenário é feito através das armas.

**Combate**: O combate é realizado de forma diferente dependendo de quem é o agressor:
- O jogador não consegue ferir nenhum inimigo diretamente, seus tiros e inclusive você mesmo simplesmente atravessam os inimigos.
- Porém alguns inimigos possuem um armamento especial capaz de o matar.

**Economia**: Não há.

**Fluxo de telas**: Há somente uma tela em que ocorre todo o jogo.

## Outros detalhes do jogo

**Opções**: Não há nenhum menu de opções.

**Replay e salvamento**: Não há opção de salvar, simplesmente quando o jogador morre, o jogo é reiniciado. Se o jogador fechar o jogo, ele também é reiniciado.

**Códigos e easter eggs**: Não há nada deste tipo a princípio.

## História, configuração e personagens

**História e narrativa**: Você controla um antigo veterano de guerra já morto. Ele trabalhava em uma base militar em uma região extremamente problemática, com um alto índice de violência e conflitos armados. A história conta que antes de morrer ele teve uma súbita iluminação, isto, é pode compreender algumas coisas que até então, não compreendia. Sua compreensão lhe fez entender o fato de que o maior causador de problemas na região, eram os próprios militares que ali estavam, toda a violência era uma reação de uma população que vivia temendo por suas vidas diante de uma força militar estrangeira hostil.

Então, nosso herói morto volta como um fantasma, e com a compreensão de que para conseguir sua liberdade, precisa cessar o ciclo de violência que ajudou a instaurar e trazer paz para a região, isto implica em eliminar a base militar em que ele próprio operou. Infelizmente, sua nova forma fantasmagórica lhe traz algumas dificuldades, como o fato de não conseguir interagir diretamente com as pessoas, mas para sua sorte sua arma consegue, e é através dela que deve cumprir sua missão.

É evidente que histórias similares rondam o mundo, então o exército possui projetos experimentais voltados a conter ameaças vindas da pós-morte, o que lhe traz alguns desafios extras, mas certamente, nada que um veterano de guerra cheio de traumas que se comunica através das armas de fogo não consiga resolver.

**Mundo**: Todo o mundo jogável é uma única base militar. Isso inclui as dependências internas e dependências externas.

**Áreas**: O mapa é dividido em 3 áreas principais:
1. Prédio da baixa patente: Este é o prédio onde ficam os soldados de patente mais baixas, o pessoal menos importante e provavelmente o menos preparado também. Ele possui ainda 2 sub-áreas, que são respectivamente o primeiro andar e o térreo:
  1.  Dormitório: Onde ficam as camas, banheiro e comida, suprimentos básicos para a sobrevivência das patentes baixas que ali moram. Costumava ser sua antiga casa, ou o mais próximo disto.
  2. Andar principal: Onde os soldados se reúnem, discutem as táticas e guardam os armamentos e o equipamento relacionado a guerra.
2. Pátio: A esquerda do prédio da baixa patente, temos o pátio. Aqui ficam principalmente os veículos utilizado pelo exército e também o é o local de exercícios no exterior, por exemplo exercícios físicos ou tiro ao alvo.
3. Prédio da alta patente: A direita do prédio da baixa patente, aqui é onde ficam os homens mais importantes da região, isto é, ao menos quando se encontram na base, já que dificilmente fazem desta base sua moradia. De forma semelhante ao outro prédio, possui duas áreas, sendo o térreo e o primeiro andar respectivamente:
  1. Andar tático: Onde os homens importantes se reúnem para tomar suas decisões importantes que vão colocar a vida dos outros (e nunca as suas) em perigo.
  2. Sala de segurança: Por algum motivo inexplicável construído no primeiro andar e não debaixo da terra, este é uma espécie de bunker. O local onde os homens de mais alta patente, os mais valorosos homens do exército correm para se esconder quando acham que suas vidam estão em risco. Ou simplesmente não querem ser incomodados.

**Personagens**:

## Fases

**Fases e mapa**: O jogo possui um só fase, e consequentemente um só mapa

1366 x 768

**Tutorial**: Não há;

## Interface

**Sistema visual**:

**Sistema de Controle**:
Como o jogo tem uma única tela, onde o jogador controla o personagem principal, todo o sistema de controle do jogo, é o sistema de controle deste personagem, e ele é controlado da seguinte forma:
- O movimento vai ser feito pelo teclado através das teclas direcionais:
  - Para os lados de desloca na direção correspondente;
  - Para baixo se abaixa;
  - Para cima pula.
- O tiro é disparado utilizando espaço.
- As teclas numéricas serão utilizadas para alternar entre as armas.
- Esc pausa o jogo.

**Audio**: A princípio, não se aplica.

**Sistema de ajuda**: Não possui.

## Inteligência artificial

**Inimigos**:

**Personagens neutros**: Não possui.

**IA de suporte**:

## Aspectos Técnicos

**Hardware Alvo**: Qualquer computador moderno é capaz de executar.

**Desenvolvimento**: O desenvolvimento está sendo feito no Windows 10 x64 com o python 3.6 e os seguintes módulos extras instalados:
- pygame 1.9.4
- py2exe 0.9.2.2

**Requerimentos de rede**: Não há necessidade conexão com a internet.

## Game Art

**Estilo de arte**:
