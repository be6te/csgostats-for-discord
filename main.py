import discord
from core.cogload import cogload as e_
from discord.ext import commands

cogload = e_()
app = commands.Bot(
    command_prefix='gg!', 
    intents=discord.Intents.all()
)

@app.event
async def on_connect():
    await cogload.cogload(bot=app)

if __name__ == '__main__':
    app.run('your bot token')
