import discord
from discord.ext import commands
import asyncio
import os

client = discord.Client()


@bot.event
async def on_ready():
    print("로그인")
    print(bot.user.name) 
    print(bot.user.id)
    print("------------------")
    await bot.change_presence(game=discord.Game(name="서버주소: Alpha.minesv.kr", type=1))
@bot.event
async def on_message(message):
    if "검색" == message.content.split(" ")[0]:
        group = message.content.split(" ")[1]
        search = requests.get("https://www.google.com/search?hl=ko&biw=958&bih=959&tbm=isch&sa=1&ei=L5ZtXJ2aLpGSr7wPiKuC-A0&q="+group)
        bp = bs(search.text, "html.parser")
        img = bp.find_all('img')
        img2=img[2]
        img_src=img2.get('src')
        embed = discord.Embed(title="Erica:", description= "https://www.google.com/search?hl=ko&biw=958&bih=959&tbm=isch&sa=1&ei=L5ZtXJ2aLpGSr7wPiKuC-A0&q="+group, color=0x383b38)
        embed.set_footer(icon_url="https://www.google.com/search?hl=ko&biw=958&bih=959&tbm=isch&sa=1&ei=L5ZtXJ2aLpGSr7wPiKuC-A0&q="+group)
        embed.set_image(url=img_src)
        await bot.send_message(message.channel, embed=embed)
        del group, search, bp, img, embed

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
