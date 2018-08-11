# W4 Discord Bot
# Build 2018

from decouple import config
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import utils

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('Ready when you are')
    print('I am running on ' + bot.user.name)
    print('With the ID: ' + bot.user.id)


@bot.event
async def on_member_join(user: discord.Member):
    await bot.say("Hi {0}! Great to see you!".format(user.name))


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


######## Encoding / Decoding ########
@bot.command(pass_context=True)
async def b64encode(ctx, *text):
    res = utils.encode_base64(' '.join(text))
    await bot.say(res)


@bot.command(pass_context=True)
async def b64decode(ctx, *text):
    res = utils.decode_base64(' '.join(text))
    await bot.say(res)


bot.run(config('TOKEN'))
