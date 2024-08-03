# This example requires the 'message_content' intent.

import discord
from discord.ext import commands
from wakeonlan import send_magic_packet
import os
from dotenv import load_dotenv

load_dotenv()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command()
@commands.has_role('Minecraft')
async def start(ctx):
    print("Starting computer")
    send_magic_packet(os.getenv("ADDRESS"))
    await ctx.send(f'Starting computer!')

@start.error
async def start_error(ctx, error):
    if isinstance(error, commands.MissingRole):
        await ctx.send("You do not have the required role to use this command.")

bot.run(os.getenv("TOKEN"))