import discord
from discord.ext import commands
from discord.embeds import Embed
import asyncio
from os import listdir

import tokens as pwrd

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="&", help_command=None, intents=intents)

@bot.command()
async def main(bot):
    async with bot:
        for filename in listdir("/home/Tintin/discord_bot/Lil_Kyubey/cogs/"):
            if filename.endswith(".py"):
                await bot.load_extension(f"cogs.{filename[:-3]}")
        await bot.start(pwrd.discord_token)
        
@bot.event
async def on_command_error(ctx, error):
    print(error)
    emb = Embed(title="<:Erreur:945123023546093611> Commande inconnue", description="Je ne connais pas cette commande ou celle-ci a plantée...", color=0xe24647)
    emb.add_field(name="Sortie:", value=str(error), inline=False)
    await ctx.channel.send(embed=emb)
    
# Démarre le bot
asyncio.run(main(bot))