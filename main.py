import discord
import os

from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()

client = commands.Bot(command_prefix='$', help_command=None)


# GIFs commands
@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.command()
async def drunk(ctx):
    await ctx.send('https://tenor.com/view/drunk-gif-22301749')


@client.command()
async def slap(ctx):
    await ctx.send('https://tenor.com/view/slapping-mad-rage-anime-backhand-gif-16422437')


@client.command()
async def wakeup(ctx):
    await ctx.send('https://tenor.com/view/sleep-wake-up-wake-up-in-night-ren-and-stimpy-gif-24104879')


@client.command()
async def depressed(ctx):
    await ctx.send('https://tenor.com/view/sad-raining-gif-17973911')


@client.command()
async def boom(ctx):
    await ctx.send('https://tenor.com/view/penis-firework-explosion-boom-gif-4932263')


@client.command()
async def pray(ctx):
    await ctx.send('https://tenor.com/view/halal-pray-praying-cat-praying-cat-gif-19802221')


@client.command()
async def dance(ctx):
    await ctx.send('https://media.discordapp.net/attachments/741858155075469393/894749228222541885/koala-fab-02.gif')


@client.command()
async def vape(ctx):
    await ctx.send(
        'https://media.discordapp.net/attachments/753289564344549519/908183938940436490/received_583865662581686.gif')


@client.command()
async def help(ctx):
    embed = discord.Embed(
        title='Possible Commands',
        description="$drunk, $slap, $wakeup, $depressed, $boom, $pray, $dance, $vape",
        color=1146986
    )
    await ctx.send(embed=embed)


# Music commands

@client.command()
async def play(ctx):
    if not ctx.message.author.voice:
        embed = discord.Embed(
            description="You need to be in a voice channel to run this command!!"
        )
        await ctx.send(embed=embed)
    elif ctx.voice_client:
        embed = discord.Embed(
            description="I am already in a voice channel, you dummy >:("
        )
        await ctx.send(embed=embed)
    else:
        voice_channel = ctx.message.author.voice.channel
        await voice_channel.connect()


@client.command()
async def leave(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if ctx.voice_client:
        embed = discord.Embed(
            description="I left the voice channel"
        )
        await ctx.send(embed=embed)
        await ctx.guild.voice_client.disconnect()
    else:
        embed = discord.Embed(
            description="I am already not in a voice channel :/"
        )
        await ctx.send(embed=embed)


client.run(os.getenv('TOKEN'))
