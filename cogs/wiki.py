import discord
from discord.ext import commands
from discord import app_commands
from discord.embeds import Embed

class Wiki(commands.GroupCog, name="wiki"):

    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()

    @app_commands.command(name="character", description="Affiche les infos d'un personnage.")
    async def character(self, react: discord.Interaction, character: str):
        await self.bot.wait_until_ready()
        await react.response.defer()
        return
    
    def create_embed(self, character: str) -> Embed:
        embed = Embed(title=character, description="des", color=0x00ff00)
        embed.set_thumbnail(url="url_link")
        embed.set_image(url="url")
        embed.add_field(name="f1", value="v1", inline=False)
        embed.set_footer(text="Depuis le Wiki Puella Magi")
        return embed


async def setup(bot) -> None:
    await bot.add_cog(Wiki(bot))