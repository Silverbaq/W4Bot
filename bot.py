# W4 Discord Bot
# Build 2018

from decouple import config
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Ready when you are')
    print('I am running on ' + bot.user.name)
    print('With the ID: ' + bot.user.id)


@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say(":ping_pong: Pong!!")


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("The username is: {0}".format(user.name))
    await bot.say("The users ID is: {0}".format(user.id))
    await bot.say("The users status is: {0}".format(user.status))
    await bot.say("The users highest role is: {0}".format(user.top_role))
    await bot.say("The user joined at: {0}".format(user.joined_at))


bot.run(config('TOKEN'))
