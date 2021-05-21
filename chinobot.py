"""
Tatsujin's ChinoBot for Discord
~~~~
A basic bot to serve my personal Discord server, as well as functioning
as my own sandbox. Capable of role assignment and other miscellaneous commands
and features to coincide with my personal server.
----------
Ver. 1.00
"""

import discord
from discord.ext import commands
initial_extensions = [
    'modules.spotify', 'modules.roles', 'modules.simple'
]
intents = discord.Intents().all()
bot = commands.Bot(command_prefix="c.", intents = intents)

if __name__ == '__main__':
    for extension in initial_extensions:
        bot.load_extension(extension)

# ERROR HANDLING:
@bot.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send("I couldn't find that command! Maybe try c.help?")
    if isinstance(error, commands.NoPrivateMessage):
        await ctx.send("I can't do that command in PMs. Try it on the server instead!")

@bot.event
async def on_ready():
    await bot.change_presence(status=discord.Status.online, 
    activity=discord.Game("ご注文はうさぎですか (*・ω・)ﾉ\nMade by tatsujin#1007"))

bot.run("")