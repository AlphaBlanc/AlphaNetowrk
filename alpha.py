import discord
from discord.ext import commands
import asyncio
import os

client = discord.Client()


@client.event
async def on_ready():
    print("로그인")
    print(bot.user.name) 
    print(bot.user.id)
    print("------------------")
    await bot.change_presence(game=discord.Game(name="서버주소: Alpha.minesv.kr", type=1))
    
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
