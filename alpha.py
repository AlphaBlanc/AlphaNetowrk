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
access_token = os.environ["BOT_TOKEN"]
client.run('NjUwMzMxOTUwNTg1ODcyMzg1.Xu7_3w.7sxswYc05b14KNl5E4Qe2ZbQNbU')
