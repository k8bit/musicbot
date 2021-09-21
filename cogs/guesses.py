import discord
import random

from discord.ext import commands
from random import randrange

class Guesses(commands.Cog):
    def __init__(self,bot):
        self.bot=bot

    @commands.command(name='hello')
    async def hello(self,ctx):
        await ctx.send("Hello!")

    @commands.command(name='guess')
    async def guess(self, ctx):
        rand = randrange(10)
        await ctx.send('guess')
        for i in range(0,5):
            response = await self.bot.wait_for('message')
            guess = int(response.content)
            if guess is not rand:
                await ctx.send('wrong guess... try again...') 
            else:
                await ctx.send('youre correct!')
                return

def setup(bot):
    bot.add_cog(Guesses(bot))
