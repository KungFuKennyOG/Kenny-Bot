import discord
import os

from dotenv import load_dotenv

load_dotenv()

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$drunk'):
        await message.channel.send('https://tenor.com/view/drunk-gif-22301749')

    if message.content.startswith('$slap'):
        await message.channel.send('https://tenor.com/view/slapping-mad-rage-anime-backhand-gif-16422437')

    if message.content.startswith('$wakeup'):
        await message.channel.send('https://tenor.com/view/sleep-wake-up-wake-up-in-night-ren-and-stimpy-gif-24104879')

    if message.content.startswith('$depressed'):
        await message.channel.send('https://tenor.com/view/sad-raining-gif-17973911')

    if message.content.startswith('$boom'):
        await message.channel.send('https://tenor.com/view/penis-firework-explosion-boom-gif-4932263')

    if message.content.startswith('$pray'):
        await message.channel.send('https://tenor.com/view/halal-pray-praying-cat-praying-cat-gif-19802221')

    if message.content.startswith('$dance'):
        await message.channel.send('https://media.discordapp.net/attachments/741858155075469393/894749228222541885/koala-fab-02.gif')

    if message.content.startswith('$vape'):
        await message.channel.send('https://media.discordapp.net/attachments/753289564344549519/908183938940436490/received_583865662581686.gif')

    if message.content.startswith('$help'):
        embed = discord.Embed(
            title='Possible Commands',
            description="$drunk, $slap, $wakeup, $depressed, $boom, $pray, $dance, $vape",
            color=1146986
        )

        await message.channel.send(embed=embed)

client.run(os.getenv('TOKEN'))
