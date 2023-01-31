import discord
from discord.ext import commands
from discord import app_commands
import var

class Basic(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()
        
    # Se déclenche quand le bot est prêt
    @commands.Cog.listener()
    async def on_ready(self):
        print("Little Kyubey connecté !")
        await self.bot.change_presence(status=discord.Status.online, activity=discord.Game(name="passer des contrats avec des nouvelles Puella Magi."))
        
    # Permet de charger un cog
    @commands.command(name="load")
    async def load(self, ctx, extention):
        await ctx.message.delete()
        await self.bot.load_extension(f"cogs.{extention}")
        await ctx.send(f"Le module {extention} a bien été chargé")
        
    # Permet de décharger un cog
    @commands.command(name="unload")
    async def unload(self, ctx, extention):
        await ctx.message.delete()
        await self.bot.unload_extension(f"cogs.{extention}")
        await ctx.send(f"Le module {extention} a bien été déchargé")
        
    # Permet de recharger un cog
    @commands.command(name="reload")
    async def reload(self, ctx, extention):
        await ctx.message.delete()
        await self.bot.unload_extension(f"cogs.{extention}")
        await self.bot.load_extension(f"cogs.{extention}")
        await ctx.send(f"Le module {extention} a bien été rechargé")
        
    # Pour synchroniser les commandes slash
    @commands.command(name="sync")
    async def sync(self, ctx) -> None:
        fmt = await ctx.bot.tree.sync()
        await ctx.send(f"{len(fmt)} commandes ont été synchronisées.")
        
        
    # Se déclenche à chaque message
    @commands.Cog.listener()
    async def on_message(self, message):
        # Premet de ne pas prendre en compte les messages envoyés par le bot
        if message.author == self.bot.user:
            return
        
        # Envoie un message si le bot est mentionné
        if self.bot.user.mentioned_in(message) and message.mention_everyone == False:
            await message.channel.send(f"{message.author.mention}, si tu veux voir la liste des commandes, tape **/help**.")
            
    # Affiche la version du Bot
    @app_commands.command(name="version", description="Affiche la version du NekoBot.")
    async def ver(self, interaction: discord.Integration) -> None:
        await interaction.response.send_message(f"Je suis en en version **{var.version}**.")
        
    # Envoie le Lien du Github du Bot
    @app_commands.command(name="github", description="Récupère le lien mon repo Github.")
    async def git(self, interaction: discord.Interaction) -> None:
        await interaction.response.send_message(f"Lien du repo: https://github.com/Tintin361/Lil_Kyubey")

    
async def setup(bot):
    await bot.add_cog(Basic(bot))