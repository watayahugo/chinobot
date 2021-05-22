import discord
from discord.ext import commands

# NAME, EMOJI ID, ROLE ID
IDENTIFICATION = {
    'OSU_EMOJI_ID': 811017982721130526, 'OSU_ROLE_ID': 802310374032146444,
    'VALORANT_EMOJI_ID': 811018181257723956, 'VALORANT_ROLE_ID': 811010939213054023,
    'CSGO_EMOJI_ID': 811018094881144862, 'CSGO_ROLE_ID': 811010887858913379,
    'EFT_EMOJI_ID': 811018504664252486, 'EFT_ROLE_ID': 811010850462629898,
}
CHAT_ID = 811017297430184006

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == CHAT_ID: # if the user reacts to a message in the #welcome chat
            member: discord.Member = payload.member
            embed_message = discord.Embed(
                title="Role assigned successfully!",
                color=0x29D0F4
            )
            role_str = None
            role = None

            if payload.emoji.id == IDENTIFICATION.get('OSU_EMOJI_ID'): #osu! role
                role = discord.utils.get(member.guild.roles, id=IDENTIFICATION.get('OSU_ROLE_ID'))
                role_str = "osu!"
            elif payload.emoji.id == IDENTIFICATION.get('VALORANT_EMOJI_ID'): #valorant role
                role = discord.utils.get(member.guild.roles, id=IDENTIFICATION.get('VALORANT_ROLE_ID'))
                role_str = "Valorant"
            elif payload.emoji.id == IDENTIFICATION.get('CSGO_EMOJI_ID'): #csgo role 
                role = discord.utils.get(member.guild.roles, id=IDENTIFICATION.get('CSGO_ROLE_ID'))
                role_str = "CS:GO"
            elif payload.emoji.id == IDENTIFICATION.get('EFT_EMOJI_ID'): #eft role
                role = discord.utils.get(member.guild.roles, id=IDENTIFICATION.get('EFT_ROLE_ID'))
                role_str = "Escape from Tarkov"
            else: return

            embed_message.description = "I've assigned you to the " + "**" + role_str + "**" + " role. " + "You should now have access to the " + role_str + " chat on DICKSWORD."
            await member.add_roles(role)
            await member.send(embed=embed_message)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == CHAT_ID: # if the user un-reacts to a message in the #welcome chat
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            member = guild.get_member(payload.user_id)

            embed_message = discord.Embed(
                title="Role unassigned successfully!",
                color=0xFC3777
            )
            role_str = None
            role = None
            
            if payload.emoji.id == IDENTIFICATION.get('OSU_EMOJI_ID'): #osu! role
                role = discord.utils.get(member.guild.roles, id=IDENTIFICATION.get('OSU_ROLE_ID'))
                role_str = "osu!"
            if payload.emoji.id == IDENTIFICATION.get('VALORANT_EMOJI_ID'): #valorant role
                role = discord.utils.get(member.guild.roles, id=IDENTIFICATION.get('VALORANT_ROLE_ID'))
                role_str = "Valorant"
            if payload.emoji.id == IDENTIFICATION.get('CSGO_EMOJI_ID'): #csgo role 
                role = discord.utils.get(member.guild.roles, id=IDENTIFICATION.get('CSGO_ROLE_ID'))
                role_str = "CS:GO"
            if payload.emoji.id == IDENTIFICATION.get('EFT_EMOJI_ID'): #eft role
                role = discord.utils.get(member.guild.roles, id=IDENTIFICATION.get('EFT_ROLE_ID'))
                role_str = "Escape from Tarkov"
            
            embed_message.description = "I've unassigned you to the " + "**" + role_str + "**" + " role."
            await member.remove_roles(role)
            await member.send(embed=embed_message)

def setup(bot):
    bot.add_cog(Roles(bot))