"""
Tatsujin's ChinoBot for Discord
~~~~
A basic bot to serve my personal Discord server, as well as functioning
as my own sandbox. Capable of role assignment and other miscellaneous commands
and features to coincide with my personal server.
----------
1.00
"""
import os
from os.path import join, dirname
from dotenv import load_dotenv
import discord
from discord.ext import commands

# GET BOT TOKEN AND MODULES
token_path = join(dirname(__file__), 'token.env')
load_dotenv(token_path)
TOKEN = os.environ.get("BOT_TOKEN")
MODULES = [
    'modules.spotify', 'modules.roles', 'modules.simple',
    'modules.help'
]

# INITIAL SETUP:
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="c.", intents = intents)
bot.remove_command("help")
@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, 
    activity=discord.Game("ご注文はうさぎですか (*・ω・)ﾉ\nMade by tatsujin#1007"))
    print("ChinoBot is ready to go!")

if __name__ == '__main__':
    for extension in MODULES:
        bot.load_extension(extension)

# ERROR HANDLING:
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I couldn't find that command! Maybe try c.help?")
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.send("I can't do that command in PMs. Try it on the server instead!")
    if isinstance(error, commands.MemberNotFound):
        await ctx.send("I couldn't find a user with that name. Try tagging them instead?")
    else: 
        await ctx.send("Uh oh! Something terrible happened.\n"
        + "Check the console for more information.")
        print(error)

# GITHUB COMMAND
@bot.command()
async def github(ctx):
    #TODO: Implement this
    await ctx.send("I'm still working on this command!")

# TOKEN FROM `token.env`
bot.run(TOKEN)