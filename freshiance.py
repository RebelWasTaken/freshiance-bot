import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='Freshiance'))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if message.content.startswith('/flip'):
        randomlist = ['heads','tails']
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('/flip'):
        randomlist = ['heads','tails']
        await client.send_message(message.channel,(random.choice(randomlist)))
client.run('NDkxODYwNzU1MjgxMzQ2NTYy.DoOA3A.YO3JyJQ00Ags7Dk0MFOIkJr1zUg')

client.login(process.env.BOT_TOKEN):
