import disnake
from Dictionaries.emojiDictionary import emojiDictionary
from Dictionaries.thPicDictionary import thDictionary
from utils.troop_methods import profileSuperTroops, leagueAndTrophies
from utils.clash import getPlayer, link_client, pingToMember, client, getClan
from utils.troop_methods import heros, heroPets, troops, deTroops, siegeMachines, spells
import aiohttp
from bs4 import BeautifulSoup
import cchardet

usafam = client.usafam
server = usafam.server
banlist = usafam.banlist


async def create_profile_stats(ctx, result):

    embed=[]

    disnakeID = await link_client.get_link(result)
    player = await getPlayer(result)
    member = await pingToMember(ctx, str(disnakeID))



    name = player.name
    link = player.share_link
    donos = player.donations
    received = player.received
    ratio = str(round((donos / (received + 1)), 2))
    bestTrophies = emojiDictionary("trophy") + str(player.best_trophies)
    friendInNeed = str(player.get_achievement("Friend in Need").value)


    clan = ""
    try:
        clan = player.clan.name
        clan = f"{clan},"
    except:
        clan = "None"

    stroops = profileSuperTroops(player)
    # print(stroops)
    if (len(stroops) > 0):
        stroops = "\n**Super Troops:**\n" + stroops + "\n"
    else:
        stroops = ""

    troph = leagueAndTrophies(player)

    th = str(player.town_hall)
    role = str(player.role)
    if role == "None":
        role = ""
    emoji = emojiDictionary(player.town_hall)

    results = await server.find_one({"server": ctx.guild.id})
    prefix = results.get("prefix")

    tag = player.tag
    tag = tag.strip("#")
    if member is not None:
        embed = disnake.Embed(title=f'{emoji} **{name}** ',
                              description="Linked to " + member.mention +
                              f"\nTh Level: {player.town_hall}\nTrophies: {troph}\n" +
                                "Tag: " + f'[{player.tag}]({link})' "\n"
                                f"Clan: {clan} {role}\n"
                                f"[Clash Of Stats Profile](https://www.clashofstats.com/players/{tag})",
                              color=disnake.Color.green())
        if member.avatar is None:
            embed.set_thumbnail(
                url="https://cdn.discordapp.com/attachments/843624785560993833/961411093622816819/4_1.png")
        else:
            embed.set_thumbnail(url=member.avatar.url)
    elif (member is None) and (disnakeID is not None):
        embed = disnake.Embed(title=f'{emoji} **{name}** ',
                              description=f"*Linked, but not on this server.*"+
                                          f"\nTh Level: {player.town_hall}\nTrophies: {troph}\n" +
                                          "Tag: " + f'[{player.tag}]({link})' "\n"
                                                    f"Clan: {clan} {role}\n"
                                                    f"[Clash Of Stats Profile](https://www.clashofstats.com/players/{tag})"
                              , color=disnake.Color.green())
        if player.town_hall >= 4:
            embed.set_thumbnail(url=thDictionary(player.town_hall))
    else:
        embed = disnake.Embed(title=f'{emoji} **{name}** ',
                              description=f"Not linked. Owner? Use `{prefix}link`" +
                                          f"\nTh Level: {player.town_hall}\nTrophies: {troph}\n" +
                                          "Tag: " + f'[{player.tag}]({link})' "\n"
                                                    f"Clan: {clan} {role}\n"
                                                    f"[Clash Of Stats Profile](https://www.clashofstats.com/players/{tag})"
                              , color=disnake.Color.green())
        if player.town_hall >= 4:
            embed.set_thumbnail(url=thDictionary(player.town_hall))




    embed.add_field(name="**Info:**",
                    value=f"<:warwon:932212939899949176>Donated: {donos} troops\n"
                          f"<:warlost:932212154164183081>Received: {received} troops\n"
                          f"<:winrate:932212939908337705>Donation Ratio: {ratio}\n"
                          f"<:sword:825589136026501160>Attack Wins: {player.attack_wins}\n"
                          f"<:clash:877681427129458739>Defense Wins: {player.defense_wins}\n"
                          f"{stroops}"
                          f"**Stats:**\n"
                          f"Best Trophies: {bestTrophies}\n"
                          f"War Stars: ??? {player.war_stars}\n"
                          f"All Time Donos: {friendInNeed}", inline=False)

    ban = await banlist.find_one({"$and": [
        {"VillageTag": f"{player.tag}"},
        {"server": ctx.guild.id}
    ]})

    if ban != None:
        date = ban.get("DateCreated")
        date = date[0:10]
        notes = ban.get("Notes")
        if notes == "":
            notes = "No Reason Given"
        embed.add_field(name="__**Banned Player**__",
                        value=f"Date: {date}\nReason: {notes}")
    return embed

async def history(ctx, result):
    discordID = await link_client.get_link(result)
    member = await pingToMember(ctx, str(discordID))
    player = await getPlayer(result)
    join = None
    try:
        join = member.joined_at
        day = str(join.day)
        month = str(join.month)
        year = str(join.year)
    except:
        pass

    result = result.strip("#")
    url = f'https://www.clashofstats.com/players/{result}/history/'
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            clans = soup.find_all("a", class_="v-list-item v-list-item--link theme--dark")
            test = soup.find_all("div", class_="subsection-title")
            num_clans = test[1].text.strip()
            text = ""
            x = 0
            for clan in clans:
                try:
                    #title_element = clan.find("div", class_="subsection-title")
                    company_element = clan.find("span", class_="text--secondary caption")
                    location_element = clan.find("div", class_="v-list-item__subtitle")
                    #print(title_element.text.strip())
                    #print(company_element.text.strip())
                    t = company_element.text.strip()
                    t = t.strip("-")
                    c = await getClan(t)
                    t = f"[{c.name}]({c.share_link}), - "
                    lstay = None
                    for d in location_element.find_all("br"):
                        lstay = "".join(d.previous_siblings)
                    # print(location_element.text.strip())
                    lstay = " ".join(lstay.split())
                    lstay = lstay.strip("Total ")
                    text += f"\u200e{t} \u200e{lstay}\n"
                    x+=1
                    if x == 5:
                        break
                except:
                    pass

        embed = disnake.Embed(title=f"{player.name} History",
                              description=f"{num_clans}",
                              color=disnake.Color.green())
        embed.add_field(name="**Top 5 Clans Player has stayed the most:**",
                        value=text, inline=False)


        result = result.strip("#")
        url = f'https://www.clashofstats.com/players/{result}/history/log'
        async with session.get(url) as response:
            soup = BeautifulSoup(await response.text(), 'lxml')
            clans = soup.find_all("a", class_="v-list-item v-list-item--link theme--dark")
            text = ""
            x = 0
            types = ["Member", "Elder", "Co-leader", "Leader"]
            for clan in clans:
                try:
                    title_element = clan.find("div", class_="v-list-item__title")
                    location_element = clan.find("div", class_="v-list-item__subtitle text--secondary")
                    t = title_element.text.strip()
                    t = " ".join(t.split())
                    ttt = t.split("#", 1)
                    clan = await getClan(ttt[1])
                    type = "No Role"
                    for ty in types:
                        if ty in t:
                            type = ty

                    t = f"\u200e[{clan.name}]({clan.share_link}), \u200e{type}"

                    lstay = location_element.text.strip()
                    lstay = " ".join(lstay.split())
                    text += f"{t} \n{lstay}\n"
                    x += 1
                    if x == 5:
                        break
                except:
                    pass

        embed.add_field(name="**Last 5 Clans Player has been seen at:**",
                        value=text, inline=False)

        if join is not None:
            embed.add_field(name="**Tenure:**",
                            value=member.display_name + " has been in this server since " + str(
                                month + "/" + day + "/" + year), inline=False)

        embed.set_footer(text="Data from ClashofStats.com")
        return embed



async def create_profile_troops(result):
    player = await getPlayer(result)
    hero = heros(player)
    pets = heroPets(player)
    troop = troops(player)
    deTroop = deTroops(player)
    siege = siegeMachines(player)
    spell = spells(player)

    embed = disnake.Embed(title="You are looking at " + player.name,
                           description="Troop, hero, & spell levels for this account.",
                           color=disnake.Color.green())
    embed.add_field(name=f'__**{player.name}** (Th{player.town_hall})__ {player.trophies}', value="Profile: " + f'[{player.tag}]({player.share_link})',
                     inline=False)

    if (hero != None):
        embed.add_field(name="**Heroes:** ", value=hero, inline=False)

    if (pets != None):
        embed.add_field(name="**Pets:** ", value=pets, inline=False)

    if (troop != None):
        embed.add_field(name="**Elixir Troops:** ", value=troop, inline=False)

    if (deTroop != None):
        embed.add_field(name="**Dark Elixir Troops:** ", value=deTroop, inline=False)

    if (siege != None):
        embed.add_field(name="**Siege Machines:** ", value=siege, inline=False)

    if (spell != None):
        embed.add_field(name="**Spells:** ", value=spell, inline=False)

    return embed