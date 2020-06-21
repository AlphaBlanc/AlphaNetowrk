import discord

client = discord.Client()


@bot.event
async def on_ready():
    print("로그인")
    print(bot.user.name) 
    print(bot.user.id)
    print("------------------")
    await bot.change_presence(game=discord.Game(name="서버주소: Alpha.minesv.kr", type=1))
@bot.event
@client.event
async def on_message(message):
    if message.content.startswith("!안녕"):
        await message.channel.send("안녕하세요")

access_token = os.environ["BOT_TOKEN"]
bot.run(access_token)
