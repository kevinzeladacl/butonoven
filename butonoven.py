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
        { "pk":"1", "name": "edlothiad","difficulty":"30" },
        { "pk":"2", "name": "elcale","difficulty":"30" },
        { "pk":"3", "name": "nainiie","difficulty":"30" },
        { "pk":"4", "name": "mogentum","difficulty":"30" },
    ]






@bot.command()
async def ayuda(ctx):

    data = '''\n
    __** ### COMANDOS NOVEN ### **__
    
    Lista de comandos habilidatos:
    ```diff
+ !noven lista
+ !noven codex <nombre>
+ !noven germinar <nombre>
```

    '''

    await ctx.send(data)


@bot.command()
async def lista(ctx):
    list = ''
    count = 0
    for plant in plants:
        count = count + 1
        list += str(count)+ ".- " + plant['name'] + '\n'

    
    
    embed = discord.Embed(title="Lista de Plantas Habilitadas",description=list, color=0x7289da)

    await ctx.reply(embed=embed)
    





@bot.command()
async def codex(ctx,name):
    
    from random import randint
    value = randint(0, 100)
    
    plant = [i for i in plants if i['name'] == name][0]
    path = "img/" + plant['name'] + "/" + plant['name'] + ".png"

    await ctx.send(file=discord.File(path))

    

@bot.command()
async def germinar(ctx,name,target: discord.Member = None):
    
    from random import randint
    value = randint(0, 100)
    img_random = randint(1, 5)

    plant = [i for i in plants if i['name'] == name][0]
    path = "img/" + plant['name'] + "/" + str(img_random) + ".png"

    img_random

    if target == None:
        target = ctx.message.author.mention

    else:
        target = target.mention
        
    if value >= int(plant['difficulty']):
        # await ctx.reply(file=discord.File(path))
        embed = discord.Embed(title="Germinación exitosa",description="La planta " + plant['name'] + " ha sido germinada con éxito", color=0x7289da)
        embed.set_image(url='https://media.discordapp.net/attachments/917592950748360756/923631518478385233/3.png?width=1160&height=257')
        await ctx.reply(embed=embed)
        
        
    else:
        await ctx.reply(file=discord.File('img/f.jpg'))
        
        
        
bot.run(token)