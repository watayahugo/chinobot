import discord
from discord.ext import commands

class Roles(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_raw_reaction_add(self, payload):
        message_id = payload.message_id
        if message_id == 811017297430184006: # if the user reacts to a message in the #welcome chat
            member: discord.Member = payload.member
            if payload.emoji.id == 811017982721130526: #osu! role
                role = discord.utils.get(member.guild.roles, id=802310374032146444)
                await member.add_roles(role)
                embed_message = discord.Embed(title="Role assigned successfully!", color=0x29D0F4)
                embed_message.description = "I have given you the osu! role in DICKSWORD.\n You should now have access to the osu chat!"
                await member.send(embed=embed_message)
            if payload.emoji.id == 811018181257723956: #valorant role
                role = discord.utils.get(member.guild.roles, id=811010939213054023)
                await member.add_roles(role)
                embed_message = discord.Embed(title = "Role assigned successfully!", color=0x29D0F4)
                embed_message.description = "I have given you the Valorant role in DICKSWORD.\n You should now have access to the Valorant chat!"
                await member.send(embed=embed_message)
            if payload.emoji.id == 811018094881144862: #csgo role 
                role = discord.utils.get(member.guild.roles, id=811010887858913379)
                await member.add_roles(role)
                embed_message = discord.Embed(title = "Role assigned successfully!", color=0x29D0F4)
                embed_message.description = "I have given you the CS:GO role in DICKSWORD.\n You should now have access to the CS:GO chat!"
                await member.send(embed=embed_message)
            if payload.emoji.id == 811018504664252486: #eft role
                role = discord.utils.get(member.guild.roles, id=811010850462629898)
                await member.add_roles(role)
                embed_message = discord.Embed(title = "Role assigned successfully!", color=0x29D0F4)
                embed_message.description = "I have given you the Escape from Tarkov role in DICKSWORD.\n You should now have access to the EFT chat!"
                await member.send(embed=embed_message)

    @commands.Cog.listener()
    async def on_raw_reaction_remove(self, payload):
        message_id = payload.message_id
        if message_id == 811017297430184006: # if the user un-reacts to a message in the #welcome chat
            guild_id = payload.guild_id
            guild = discord.utils.find(lambda g : g.id == guild_id, self.bot.guilds)
            member = guild.get_member(payload.user_id)
            
            if payload.emoji.id == 811017982721130526: #osu! role
                role = discord.utils.get(member.guild.roles, id=802310374032146444)
                await member.remove_roles(role)
                embed_message = discord.Embed(title="Role unassigned successfully!", color=0xFC3777)
                embed_message.description = "I removed the osu! role from you.\nIf you want access to the osu! chat again, just react to the role in #welcome"
                await member.send(embed=embed_message)
            if payload.emoji.id == 811018181257723956: #valorant role
                role = discord.utils.get(member.guild.roles, id=811010939213054023)
                await member.remove_roles(role)
                embed_message = discord.Embed(title = "Role unassigned successfully!", color=0xFC3777)
                embed_message.description = "I removed the Valorant role from you.\nIf you want access to the Valorant chat again, just react to the role in #welcome"
                await member.send(embed=embed_message)
            if payload.emoji.id == 811018094881144862: #csgo role 
                role = discord.utils.get(member.guild.roles, id=811010887858913379)
                await member.remove_roles(role)
                embed_message = discord.Embed(title = "Role unassigned successfully!", color=0xFC3777)
                embed_message.description = "I removed the CS:GO role from you.\nIf you want access to the CS:GO chat again, just react to the role in #welcome"
                await member.send(embed=embed_message)
            if payload.emoji.id == 811018504664252486: #eft role
                role = discord.utils.get(member.guild.roles, id=811010850462629898)
                await member.remove_roles(role)
                embed_message = discord.Embed(title = "Role unassigned successfully!", color=0xFC3777)
                embed_message.description = "I removed the Escape from Tarkov role from you.\nIf you want access to the EFT chat again, just react to the role in #welcome"
                await member.send(embed=embed_message)

def setup(bot):
    bot.add_cog(Roles(bot))