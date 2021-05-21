import discord
from discord.ext import commands
import random

class Simple(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
        help = "Flips a coin (heads or tails)",
        brief = "Flips a coin"
    )
    @commands.guild_only()
    async def coinflip(self, ctx):
        user: str = ctx.author
        flip = random.choice(['Heads', 'Tails'])
        message = discord.Embed(title="It's " + flip + "!", color=0x29D0F4)
        await ctx.send(embed=message)

    @commands.command(
        name = "8ball"
    )
    @commands.guild_only()
    async def _8ball(self, ctx, *, content:str = None):
        responses = [
            "It is Certain.",
            "It is decidedly so.",
            "Without a doubt.",
            "Yes definitely",
            "You may rely on it.",
            "As I see it, yes.",
            "Most likely.",
            "Outlook good.",
            "Yes.",
            "Signs point to yes.",
            "Reply hazy, try again.",
            "Ask again later.",
            "Better not tell you now.", 
            "Cannot predict now.",
            "Concentrate and ask again.", 
            "Don't count on it.",
            "My reply is no.",
            "My sources say no.",
            "Outlook not so good.",
            "Very doubtful."
        ]
        choice = random.choice(responses)
        clr = None
        if responses.index(choice) <= 9:
            clr = 0x2adb21
        elif responses.index(choice) <= 14:
            clr = 0xe1f01a
        else:
            clr = 0xf21616
        message = discord.Embed(title=choice,color=clr)
        if content is not None: 
            message.description = content
        await ctx.reply(embed=message)

def setup(bot):
    bot.add_cog(Simple(bot))