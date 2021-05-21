import discord
from discord.ext import commands

class SpotifyMethod(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(
    help = "Returns information about the user's Spotify listening session.",
    brief = "Returns info about your Spotify session"
    )
    @commands.guild_only()
    async def spotify(self, ctx, user: discord.Member = None):
        user = user or ctx.author  # default to the caller
        spot = next((activity for activity in user.activities if isinstance(activity, discord.Spotify)), None)
        if spot is None:
            await ctx.send(f"{user.name} is not listening to Spotify")
            return
        songlink = spot.track_id
        embedspotify = discord.Embed(title=f"{user.name} is listening to:", color=0x1eba10)
        embedspotify.add_field(name="Song", value=spot.title, inline=False)
        embedspotify.add_field(name="Artist", value=spot.artist, inline=False)
        embedspotify.add_field(name="Album", value=spot.album, inline=False)
        embedspotify.description = "[Track link](https://open.spotify.com/track/" + songlink + ")"
        embedspotify.set_thumbnail(url=spot.album_cover_url)
        await ctx.send(embed=embedspotify)

def setup(bot):
    bot.add_cog(SpotifyMethod(bot))