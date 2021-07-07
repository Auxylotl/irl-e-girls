import random
import discord
from discord import embeds
from discord.ext import commands
from discord.ext.commands import cooldown, BucketType
from discord.ext.commands import (CommandOnCooldown)
import asyncio
from discord.ext import tasks
import base64
import os
from discord.utils import get
from discord import Member, Embed
import json
from requests.api import request
import requests
import urllib.request
import datetime
import time
from discord.ext.commands import has_permissions, MissingPermissions, BotMissingPermissions

bot = commands.Bot(command_prefix=["e.", "E."], intents=discord.Intents.all())
bot.remove_command('help')

states = ["alaska", "alabama", "arkansas", "arizona", "california", "colorado", "connecticut", "delaware", "florida", "georgia", "hawaii", "iowa", "idaho", "illinois", "indiana", "kansas", "kentucky", "louisiana", "massachusetts", "maryland", "maine", "michigan", "minnesota", "missouri", "mississippi", "montana",
          "north carolina", "north dakota", "nebraska", "new hampshire", "new jersey", "new mexico", "nevada", "new york", "ohio", "oklahoma", "oregon", "pennsylvania", "rhode island", "south carolina", "south dakota", "tennessee", "texas", "utah", "virginia", "vermont", "washington", "wisconsin", "west virginia", "wyoming"]

genders = ["male", "female", "nonbinary"]

orientations = ["straight", "homosexual", "bisexual", "pansexual"]


async def askage(dm):
    await dm.send("How old are you? Enter a number such as `25`")

    def age(msg):
        return msg.author == dm.recipient and msg.channel == dm
    msg = await bot.wait_for("message", check=age)
    return msg


async def askstate(dm):
    await dm.send("What state are you from? Answer in the whole name\nex: `California`, `New York`")

    def state(msg):
        return msg.author == dm.recipient and msg.channel == dm
    msg = await bot.wait_for("message", check=state)
    return msg


async def askgender(dm):
    await dm.send("What gender do you align most closely with? Answer with\n`male`, `female` or `nonbinary` only")

    def gender(msg):
        return msg.author == dm.recipient and msg.channel == dm
    msg = await bot.wait_for("message", check=gender)
    return msg


async def askorientation(dm):
    await dm.send("Finally, what orientation do you align most closely with? Answer with\n`straight`, `homosexual`, `bisexual` or `pansexual` only")

    def orientation(msg):
        return msg.author == dm.recipient and msg.channel == dm
    msg = await bot.wait_for("message", check=orientation)
    return msg


@bot.event
async def on_ready():
    print("onnline!")


@bot.event
async def on_member_join(member):
    dm = await member.create_dm()
    await dm.send("Hello there! Welcome to irl e-girls! Before I can let you in, I do need to ask a few questions.")

    async def tryage():
        msg = await askage(dm)
        if msg.content.isdigit():
            if int(msg.content) < 13:
                await dm.send("Sorry, you are too young for this server.")
                return False
            else:
                if int(msg.content) >= 13 and int(msg.content) <= 15:
                    role = discord.utils.get(
                        member.guild.roles, name="13-15")
                    await member.add_roles(role)
                elif int(msg.content) >= 16 and int(msg.content) <= 18:
                    role = discord.utils.get(
                        member.guild.roles, name="16-18")
                    await member.add_roles(role)
                else:
                    role = discord.utils.get(
                        member.guild.roles, name="19+")
                    await member.add_roles(role)
                return True
        else:
            await dm.send("That's not even a number???")
            await tryage()

    async def trystate():
        msg = await askstate(dm)
        if msg.content.lower() in states:
            lower = msg.content.lower()
            lol = ""
            x = lower.split(" ")
            for letter in x:
                letter = letter.capitalize()
                lol += letter + " "
            lol = lol.rstrip()
            role = discord.utils.get(
                member.guild.roles, name=lol)
            await member.add_roles(role)
            pass
        else:
            await dm.send("That's not a valid state!")
            await trystate()

    async def trygender():
        msg = await askgender(dm)
        if msg.content.lower() in genders:
            lower = msg.content.lower()
            capitalized = lower.capitalize()
            role = discord.utils.get(
                member.guild.roles, name=capitalized)
            await member.add_roles(role)
            pass
        else:
            await dm.send("That's not a valid gender!")
            await trygender()

    async def tryorientation():
        msg = await askorientation(dm)
        if msg.content.lower() in orientations:
            lower = msg.content.lower()
            capitalized = lower.capitalize()
            role = discord.utils.get(
                member.guild.roles, name=capitalized)
            await member.add_roles(role)
            pass
        else:
            await dm.send("That's not a valid orientation!")
            await tryorientation()
    oldenough = await tryage()
    if oldenough == True:
        await trystate()
        await trygender()
        await tryorientation()
        await dm.send("Thank you for answering these! You now have access to the server.")
        role = discord.utils.get(member.guild.roles, name="Verified Members")
        await member.add_roles(role)

bot.run(os.environ["token"])
