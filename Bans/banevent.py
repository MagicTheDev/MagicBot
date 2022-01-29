import coc
import discord
from HelperMethods.clashClient import client, coc_client, getPlayer
usafam = client.usafam
server = usafam.server
clans = usafam.clans
whitelist = usafam.whitelist
banlist = usafam.banlist

from discord.ext import commands

class banev(commands.Cog):

    def __init__(self, bot: commands.Bot):
        self.bot = bot
        coc_client.add_events(self.foo)

    @coc.ClanEvents.member_join()
    async def foo(self, member, clan):
        tag = member.tag
        results = await banlist.find_one({"VillageTag": tag})
        if results != None:
            cc = await clans.find_one({"tag": f"{clan.tag}"})
            server = cc.get("server")
            server = self.bot.get_guild(server)

            results = await banlist.find_one({"$and": [
                {"VillageTag": tag},
                {"server": server.id}
            ]})

            if results != None:
                notes = results.get("Notes")
                if notes == "":
                    notes = "No Reason Given"
                date = results.get("DateCreated")
                date = date[0:10]

                channel = cc.get("clanChannel")

                role = cc.get("generalRole")

                role =  server.get_role(role)
                channel = self.bot.get_channel(channel)

                player = await getPlayer(member.tag)

                embed = discord.Embed(
                    description=f"[WARNING! BANNED PLAYER {member.name} JOINED]({player.share_link})",
                    color=discord.Color.green())
                embed.add_field(name="Banned Player.", value=f"Player {member.name} [{member.tag}] has joined {clan.name} and is on the {server.name} BAN list!\n\n"
                                                             f"Banned on: {date}\nReason: {notes}")
                embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/843624785560993833/932701461614313562/2EdQ9Cx.png")
                await channel.send(content=role.mention,embed=embed)

def setup(bot: commands.Bot):
    bot.add_cog(banev(bot))