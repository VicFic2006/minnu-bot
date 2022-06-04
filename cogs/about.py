import discord
from discord import app_commands
from discord.ext import commands

class about(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot
    
    @app_commands.command(name="help", description="shows help")
    async def help(self, interaction: discord.Interaction):
        embedVar = discord.Embed(
        title="Minnu Bot",
        description="I am a simple bot created by VicFic. Source: https://github.com/VicFic2006/minnu-bot",
        color=0xC7DDFC)
        embedVar.set_image(url = 'https://i.imgur.com/BLN3a1f.png')
        embedVar.add_field(name="GENERAL COMMANDS", value="`/help` `/hello` `/ping` `/getpfp`", inline=False)
        embedVar.add_field(name="YOUTUBE COMMANDS", value=" `/play` `/stop`", inline=False)
        await interaction.response.send_message(embed=embedVar)

    @app_commands.command(name="hello", description="Hello!")
    async def hello(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Hello {interaction.user.name}!")

    @app_commands.command(name="getpfp", description="Get a user's profile picture")
    async def getpfp(self, interaction: discord.Interaction, user: discord.Member = None) -> None:
        user = user or interaction.user
        await interaction.response.send_message(interaction.user.avatar)

    @app_commands.command(name="ping", description="Get the Discord Websocket Protocol Latency")
    async def ping(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"My ping is {round(self.bot.latency * 1000)}ms")


async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        about(bot),
        ## The server ID's should be added in a list as discord.Object
        guilds = [discord.Object(id = 'SERVER_ID')]
    )
