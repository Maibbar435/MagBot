import discord
from discord.ext import commands
from random import randint
import config

BOT = commands.Bot(command_prefix='#')

@BOT.event
async def on_ready():
    print(config.NAME + ' Online')

@BOT.command(name = 'join', pass_context = True)
async def join(ctx):
    channel = ctx.author.voice.channel
    if channel is not None:
        await channel.connect()
    else:
        await ctx.send("You don't connected to any chat")

BOT.run(config.TOKEN)
