from ast import While
from email import message
from click import pass_context
import gtts
import io
from msilib.schema import InstallUISequence
from multiprocessing.connection import wait
from pickletools import optimize
import sys
import textwrap
from asyncio.base_events import Server
from telnetlib import AYT
from async_timeout import timeout
from turtle import width
from typing import ContextManager, Text
from unicodedata import category
from functools import partial
from venv import create
from cv2 import bitwise_and
import discord
import uuid
from matplotlib import image
from matplotlib.animation import PillowWriter
from matplotlib.pyplot import connect
from matplotlib.style import use
from pyparsing import And
import requests
import shutil
import random
import asyncio
import os
from PIL import Image , ImageOps , ImageDraw , ImageFont
import traceback
from io import BytesIO
from discord import member
from discord import voice_client
from discord.colour import Color
from discord.ext.commands.converter import CategoryChannelConverter, MemberConverter
from playsound import playsound
from discord import asset
from discord import user
from pathlib import Path
from discord import file
from discord.ext.commands import Bot
from importlib import import_module, reload  
from mutagen.mp3 import MP3
from setuptools import find_namespace_packages
from sklearn.datasets import load_wine

import youtube_dl
from discord.utils import get
from discord import Embed, FFmpegPCMAudio
from random import choice
from dotenv import load_dotenv
from discord import client
from discord import channel
from discord import guild
from discord.voice_client import VoiceClient
from discord import embeds
from discord.ext import commands
from youtube_dl.YoutubeDL import YoutubeDL
from youtube_dl.utils import parse_iso8601


intents=intents=discord.Intents.all()

TOKEN = 'bot_token'

bot=commands.Bot(command_prefix='!',intents=intents)


#Member Join message
@bot.event
async def on_member_join(member):
    myEmbed = discord.Embed(title="Hello :D", description="Welcome to my server", color=0x00ff00)
    myEmbed.add_field(name="type", value="test bot", inline=False)
    myEmbed.set_footer(text="under mantainance")
    myEmbed.set_author(name="about bot")
    await member.send(embed=myEmbed)
    myEmbed1 = discord.Embed(title="Hello :D", description=f'Welcome to my server {member.mention}', color=0x00ff00)
    myEmbed1.add_field(name="type", value="test bot", inline=False)
    myEmbed1.set_footer(text="under mantainance")
    myEmbed1.set_author(name="about bot")
    guild = bot.get_guild(758911606012248075)
    channel = guild.get_channel(758911606464708609)
    await channel.send(embed=myEmbed1)
    

#Member leave message
@bot.event
async def on_member_remove(member):
    myEmbed = discord.Embed(title=":(", description="Sad to see you leave", color=0x00ff00)
    myEmbed.add_field(name="type", value="test bot", inline=False)
    myEmbed.set_footer(text="under mantainance")
    myEmbed.set_author(name="about bot")
    await member.send(embed=myEmbed)

#cooldown
@bot.event
async def on_command_error(ctx,error):
    if isinstance(error, commands.CommandOnCooldown):
        await ctx.send(f"{ctx.author.mention} **Still on cooldown** time left:{error.retry_after:.2f}",delete_after = 60.0)

#disconnect someone infinite times
@bot.event
async def on_voice_state_update(member, before, after):
    MY_ID = None
    if (member.id == MY_ID):
        if (before.channel is None and after.channel is not None) or before.channel is not None:
            await member.edit(voice_channel=None)


#testgame
@bot.command()
async def guess(ctx):
    await ctx.send("Guess the number from 1 to 5!")
    numbers = ["1","2","3","4","5"]
    choice = random.choice(numbers)
    answer = await bot.wait_for("message")
    if ctx.message.author:
        if answer.content == choice:
            await ctx.send("You guessed the correct number!")
        else:
            await ctx.send(f"You lost! The number was {choice}")


#TTS
#Many languages can be added by changind the lang parameter in gtts.gTTS
@bot.command()
async def tts(ctx,*,filefortts):
    global f_name
    voice_client = ctx.message.guild.voice_client
    voice = discord.utils.get(bot.voice_clients, guild=ctx.guild)
    if voice==None:
        await ctx.send("not connected to a voice channel use !join")
    else:
        server = ctx.message.guild
        voice_channel = server.voice_client 
        voice_client = ctx.message.guild.voice_client
        if voice_client.is_playing():
            await ctx.send(f"{ctx.author.mention} already playing an audio")
        else:
            t1=gtts.gTTS(text=filefortts,lang="hi")
            f_name= str(uuid.uuid4()) + '.mp3'  
            t1.save(f_name)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=f_name))
            await asyncio.sleep(5)
            os.remove(f_name)

#stopping the TTS
@bot.command()
async def stts(ctx):
    voice_client = ctx.message.guild.voice_client
    global f_name 
    if voice_client.is_playing():
         voice_client.stop()
         await asyncio.sleep(3)
         await os.remove(f_name)
    else:
        await ctx.send("The bot is not playing anything at the moment.")


#Spam a certain message in chat
@bot.command(name='spam', help='Spams the input message for x number of times')
async def spam(ctx, amount:int, *,message):
        if "@" in message:
            await ctx.send("you cannot tag anyone")
        else:
            if amount>=100:
                await ctx.send("Amount cant exceed 100 ")
            else:
                for i in range(amount): # Do tohe next thing amount times
                    await ctx.send(message) # Sends message where command was called     d


#clear certain amount of messages
@bot.command()
@commands.cooldown(1,10,commands.BucketType.user)
async def deletetext(ctx,amount=5):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f"{ctx.author.mention} deleted {amount} messages",delete_after = 5.0)


#change a person's Nickname in server
@bot.command()
async def nick(ctx, m: discord.Member, * ,newnick):
    await m.edit(nick=newnick)
    await ctx.send(f'nickname changed for {m.mention} by {ctx.author.mention}')


#Wanted poster on a particular user
@bot.command()
async def wanted(ctx, user: discord.Member = None):
    if user is None:
        user=ctx.author
    test=Image.open("F:\VS code python\git_discordbo5t\wanted.jpg")
    asset=user.avatar_url_as(size=128)
    data = BytesIO(await asset.read())
    pfp=Image.open(data)
    pfp=pfp.resize((177,177))
    test.paste(pfp,(120,212))
    test.save("wanted_edit.jpg")
    await ctx.send(file=discord.File('wanted_edit.jpg'))


#play a certain MP3 File on voice channel
@bot.command()
@commands.cooldown(1,10,commands.BucketType.user)
async def laugh(ctx):
            server = ctx.message.guild
            voice_channel = server.voice_client
            if not voice_channel.is_playing():
                if not ctx.message.author.voice:
                    await ctx.send(f"Please connect to voice channel {ctx.author.mention}",delete_after = 60.0)
                else:
                    await voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source='F:\VS code python\git_discordbo5t\Laugh.mp3'))
            else:
                await ctx.send("Bot is not connected or bot is already playing an audio",delete_after = 60.0)



#adding Caption to images
@bot.command()
async def save(ctx,*,message_user):
    # USAGE: use command .save in the comment box when uploading an image to save the image as a jpg
    try:
        url = ctx.message.attachments[0].url            # check for an image, call exception if none found
    except IndexError:
        print("Error: No attachments")
        await ctx.send("No attachments detected!")
    else:
        if url[0:26] == "https://cdn.discordapp.com":   # look to see if url is from discord
            r = requests.get(url, stream=True)
            imageName = str(uuid.uuid4()) + '.jpg'      # uuid creates random unique id to use for image names
            with open(imageName, 'wb') as out_file:
                shutil.copyfileobj(r.raw, out_file)     # save image (goes to project directory)
            img1=Image.open(imageName)
            width_p = img1.width
            height = img1.height
            img1 = img1.resize((int(img1.width*2),int(img1.height*2)))
            f_size = 40
            img1= ImageOps.expand(img1,border=(0,90,0,0))
            draw = ImageDraw.Draw(img1)
            myFont = ImageFont.truetype("F:\\VS code python\\Avenir-Medium.ttf",f_size)
            lines = textwrap.wrap(message_user, width=(width_p/10))
            offset = margin = 0
            for line in lines:
                draw.text((offset,margin), line, font=myFont, fill=(255,255,255),align='right')
                margin += myFont.getsize(line)[1]
                print(myFont.getsize(line)[1])
                print(margin)
            rgb_im = img1.convert('RGB')
            with io.BytesIO() as image_binary:
                        rgb_im.save(image_binary, 'PNG',optimize=True)
                        image_binary.seek(0)
                        await ctx.send(file=discord.File(fp=image_binary, filename="image.png"))
                        await asyncio.sleep(10)
                        os.remove(imageName)





#playing songs 
youtube_dl.utils.bug_reports_message = lambda: ''

ytdl_format_options = {
    'format': 'bestaudio/best',
    'restrictfilenames': True,
    'noplaylist': True,
    'nocheckcertificate': True,
    'ignoreerrors': False,
    'logtostderr': False,
    'quiet': True,
    'no_warnings': True,
    'default_search': 'auto',
    'source_address': '0.0.0.0' # bind to ipv4 since+ ipv6 addresses cause issues sometimes
}

ffmpeg_options = {
    'options': '-vn'
}

ytdl = youtube_dl.YoutubeDL(ytdl_format_options)

class YTDLSource(discord.PCMVolumeTransformer):
    def __init__(self, source, *, data, volume=0.5):
        super().__init__(source, volume)
        self.data = str(data)
        self.title = data.get('title')
        self.url = ""

    @classmethod
    async def from_url(cls, url, *, loop=None):
        loop = loop or asyncio.get_event_loop()
        data = await loop.run_in_executor(None, lambda: ytdl.extract_info(url, download=True))
        if 'entries' in data:
            # take first item from a playlist
            data = data['entries'][0]
        filename = ytdl.prepare_filename(data)
        return filename


#Making a bot joining a Voice channel
@bot.command(name='join', help='Tells the bot to join the voice channel')
async def join(ctx):
    if not ctx.message.author.voice:
        await ctx.send("{} is not connected to a voice channel".format(ctx.message.author.name),delete_after = 60.0)
        return
    else:
        channel = ctx.message.author.voice.channel
        voice_client = ctx.message.guild.voice_client
        if voice_client is not None:
            await voice_client.disconnect() 
            await ctx.send("moved to voice channel : **{}**".format(ctx.author.voice.channel),delete_after = 60.0)
            await channel.connect()
        else:
            await ctx.send("connected to voice channel : **{}**".format(ctx.author.voice.channel),delete_after = 60.0)
            await channel.connect()


#Making a Bot leaving the voice channel
@bot.command(name='leave', help='To make the bot leave the voice channel')
async def leave(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_connected():
        await voice_client.disconnect()
    else:
        await ctx.send("The bot is not connected to a voice channel.")

#playing song
@bot.command(name='play_song', help='To play song')
async def play(ctx,*,url):
    try :
        server = ctx.message.guild
        voice_channel = server.voice_client
        async with ctx.typing():
            global filename
            filename =  await YTDLSource.from_url(url, loop=bot.loop)
            voice_channel.play(discord.FFmpegPCMAudio(executable="ffmpeg.exe", source=filename))
        base=os.path.basename(filename)
        file = os.path.splitext(base)[0]
        file = file.split("_")
        await ctx.send('**Now playing:** {}'.format(" ".join(file))) 
        while voice_channel.is_playing():
            await asyncio.sleep(1)
        else:
            await asyncio.sleep(3)
            while voice_channel.is_playing():
                break
            else:
                os.remove(filename)
    except:
        await ctx.send("The bot is not connected to a voice channel.")

#deleting the file 
@bot.command(name="delete",help="delete the file")
async def delete(ctx):
    global filename 
    os.remove(filename)   


#pausing the song 
@bot.command(name='pause', help='This command pauses the song')
async def pause(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
        await voice_client.pause()
    else:
        await ctx.send("The bot is not playing anything at the moment.")

#resuming the song 
@bot.command(name='resume', help='Resumes the song')
async def resume(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_paused():
        voice_client.resume()
    else:
        await ctx.send("The bot was not playing anything before this. Use play_song command")

#stop the song being played
@bot.command(name='stop', help='Stops the song')
async def stop(ctx):
    voice_client = ctx.message.guild.voice_client
    if voice_client.is_playing():
         voice_client.stop()
         await asyncio.sleep(3)
         await os.remove(filename)
    else:
        await ctx.send("The bot is not playing anything at the moment.")



#-------------------------------------------------------------------------



#restarting bot
def restart_bot(): 
  os.execv(sys.executable, ['bot.py'] + sys.argv)

@bot.command(name= 'restart')
async def restart(ctx):
    await ctx.send("Restarting the bot")
    await bot.close()


@bot.event
async def on_ready():
    print('My bot is ready')
    embed = discord.Embed(
        title = f"{bot.user.name} Bot is online",delete_after = 60.0, 
    )
    embed.set_author(name="discordbot",icon_url="https://discord.com/assets/3c6ccb83716d1e4fb91d3082f6b21d77.png")

    embed.set_thumbnail(url="https://discord.com/assets/3c6ccb83716d1e4fb91d3082f6b21d77.png")

    embed.set_footer(
        text='''Enjoy
Type !restart if bot fails to work ''',
    )
    #sending alerts that the bot is online
    # await bot.get_channel('server_id').send(embed=embed,delete_after = 60.0)
    # await bot.get_channel('server_id').send(embed=embed,delete_after = 60.0)
    # await bot.get_channel('server_id').send(embed=embed,delete_after = 60.0)
bot.run('Bot_token')


























































