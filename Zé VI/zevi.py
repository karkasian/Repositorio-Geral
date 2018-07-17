##ZÉ VI
##Desenvolvido por:     Jhordan Silveira de Borba
##E-mail:               jhordandecacapava@gmail.com
##Website:              https://sapogithub.github.io
##Mais informações:     https://github.com/SapoGitHub/Repositorio-Geral/wiki/Zé-VI
##2018

import random                       #Biblioteca para comandos aleatorios
import discord                      #Biblioteca para trabalhar com o discord
from discord.ext import commands

#Definimos nosso bot
bot = commands.Bot(command_prefix='!', description='Vamo esculachar!!!')

#Vamos printar quando conectar ao discord
@bot.event
async def on_ready():
    print('Logado como:')
    print(bot.user.name)


#Comandos
@bot.command(name='bola8',
                description="Faça uma pergunta que possa ser respondida com sim ou não.",
                brief="Respostas sim/não.",
                aliases=['bola_oito', 'bolaoito'],
                pass_context=True)
async def ball(context):
    respostas=['sim','não']
    await bot.say(context.message.author.mention+': a resposta para sua pergunta é ... '+random.choice(respostas)+'!')


#Criamos uma categoria de comandos
class Informativo:
    """Comandos que dão informações sobre o bot"""
    @commands.command(brief="Informações sobre o bot.")
    async def infor(self):
        embed = discord.Embed(title="Nome", description="Zé VI", color=0xeee657)
        embed.add_field (name="Descrição", value="Vamo esculachar!!")
        await bot.say(embed=embed)

#Adicionamos os comandos da categora informativo
bot.add_cog(Informativo())

#Vamos rodar o bot
bot.run('')
