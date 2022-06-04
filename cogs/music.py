import discord
from discord import app_commands
from discord.ext import commands
import youtube_dl
import validators

class music(commands.Cog):
    def __init__(self, bot: commands.Bot) -> None:
        self.bot = bot

    # Stuff I stole from https://python.land/build-discord-bot-in-python-that-plays-music
    # and https://replit.com/@maxcodez/DryZestyVariety#music.py

    @app_commands.command(name="play", description="Play music. You can enter a song name or url")
    async def play(self, interaction: discord.Interaction, song: str) -> None:

        if not interaction.user.voice:
            await interaction.response.send_message("You are not connected to a voice channel")
        else:
            channel = interaction.user.voice.channel
            await channel.connect()
            interaction.guild.voice_client.stop()
            FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
            YDL_OPTIONS = {'format':"bestaudio"}
            vc = interaction.guild.voice_client
            
            await interaction.response.send_message(f"Playing {song}")
            with youtube_dl.YoutubeDL(YDL_OPTIONS) as ydl:
                if validators.url(song):
                    info = ydl.extract_info(song, download=False)
                else:
                    # This part is a little finicky
                    # See this -> https://stackoverflow.com/questions/63388364/searching-youtube-videos-using-youtube-dl#63451743
                    info = ydl.extract_info(f"ytsearch:{song}", download=False)['entries'][0]
                url2 = info['formats'][0]['url']
                # await interaction.response.send_message(f"Playing {info['title']}")
                source = await discord.FFmpegOpusAudio.from_probe(url2, **FFMPEG_OPTIONS)
                vc.play(source)
        
    @app_commands.command(name="stop", description="To make the bot stop the music")
    async def stop(self, interaction: discord.Interaction) -> None:
        voice_client = interaction.guild.voice_client
        if voice_client.is_connected():
            await voice_client.disconnect()
            await interaction.response.send_message("Stopped music.")
        else:
            await interaction.response.send_message("The bot is not connected to a voice channel.")

async def setup(bot: commands.Bot) -> None:
    await bot.add_cog(
        music(bot),
        # The server IDs' shoudl be added in a list as discord.Object
        guilds = [discord.Object(id = 'SERVER_ID')]
    )
