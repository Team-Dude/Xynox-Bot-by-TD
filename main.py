# Discord-Bot-Xynox
# Xynox is a discord bot used for fun activities, moderation tasks and much more
# Import Discord Package
from asyncio.exceptions import SendfileNotAvailableError
from re import I
import discord
import random
import requests
import keep_alive
import json
import asyncpraw
import praw
import json
import sys
import datetime
import os
import dotenv
import environ
from colorama import Fore
from TextToOwO.owo import text_to_owo
from os import name, path, system
import time
from datetime import date
import urllib
from discord import player
from discord import colour
from discord.embeds import Embed
import youtube_dl
from bs4 import BeautifulSoup
from discord.utils import get
import asyncio
import datetime
import pymongo
from pymongo import MongoClient
from random import choice
import aiohttp
import traceback
from PIL import Image
from io import BytesIO
from discord import user
from discord.client import Client
from discord.flags import Intents
from random import choice
from discord import channel
from discord import message
from discord import activity
from discord import member
from discord.activity import Activity, Streaming
from discord.colour import Color
from discord.enums import ActivityType, Status
from discord.ext import commands
from ttt import *
from discord.ext.commands.cooldowns import BucketType
from discord_components import *
from discord_buttons_plugin import *
from discord import Client
from discord.ext.commands import context
# import cogs._json



intents = discord.Intents.all()
intents.members = True

my_secret = os.environ['TOKEN']
my_prefix = os.environ['prefix']


queues = {}

def check_queue(ctx, id):
    if queues[id] != []:
        voice = ctx.guild.voice_client
        source = queues[id].pop(0)
        player = voice.play(source)

# #Defining Get prefix
# def get_prefix(client, message):
#     data = cogs._json.read_json('prefixes')
#     if not str(message.guild.id) in data:
#         return commands.when_mentioned_or('%')(client, message)
#     return commands.when_mentioned_or(data[str(message.guild.id)])(client, message)




#Client (Xynox)
client = commands.Bot(command_prefix = '%' ,owner_id = 411735063227793410,intents = discord.Intents.all())
client.DEFAULT_PREFIX = my_prefix
DiscordComponents(client)
buttons = ButtonsClient(client)
client.remove_command("help")




#Ready
@client.event
async def on_ready():
  while 1:
        urllib.request.urlopen("https://Xynox-py.commandozgaming.repl.co")
        await asyncio.sleep(500)

#Welcome
@client.event
async def on_member_join(member):
  embed=discord.Embed(title='Welcome To Our Server',description=f'Hey {ctx.author.mention}, We hope you have a great time here. Make sure to read the rules-and-info and if you have any questions or need some help, just ask our moderators.\n\tThank you for joining us!',color = 0x00ffff)
  await member.send(embed=embed)


# @client.event
# async def on_message(message):
#     #Ignore messages sent by yourself
#     if message.author.id == client.user.id:
#         return


#     #Whenever the bot is tagged, respond with its prefix
#     if f"<@!{client.user.id}>" in message.content:
#         data = cogs._json.read_json('prefixes')
#         if str(message.guild.id) in data:
#             prefix = data[str(message.guild.id)]
#         else:
#             prefix = '%'
#         prefixMsg = await message.channel.send(f"My prefix here is `{prefix}`")
#         await prefixMsg.add_reaction('👀')

#     await client.process_commands(message)


  


#ERRORS
@client.event
async def on_command_error(ctx, error):
  if isinstance(error, commands.NSFWChannelRequired):
    embed= discord.Embed(title='I Caught A PERVERT!!!', description="❌💦 This Command Works In NSFW Channel", color=0xccffff)
    embed.set_image(url ='https://media0.giphy.com/media/W5C9c8nqoaDJWh34i6/giphy.gif' )
    await ctx.send(embed=embed)
  if isinstance(error, commands.CommandNotFound):
    embed= discord.Embed(title='ERROR!!!', description="❌ This Command Doesn't Exist.. lol", color=0x00ffcc)
    await ctx.send(embed=embed)
  if isinstance(error, commands.MissingRequiredArgument):
    embed= discord.Embed(title='Dumb!!', description="❌ Bruh..! Mention Someone Or write its ID", color=0xffff66)
    embed.set_image(url ='https://cdn.discordapp.com/attachments/891653685984247818/893580629441146880/image_2021-10-01_235104.png_1.png' )
    await ctx.reply(embed=embed)
  if isinstance(error, commands.CommandOnCooldown):
    embed = discord.Embed(title=f"Slow it down bro!",description=f"❌Try again in {error.retry_after:.2f}s.", color=0xccff9f)
    await ctx.reply(embed=embed)



@client.command(pass_context=True)
@commands.cooldown(1, 10,commands.BucketType.guild)
async def credits(ctx):
  embed = discord.Embed(title='Xynox Credits',description='\n',color=0x1a1a1a)
  embed.add_field(name='Bot Development',value='Qari_Sahab#8077\n\t\t\t\n [click here](https://bit.ly/2ZYG35g)')
  embed.add_field(name='Web Development',value='DexSter#2080')
  embed.set_image(url='https://media.discordapp.net/attachments/756117986586263572/898602415945842688/Untitled_1.png?width=436&height=436')
  embed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

  await ctx.send(embed=embed)



@client.command(pass_context=True)
@commands.is_owner()
async def servers(ctx):
  servers = list(client.guilds)
  await ctx.send(f"Connected on {str((servers))} servers:")
  await ctx.send('\n'.join(guild.name for guild in guilds))

@client.command()
@commands.cooldown(1, 20,commands.BucketType.guild)
async def nitro(ctx, member: discord.Member = None):
  if member == None:
    member = ctx.author

  embed = discord.Embed(title = "**You've been gifted a subscription!**", 
                        description = f"||**{member.mention}**|| has been gifted Nitro for **1 month!**",
                        color = 0xc17ce0)

  embed.set_image(url = 'https://media.threatpost.com/wp-content/uploads/sites/103/2021/04/19145523/Discord-Nitro-e1618858537976.png' )



  await buttons.send(
    content = None,
    embed = embed,
    channel = ctx.channel.id,
    components = [
      ActionRow([
        Button(
          style = ButtonType().Link,
          label = "Accept",
          url = "https://youtu.be/dQw4w9WgXcQ"
        )
      ])
    ]
  )



#fast type game
@client.command(name='type',aliases=['typing','ty','tp'])
async def type(ctx):

    url = "https://linguatools-sentence-generating.p.rapidapi.com/realise"

    querystring = {"object":"thief","subject":"police","verb":"arrest"}

    headers = {
        'x-rapidapi-host': "linguatools-sentence-generating.p.rapidapi.com",
        'x-rapidapi-key': "2e052e1015mshb9e9027e2def188p17d478jsn0c14295263a3"
        }

    response = requests.request("GET", url, headers=headers, params=querystring)

    print(response.text)


    answers = ['The secret ingredient to his wonderful life was crime',"The irony of the situation wasn't lost on anyone in the room",'Check back tomorrow; I will see if the book has arrived','A kangaroo is really just a rabbit on steroids',"That is an appealing treasure map that I can't read","I am happy to take your donation; any amount will be greatly appreciated","The quick brown fox jumped over the lazy dog",'Gwen had her best sleep ever on her new bed of nails','Just a nice little test']


    starttime = time.time()
    answer = random.choice(answers)
    timer = random.randint(13,18)
    await ctx.send(f"You have **{timer}** seconds to type:\n\t ```{answer}```")

    def is_correct(msg):
        return msg.author==ctx.author

    try:
        guess = await client.wait_for('message', check=is_correct, timeout=timer)
    except asyncio.TimeoutError:
        return await ctx.send("You took too long :(")

    if guess.content == answer:
        await ctx.send("You got it!")
        fintime = time.time()
        total = fintime - starttime
        round_total = round(total)
        if round_total == timer - 1 : 
          await ctx.send(f"{round_total} seconds. **Sheesh That was close!!**")
        elif round_total == 1 :
          await ctx.send(f"{round_total} seconds.**Stop Copy Pasting Idiot!!**")
        elif round_total == 2 :
          await ctx.send(f"{round_total} seconds.**Stop Copy Pasting Idiot!!**")
        elif round_total == 3 :
          await ctx.send(f"{round_total} seconds.**Stop Copy Pasting Idiot!!**")
        elif round_total == 4 :
          await ctx.send(f"{round_total} seconds.**Stop Copy Pasting Idiot!!**")
        elif round_total == 5 :
          await ctx.send(f"{round_total} seconds.**Stop Copy Pasting Idiot!!**")
        else:
          await ctx.send(f"{round_total} seconds.")

    else:
        await ctx.send("Nope, that wasn't really right")
        fintime = time.time()
        total = fintime - starttime
        await ctx.send(f"{round(total)} seconds")






#USERINFO

@client.command()
async def userinfo(ctx, member: discord.Member = None):
    member  =ctx.author if not member else member
    roles = [role for role in member.roles]


    myEmbed = discord.Embed(color=0xff66ff, timestamp=ctx.message.created_at)
    myEmbed.set_author(name=f"User Info - {member}")
    myEmbed.set_thumbnail(url=member.avatar_url)
    myEmbed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)

    myEmbed.add_field(name="ID:",value=member.id, inline=True)
    myEmbed.add_field(name="NICKNAME:",value=member.display_name, inline=True)

    myEmbed.add_field(name="Created At:", value=member.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)
    myEmbed.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline=True)

    myEmbed.add_field(name=f"Roles ({len(roles)})", value=" ".join([role.mention for role in roles]), inline=True)
    myEmbed.add_field(name="Top Role", value=member.top_role.mention, inline=True)

    myEmbed.add_field(name="Bot?", value=member.bot, inline=True)

    await ctx.send(embed=myEmbed)



@client.command(name='wanted')
async def wanted(ctx,member: discord.Member=None):
  if member == None:
      member = ctx.author

  wanted = Image.open("wanted.jpg")

  asset = member.avatar_url_as(size=128)
  data = BytesIO(await asset.read())
  pfp= Image.open(data)

  pfp=pfp.resize((256,254))
  wanted.paste(pfp,(96,199))

  wanted.save("profile.jpg")
  await ctx.send(file= discord.File("profile.jpg"))
  


#tweet
@client.command()
async def tweet(ctx, username: str, *, message: str):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(f"https://nekobot.xyz/api/imagegen?type=tweet&username={username}&text={message}") as r:
            res = await r.json()
            em = discord.Embed()
            em.set_image(url=res["message"])
            await ctx.send(embed=em)



#Waifu commands

@client.command(name='waifu')
async def waifu(ctx,member:discord.Member=None):
  if member == None:
      member = ctx.author

  n = random.randrange(1,100)
  myEmbed = discord.Embed(title='Waifu Rating <:aquacry:889856822645764116>', color=0x9966ff)
  myEmbed.add_field(name=f'{member} Are {n}/100% Waifu',value='\u200b')
  myEmbed.set_footer(text=f"Requested by Weebu {ctx.author}", icon_url=ctx.author.avatar_url)

  await ctx.message.channel.send(embed=myEmbed)



#MEME COMMAND
@client.command(name="meme")
async def meme(ctx, subred="memes"): # default subreddit is memes, later in the command you can select one of your choice (example: !meme python --> chooses r/python reddit post)
    # msg = await ctx.send('Loading ...')

    reddit = asyncpraw.Reddit(client_id='1Er4dSJP7SvumGvOWOZ9NQ',
                              client_secret='LE41WBG2879uXkO42hoPVTOUZV97iQ',
                              username='EnvironmentalMilk448',
                              password='Commandoz123',
                              user_agent='Tutorial Bot :D')

    subreddit = await reddit.subreddit(subred)
    all_subs = []
    top = subreddit.hot(limit=100) # will choose between the top 50 memes

    async for submission in top:
        all_subs.append(submission)

    random_sub = random.choice(all_subs)

    name = random_sub.title
    url = random_sub.url

    # embed = Embed(title=f'__{name}__', colour=discord.Colour.random(), timestamp=ctx.message.created_at, url=url)

    # embed.set_image(url=url)
    # embed.set_author(name=ctx.message.author, icon_url=ctx.author.avatar_url)
    # embed.set_footer(text=f'Requested By {ctx.author}')
    # await ctx.send(embed=embed)
    await ctx.send(url)
    # await msg.edit('Here') # < and > remove the embed link
    # return


@client.command()
async def weather(ctx, *, city):
    weather_key = os.environ['weather key']
    if city == None:
      city = 'lahore'
    if weather_key == '':
        print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}Weather API key has not been set in the config.json file"+Fore.RESET)
    else:
        try:
            req = requests.get(f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={weather_key}')
            r = req.json()
            temperature = round(float(r["main"]["temp"]) - 273.15, 1)
            lowest = round(float(r["main"]["temp_min"]) - 273.15, 1)
            highest = round(float(r["main"]["temp_max"]) - 273.15, 1)
            weather = r["weather"][0]["main"]
            humidity = round(float(r["main"]["humidity"]), 1)
            wind_speed = round(float(r["wind"]["speed"]), 1)
            clouds = r["clouds"]["all"]
            em = discord.Embed(description=f'''
            Temperature: `{temperature}`
            Lowest: `{lowest}`
            Highest: `{highest}`
            Weather: `{weather}`
            Humidity: `{humidity}`
            Wind Speed: `{wind_speed}`
            ||Clouds:|| ||`{clouds}`||
            ''')
            em.add_field(name='City', value=city.capitalize())
            em.set_thumbnail(url='https://ak0.picdn.net/shutterstock/videos/1019313310/thumb/1.jpg')
            try:
                await ctx.send(embed=em)
            except:
                await ctx.send(f'''
                Temperature: {temperature}
                Lowest: {lowest}
                Highest: {highest}
                Weather: {weather}
                Humidity: {humidity}
                Wind Speed: {wind_speed}
                City: {city.capitalize()}
                ''')    
        except KeyError:
            await ctx.send(f"[ERROR]: {Fore.YELLOW}{city} Is not a real city"+Fore.RESET)
        else:
            print(f"{Fore.RED}[ERROR]: {Fore.YELLOW}{req.text}"+Fore.RESET)


@client.command(aliases=['mypp', 'sizepp','ppsize','pp','PP'])
async def PPSize(ctx):
      responses2 = ['Your PP is 2cm. 8==D',
                    'Your PP is 38cm. 8===========D',
                    'Your PP is 0cm. 8=D',
                    "Your PP is too small to be measured.'-' ",
                    'Your PP is -16cm. 🙃',
                    'Your PP is bigger than ur height. 🍆',
                    'I can not even see your PP mate. 👀',
                    'Your PP is 6cm.  8====D',
                    'Your PP is 9cm.  8======D',
                    'Your PP is 13cm.  8========D',
                    "Wait,You Even Have A PP?  O-O"]
      answer = random.choice(responses2)
      pp = discord.Embed(title='PP Size Activated!',color = 0x000000)
      pp.add_field(name='Measuring your PP... Please wait!',value=f'{answer}',inline = True)
      await ctx.channel.send(embed=pp)

@client.command(pass_context=True)
async def best(ctx):
    try:
        await ctx.send((choice(tuple(member.mention for member in ctx.guild.members if not member.bot and member!=ctx.author))) + " Is The Best User")
    except IndexError:
        await ctx.send("You are the only human member on it!")



@client.command(aliases=['gayrate'])
async def gay(ctx,member:discord.Member=None):
  if member == None:
    member = ctx.author.mention

  n = random.randrange(1,100)
  nr = n/1.17
  if nr>25 and nr<50:
    emoji = '<:what:930426250063913000>'
  elif nr>=50 and nr<75:
    emoji = "👀"
  elif nr<=25 and nr>0:
    emoji  =" "
  else:
    emoji = "<:gey:930436712939806780>"
  myEmbed = discord.Embed(title='Gay Meter 🏳️‍🌈', color=0x9966ff)
  myEmbed.add_field(name='Y U Gae...',value=f'{member} is {nr:.2f}% gay {emoji} ',inline=True)
  myEmbed.set_footer(text=f"Requested by Pervert {ctx.author}", icon_url=ctx.author.avatar_url)

  await ctx.message.channel.send(embed=myEmbed)

                                        
                                        
#WYR 
async def web_scrape(text):
  async with aiohttp.ClientSession() as session:
    async with session.get(text) as r:
      status = r.status
      if status == 200:
        text =await r.text()
      return text


@client.command(aliases=['wyr','rather'])
@commands.cooldown(1, 7)   
async def wouldyourather(ctx):
  text = await web_scrape("https://either.io/")
  soup = BeautifulSoup(text, 'lxml')
  l=[]
  for choice in soup.find_all("span",{"class":"option-text"}):
    l.append(choice.text)
  
  embed= discord.Embed(title='Would You Rather', url='https://either.io/',icon_url=client.user.avatar_url,color=0xba3ca6)
  embed.add_field(name='EITHER...',value=f":regional_indicator_a: {l[0]}",inline=False)
  embed.add_field(name='OR...',value=f":regional_indicator_b: {l[1]}")
  msg = await ctx.send(embed=embed)
  await msg.add_reaction("🇦")
  await msg.add_reaction("🇧")


#TICTACTOE
@client.command(aliases=['ttt','create'], pass_context=True)
async def TicTacToe(ctx):
    await ticTacToe(ctx, client)

              
             
              


#ANIMAL PICS

#CAT PICS
@client.command(aliases=['CAT','cats','CATS'])
async def cat(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/cat')
      catjson = await request.json()
# get the fact request
      request2 = await session.get('https://some-random-api.ml/facts/cat')
      factjson = await request2.json()

   embed = discord.Embed(title="MEOW! 🐱", color=discord.Color.purple())
   embed.set_image(url=catjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)


#DOG PICS
@client.command(aliases=['DOG','DOGS','dogs'])
async def dog(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/dog')
      dogjson = await request.json()
# get the fact request
      request2 = await session.get('https://some-random-api.ml/facts/dog')
      factjson = await request2.json()

   embed = discord.Embed(title="WOOF! 🐶", color=0x996600)
   embed.set_image(url=dogjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)


#FOX PICS
@client.command(aliases=['FOX','foxes','FOXES'])
async def fox(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/fox')
      foxjson = await request.json()
# get the fact request
      request2 = await session.get('https://some-random-api.ml/facts/fox')
      factjson = await request2.json()

   embed = discord.Embed(title="YEET! 🦊", color=discord.Color.orange())
   embed.set_image(url=foxjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)


#BIRD PICS
@client.command(aliases=['BIRD','birds','BIRDS'])
async def bird(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/bird')
      birdjson = await request.json()
# get the fact request
      request2 = await session.get('https://some-random-api.ml/facts/bird')
      factjson = await request2.json()

   embed = discord.Embed(title="CHIRP 🐦", color=discord.Color.red())
   embed.set_image(url=birdjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)

#KANGAROO PICS
@client.command()
async def kan(ctx):
   async with aiohttp.ClientSession() as session:
      request = await session.get('https://some-random-api.ml/img/kangaroo')
      kanjson = await request.json()
# get the fact request
      request2 = await session.get('https://some-random-api.ml/facts/kangaroo')
      factjson = await request2.json()

   embed = discord.Embed(title="POOP", color=discord.Color.purple())
   embed.set_image(url=kanjson['link'])
   embed.set_footer(text=factjson['fact'])
   await ctx.send(embed=embed)



  
#RPS
@client.command()
async def rps(ctx, message):
    answer =  message.lower()
    choices = ['rock', 'paper', 'scissors']
    computers_answer = random.choice(choices)
    if answer not in choices:
        await ctx.send("This is not a valid option! Plz Select The Following Options: rock, paper, scissors")
        return
    else:
        if computers_answer == answer:
            await ctx.send(f'Tie! We Both Picked {answer}')
        if computers_answer == 'rock':
            if answer == 'paper':
                await ctx.send(f'**SHIT!** You Win! I Picked {computers_answer} and You Picked {answer}')
        if computers_answer == 'rock':
            if answer == 'scissors':
                await ctx.send(f'**HAHA!** You Lose! I Picked {computers_answer} and You Picked {answer}')
        if computers_answer == 'paper':
            if answer == 'rock':
                await ctx.send(f'**HAHA!** You Lose! I Picked {computers_answer} and You Picked {answer}')
        if computers_answer == 'paper':
            if answer == 'scissors':
                await ctx.send(f'**SHIT!** You Win! I Picked {computers_answer} and You Picked {answer}')
        if computers_answer == 'scissors':
            if answer == 'rock':
                await ctx.send(f'**SHIT!** You Win! I Picked {computers_answer} and You Picked {answer}')
        if computers_answer == 'scissors':
            if answer == 'paper':
                await ctx.send(f'**HAHA!** You Lose! I Picked {computers_answer} and You Picked {answer}')


@client.command(aliases=['slots', 'bet', 'slotmachine'])
async def slot(ctx):
    emojis = "🍎🍊🍐🍋🍉🍇🍓🍒"
    a = random.choice(emojis)
    b = random.choice(emojis)
    c = random.choice(emojis)
    aw = "**Here Take A Cookie 🍪**","**Congrats Ur Life Purpose Has Been Fulfilled**","**Yayy! Ur Gf loves U Now**","**Nice Going Chad!**"
    bw = "**So Close Yet So Far!**","**Cool**","**Could Have done better**","**gg**","**GG**"
    cw = "**Suck My Dick Anyway**","**Faggot!!**","**What A Wimp!**","**Go Play Fortnite**","**'-'**"

    ar = random.choice(aw)
    br = random.choice(bw)
    cr = random.choice(cw)

    slotmachine = f"**[ {a} {b} {c} ]\n{ctx.author.name}**,"
    if a == b == c:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "**We Have A True Winner** ✨🎈🎉🎊", "description": f"{slotmachine} All matchings, you won!\n{ar}"}))
    elif (a == b) or (a == c) or (b == c):
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} 2 in a row, you won!\n{br}"}))
    else:
        await ctx.send(embed=discord.Embed.from_dict(
            {"title": "Slot machine", "description": f"{slotmachine} No match, you lost\n{cr}"}))




@client.command(pass_context=True,aliases = ['f'])
async def F(ctx, member:discord.Member = None):
        await ctx.send(f"{ctx.author.mention} Have Paid Respects")

@client.command(pass_context=True, aliases=['UWU'])
async def uwu(ctx, member: discord.Member=None):  
    await ctx.send('**UwU**')

@client.command(pass_context=True, aliases=['OWO'])
async def owo(ctx, member: discord.Member=None):  
    await ctx.send('OwO')  

@client.command(pass_context=True,aliases =['POOP'])
async def poop(ctx, member: discord.Member=None):  
    await ctx.send(
                   "░░░░░░▄▀▀▀▀░░░░░█▄▄░░░░""\n"   
                   "░░░░░░█░█░░░░░░░░░░▐░░░""\n"
                   "░░░░░░▐▐░░░░░░░░░▄░▐░░░""\n"
                   "░░░░░░█░░░░░░░░▄▀▀░▐░░░""\n"
                   "░░░░▄▀░░░░░░░░▐░▄▄▀░░░░""\n"
                   "░░▄▀░░░▐░░░░░█▄▀░▐░░░░░""\n"
                   "░░█░░░▐░░░░░░░░▄░█░░░░░""\n"
                   "░░░█▄░░▀▄░░░░▄▀▐░█░░░░░""\n"
                   "░░░█▐▀▀▀░▀▀▀▀░░▐░█░░░░░""\n"
                   "░░▐█▐▄░░▀░░░░░░▐░█▄▄░░░""\n"
                   "░░░▀▀▄░░░░░░░░▄▐▄▄▄▀░░░""\n")

    
@client.command(name='hy',aliases=['hi','hello'])
async def hy(ctx):
    responses = ['**Idiot** Why did you interrupted in my technical analysis?', '**Wassup!!!**', 'What labour do you want me to execute?','**Greetings User!**', '***NIGGA!,WHY TF YOU WOKE ME UP?***', "Yes My beautiful human being","" ]
    await ctx.send(choice(responses))

#Move to different vcs
@client.command(aliases=['vm'])
@commands.has_permissions(administrator=True)
async def voicemove(ctx, members:commands.Greedy[discord.Member], *, channel:discord.VoiceChannel):
  for member in members:
    await member.move_to(channel=channel)
    await ctx.send("**User Has Been Successfully Dragged**")



  
#Ping
@client.command(name='ping')
async def ping(ctx):
    await ctx.send(f'**🏓Pong!** {round(client.latency * 1000)}ms')

#Responses
@client.command(aliases=['8ball', 'test'])
async def eightball(ctx, *, question):
    responses = ['It is certain.',
                'It is decidedly so.',
                'Without a doubt.',
                'Yes - Definitely.',
                'As I see it, yes.',
                'Most likely.',
                'Yes.',
                'HAHA - are u kidding?.',
                'You dont wanna hear it.',
                'Cant tell you right now',
                'Cannot predict now',
                'Obviously',
                'Im Sorry',
                'My research says no',
                'Unfortunately! No!!!',
                'Very Doubtful',]
    await ctx.send( random.choice(responses))


class cricBot():
    @client.group(name='cric', invoke_without_command=True)
    async def cric(ctx):

        #COMMENTARY LINES AND VENUE
        cout = ['BOWLED EM!!','LBW shout and GONE!!','Up in the air andd TAKEN!!','Outside Edge GONE!!']
        cscore = ['Great shot!!','Classy Batting','Wonderful Timing of The Bat...']
        venue = ['Lords','Eden Gardens','Qadaffi','Wankede','Melbourne']

        rcout = random.choice(cout)
        rcscore = random.choice(cscore)
        rvenue = random.choice(venue)
        
        # EMBED SETTINGS
        embed_home = discord.Embed(
            title="Welcome to Cricket Match",
            description=f"{OPEN}",
            color = discord.Color.red()
        )

        embed_home.set_footer(text='**Get Ready For The Next Battle!**')
        embed_home.set_thumbnail(url="https://media.discordapp.net/attachments/617339888324575232/921011536099684392/xy.png?width=758&height=676")

        await ctx.send(embed=embed_home)

    @cric.command(name='play')
    async def play(ctx):

        # EMBED SETTINGS

        ## Creating embed templates for scorecard
        embed_score = discord.Embed(
            title='Scoreboard',
            description='Classy Shot!!',
            color=discord.Color.red()
        )

        
        embed_inning = discord.Embed(
            title='Scoreboard',
            description='INNINGS OVER!! Well Played. Have a look at innings scorecard below.',
            color=discord.Color.red()
        )

        embed_go = discord.Embed(
            title = 'Scoreboard', 
            color=discord.Color.red()
        )

        embed_start = discord.Embed(
            title = 'Game Start',
            description = f'Hello **{ctx.author}** 👋\n\nLet us begin with toss. Enter **"heads"** or **"tails"** as your choice for the toss.\n\nBest of luck!!!',
            color=discord.Color.red()
        )

        embed_sec_start = discord.Embed(
            title='SECOND INNINGS',
            description=f'{ctx.author} it is your time to rock the pitch with some cool bowling action. Let the **SECOND INNINGS** begin!!!' 
        )

        embed_toss_sys = discord.Embed(
            title='Scoreboard',
            description='**System** won the toss. System chooses to **bowl first**. Best of luck!!!\n\n*Enter any number from 1 to 6 to begin the match.*'
        )
        embed_toss_user_ch = discord.Embed(
            title='Scoreboard',
            description='You have won the toss!! What do you choose? Enter **bat** for batting first and **bowl** for bowling first.'
        )
        embed_toss_user = discord.Embed(
            title='Scoreboard',
            description=f'Well that sound a good choice. Best of luck!!\n\n*Enter any number from 1 to 6 to start*'
        )

        ## Setting embed footers
        embed_score.set_footer(text=f'Honorable Venues: Lords Cricket Stadium')
        embed_inning.set_footer(text=f'Venue: Eden Gardens Cricket Stadium')
        embed_go.set_footer(text=f'Honorable Venues: Qadaffi Cricket Stadium')
        embed_start.set_footer(text=f'Honorable Venues: Wankhede Cricket Stadium')
        embed_sec_start.set_footer(text=f'Honorable Venues: Melbourne Cricket Stadium')
        embed_toss_sys.set_footer(text=f'Honorable Venues: Oval Cricket Stadium')
        embed_toss_user_ch.set_footer(text=f'Honorable Venues: National Cricket Stadium')
        embed_toss_user.set_footer(text=f'Honorable Venues: Modi Cricket Stadium')        

        ## Setting embed thumbnails
        embed_score.set_thumbnail(url="https://media.discordapp.net/attachments/617339888324575232/921011536099684392/xy.png?width=758&height=676")
        embed_inning.set_thumbnail(url="https://media.discordapp.net/attachments/617339888324575232/921011536099684392/xy.png?width=758&height=676")
        embed_go.set_thumbnail(url="https://media.discordapp.net/attachments/617339888324575232/921011536099684392/xy.png?width=758&height=676")
        embed_start.set_thumbnail(url="https://media.discordapp.net/attachments/617339888324575232/921011536099684392/xy.png?width=758&height=676")
        embed_sec_start.set_thumbnail(url="https://media.discordapp.net/attachments/617339888324575232/921011536099684392/xy.png?width=758&height=676")
        embed_toss_sys.set_thumbnail(url="https://media.discordapp.net/attachments/617339888324575232/921011536099684392/xy.png?width=758&height=676")
        embed_toss_user_ch.set_thumbnail(url="https://media.discordapp.net/attachments/617339888324575232/921011536099684392/xy.png?width=758&height=676")
        embed_toss_user.set_thumbnail(url="https://media.discordapp.net/attachments/617339888324575232/921011536099684392/xy.png?width=758&height=676")

        # BOT SETTINGS
        ## Send start message at beginning
        await ctx.send(embed=embed_start)

        ## Setting variables
        run_cho = [1,2,3,4,5,6]
        toss_choice = ['heads', 'tails']
        user_score = 0
        user_wick = 0
        sys_score = 0
        sys_wick = 0
        sys_toss = random.choice(toss_choice)

        # Toss
        try:
            user_toss_ch = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

            if sys_toss != user_toss_ch:
                await ctx.send(embed=embed_toss_sys)

                # User batting

                while (user_wick != 1):
                    try:
                        bat_msg = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
                        sys_ch = random.choice(run_cho)

                        if int(bat_msg.content) < 1 or int(bat_msg.content) > 6: 
                            await ctx.send("Invalid input.")
                        
                        elif int(bat_msg.content) != sys_ch:
                            user_score = user_score + int(bat_msg.content)
                            await ctx.send(embed=embed_score)
                            await ctx.send(f'**{ctx.author.name} Score:** {user_score} ')
                            

                        elif int(bat_msg.content) == sys_ch:
                            user_wick = user_wick + 1
                            await ctx.send(f"OUT!!! BOWLED EM!!")

                    except asyncio.TimeoutError:
                        await ctx.send("Match Abandoned! You Left The Field LoL...")
                        break

                embed_inning.add_field(
                    name=f'{ctx.author} Score',
                    value=f'{user_score}'
                )
                embed_inning.add_field(
                    name="System Score",
                    value=f'{sys_score}'
                )
                await ctx.send(embed=embed_inning)
                await ctx.send(embed=embed_sec_start)

                # System batting

                while (sys_wick != 1) and (sys_score <= user_score):
                    try:
                        bowl_msg = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)  
                        sys_ch = random.choice(run_cho)      
                    
                        if int(bowl_msg.content) < 1 or int(bowl_msg.content) > 6:
                            await ctx.send("Invalid input.")
                        
                        elif int(bowl_msg.content) != sys_ch:
                            sys_score = sys_score + sys_ch
                            await ctx.send(embed=embed_score)
                            await ctx.send(f'**System score:** {sys_score}')
                        
                        elif int(bowl_msg.content) == sys_ch:
                            sys_wick = sys_wick + 1
                            await ctx.send(f"OUT!!! BOWLED EM!!")
                    
                    except asyncio.TimeoutError:
                        await ctx.send("Match Abandoned! You Left The Field LoL...")
                        break
                
                # Final scorecard if system wins

                if sys_score > user_score:

                    embed_go.add_field(name=f"{ctx.author} Score: ", value=f"{user_score}", inline=False)
                    embed_go.add_field(name="System Score: ", value=f"{sys_score}", inline=False)
                    embed_go.add_field(name="Result", value='What a game!! Well played both sides. However, today **Xynox** won the game.', inline=False)
                    await ctx.send(embed=embed_go)

                # Final scorecard if user wins

                elif sys_score < user_score:
                    embed_go.add_field(name=f"{ctx.author} Score: ", value=f"{user_score}")
                    embed_go.add_field(name="System Score: ", value=f"{sys_score}")
                    embed_go.add_field(name="Result", value=f'What a game!! Well played both sides. **{ctx.author}** won the game.', inline=False)
                    await ctx.send(embed=embed_go)
            
            elif sys_toss == (user_toss_ch):
                
                await ctx.send(embed=embed_toss_user_ch)
                user_ch_bb = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)

                if (user_ch_bb) == "bat":
                    
                    await ctx.send(embed=embed_toss_user)

                    # User batting

                    while (user_wick != 1):
                        try:
                            bat_msg = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
                            sys_ch = random.choice(run_cho)

                            if int(bat_msg.content) < 1 or int(bat_msg.content) > 6: 
                                await ctx.send("Invalid input.")
                            
                            elif int(bat_msg.content) != sys_ch:
                                user_score = user_score + int(bat_msg.content)
                                await ctx.send(embed=embed_score)
                                await ctx.send(f'**{ctx.author.name} Score:** {user_score}')

                            elif int(bat_msg.content) == sys_ch:
                                user_wick = user_wick + 1
                                await ctx.send(f"OUT!!! BOWLED EM!!")

                        except asyncio.TimeoutError:
                            await ctx.send("Match Abandoned! You Left The Field LoL...")
                            break

                    embed_inning.add_field(
                        name=f'{ctx.author} Score',
                        value=f'{user_score}'
                    )
                    embed_inning.add_field(
                        name="System Score",
                        value=f'{sys_score}'
                    )
                    await ctx.send(embed=embed_inning)
                    await ctx.send(embed=embed_sec_start)

                    # System batting

                    while (sys_wick != 1) and (sys_score <= user_score):
                        try:
                            bowl_msg = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)   
                            sys_ch = random.choice(run_cho)     
                        
                            if int(bowl_msg.content) < 1 or int(bowl_msg.content) > 6:
                                await ctx.send("Invalid input.")
                            
                            elif int(bowl_msg.content) != sys_ch:
                                sys_score = sys_score + sys_ch
                                await ctx.send(embed=embed_score)
                                await ctx.send(f'**System score:** {sys_score}')
                            
                            elif int(bowl_msg.content) == sys_ch:
                                sys_wick = sys_wick + 1
                                await ctx.send(f"OUT!!! BOWLED EM!!")
                        
                        except asyncio.TimeoutError:
                            await ctx.send("Match Abandoned! You Left The Field LoL...")
                            break
                    
                    # Final scorecard if system wins

                    if sys_score > user_score:

                        embed_go.add_field(name=f"{ctx.author} Score: ", value=f"{user_score}", inline=False)
                        embed_go.add_field(name="System Score: ", value=f"{sys_score}", inline=False)
                        embed_go.add_field(name="Result", value='What a game!! Well played both sides. However, today **system** won the game.', inline=False)
                        await ctx.send(embed=embed_go)

                    # Final scorecard if user wins

                    elif sys_score < user_score:
                        embed_go.add_field(name=f"{ctx.author} Score: ", value=f"{user_score}")
                        embed_go.add_field(name="System Score: ", value=f"{sys_score}")
                        embed_go.add_field(name="Result", value=f'What a game!! Well played both sides. **{ctx.author}** won the game.', inline=False)
                        await ctx.send(embed=embed_go)
                
                elif user_ch_bb == "bowl":

                    await ctx.send (embed=embed_toss_user)

                    # System batting

                    while (sys_wick != 1) and (sys_score <= user_score):
                        try:
                            bowl_msg = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
                            sys_ch = random.choice(run_cho)        
                        
                            if int(bowl_msg.content) < 1 or int(bowl_msg.content) > 6:
                                await ctx.send("Invalid input.")
                            
                            elif int(bowl_msg.content) != sys_ch:
                                sys_score = sys_score + sys_ch
                                await ctx.send(embed=embed_score)
                                await ctx.send(f'**System score:** {sys_score}')
                            
                            elif int(bowl_msg.content) == sys_ch:
                                sys_wick = sys_wick + 1
                                await ctx.send(f"OUT!!! BOWLED EM!!")
                        
                        except asyncio.TimeoutError:
                            await ctx.send("Match Abandoned! You Left The Field LoL...")
                            break

                    embed_inning.add_field(
                        name=f'{ctx.author} Score',
                        value=f'{user_score}'
                    )
                    embed_inning.add_field(
                        name="System Score",
                        value=f'{sys_score}'
                    )
                    await ctx.send(embed=embed_inning)
                    await ctx.send(embed=embed_sec_start)                

                    # User batting

                    while (user_wick != 1):
                        try:
                            bat_msg = await client.wait_for("message", timeout=15, check=lambda message: message.author == ctx.author and message.channel == ctx.channel)
                            sys_ch = random.choice(run_cho)

                            if int(bat_msg.content) < 1 or int(bat_msg.content) > 6: 
                                await ctx.send("Invalid input.")
                            
                            elif int(bat_msg.content) != sys_ch:
                                user_score = user_score + int(bat_msg.content)
                                await ctx.send(embed=embed_score)
                                await ctx.send(f'**{ctx.author.name} Score:** {user_score} ')

                            elif int(bat_msg.content) == sys_ch:
                                user_wick = user_wick + 1
                                await ctx.send("OUT!!! BOWLED EM!!!")

                        except asyncio.TimeoutError:
                            await ctx.send("Match Abandoned! You Left The Field LoL...")
                            break
                    
                    # Final scorecard if system wins

                    if sys_score > user_score:

                        embed_go.add_field(name=f"{ctx.author} Score: ", value=f"{user_score}", inline=False)
                        embed_go.add_field(name="System Score: ", value=f"{sys_score}", inline=False)
                        embed_go.add_field(name="Result", value='What a game!! Well played both sides. However, today **system** won the game.', inline=False)
                        await ctx.send(embed=embed_go)

                    # Final scorecard if user wins

                    elif sys_score < user_score:
                        embed_go.add_field(name=f"{ctx.author} Score: ", value=f"{user_score}")
                        embed_go.add_field(name="System Score: ", value=f"{sys_score}")
                        embed_go.add_field(name="Result", value=f'What a game!! Well played both sides. **{ctx.author}** won the game.', inline=False)
                        await ctx.send(embed=embed_go)

        except asyncio.TimeoutError:
            await ctx.send("Match Abandoned! You Left The Field LoL...")   


@client.command(aliases=['purge'])
@commands.cooldown(1, 5,commands.BucketType.guild)
@commands.has_permissions(manage_messages = True)
async def clear(ctx, amount=2):
    await ctx.channel.purge(limit=amount+1)


#Kick/Ban/Unban
@client.command(name='kick')
@commands.has_permissions(kick_members=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    await member.kick(reason=reason)
    await member.send('You Have Been Kicked From The Server Because:'+reason)


@client.command(name='ban')
@commands.has_permissions(ban_members=True)
async def ban(ctx, member : discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'{member.mention} has been banned')


@client.command(name='unban')
@commands.has_permissions(ban_members=True)
async def unban(ctx,*,member):
    banned_users = await ctx.guild.bans()
    member_name, member_disc = member.split('#')

    for banned_entry in banned_users:
        user = banned_entry.user

        if (user.name, user.discriminator)==(member_name,member_disc):

            await ctx.guild.unban(user)
            await ctx.send(member_name +" has been unbanned!")
            return

    await ctx.send(member+"was not found")


@client.command(name='mute')
async def version(context):
    myEmbed = discord.Embed(title="Oh No!",description='**This Command is under construction,plz bear with us and use other commands**', color=0x000000)
    myEmbed.set_image(url='https://i.imgur.com/JDNYg87.png')
    await context.message.channel.send(embed=myEmbed)

@client.command(name='unmute')
async def version(context):
    myEmbed = discord.Embed(title="Oh No!",description='**This Command is under construction,plz bear with us and use other commands**', color=0x000000)
    myEmbed.set_image(url='https://i.imgur.com/JDNYg87.png')
    await context.message.channel.send(embed=myEmbed)


@client.listen()
async def on_message(message):
    if "tatti" in message.content.lower():
        await message.channel.send('Yummy 🤤')
        await client.process_commands(message)

@client.listen()
async def on_message(message):
    if message.content.startswith (f"<@!{client.user.id}>") and len(message.content) == len(f"<@!{client.user.id}>"):
        await message.channel.send(f'My Prefix for this server is `{my_prefix}`')
        await client.process_commands(message)





@client.command(pass_context=True,help='Hugs a user')
async def hug(ctx,*, member: discord.Member = None):
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://nekos.best/api/v1/hug')
      hugjson = await request.json()
    author_name = ctx.message.author.name
    embed = discord.Embed(title = '\n', description = f'{author_name} hugged {member.mention}', color = 0x009933)
    embed.set_image(url=hugjson["url"])
    await ctx.send(embed=embed)

@client.command(pass_context=True,help='slap a user')
async def slap(ctx,*, member: discord.Member = None):
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://nekos.best/api/v1/slap')
      slapjson = await request.json()
    author_name = ctx.message.author.name
    embed = discord.Embed(title = '\n', description = f'{author_name} slaped {member.mention}', color = 0x009933)
    embed.set_image(url=slapjson['url'])
    await ctx.send(embed=embed)

@client.command(pass_context=True,help='Kiss a user')
async def kiss(ctx,*, member: discord.Member = None):
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://nekos.best/api/v1/kiss')
      kissjson = await request.json()
    author_name = ctx.message.author.name
    embed = discord.Embed(title = '\n', description = f'{author_name} kissed 💋 {member.mention}', color = 0x009933)
    embed.set_image(url=kissjson['url'])
    await ctx.send(embed=embed)


@client.command(pass_context=True,help='Blushes')
async def blush(ctx,*, member: discord.Member = None):
    async with aiohttp.ClientSession() as session:
      request = await session.get('https://nekos.best/api/v1/blush')
      blushjson = await request.json()
    author_name = ctx.message.author.name
    embed = discord.Embed(title = '\n', description = f'{member.mention} blushed 😳', color = 0x009933)
    embed.set_image(url=blushjson['url'])
    await ctx.send(embed=embed)



#Change Custom Status

@client.event
async def on_ready():
        # Setting 'Playing' Status
        await client.change_presence(activity=discord.Game(name="on {len(client.guilds)} servers | $help"))

        # Setting 'Streaming' Status
        await client.change_presence(activity=discord.Streaming(name="My Stream", url="my_youtube_url"))

        # Setting 'Listening' Status
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.listening,name="Gangnam Style"))

        # Setting 'Watching' Status 
        await client.change_presence(activity=discord.Activity(type=discord.ActivityType.watching,name="over the mods"))

        print=("Ready")


async def change_presence():
    await client.wait_until_ready()

    statuses = ["Mario | %help", f"on {len(client.guilds)} servers | %help", "discord.py | %help"]

    while not client.is_closed():

        status = random.choice(statuses)

        await client.change_presence(activity=discord.Game(name=status))

        await asyncio.sleep(10)
client.loop.create_task(change_presence())




@client.command(name='server')
async def server(ctx):
        await ctx.send("https://discord.gg/GTvG7Txtg8")
        
        await client.process_commands(message)


@client.command(name='serverinfo')
async def serverinfo(ctx):
  role_count = len(ctx.guild.roles)
  bot_list = [bot.mention for bot in ctx.guild.members if bot.bot]


  myEmbed = discord.Embed(timestamp=ctx.message.created_at, color=0x00ffcc)
  myEmbed.add_field(name="Name", value=f"{ctx.guild.name}",inline=False)
  myEmbed.set_thumbnail(url = str(ctx.guild.icon_url))
  myEmbed.add_field(name="Member Count", value=ctx.guild.member_count,inline=True)
  myEmbed.add_field(name="Highest Role", value=ctx.guild.roles[-2],inline=True)
  myEmbed.add_field(name="Number Of Roles", value=str(role_count),inline=True)
  myEmbed.add_field(name="Server Name", value=ctx.guild.name, inline=True)
  myEmbed.add_field(name="Server ID", value=ctx.guild.id, inline=True)
  myEmbed.add_field(name="Region", value=ctx.guild.region, inline=True)
  myEmbed.set_footer(text=f"Requested by {ctx.author}", icon_url=ctx.author.avatar_url)
  



  await ctx.message.channel.send(embed=myEmbed)


@client.command(aliases=['ri', 'role'])
async def roleinfo(ctx, *, role: discord.Role): 
    guild = ctx.guild
    since_created = (ctx.message.created_at - role.created_at).days
    role_created = role.created_at.strftime("%d %b %Y %H:%M")
    created_on = "{} ({} days ago)".format(role_created, since_created)
    users = len([x for x in guild.members if role in x.roles])
    if str(role.colour) == "#000000":
        colour = "default"
        color = ("#%06x" % random.randint(0, 0xFFFFFF))
        color = int(colour[1:], 16)
    else:
        colour = str(role.colour).upper()
        color = role.colour
    em = discord.Embed(colour=color)
    em.set_author(name=f"Name: {role.name}"
    f"\nRole ID: {role.id}")
    em.add_field(name="Users", value=users)
    em.add_field(name="Mentionable", value=role.mentionable)
    em.add_field(name="Hoist", value=role.hoist)
    em.add_field(name="Position", value=role.position)
    em.add_field(name="Managed", value=role.managed)
    em.add_field(name="Colour", value=colour)
    em.add_field(name='Creation Date', value=created_on)
    await ctx.send(embed=em)


@client.command(name='help')
async def help(ctx):
  member=ctx.author
  print('done')
  titlemessage=f"Server Name:{ctx.guild.name}"
  embed=discord.Embed(title=titlemessage,description="Below is the list to help u in every aspect",color=0x3399ff)
  embed.add_field(name="About Xynox",value="[Commands List](https://basitshahidhamid.wixsite.com/xynox/commands)\n[Xynox Status](https://basitshahidhamid.wixsite.com/xynox/status)",inline=False)
  embed.add_field(name="Get Xynox",value="[Add Xynox to ur server](https://discord.com/api/oauth2/authorize?client_id=844450850503000114&permissions=3522685559&scope=bot)")
  embed.set_footer(text=f"Requested by {member}\nID = {member.id}",icon_url=ctx.author.avatar_url)


  await member.send(embed=embed)
  await ctx.send(f"Check your dms {member.mention}",delete_after=5)


keep_alive.keep_alive()


#COGS
@client.command()
@commands.is_owner()
async def load(ctx, extension):
  client.load_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def unload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')

@client.command()
@commands.is_owner()
async def reload(ctx, extension):
  client.unload_extension(f'cogs.{extension}')
  client.load_extension(f'cogs.{extension}')



for filename in os.listdir('./cogs'):
  if filename.endswith('.py'):
    client.load_extension(f'cogs.{filename[:-3]}')




# Run the client on the server
client.run(my_secret)


