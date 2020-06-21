import discord
from discord.ext import commands
import asyncio
import os

client = discord.Client()


@client.event
async def on_ready():

    await client.change_presence(status=discord.Status.online, activity=discord.Game("서버주소: Alpha.minesv.kr"))
    print("로그인!")
    
@client.event
async def on_message(message): # do action when message sent
    if message.author.bot: # if chatter is bot
        return None # do not react
    print(message.content)
    if message.content.startswith("!테스트"): # if user send message !명령어
        await message.channel.send("테스트 명령어!")

    if message.content.startswith("!넌누구니"):
        await message.channel.send("삐리리릭! 도우미봇이에요!")

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
