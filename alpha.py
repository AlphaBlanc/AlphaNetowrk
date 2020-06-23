import discord
from discord.ext import commands
import asyncio
import pymysql
import os
import sqlite3

bot = commands.Bot(command_prefix='!')
client = discord.Client()

@client.event
async def on_ready():
    print("로그인")
    print(bot.user.name) 
    print(bot.user.id)
    print("------------------")
    await bot.change_presence(game=discord.Game(name="서버주소: Alpha.minesv.kr", type=1))
    
@client.event
hostver = os.environ["HOST_TOKEN"]
portver = os.environ["PORT_TOKEN"]
userver = os.environ["USER_TOKEN"]
passwdver = os.environ["PASSWD_TOKEN"]
dbver = os.environ["DB_TOKEN"]
CHANNEL_ID = os.environ["CHANNEL_TOKEN"]

async def on_message(message):
    if message.author.bot:
        return None
    if(message.content.split(" ")[0] == "!사전예약"):
        if message.channel.id == CHANNEL_ID:
            await message.delete()
            name = message.content.split("!사전예약 ")[1]
            await message.guild.get_channel(message.channel.category_id).set_permissions(message.guild.get_member(int(message.author.id)), send_messages=False)
            await message.author.send(embed=discord.Embed(title="AlphaNetwork", description = "정상적으로 사전예약에 참여하셨습니다.\n닉네임: " + name, color = 0x00ff00))
            await message.channel.send(embed=discord.Embed(title="AlphaNetwork", description = name + "님께서 사전예약에 참여하셨습니다.", color = 0x00ff00))

            db = pymysql.connect(host='(hostver)', port=(portver), user='(userver)', passwd='(passwdver)', db='(dbver)', charset='utf8')
            cursor = db.cursor()
            sql = "INSERT LIST(name) VALUES(%s);"
            val = ("" + name)
            cursor.execute(sql, val)
            db.commit()
            db.close()

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
