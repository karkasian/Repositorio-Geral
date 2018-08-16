##GESTOR POKÉMON
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Gestor-Pok%C3%A9mon
##2018

from selenium import webdriver                          #Biblioteca de automatização de tarefas no navegador

#Vamos criar nossa lista de pokémons lendários
lend=('Articuno','Zapdos','Moltres','Mewtwo','Mew',
'Raikou','Entei','Suicune','Lugia','Ho-Oh','Celebi',
'Regirock','Regice','Registeel','Latias','Latios',
'Groudon','Rayquaza','Jirachi','Deoxys',
'Uxie','Mesprit','Azelf','Dialga','Palkia','Heatran','Regigigas',
'Cresselia','Phione','Manaphy','Darkrai','Shaymin','Arceus',
'Victini','Cobalion','Terrakion','Virizion','Tornadus','Thundurus',
'Reshiram','Zekrom','Landorus','Kyurem','Keldeo','Meloetta','Genesect',
'Xerneas','Yveltal','Zygarde','Diancie','Hoopa','Volcanion',
'Type:Null','Silvally','TapuKoko','TapuLele','TapuBulu','TapuFini','Cosmog',
'Cosmoem','Solgaleo','Lunala','Necrozma','Magearna','Marshadow','Zeraora')

#E a lista com o primeiro pokémon de cada geração
ger=[1,
152,
252,
387,
494,
650,
722]

# E uma lista com todos os tipos de pokémons:
tipos=('NORMAL','FIRE','WATER','ELECTRIC','GRASS','ICE','FIGHTING','POISON','GROUND',
       'FLYING','PSYCHIC','BUG','ROCK','GHOST','DRAGON','DARK','STEEL','FAIRY')
       

#ETAPA 1: Vamos obter todos pokémons da página---------------------------------------------------------------------------------------------
driver = webdriver.Chrome()                     #Conectamos no Chrome
driver.get("https://pokemondb.net/pokedex/all") #Abrimos a pagina do WhatsApp Web
print('Página carregada.')
c=1                                             #contador
pks=[]                                          #Vamos guardar nossas strings com os dados sobre os pokémons
g=0                                             #Nossa geração atual
#Vamos percorrer todos pokémons
while(True):

    try:                                        #Vamos descobrir se existe o atual pokémon
       driver.find_element_by_xpath('//*[@id="pokedex"]/tbody/tr['+str(c)+']')
    except:                                     #Se não existe, saimos do while
        break
    
    ide=int(driver.find_element_by_xpath('//*[@id="pokedex"]/tbody/tr['+str(c)+']'+'/td[1]').text)   #Vamos pegar o id
    
    n=driver.find_element_by_xpath('//*[@id="pokedex"]/tbody/tr['+str(c)+']'+'/td[2]').text          #Vamos pegar o nome
    ns=n.split('\n')            #dividimos nas quebras de linha
    nome=ns[0]                  #Guardamos o primeiro nome
    if (len(ns)>1):             #Se temos duas partes
        nome=nome+': '+ns[1]    #Guardamos o segundo

    t=driver.find_element_by_xpath('//*[@id="pokedex"]/tbody/tr['+str(c)+']'+'/td[3]').text          #Vamos pegar o tipo
    ts=t.split('\n')    #dividimos nas quebras de linha
    tipo1=ts[0]         #Guardamos o primeiro tipo
    if (len(ts)>1):     #Se temos duas partes
        tipo2=ts[1]     #Guardamos o segundo tipo
    else:
        tipo2='Null'    #Ou então é nulo

    total=int(driver.find_element_by_xpath('//*[@id="pokedex"]/tbody/tr['+str(c)+']'+'/td[4]').text)    #Total
    hp=int(driver.find_element_by_xpath('//*[@id="pokedex"]/tbody/tr['+str(c)+']'+'/td[5]').text)       #HP
    attack=int(driver.find_element_by_xpath('//*[@id="pokedex"]/tbody/tr['+str(c)+']'+'/td[6]').text)   #Attack
    defense=int(driver.find_element_by_xpath('//*[@id="pokedex"]/tbody/tr['+str(c)+']'+'/td[7]').text)  #Defense
    spatk=int(driver.find_element_by_xpath('//*[@id="pokedex"]/tbody/tr['+str(c)+']'+'/td[8]').text)    #Sp. Atk
    spdef=int(driver.find_element_by_xpath('//*[@id="pokedex"]/tbody/tr['+str(c)+']'+'/td[9]').text)    #Sp. Def
    speed=int(driver.find_element_by_xpath('//*[@id="pokedex"]/tbody/tr['+str(c)+']'+'/td[6]').text)    #Speed

    if ide in ger:          #Se é o primeiro pokémon de uma geração
        g=g+1               #Avançamos nossa geração
        ger.remove(ide)     #Removemos de nossa lista

    if ns[0] in lend:       #Se nosso pokémon esta na lista dos lendarios
        l=True              #É lendario
    else:
        l=False

    tab='	'           #O tab
    #Vamos montar a linha
    linha=str(ide)+tab+nome+tab+tipo1+tab+tipo2+tab+str(total)+tab+str(hp)+tab+str(attack)+tab+str(defense)+tab+str(spatk)+tab+str(spdef)+tab+str(speed)+tab+str(g)+tab+str(l)+'\n'
    pks.append(linha)       #Vamos salvar a linha
    print(c)
    c=c+1                                   #Avançamos o elemento

print('Dados capturados.')
#Agora podemos guardar as linhas no arquivo
arquivo = open('pokemon.csv', mode='w', encoding="utf-8")
cabecalho='#'+tab+'Name'+tab+'Type 1'+tab+'Type 2'+tab+'Total'+tab+'HP'+tab+'Attack'+tab+'Defense'+tab+'Sp. Atk'+tab+'Sp. Def'+tab+'Speed'+tab+'Generation'+tab+'Legendary\n'
arquivo.write(cabecalho)
arquivo.writelines(pks)
arquivo.close()
print('Conjunto de dados criados.')
