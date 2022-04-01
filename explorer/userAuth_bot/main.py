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
def sendToBot(response_required, text, photos= None, rebuild=False):    
    captcha_user = [-1]
    captcha_command_exists = False
    for command in bot.commands:
        if command == "captcha":
            print("captcha exists in commands")
            captcha_command_exists = True
            break
    @bot.event
    async def on_ready():
        guild = discord.utils.get(bot.guilds, name=GUILD)
        print(
            f'{bot.user} is connected to the following guild:\n'
            f'{guild.name}(id: {guild.id})'
        )

        channel = bot.get_channel(int(CHANNEL_ID))    
        print(f'I found the channel:{channel.id}')
        for command in bot.commands:
            print(f"command {command}")
        bot.dispatch("sendToBot", text, channel)

    @bot.event
    async def on_sendToBot(msg, channel):        
        response = msg
        if photos != None:             
            await channel.send(file=discord.File(fp=BytesIO(photos[0]), filename='text.png'))
            await channel.send(file=discord.File(fp=BytesIO(photos[1]), filename='images.png'))
            
        await channel.send(response) 
        if not response_required:
            bot.dispatch("logout")   

    

    if not rebuild:
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
    print("after run captcha is " + str(captcha_user[0]))
    return captcha_user[0]

