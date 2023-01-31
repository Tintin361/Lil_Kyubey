# Bibliothèques de Discord
import discord
from discord.ext import commands
from discord.embeds import Embed
from discord import app_commands

# Autres
from pybooru import Danbooru
from random import choice

# Bibliothèques locales
import tokens as pswd
import var
import colors

safe = Danbooru('safebooru', username="Kiri-chan27", api_key=pswd.danbooru_api)


class Search(commands.Cog):
    
    def __init__(self, bot) -> None:
        self.bot = bot
        super().__init__()
        
    @app_commands.command(name="search", description="Affiche une image de Madoka Kaname.")
    async def holy_quintet(self, interaction: discord.Interaction, personnage: var.char_or, fichier: var.file_type):
        await interaction.response.defer(ephemeral=False)
        
        if fichier == 'image':
            full_tag = f"{personnage}"
        else:
            full_tag = f"{personnage} {fichier}"
        
        
        valid = False
        while not valid:
            try:
                image = choice(safe.pool_list(tags=full_tag, limit=3000))
                
                current_char = personnage.replace('_', ' ').title().lower()
                print(current_char)
                color = colors.charList[current_char.split()[0]]
                
                msg = Embed(title="Recherche:", description=f"**{current_char}** de la série Puella Magi Madoka Magica", color=color)
                msg.set_image(url=image['file_url'])
                msg.set_footer(text=f"Depuis Safebooru - ID: {image['id']}", icon_url="https://danbooru.donmai.us/packs/static/images/danbooru-logo-128x128-ea111b6658173e847734.png")
                    
                view = discord.ui.View(timeout=None)
                view.add_item(discord.ui.Button(label="Lien vers l'image", style=discord.ButtonStyle.link, url=image['url']))
            
                await interaction.followup.send(embed=msg, view=view)
                valid = True
                
            except:
                valid = True
        
async def setup(bot):
    await bot.add_cog(Search(bot))