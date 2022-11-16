import json
import os
import discord
import requests
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.all()


bot = commands.Bot(command_prefix = 't$', intents=intents)


#Gets list of tews members id
def get_clan():
    response = requests.get("https://brawlhalla.fly.dev/v1/utils/clan?clan_id=527406")
    json_data = json.loads(response.text)
    clanlist = json_data["data"]["clan"]
    memberlist = []
    for x in range(len(clanlist)):
        members = clanlist[x]["brawlhalla_id"]
        memberlist.append(members)
    return(memberlist)

    

#Tews ID: 527406
#Tews II ID: 1374400

#Gets elo of a given brawlhalla ID
def get_rank():
    member_id = get_clan()
    memberlist = []
    # response = requests.get("https://brawlhalla-api.herokuapp.com/v1/ranked/id?brawlhalla_id=" + str(member_id[9]))
    # json_data = json.loads(response.text)
    # elo = json_data["data"]["brawlhalla_id"]
    # name = json_data["data"]["name"]
    # memberlist.append(tuple((name, elo)))
    for x in range(len(member_id)):
        try:
            response = requests.get("https://brawlhalla.fly.dev/v1/ranked/id?brawlhalla_id=" + str(member_id[x]))
            json_data = json.loads(response.text)
            elo = json_data["data"]["rating"]
            name = json_data["data"]["name"]
            memberlist.append(tuple((name, elo)))
        except Exception as error:
            print(error)
    return(memberlist)

#For the embedded format on discord
def get_embed():
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0x7289DA)
    embed.set_author(name="Tewsrankbot", url="https://twitter.com/RealDrewData", icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")
    embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
    embed.add_field(name="Tews Leadeboard" ,value="uh", inline=False)
    embed.add_field(name="Name", value="This is the value for field 1.\n This is an inline field.", inline=True)
    embed.add_field(name="Elo", value="This is the value for field 1. This is an inline field.", inline=True)
    return(embed)


#Gets  the elo ratings of all members of Tews
def get_leaderboard():
    members = get_rank()
    members.sort(key=lambda x:x[1], reverse=True)
    names = [x[0] for x in members]
    elo = [str(x[1]) for x in members]
    numbers = list(range(1, len(members)+1))
    rank = [str(x) for x in numbers]
    embed=discord.Embed(title="Tews Leadboard", color=0x7289DA)
    embed.set_author(name="TewsRankBot", icon_url="https://cdn.discordapp.com/icons/160098918032605184/b3a614d2cbccef36ca04d5a260600d29.webp?size=240")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/160098918032605184/b3a614d2cbccef36ca04d5a260600d29.webp?size=240")
    embed.add_field(name="Rank", value="\n".join(rank), inline = True)
    embed.add_field(name="Name", value="\n ".join(names), inline=True)
    embed.add_field(name="Elo", value="\n".join(elo), inline=True)
    return(embed)


#For Tews II

#gets list of tews II members ID
def get_clan2():
    response = requests.get("https://brawlhalla.fly.dev/v1/utils/clan?clan_id=1374400")
    json_data = json.loads(response.text)
    clanlist = json_data["data"]["clan"]
    memberlist = []
    for x in range(len(clanlist)):
        members = clanlist[x]["brawlhalla_id"]
        memberlist.append(members)
    return(memberlist)

    

#Tews ID: 527406
#Tews II ID: 1374400

#Gets elo of a given brawlhalla ID(idk why I have it twice LMAO)
def get_rank2():
    member_id = get_clan2()
    memberlist = []
    # response = requests.get("https://brawlhalla-api.herokuapp.com/v1/ranked/id?brawlhalla_id=" + str(member_id[9]))
    # json_data = json.loads(response.text)
    # elo = json_data["data"]["brawlhalla_id"]
    # name = json_data["data"]["name"]
    # memberlist.append(tuple((name, elo)))
    for x in range(len(member_id)):
        try:
            response = requests.get("https://brawlhalla.fly.dev/v1/ranked/id?brawlhalla_id=" + str(member_id[x]))
            json_data = json.loads(response.text)
            elo = json_data["data"]["rating"]
            name = json_data["data"]["name"]
            memberlist.append(tuple((name, elo)))
        except Exception as error:
            print(error)
    return(memberlist)

#For the embedded format on discord
def get_embed():
    embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0x7289DA)
    embed.set_author(name="Tewsrankbot", url="https://twitter.com/RealDrewData", icon_url="https://pbs.twimg.com/profile_images/1327036716226646017/ZuaMDdtm_400x400.jpg")
    embed.set_thumbnail(url="https://i.imgur.com/axLm3p6.jpeg")
    embed.add_field(name="Tews Leadeboard" ,value="uh", inline=False)
    embed.add_field(name="Name", value="This is the value for field 1.\n This is an inline field.", inline=True)
    embed.add_field(name="Elo", value="This is the value for field 1. This is an inline field.", inline=True)
    return(embed)

#Gets  the elo ratings of all members of Tews II
def get_leaderboard2():
    members = get_rank2()
    members.sort(key=lambda x:x[1], reverse=True)
    names = [x[0] for x in members]
    elo = [str(x[1]) for x in members]
    numbers = list(range(1, len(members)+1))
    rank = [str(x) for x in numbers]
    embed=discord.Embed(title="Tews Leadboard", color=0x7289DA)
    embed.set_author(name="TewsRankBot", icon_url="https://cdn.discordapp.com/icons/160098918032605184/b3a614d2cbccef36ca04d5a260600d29.webp?size=240")
    embed.set_thumbnail(url="https://cdn.discordapp.com/icons/160098918032605184/b3a614d2cbccef36ca04d5a260600d29.webp?size=240")
    embed.add_field(name="Rank", value="\n".join(rank), inline = True)
    embed.add_field(name="Name", value="\n ".join(names), inline=True)
    embed.add_field(name="Elo", value="\n".join(elo), inline=True)
    return(embed)



#Prints after bot is ready for usage
@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


# @client.command()
# async def embed(ctx):
#     embed=discord.Embed(title="Sample Embed", url="https://realdrewdata.medium.com/", description="This is an embed that will show how to build an embed and the different components", color=0xFF5733)
#     await ctx.send(embed=embed)



#Defines the message commands to be used in discord
@bot.command()
async def first(message):
    embed = get_leaderboard()
    await message.channel.send(embed=embed)


@bot.command()
async def second(message):
    embed = get_leaderboard2()
    await message.channel.send(embed=embed)
    

# async def my_background_task():
#     while not client.is_closed():
#         embed = get_leaderboard()
#         msg = await message.channel.send(embed=embed)
#         message = await client.get_channel(msg.channel.id).fetch_message(msg.id)
#         newEmbed = get_leaderboard()
#         await message.edit(embed = newEmbed)
#         #await asyncio.sleep(30)

#bg_task = client.loop.create_task(my_background_task())






# get token from .env file
token = os.getenv('dc')

bot.run(token)
