from re import DEBUG
import requests
import time
import os
import discord #importamos para conectarnos con el bot
from discord.ext import commands #importamos los comandos
import datetime



from config import token



bot = commands.Bot(command_prefix='!noven ', description="This is a KZ Team bot")

plants = [
        { "pk":"1", "number":":one:", "name": "elcale","difficulty":"50" },
        { "pk":"2", "number":":two:", "name": "mogentum","difficulty":"50" },
        { "pk":"3", "number":":three:", "name": "nainiie","difficulty":"50" },
        { "pk":"4", "number":":four:", "name": "edlothiad","difficulty":"50" },
    ]






@bot.command()
async def ayuda(ctx):

    data = '''\n
    
    !noven lista
    !noven codex <nombre>
    !noven germinar <nombre>


    '''

    embed = discord.Embed(title="Lista de comandos habilidatos :butoGG:",description=data, color=0x7289da)

    await ctx.reply(embed=embed)


@bot.command()
async def lista(ctx):
    list = ''
    count = 0
    for plant in plants:
        count = count + 1
        list += plant["number"] + " "+ plant['name'] + '\n'

    
    list += '\n' + 'Debes copiar y pegar el nombre de la planta tal cual esta en la lista.'
    embed = discord.Embed(title="Lista de Plantas Habilitadas :butoVR:",description=list, color=0x7289da)

    await ctx.reply(embed=embed)
    





@bot.command()

async def codex(ctx,name):
    
    from random import randint
    value = randint(0, 100)
    
    plant = [i for i in plants if i['name'] == name][0]
    path = "https://raw.githubusercontent.com/kevinzeladacl/butonoven/master/img/" + plant['name'] + "/" + plant['name'] + ".png"

    embed = discord.Embed(title="Busquéda Éxitosa :butoSUB:",description="Tenemos la siguiente información de esta planta :butoElfos:", color=0x00dd19)
    embed.set_image(url=path)
    await ctx.reply(embed=embed)

    

@bot.command()
async def germinar(ctx,name,target: discord.Member = None):
    
    from random import randint
    value = randint(0, 100)
    img_random = randint(1, 5)

    plant = [i for i in plants if i['name'] == name][0]
    path = "https://raw.githubusercontent.com/kevinzeladacl/butonoven/master/img/" + plant['name'] + "/" + str(img_random) + ".png"

    img_random

    if target == None:
        target = ctx.message.author.mention

    else:
        target = target.mention
        
    if value >= int(plant['difficulty']):
        # await ctx.reply(file=discord.File(path))
        embed = discord.Embed(title="Germinación exitosa :butoElfos:",description="La planta ha sido germinada con éxito :butoLove:", color=0x00dd19)
        embed.set_image(url=path)
        await ctx.reply(embed=embed)
        
        
    else:
        random_frase = randint(1, 10)
        frases = [
        "No te preocupes, seguramente no era el momento de que germinara, ¡vuelve a intentarlo!",
        "Al parecer, algo a salido mal, ¡pero que no panda el cunico!, no siempre las cosas resultan en el primer intento",
        "Descuida, lo bueno siempre tarda en llegar, ¡no pierdas la esperanza!",
        "¡No desistas!, ya saldrá, ten confianza",
        "Hasta los deportistas profesionales de elite tienen fallos, ¡no te rindas, tu puedes!",
        "Probablemente, este no era el mejor momento para que floreciera, ¡Animo!, todo debe suceder a su debido tiempo",
        "Respira hondo, profundo y vuelve a intentarlo, la variable del error siempre estará en nuestras vidas, no te desanimes",
        "No ha florecido, pero no te pongas triste, ¡siempre puedes volver a internarlo!",
        "Las flores son un mundo, a veces no germinan porque simplemente no quieren (o les da pereza), pero no pierdas la fe.",
        " Oh no, no ha germinado, sin embargo, no te sientas mal, ¡a todos nos puede pasar, animo!",
        ]

        embed = discord.Embed(title="Germinación Fallida :butoCry:",description=frases[random_frase], color=0xff162f)
        embed.set_image(url='https://raw.githubusercontent.com/kevinzeladacl/butonoven/master/img/f.jpg')
        await ctx.reply(embed=embed)
        
        
        
bot.run(token)