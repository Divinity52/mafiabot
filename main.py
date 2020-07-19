import discord
import random
import os
from discord.ext import commands
from Token import Token

client = discord.Client()
bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')
    await bot.change_presence(activity=discord.Game(name="With The Wolf Mafia"))


@bot.command(pass_context=True)
async def choose(ctx, rname, amount):
    for letter in rname:
        if letter == '_':
            rname = rname.replace(letter, " ")
    list_ = []
    full = False
    for member in ctx.message.guild.members:
        for role in member.roles:
            if role.name == rname:
                if member.name not in list_:
                    list_.append(member.name)
                    full = True
    if full:
        success = True
        try:
            list_2 = random.sample(list_, int(amount))

        except ValueError:
            success = False
        if success:
            if int(amount) >= 2:
                await ctx.send(f'The Winners Are:\n▬▬▬▬▬▬▬▬▬▬')
            else:
                await ctx.send(f'The Winner Is:\n▬▬▬▬▬▬▬▬▬▬')
            for j in range(int(amount)):
                await ctx.send(f'`{j + 1}). {list_2[j]}`')
            await ctx.send('▬▬▬▬▬▬▬▬▬▬')
        else:
            await ctx.send(f'There is not {str(amount)} Member{"s" if int(amount) >= 2 else ""} with Role {rname}')
    elif not full:
        await ctx.send(f'No-one has a role named {rname}!')


client.run(os.environ['DISCORD_TOKEN'])