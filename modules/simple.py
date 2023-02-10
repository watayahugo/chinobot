import discord
from discord.ext import commands
import random


class Simple(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    @commands.guild_only()
    async def coinflip(self, ctx):
        user: str = ctx.author
        flip = random.choice(["Heads", "Tails"])
        message = discord.Embed(title="It's " + flip + "!", color=0x29D0F4)
        await ctx.send(embed=message)

    @commands.command()
    @commands.guild_only()
    async def roll(self, ctx, number: int = None):
        if number is None:
            number = 100
        random_number = random.randint(0, number)
        embed_message = discord.Embed(
            description=ctx.author.name + " rolled " + str(random_number) + " point(s)!"
        )
        await ctx.send(embed=embed_message)

    @commands.command(name="8ball")
    @commands.guild_only()
    async def _8ball(self, ctx, *, content: str = None):
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
            "Very doubtful.",
        ]
        choice = random.choice(responses)
        clr = None
        if responses.index(choice) <= 9:
            clr = 0x2ADB21
        elif responses.index(choice) <= 14:
            clr = 0xE1F01A
        else:
            clr = 0xF21616
        message = discord.Embed(title=choice, color=clr)
        if content is not None:
            message.description = content
        await ctx.reply(embed=message)

    @commands.command()
    @commands.guild_only()
    async def echo(self, ctx, *, content: str = None):
        if content is None:
            await ctx.send("You need to specify a message argument, silly.")
        await ctx.send(content)


def setup(bot):
    bot.add_cog(Simple(bot))
