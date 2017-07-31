import discord
import asyncio
from discord.ext import commands
import random
description = "A basic bot, made by /u/Majooj. Most functionality was thought up by 7π."

bot = commands.Bot(command_prefix="-", description = description, pm_help = True)

@bot.event
async def on_ready():
    print("Logged in as")
    print(bot.user.name)
    print(bot.user.id)
    print("-------------")
    await bot.change_presence(game=discord.Game(name='Type -help for commands.'))

@bot.command(description = "-quran - Quotes a verse of the Quran (quran.com) Offers basic translation. ")
async def quran(chapter : str, verse : str):
    await bot.say("https://quran.com/" + chapter + "/" + verse)

@bot.command(description = "-quran - Quotes a verse of the Quran (quranx.com). Offers tafsir and ahadith on the specified verse.")
async def quranx(chapter : str, verse : str):
    await bot.say("http://quranx.com/" + chapter + "." + verse)

@bot.command(description = "-sunnah - Quotes ahadith from various books (sunnah.com). Offers hadith translation in English and Urdu, and gives the hadith grading, as well as reference. Author = [Bukhari], [Muslim], [Nasai], [AbuDawud], [IbnMajah]. Use in-book references. Currently under maintanence.")
async def hadith(author : str, book : str, number : str):
    await bot.say("https://sunnah.com/" + author + "/" + book + "/" + number)

@bot.command(pass_context = True)
async def kys():
    rand = random.randint(0,4)
    kys = ["i'm on it", "i need fentanyl", "kill me right now please", "END IT PLZ"]
    if rand == 4:
        await bot.say("do you know what's soulless, depressed, and ready to die?")
        await asyncio.sleep(3)
        await bot.say("me")
    else:
        await bot.say(kys[rand])
        
@bot.command(pass_context = True)
async def kms(ctx):
    rand = random.randint(0,4)
    kms = ["i'll get the rope", "do it!", "share this bottle with me", "<:hmm:275971766197813249>", ":knife:"]
        await bot.say(kms[rand])

@bot.command()
async def askmufti():
    rand = random.randint(0,2)
    if rand == 1:
        await bot.say("Allah knows best.")
    elif rand == 2:
        await bot.say("الله أعلم")
    else:
        await bot.say("allahu a3lam")

@bot.event
async def on_message(message):
    if message.content.startswith("ayy"):
        await bot.send_message(message.channel, "lmao")
    elif message.content.startswith("TAKBEER"):
        await bot.send_message(message.channel, "ALLAHU AKBAR!")
    elif message.content.startswith("*triggered*"):
        await bot.send_message(message.channel, "you have activated my PTSD card")
    elif message.content.startswith("lit"):
        await bot.send_message(message.channel, ":fire:")
    elif message.content.startswith("shia"):
        await bot.send_message(message.channel, "*kaffir")
    await bot.process_commands(message)


@bot.command(pass_context = True, description = "-purgeuser @mention <amount> (Note: It will scan the last <amount> messages and delete all of the ones said by @mention")
@commands.has_permissions(manage_messages=True)
async def purgeuser(ctx, member: discord.Member, amount):
    def usermessage(m):
        return m.author == member
    if int(amount) > 1 and int(amount) < 51:
        delete = await bot.purge_from(ctx.message.channel, limit = int(amount), check = usermessage)
        await bot.say(str(len(delete)) + " messages deleted.")
        logs = "PLACEHOLDER" #Paste the ID copied from "Copy ID" (enable developer mode), for your log channel.
        await bot.send_message(bot.get_channel(logs), (str(len(delete))) + " messages deleted by @" + str(ctx.message.author) + " in #" + str(ctx.message.channel))
    else:
        await bot.say("Amount of purged messages should be greater than 1 and lower than 51")
        
@bot.command(pass_context = True)
@commands.has_permissions(manage_messages=True)
async def purge(ctx, amount):
    if int(amount) > 1 and int(amount) < 101:
        delete = await bot.purge_from(ctx.message.channel, limit = int(amount))
        await bot.say(str(len(delete)) + " messages deleted.")
        logs = "PLACEHOLDER" #Paste the ID copied from "Copy ID" (enable developer mode), for your log channel.
        await bot.send_message(bot.get_channel(logs), (str(len(delete))) + " messages deleted by @" + str(ctx.message.author) + " in #" + str(ctx.message.channel))
    else:
        await bot.say("Amount of purged messages should be greater than 1 and lower than 101")

@bot.command(pass_context = True)
@commands.has_permissions(ban_members=True)
async def ban(ctx, member: discord.Member, amount: int=1):
    await bot.ban(member, delete_message_days = amount)
    await bot.say(member.name + " was banned. Please -log the reason.")
    logs = "PLACEHOLDER" #Paste the ID copied from "Copy ID" (enable developer mode), for your log channel.
    await bot.send_message(bot.get_channel(logs), member.name + " has been banned by " + str(ctx.message.author) + ".")

@bot.command()
@commands.has_permissions(manage_messages=True)
async def log(*, reason : str):
    logs = "PLACEHOLDER" #Paste the ID copied from "Copy ID" (enable developer mode), for your log channel.
    await bot.send_message(bot.get_channel(logs), reason)
                  
bot.run('PLACEHOLDER') #Paste the code given by Discord here.
