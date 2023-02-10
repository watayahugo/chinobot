import discord
from discord.ext import commands


class Help(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def help(self, ctx, args: str = None):
        user = ctx.author
        embed_message = None
        # Command specific help messages
        if args is not None:
            if args == "spotify":
                embed_message = embed_spotify()
            elif args == "8ball":
                embed_message = embed_8ball()
            elif args == "coinflip":
                embed_message = embed_coinflip()
            elif args == "help":
                embed_message = embed_help()
            elif args == "github":
                embed_message = embed_github()
            elif args == "roll":
                embed_message = embed_roll()
            elif args == "echo":
                embed_message = embed_echo()
            else:
                await ctx.send(
                    "I can't find the command " + "`" + args + "`" + "\nTry `c.help`!"
                )
                return
            await ctx.send(embed=embed_message)
        else:
            embed_message = discord.Embed(
                title="List of commands/features",
                color=0x31E8EB,
                description="Use `c.help [command]` for command help.\n Example: `c.help spotify`",
            )
            embed_message.set_thumbnail(
                url="https://user-images.githubusercontent.com/12385776/119098969-6c902480-b9e4-11eb-9b7a-8e9a087854c8.jpg"
            )
            # List all commands with brief descriptions
            embed_message.add_field(
                name="spotify", value="Sends message of user's Spotify session."
            ).add_field(name="8ball", value="Uses a Magic 8-Ball!").add_field(
                name="coinflip", value="Tosses a coin (heads/tails)."
            ).add_field(
                name="help", value="Displays this message."
            ).add_field(
                name="github", value="Sends link of the ChinoBot repo."
            ).add_field(
                name="roll", value="Rolls a random number."
            ).add_field(
                name="echo", value="Repeats the content of your message."
            )
            await ctx.reply("I sent you a DM with all of my commands!")
            await user.send(embed=embed_message)


# COMMAND SPECIFIC EMBEDS
def embed_spotify():
    embed_message = discord.Embed(
        title="`spotify` command",
        color=0x31E8EB,
        description="Returns a message to the caller that identifies the song, album"
        + " and artist that the user is listening to on Spotify.\n"
        + "When no user is defined, command defaults to your own Spotify session.",
    )
    embed_message.set_footer(text="LEGEND: [] = Optional and <> = Required")
    embed_message.add_field(
        name="Syntax:",
        value="`c.spotify [user]`\n`[user]` supports tagging.",
        inline=False,
    ).add_field(
        name="Example:",
        value="c.spotify tatsujin`\n`c.spotify @tatsujin`",
        inline=False,
    )
    return embed_message


def embed_8ball():
    embed_message = discord.Embed(
        title="`8ball` command",
        color=0x31E8EB,
        description="Replies to the caller with a message with a "
        + "[Magic 8-Ball](https://en.wikipedia.org/wiki/Magic_8-Ball) reading.",
    )
    embed_message.set_footer(text="LEGEND: [] = Optional and <> = Required")
    embed_message.add_field(
        name="Syntax:", value="`c.8ball [message]`", inline=False
    ).add_field(
        name="Example:",
        value="`c.8ball Will something amazing happen today?`\n`c.8ball`",
        inline=False,
    )
    return embed_message


def embed_coinflip():
    embed_message = discord.Embed(
        title="`coinflip` command",
        color=0x31E8EB,
        description="Flips a coin and returns to the caller whether it was heads/tails.",
    )
    embed_message.set_footer(text="LEGEND: [] = Optional and <> = Required")
    embed_message.add_field(name="Syntax:", value="`c.coinflip`", inline=False)
    return embed_message


def embed_help():
    embed_message = discord.Embed(
        title="`help` command",
        color=0x31E8EB,
        description="Returns a list of my comman.. wait a second, don't you already know this?",
    )
    return embed_message


def embed_github():
    embed_message = discord.Embed(
        title="`github` command",
        color=0x31E8EB,
        description="Returns the link to the ChinoBot GitHub repository.",
    )
    embed_message.set_footer(text="LEGEND: [] = Optional and <> = Required")
    embed_message.add_field(name="Syntax:", value="`c.github`", inline=False)
    return embed_message


def embed_roll():
    embed_message = discord.Embed(
        title="`roll` command",
        color=0x31E8EB,
        description="Rolls a random integer from 0 to the specified integer, inclusive."
        + "\nIf number is not specified, rolls from 0 to 100 inclusive by default.",
    )
    embed_message.set_footer(text="LEGEND: [] = Optional and <> = Required")
    embed_message.add_field(
        name="Syntax:", value="`c.roll [number]`", inline=False
    ).add_field(name="Example:", value="`c.roll 200`")
    return embed_message


def embed_echo():
    embed_message = discord.Embed(
        title="`echo` command",
        color=0x31E8EB,
        description="Repeats the content of the command after calling.",
    )
    embed_message.set_footer(text="LEGEND: [] = Optional and <> = Required")
    embed_message.add_field(
        name="Syntax:", value="`c.echo <content>`", inline=False
    ).add_field(name="Example:", value="`c.echo Repeat this message!`")
    return embed_message


def setup(bot):
    bot.add_cog(Help(bot))
