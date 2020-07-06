import discord
import logging
import random

from cogs import guesses 
from discord.ext import commands
bot=commands.Bot(command_prefix='!')

if __name__ == '__main__':
    bot.load_extension("cogs.guesses")

@bot.event
async def on_ready():
    print('We have logged in as ' + str(bot.user.name))

@bot.command(name='logout')
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

    
bot.run('TOKEN',bot=True)
