import discord
from discord.ext import commands
from discord import app_commands
import var

class Tools(commands.GroupCog, name="tools"):

    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()

    # Affiche la version du Bot
    @app_commands.command(name="version", description="Affiche la version de Little Kyubey.")
    async def ver(self, react: discord.Integration) -> None:
        await react.response.send_message(f"Little Keybey est en version {var.version}", ephemeral=True)

    # Renvoie un lien vers le repo GitHub
    @app_commands.command(name="github", description="Lien vers le repo sur GitHub.")
    async def git(self, interaction: discord.Interaction):
        message = Embed(title="Lien du GitHub:", color=0xfbfcfc).add_field(name="Repo de Kiri-Chan:", value="https://github.com/Tintin361/Kiri-chan")\
        .add_field(name="Repo de Little Kyubey", value="https://github.com/Tintin361/Lil_Kyubey")\
        .add_field(name="Repo de NekoBot", value="https://github.com/Tintin361/NekoBot")\
        .add_field(name="Repo de VeemoBot", value="https://github.com/Tintin361/VeemoBot")
        await interaction.response.send_message(embed=message, ephemeral=True)

    # Retourne la latence
    @app_commands.command(name="ping", description="Affiche la latence.")
    async def ping(self, interaction: discord.Interaction):
        await interaction.response.send_message(f"La latence est de: **{self.bot.latency * 1000}** millisecondes.", ephemeral=True)


async def setup(bot):
    await bot.add_cog(Tools(bot))