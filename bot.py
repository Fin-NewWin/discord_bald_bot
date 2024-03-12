import os

import discord
from dotenv import load_dotenv

import responses

load_dotenv()


async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
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
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f"{client.user} is ready.")

    @client.event
    async def on_message(msg):
        if msg.author == client.user:
            return

        username = str(msg.author)
        user_message = str(msg.content)
        channel = str(msg.channel)

        print(user_message)

        print(f"{username} said: '{user_message}' ({channel})")

        await send_message(msg, user_message, is_private=False)

    client.run(token)
