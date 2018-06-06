#Nanna Bot for Russian State Law
import discord
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
from random import randint
import os

bot = commands.Bot(command_prefix="?R ")

@bot.event
async def on_ready():
    print("Nanna bot online.")
    await bot.change_presence(game=discord.Game(name='With Stalin | `?R help`'))

@bot.command(pass_context=True)
async def ping(ctx):
    await bot.say("Hello there!")

@bot.command(pass_context=True)
async def server(ctx):
    embed = discord.Embed(title="This is the info of: {}!".format(ctx.message.server.name), description="The server info!", color=0x0000)
    embed.add_field(name="Name!", value=ctx.message.server.name, inline=True)
    embed.add_field(name="Members!", value=len(ctx.message.server.members), inline=True)
    embed.add_field(name="Roles!", value=len(ctx.message.server.roles), inline=True)
    embed.set_thumbnail(url=ctx.message.server.icon_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def info_embed(ctx, user: discord.Member):
    embed = discord.Embed(title="{}'s info".format(user.name), description="Found info!", color=0x0000)
    embed.add_field(name="Name", value=user.name, inline=True)
    embed.add_field(name="ID", value=user.id, inline=True)
    embed.add_field(name="Status", value=user.status, inline=True)
    embed.add_field(name="Highest role", value=user.top_role, inline=True)
    embed.add_field(name="Joined at", value=user.joined_at, inline=True)
    embed.set_thumbnail(url=user.avatar_url)
    await bot.say(embed=embed)

@bot.command(pass_context=True)
async def kick(ctx, user: discord.Member):
    await bot.say("The admins have deemed you unfit to serve, goodbye.")
    await bot.kick(user)

@bot.command(pass_context=True)
async def purge(ctx, number):
    number = int(number)
    if number > 99 or number < 1:
        await bot.say("I'm sorry, but I can only delete up to 99 messages and greater than one!")
    else:
        messages = []
        channel = ctx.message.channel
        async for x in bot.logs_from((channel), limit = number + 1):
            messages.append(x)
        await bot.delete_messages(messages)
        await bot.say("I have purged it!")

@bot.command(pass_context=True)
async def math(ctx, number1, number2):
    number1 = int(number1)
    number2 = int(number2)
    await bot.say(number1 + number2)
    await bot.say(number1 - number2)
    await bot.say(number1 * number2)
    await bot.say(number1 % number2)

@bot.command(pass_context=True)
async def eightball(ctx):
    saying = randint(1, 8)
    if saying == 1:
        await bot.say("`It is decidedly so.`")
    elif saying == 2:
        await bot.say("`Concentrate and ask again.`")
    elif saying == 3:
        await bot.say("`It is not.`")
    elif saying == 4:
        await bot.say("`It is certain.`")
    elif saying == 5:
        await bot.say("`Reply hazy, ask again later.`")
    elif saying == 6:
        await bot.say("`Better not tell you now.`")
    elif saying == 7:
        await bot.say("`As I see it, yes.")
    else:
        await bot.say("`As I see it, no.")

@bot.command(pass_context=True)
async def stalin(ctx):
    stalin = randint(0, 10)
    if stalin == 0:
        await bot.say('https://cdn.discordapp.com/attachments/437973953546289172/453723617742553098/images.png')
    elif stalin == 1:
        await bot.say('https://cdn.discordapp.com/attachments/437973953546289172/453723553070841856/images.png')
    elif stalin == 2:
        await bot.say('https://cdn.discordapp.com/attachments/437973953546289172/453723076530536460/9k.png')
    elif stalin == 3:
        await bot.say('https://cdn.discordapp.com/attachments/437973953546289172/453723107803267093/9k.png')
    elif stalin == 4:
        await bot.say('https://cdn.discordapp.com/attachments/437973953546289172/453723138430337024/images.png')
    elif stalin == 5:
        await bot.say('https://cdn.discordapp.com/attachments/437973953546289172/453723192507236352/images.png')
    elif stalin == 6:
        await bot.say('https://cdn.discordapp.com/attachments/437973953546289172/453723258047692801/images.png')
    elif stalin == 7:
        await bot.say('https://cdn.discordapp.com/attachments/437973953546289172/453723304050556929/images.png')
    elif stalin == 8:
        await bot.say('https://cdn.discordapp.com/attachments/437973953546289172/453723360526860299/images.png')
    elif stalin == 9:
        await bot.say('https://cdn.discordapp.com/attachments/437973953546289172/453723412305674260/images.png')
    else:
        await bot.say('https://cdn.discordapp.com/attachments/437973953546289172/453723470144995339/images.png')


@bot.command(pass_context=True)
async def info(ctx, user: discord.Member):
    await bot.say("Your comrade's name is: {}!".format(user.name))
    await bot.say("Their ID is: {}!".format(user.id))
    await bot.say("Their status is: {}!".format(user.status))
    await bot.say("Their highest role is: {}!".format(user.top_role))
    await bot.say("They joined at: {}!".format(user.joined_at))

@bot.command(pass_context=True)
async def RNG(ctx):
    rng = randint(0, 10000000000)
    await bot.say(rng)

@bot.command(pass_context=True)
async def diceroll(ctx):
    die_roll = randint(1, 6)
    await bot.say(die_roll)

@bot.command(pass_context=True)
async def random(ctx, random1, random2):
    random1 = int(random1)
    random2 = int(random2)
    await bot.say(randint(random1, random2))

@bot.command(pass_context=True)
async def ban(ctx, user: discord.Member):
    await bot.say("You've been deemed ***extremely*** unfit to serve, goodbye.")
    await bot.ban(user)

@bot.event
async def on_member_join(member):
    fmt = "Welcome to the server, please welcome your comrade!"
    await bot.say(fmt)

@bot.event
async def on_member_remove(member):
    await bot.say("Farewell, please enjoy the rest of your time on Earth. We hope to see you again soon.")

bot.run(os.environ['BOT_TOKEN'])
