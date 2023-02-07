import discord
from discord.ext import discord

#main bot config

intents = discord.Intents.ALL()
bot = commands.Bot(command_prefix='>', intents=intents)

#main bot functions

@bot.event
async def on_ready(self):
    print(f"Logged into bot with {self.user}")

@bot.command()
async def ping(ctx):
    await ctx.reply('PONG')

#End Of Bot

bot.token('TOKEN')
