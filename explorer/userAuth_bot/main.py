# bot.py

import os
import discord
from io import BytesIO
from dotenv import load_dotenv
from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')
CHANNEL_ID = os.getenv('CHANNEL_ID')

bot = commands.Bot(command_prefix='!')
channel = None
def sendToBot(response_required, text, photos= None):    
    captcha_user = [-1]
    @bot.event
    async def on_ready():
        guild = discord.utils.get(bot.guilds, name=GUILD)
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

        channel = bot.get_channel(int(CHANNEL_ID))    
        print(f'I found the channel:{channel.id}')
        bot.dispatch("sendToBot", text, channel)

    @bot.event
    async def on_sendToBot(msg, channel):        
        response = msg
        if photos != None: 
            await channel.send(photos[0])
            await channel.send(photos[1])
        await channel.send(response) 
        if not response_required:
            bot.dispatch("logout")   

    @bot.command(name='captcha')
    async def captcha(ctx, selected: int):    
        captcha_user[0] = selected 
        response = "you entered the captcha succefully"
        await ctx.send(response)
        bot.dispatch("logout") 

    @bot.event
    async def on_logout():        
        await bot.close()

    bot.run(TOKEN)
    print("after run")
    return captcha_user[0]

