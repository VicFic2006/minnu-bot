import discord
from discord.ext import commands

class MyBot(commands.Bot):

    def __init__(self):
        super().__init__(
            command_prefix='$',
            intents= discord.Intents.all(),
            application_id= 'APPLICATION_ID')

    async def setup_hook(self):
        COG_LIST = ["about", "music"]
        SERVER_LIST = ['THE_ID_OF_THE_SERVERS_YOU_WANT_YOUR_BOT_TO_BE_IN']

        for i in range(len(COG_LIST)):
            await self.load_extension(f"cogs.{COG_LIST[i]}")
        for i in range(len(SERVER_LIST)):
            await bot.tree.sync(guild= discord.Object(id= SERVER_LIST[i]))

    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

bot = MyBot()
bot.run('BOTCODE')
