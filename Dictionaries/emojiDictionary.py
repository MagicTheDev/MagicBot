
def emojiDictionary(emojiName):
    switcher = {
        "Barbarian King": "<:BarbarianKing:701626158181122210>",
        "Archer Queen": "<:ArcherQueen:701626158487175270>",
        "Grand Warden": "<:GrandWarden:701933765450268672>",
        "Royal Champion": "<:RoyalChampion:701933810648088606>",
        "Archer": "<:Archer:701626909498409040>",
        "Baby Dragon": "<:BabyDragon:701626909586358364>",
        "Barbarian": "<:Barbarian:701626910207115274>",
        "Bowler": "<:Bowler:701626910614093844>",
        "Electro Dragon": "<:ElectroDragon:701626910735728672>",
        "Dragon": "<:Dragon:701626910752374804>",
        "Dragon Rider": "<:dragon_rider:855686522653114399>",
        "Balloon": "<:Balloon:701626912241352745>",
        "Ice Golem": "<:IceGolem:701626913701101668>",
        "Miner": "<:Miner:701626913793245255>",
        "Hog Rider": "<:HogRider:701626914506276895>",
        "Yeti": "<:Yeti:701626914816655431>",
        "Wizard": "<:Wizard:701626914841821186>",
        "Healer": "<:Healer:701626914930163783>",
        "Giant": "<:Giant:701626915026370671>",
        "Goblin": "<:Goblin:701626915165044828>",
        "Witch": "<:Witch:701626915173433385>",
        "Minion": "<:Minion:701626915311583294>",
        "P.E.K.K.A": "<:PEKKA:701626915328491610>",
        "Wall Breaker": "<:WallBreaker:701626915357982742>",
        "Golem": "<:Golem:701626915395600394>",
        "Lava Hound": "<:LavaHound:701626915479355483>",
        "Valkyrie": "<:Valkyrie:701626915680681994>",
        "Headhunter": "<:Headhunter:742121658386481262>",
        "Super Wall Breaker" : "<:SuperWallBreaker:701626916133666896>",
        "Super Barbarian": "<:SuperBarbarian:701626916087529673>",
        "Super Archer": "<:SuperArcher:750010593045643355>",
        "Super Giant": "<:SuperGiant:701626915902980197>",
        "Sneaky Goblin": "<:SneakyGoblin:701626916129734787>",
        "Rocket Balloon": "<:RocketBalloon:854368171682431006>",
        "Super Wizard": "<:SuperWizard:785536616864153610>",
        "Inferno Dragon": "<:InfernoDragon:742121658386743366>",
        "Super Minion": "<:SuperMinion:771375748916576286>",
        "Super Valkyrie": "<:SuperValkyrie:771375748815519825>",
        "Super Witch": "<:SuperWitch:742121660324511818>",
        "Ice Hound": "<:IceHound:785539963068481546>",
        "Super Dragon" : "<:SuperDragon:918876075809964072>",
        "Super Bowler" : "<:SuperBowler:892035736168185876>",
        "Unicorn": "<:Unicorn:830510531483795516>",
        "Mighty Yak": "<:MightyYak:830510531222962278>",
        "Electro Owl": "<:ElectroOwl:830511434269982790>",
        "L.A.S.S.I":"<:LASSI:830510531168829521>",
        "trophy": "<:trophyy:849144172698402817>",
        "Wall Wrecker": "<:WallWrecker:701628825142034482>",
        "Battle Blimp": "<:BattleBlimp:701628824395317328>",
        "Stone Slammer":  "<:StoneSlammer:701628824688918588>",
        "Siege Barracks":"<:SiegeBarracks:701628824651169913>",
        "Log Launcher":"<:LogLauncher:785540240358113312>",
        "Flame Flinger" : "<:FlameFlinger:918875579904847873>",
        "Skeleton Spell": "<:skel:652161148241707029>",
        "Rage Spell": "<:rs:665562307606347822>",
        "Poison Spell": "<:ps:652161145582387210>",
        "Healing Spell": "<:hs:652161148057026580>",
        "Invisibility Spell": "<:invi:785474117414551582>",
        "Jump Spell": "<:js:652161148032122897>",
        "Lightning Spell": "<:ls:726648294461407441>",
        "Haste Spell": "<:haste:652161145125470208>",
        "Freeze Spell": "<:fs:652161149193682974>",
        "Earthquake Spell": "<:es:652161143975968798>",
        "Bat Spell": "<:bat:652161147679670301>",
        "Clone Spell": "<:cs:652161148958801920>",
        "clan castle" : "<:clan_castle:855688168816377857>",
        "shield" : "<:clash:855491735488036904>",
        2: "<:02:701579364483203133>",
        3: "<:03:701579364600643634>",
        4: "<:04:701579365850284092>",
        5 : "<:05:701579365581848616>",
        6 : "<:06:701579365573459988>",
        7 : "<:07:701579365598756874>",
        8 : "<:08:701579365321801809>",
        9 : "<:09:701579365389041767>",
        10 : "<:10:701579365661671464>",
        11 : "<:11:701579365699551293>",
        12 : "<:12:701579365162418188>",
        13 : "<:132:704082689816395787>",
        14 : "<:14:828991721181806623>",
        "Heroic Heist" : "<:dark_elixir:858423313894211584>",
        "Nice and Tidy" : "<:bush:858423580319678564>",
        "Clan War Wealth" : "<:gold:801033639507918858>",
        "Friend in Need" : "<:clan_castle:855688168816377857>",
        "Sharing is caring" : "<:rs:665562307606347822>",
        "Siege Sharer" : "<:sb:665361865861234700>",
        "War Hero" : "⭐",
        "War League Legend" : "<:LeagueMedal:858424820857307176>",
        "Games Champion" : "<:cg:858425112256970772>",
        "Unbreakable" : "<:clash:855491735488036904>",
        "Conqueror" : "⚔️",
        "Sweet Victory" : "<:trophyy:849144172698402817>",
        "Humiliator" : "<:Town_Hall8:831746066864144406>",
        "Union Buster" : "<:bh:858426739608649778>",
        "Wall Buster" : "<:wall:858427105045250078>",
        "Well Seasoned" : "<:pass:858432465872879637>"


    }

    emoji = switcher.get(emojiName, "No Emoji Found")
    return emoji
