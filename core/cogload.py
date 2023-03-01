import os, sys

class cogload:
    def __init__(self):
        self.path = './'

    async def cogload(self, bot):
        for filename in os.listdir('./commands'):
            if filename.endswith('.py'):
                await bot.load_extension(f'commands.{filename[:-3]}')
