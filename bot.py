# W4 Discord Bot
# Build 2018

from decouple import config
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import utils
import chatcontroller
from time import sleep
from threading import Thread

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


############### GIF ###############
@bot.command(pass_context=True)
async def hackerman(ctx):
    await bot.say("https://media.giphy.com/media/VHHxxFAeLaYzS/giphy.gif")


@bot.command(pass_context=True)
async def bob(ctx):
    await bot.say("https://media.giphy.com/media/hcwIm2NdTYhva/giphy.gif")


############### Help ###############
@bot.command(pass_context=True)
async def showhelp(ctx):
    await bot.say("The different commands are:")
    await bot.say("!ping \tThis will return a pong")
    await bot.say("!info @[user] \tThis will give you information about a user")
    await bot.say("!b64encode text \tThis will base64 encode the 'text'")
    await bot.say("!b64decode text \tThis will decode base64")


######## Encoding / Decoding ########
@bot.command(pass_context=True)
async def b64encode(ctx, *text):
    res = utils.encode_base64(' '.join(text))
    await bot.say(res)


@bot.command(pass_context=True)
async def b64decode(ctx, *text):
    res = utils.decode_base64(' '.join(text))
    await bot.say(res)


############### Chat bot ###############
@bot.command(pass_context=True)
async def chat(ctx, *text):
    result = chatcontroller.chat_with_bot(' '.join(text))
    await bot.say(result)


# Auto chat
'''
@bot.command(pass_context=True)
async def enable_auto(ctx):
    auto_chat = True
    Thread(target=auto_chatbot).start()
    await bot.say(auto_chat)


@bot.command(pass_context=True)
async def chat2(*text):
    result = chatcontroller.chat_with_bot(' '.join(text))
    await bot.say(result)


@bot.command(pass_context=True)
async def disable_auto(ctx):
    auto_chat = False
    await bot.say(auto_chat)


def auto_chatbot():
    global auto_chat
    auto_chat = True
    while auto_chat:
        chat2(' ')
        sleep(10)
'''

bot.run(config('TOKEN'))
