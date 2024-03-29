import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import responses

load_dotenv()


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        if response:
            (
                await message.author.send(response)
                if is_private
                else await message.channel.send(response)
            )

    except Exception as e:
        print(e)


def run_discord_bot():
    token = os.getenv("DISCORD_TOKEN") or ""

    intents = discord.Intents.default()
    intents.message_content = True

    prefix = "!"

    client = commands.Bot(command_prefix=prefix, intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is ready.")

    @client.listen()
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")

        if user_message[0] == prefix:
            return
        else:
            await send_message(message, user_message, is_private=False)

    @client.command()
    async def roll(ctx):
        await ctx.send("Rolling...")

    @client.command()
    async def FTD(ctx): # FTD = "F**k the dealer (card game)"
        await ctx.send("FTD")
        message = await ctx.send("Players join within 10 seconds by reacting with a thumbs up")
        thumbs_up = "👍"
        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == thumbs_up

        ace  = await ctx.send("Vote Ace as 1 or 14")
        await message.add_reaction(thumbs_up)

        

    

    client.run(token)
