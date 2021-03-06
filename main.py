import discord
import random
import os

from discord.embeds import Embed
import admin_list
from discord.ext.commands import Bot
from discord.utils import get
import puella_list as pl
import csv
import tokens as tk
from urllib import request
from shutil import copyfile, move

bot = Bot(command_prefix="&", help_command=None)
token = tk.discord_token

online_msg = "passer des contrats avec des nouvelles Puella Magi"
admins = admin_list.get_admin()
versionCode = "0.3.1"


# functions
def gif_random(path):
	file = random.choice(os.listdir(path))
	file_path = path + str(file)
	return file_path


# on_ready function
@bot.event
async def on_ready():
	print("Little Kyubey connecté !")
	await bot.change_presence(status=discord.Status.online, activity=discord.Game(name=online_msg))


# Gifs commands with each character (and full random)
@bot.command()
async def randomGif(ctx):
	await ctx.message.delete()
	file_return = gif_random("gifs/all/")
	await ctx.send(file=discord.File(file_return))


@bot.command()
async def madokaGif(ctx):
	await ctx.message.delete()
	file_return = gif_random("gifs/madoka/")
	await ctx.send(file=discord.File(file_return))


@bot.command()
async def sayakaGif(ctx):
	await ctx.message.delete()
	file_return = gif_random("gifs/sayaka/")
	await ctx.send(file=discord.File(file_return))


@bot.command()
async def mamiGif(ctx):
	await ctx.message.delete()
	file_return = gif_random("gifs/mami/")
	await ctx.send(file=discord.File(file_return))


@bot.command()
async def kyokoGif(ctx):
	await ctx.message.delete()
	file_return = gif_random("gifs/kyoko/")
	await ctx.send(file=discord.File(file_return))


@bot.command()
async def homuraGif(ctx):
	await ctx.message.delete()
	file_return = gif_random("gifs/homura/")
	await ctx.send(file=discord.File(file_return))


@bot.command()
async def irohaGif(ctx):
	await ctx.message.delete()
	file_return = gif_random("gifs/iroha/")
	await ctx.send(file=discord.File(file_return))


@bot.command()
async def lilKyubeyGif(ctx):
	await ctx.message.delete()
	file_return = gif_random("gifs/lil_kyubey/")
	await ctx.send(file=discord.File(file_return))

@bot.command()
async def addGif(ctx, char, url):
	await ctx.message.delete()
	charList = pl.return_dict()
	charCap = char.capitalize()
	charLow = char.lower()

	if charCap in charList:
		with open('number_list.csv', mode='r') as csvfile:
			reader = csv.reader(csvfile)
			char_dict = {rows[0]:rows[1] for rows in reader}
			print(char_dict)
			puella_num = char_dict[charLow]

		try:
			request.urlretrieve(url, charLow + str(puella_num) + ".gif")
		except:
			await ctx.send("Désolé mais ton lien n'est pas valide.")
			return None

		file_name = charLow + str(puella_num) + ".gif"
		puella_num = int(puella_num) + 1
		char_dict[charCap] = puella_num

		with open('number_list.csv', "w") as csvfile:
			for key in char_dict.keys():
				csvfile.write("%s, %s\n" % (key, char_dict[key]))

		original_path = r"/home/Tintin/Desktop/Lil_Kyubey/" + file_name
		new_path = r"/home/Tintin/Desktop/Lil_Kyubey/" + charLow + "/" + file_name

		copyfile(original_path, new_path)
		move(original_path, new_path)

	else:
		await ctx.send("Pour ajouter un gif, entre: *&addGif [nom de la Puella Magi] [url]*")


# Favorite Puella Magi command
@bot.command()
async def choose(ctx, char):
    await ctx.message.delete()
    return None
    magical_girl1 = char.lower()
    magical_girl = magical_girl1.capitalize()
    guild = ctx.guild
    user = ctx.message.author

    charList = pl.return_dict()
    colour = charList[magical_girl]

    if magical_girl in charList:
        if get(guild.roles, name=char):
            pass
        else:
            mg = magical_girl.capitalize()
            await guild.create_role(name=mg, colour=discord.Colour(colour))

        for key in charList.values():
            check_role = get(guild.roles, name=key)
            if check_role in user.roles:
                pass
            else:
                await user.remove_roles(check_role)


        role = discord.utils.get(guild.roles, name=mg)
        await user.add_roles(role)

    else:
        await ctx.send("Désolé, je n'ai pas compris quelle Puella Magi tu as choisis\nTu peux choisir entre:\n- Madoka Kamane\n- Sayaka Miki\n- Mami Tomoe\n- Kyoko Sakura\n- Homura Akemi\n\n(Entre juste le prénom)")


# Help Command with embed messages
@bot.command()
async def help(ctx):
	await ctx.message.delete()
	
	embedMsg = discord.Embed(title="Liste des commandes", description="Liste de toutes les catégories.", color=0xffffff)
	embedMsg.add_field(name="Images & Gifs", value="*&helpImages*", inline=False)
	embedMsg.add_field(name="Musiques & Sons", value="*&helpMusic*", inline=False)
	embedMsg.add_field(name="Puella Magi", value="&helpPuellaMagi", inline=False)
	embedMsg.add_field(name="Administratif", value="*&helpAdmin*", inline=False)
	
	await ctx.channel.send(embed=embedMsg)


@bot.command()
async def helpImages(ctx):
	await ctx.message.delete()

	embedMsg = discord.Embed(title="Liste des commandes pour les images et gifs:", color=0x15dcf2)
	embedMsg.add_field(name="*&randomGif*", value="Envoie un gif au hasard depuis mes fichiers.")
	embedMsg.add_field(name="*&madokaGif*", value="Envoie un gif au hasard de Madoka Kamane.")
	embedMsg.add_field(name="*&sayakaGif*", value="Envoie un gif au hasard de Sayaka Miki.")
	embedMsg.add_field(name="*&mamiGif*", value="Envoie un gif au hasard de Mami Tomoe.")
	embedMsg.add_field(name="*&kyokoGif*", value="Envoie un gif au hasard de Kyoko Sakura.")
	embedMsg.add_field(name="*&homuraGif*", value="Envoie un gif au hasard d'Homura Akemi.")
	embedMsg.add_field(name="*&irohaGif*", value="Envoie un gif au hasard d'Iroha Takami.")
	embedMsg.add_field(name="*&lilKyubeyGif*", value="Envoie un gif au hasard de Little Kyubey.")
	embedMsg.add_field(name="*&addGif [nom de la Puella Magi] [url]*", value="Télécharge le gif dans les fichiers du bot.")

	await ctx.channel.send(embed=embedMsg)

@bot.command()
async def helpMusic(ctx):
	await ctx.message.delete()

	embedMsg = discord.Embed(title="Liste des commandes pour les musiques et les sons:",
	    color=0xc3ff00)
	embedMsg.add_field(name="*Rien*", value="Ne fait rien. :+1:")
	await ctx.channel.send(embed=embedMsg)

@bot.command()
async def helpPuellaMagi(ctx):
    await ctx.message.delete()

    embedMsg = discord.Embed(title="Liste des commandes Puella Magi:", description="Ce sont des commandes pour les Puella Magi", color=0xbe5683)
    embedMsg.add_field(name="*&choose*", value="Choisis ta Puella Magi préférée.")
    await ctx.channel.send(embed=embedMsg)

@bot.command()
async def helpAdmin(ctx):
	await ctx.message.delete()

	embedMsg = discord.Embed(
	    title="Liste des commandes admins:",
	    description=
	    "Ces commandes ne sont utilisable que par les administrateurs.",
	    color=0x000000)
	embedMsg.add_field(name="*&online*", value="Active le Statut: 'En Ligne'.")
	embedMsg.add_field(name="*&idle*", value="Active le Statut: 'Occupé'.")
	embedMsg.add_field(name="*&dnd*", value="Active le Statut: 'Ne pas Déranger'.")
	embedMsg.add_field(name="*&invisible*", value="Active le Statut: 'Invisible'.")
	embedMsg.add_field(name="*&version*", value="Revoie le numéro de version.")
	await ctx.channel.send(embed=embedMsg)


# Status commands
@bot.command()
async def online(ctx):
	if ctx.author.id in admins:
		await bot.change_presence(status=discord.Status.online,
        activity=discord.Game(name=online_msg))
		await ctx.message.delete()
	else:
		await ctx.send("Désolé, tu n'est pas un admin.")
		await ctx.message.delete()


@bot.command()
async def idle(ctx):
	if ctx.author.id in admins:
		await bot.change_presence(status=discord.Status.idle, activity=discord.Game(online_msg))
		await ctx.message.delete()
	else:
		await ctx.send("Désolé, tu n'est pas un admin.")
		await ctx.message.delete()


@bot.command()
async def dnd(ctx):
	if ctx.author.id in admins:
		await bot.change_presence(status=discord.Status.do_not_disturb,
        activity=discord.Game(name=online_msg))
		await ctx.message.delete()
	else:
		await ctx.send("Désolé, tu n'est pas un admin.")
		await ctx.message.delete()


@bot.command()
async def invisible(ctx):
	if ctx.author.id in admins:
		await bot.change_presence(status=discord.Status.invisible)
		await ctx.message.delete()
	else:
		await ctx.send("Désolé, tu n'est pas un admin.")
		await ctx.message.delete()


@bot.command()
async def ping(ctx):
    await ctx.message.delete()
    await ctx.send("Latence: " + str(bot.latency * 1000) + " ms.")


# Version Command
@bot.command()
async def version(ctx):
	await ctx.message.delete()
	await ctx.send("Je suis en version " + versionCode + ".")

bot.run(token)