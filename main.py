from discord import channel
from discord.embeds import Embed
import discord
from discord.ext import *
import os
import random
import string
from discord.ext import commands
from dotenv import load_dotenv
from discord.ext import commands
import requests
import sys
import threading
from discord.utils import get
import discord
import asyncio
from threading import Thread
import re
import tracemalloc
from fake_useragent import UserAgent
tracemalloc.start()


#
#
#   OXYTOOL FOLLOW BOT 
#   PLEASE DON'T SHARE ON YOUTUBE CONVINCING PEOPLE THAT IT IS YOURS :]
#
#

# 1 if token random from txt 2 if token normal from txt
typex = 2

#prefx
prefxx = "."
#token
token = ""
#roles
x1 = "basic"
x2 = "vip"
x3 = "megavip"
x4 = "ultravip"
#gen channel
genchannel = 895278697077153873





load_dotenv()
bot = commands.Bot(command_prefix=prefxx, help_command=None)

def init():
    loop = asyncio.get_event_loop()
    loop.create_task(bot.run(token))
    Thread(target=loop.run_forever).start()


@bot.command()
async def tfollow(ctx, arg):
    if ctx.channel.id == genchannel:
        
        
        role1 = discord.utils.get(ctx.guild.roles, name=x2)
        role2 = discord.utils.get(ctx.guild.roles, name=x3)
        role3 = discord.utils.get(ctx.guild.roles, name=x4)
        
        follow_count = 50
        
        if role1 in ctx.author.roles:
            follow_count = follow_count + 100
        elif role2 in ctx.author.roles:
            follow_count = follow_count + 200
        elif role3 in ctx.author.roles:
            follow_count = follow_count + 400
            
            

        embed=discord.Embed()
        embed.add_field(name=f"TWITCH FOLLOWS", value=f"Adding: ```{follow_count}``` follows to: ```{arg}``` ", inline=False)
        await ctx.send(embed=embed)



        def follow():
            
            if typex == 2:
                
                class tokens:
                    tokens = ''
                
                tokens.tokens = open('token.txt', 'r').read()
                
                
                
                for i in range(follow_count):
                    
                    token = tokens.tokens.partition('\n')[0]
                    tokens.tokens = sansfirstline = '\n'.join(tokens.tokens.split('\n')[1:])
                    
                    
                    ua = UserAgent()
                    userAgent = ua.random

                    headers = {
                    'Client-ID': "ymd9sjdyrpi8kz8zfxkdf5du04m649",
                    "Authorization": "OAuth wukbrnwp5f6uo4barxkzfpkacyugob",
                    'Accept': 'application/vnd.twitchtv.v5+json'
                        }

                    url = f"https://api.twitch.tv/kraken/users?login={arg}"
                    response = requests.get(url, headers=headers )


                    start = response.text.find('_id":"') + 6
                    end = response.text.find('",', start)
                    id = response.text[start:end]
                    print(id)
                    user_agent = userAgent
                    payload = '[{\"operationName\":\"FollowButton_FollowUser\",\"variables\":{\"input\":{\"disableNotifications\":false,\"targetID\":\"%s\"}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"51956f0c469f54e60211ea4e6a34b597d45c1c37b9664d4b62096a1ac03be9e6\"}}}]' % id
                    url = 'https://gql.twitch.tv/gql'
                    headers = {
                    "Authorization": f"OAuth {token}",
                    "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                    "Content-Type": "application/json"
                            }
                    print(requests.post(url, data=payload, headers=headers).text)

            elif typex == 1:

                for i in range(follow_count):
                
                    lines = open('token.txt').read().splitlines()
                    token =random.choice(lines)

                    ua = UserAgent()
                    userAgent = ua.random
                    
                    headers = {
                    'Client-ID': "ymd9sjdyrpi8kz8zfxkdf5du04m649",
                    "Authorization": "OAuth wukbrnwp5f6uo4barxkzfpkacyugob",
                    'Accept': 'application/vnd.twitchtv.v5+json'
                        }

                    url = f"https://api.twitch.tv/kraken/users?login={arg}"
                    response = requests.get(url, headers=headers )

                    start = response.text.find('_id":"') + 6
                    end = response.text.find('",', start)
                    id = response.text[start:end]
                    print(id)
                    user_agent = userAgent
                    payload = '[{\"operationName\":\"FollowButton_FollowUser\",\"variables\":{\"input\":{\"disableNotifications\":false,\"targetID\":\"%s\"}},\"extensions\":{\"persistedQuery\":{\"version\":1,\"sha256Hash\":\"51956f0c469f54e60211ea4e6a34b597d45c1c37b9664d4b62096a1ac03be9e6\"}}}]' % id
                    url = 'https://gql.twitch.tv/gql'
                    headers = {
                    "Authorization": f"OAuth {token}",
                    "Client-Id": 'kimne78kx3ncx6brgo4mv6wki5h1ko',
                    "Content-Type": "application/json"
                            }
                    print(requests.post(url, data=payload, headers=headers).text)

                
        threading.Thread(target=follow).start()

    
  
    else:
        embed=discord.Embed(title="WARNING", description=f"Commands are only allowed on {genchannel}")
        await ctx.send(embed=embed)
        return
        
        
@bot.command()
async def help(ctx):
    embed=discord.Embed(title="Help", description=f"""```.tfollow <user>``` twitch follows
```.help```help command""")
    await ctx.send(embed=embed)
        
init()
