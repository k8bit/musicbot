#!/bin/bash

# Python built-in libraries
import discord
import logging
import random
import os

from cogs import guesses 

from dotenv import load_dotenv
from discord.ext import commands


bot=commands.Bot(command_prefix='!')
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

if __name__ == '__main__':
    bot.load_extension("cogs.guesses")

@bot.event
async def on_ready():
    print(str(bot.user.name) + " is now logged in")

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    
    if message.content == "foo":
        await message.channel.send('hello to u too')
    elif message.content == "raise-exception": 
        raise discord.DiscordException

@bot.command(name='logout')
@commands.is_owner()
async def shutdown(ctx):
    await ctx.bot.logout()

@bot.event
async def on_error(event, *args, **kwargs):
    with open('error.log', 'a') as fp:
        if event == 'on_message': 
            fp.write(f'Unhandled message: {args[0]}\n')
        else:
            raise

bot.run(TOKEN)

