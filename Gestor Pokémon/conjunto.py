##GESTOR POKÉMON
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Gestor-Pok%C3%A9mon
##2018

from selenium import webdriver                          #Biblioteca de automatização de tarefas no navegador

#Vamos criar nossa lista de pokémons lendários
lend=('Articuno',' Zapdos',' Moltres',' Mewtwo',' Mew',
'Raikou',' Entei',' Suicune',' Lugia',' Ho-Oh',' Celebi',
'Regirock',' Regice',' Registeel',' Latias',' Latios',
'Groudon',' Rayquaza',' Jirachi',' Deoxys',
'Uxie',' Mesprit',' Azelf',' Dialga',' Palkia',' Heatran',' Regigigas',
'Cresselia',' Phione',' Manaphy',' Darkrai',' Shaymin',' Arceus',
'Victini',' Cobalion',' Terrakion',' Virizion',' Tornadus',' Thundurus',
'Reshiram',' Zekrom',' Landorus',' Kyurem',' Keldeo',' Meloetta',' Genesect',
'Xerneas',' Yveltal',' Zygarde',' Diancie',' Hoopa',' Volcanion',
'Type: Null',' Silvally',' Tapu Koko',' Tapu Lele',' Tapu Bulu',' Tapu Fini',' Cosmog',
'Cosmoem',' Solgaleo',' Lunala',' Necrozma',' Magearna',' Marshadow',' Zeraora')

#E a lista com o primeiro pokémon de cada geração
ger=('1',
'152',
'252',
'387',
'494',
'650',
'722')

g=0                                             #Nossa geração atual
driver = webdriver.Chrome()                     #Conectamos no Chrome
driver.get("https://pokemondb.net/pokedex/all") #Abrimos a pagina do WhatsApp Web
print('!')
ide=1                                           #Nosso pokémon inicial
continua=True                                   #Variável de controle para nosso while

#Vamos percorrer todos pokémons
while(continua):
    
    if (ide in ger):    #Se estamos no primeiro pokémon de uma geração
        ger=ger+1       #Avançamos a geração
    
    ide=ide+1   #Avançamos o ID
    break

#Caminho para cada pokémon
#//*[@id="pokedex"]/tbody/tr[1]
