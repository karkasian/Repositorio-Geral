##ZÉ VI
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Zé-VI
##2018

import random                       #Biblioteca para comandos aleatorios
import discord                      #Biblioteca para trabalhar com o discord
from discord.ext import commands
import tweepy                       #Biblioteca de interação com o Twitter

#CREDENCIAIS----------------------------------------------------------------------------------------------------------------

token=                  ''       #Token
consumer_key =          ''                                         #Consumer Key (API Key)
consumer_secret=        ''                #Consumer Secret (API Secret)
access_token=           ''                #Access Token
access_token_secret=    ''                     #Access Token Secret

#COFIGURAÇÃO DISCORD---------------------------------------------------------------------------------------------------------
help_attrs = dict(hidden=True)
bot = commands.Bot(command_prefix='!', description='Vamo esculachar!!!', help_attrs=help_attrs)

#Vamos printar quando conectar ao discord
@bot.event
async def on_ready():
    print('Logado como:')
    print(bot.user.name)

#CONEXÃO TWITTER-------------------------------------------------------------------------------------------------------------
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

#COMANDOS--------------------------------------------------------------------------------------------------------------------
#Comando da Bola 8
@bot.command(name='bola8', #Como pode ser chamado a funçaõ no discord
                description="Faça uma pergunta que possa ser respondida com sim ou não.", #Descrição que aparece no !help bola8
                brief="Respostas sim/não.", #Descrição que aparece no !help
                aliases=['bola_oito', 'bolaoito'], #Outras formas de chamar a mesma função
                pass_context=True)  #Se vai passar o contexto
async def ball(context):
    respostas=['sim','não']
    await bot.say(context.message.author.mention+': a resposta para sua pergunta é ... '+random.choice(respostas)+'!')

#Comando do Twitter
@bot.command(name='Twite',
                description="Twite qualquer coisa.",
                brief="Twite qualquer coisa.",
                aliases=['twite','tw'],
                pass_context=False)
async def tweet(*frase):
    tweet=''                            #Variável pra guardar a frase que vai twitar
    for palavra in frase:                      
        tweet=tweet+' '+x
    api.update_status(status=tweet)     #Twitamos a frase
    await bot.say('Twitado!')

#Criamos uma categoria de comandos
class Informativo:
    """Comandos que dão informações."""

    #Comando com informações sobre o bot
    @commands.command(brief="Sobre o bot.")
    async def info(self):
        embed = discord.Embed(title="Nome", description="Zé VI", color=0xeee657)
        embed.add_field (name="Descrição", value="Vamo esculachar!!")
        embed.add_field (name="Gmail e Twitter",value='zeromildobot@gmail.com:zeromildao')
        await bot.say(embed=embed)

#Adicionamos os comandos da categora informativo
bot.add_cog(Informativo())

#RODAR O BOT----------------------------------------------------------------------------------------------------------------
bot.run(token)

#ZONA DE TESTES FORA DO DISCORD---------------------------------------------------------------------------------------------
api.update_status(status=tweet)
