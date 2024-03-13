import datetime
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

import opggapi
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
    TOKEN = os.getenv("DISCORD_TOKEN") or ""
    # OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

    intents = discord.Intents.default()
    intents.message_content = True

    prefix = "!"

    client = commands.Bot(command_prefix=prefix, intents=intents)

    # ai = openai.OpenAI(
    #     # This is the default and can be omitted
    #     api_key=os.environ.get("OPENAI_API_KEY"),
    # )

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
    async def opgg(ctx):
        # print(message)
        responses = opggapi.retrieve_rank("na", "Not Relapse-NA1")
        print(responses)
        responses[3] = str(responses[3]).replace(" ", "%20")

        embed = discord.Embed(
            title="pho king#eboy",
            description=responses[1] + " " + responses[2],
            url=str(responses[3]),
            color=discord.Color.random(),
        )
        embed.set_image(url=responses[0])
        print(responses[3])
        print(responses[0])
        await ctx.send(embed=embed)

    # FIX: pay for chat gpt to get tier 1 access
    #      can't use api because poor
    # @client.command()
    # async def gpt(ctx, message=""):

    #     if message == "":
    #         await ctx.send("Please provide a message to Chat GPT.")
    #         return
    #     else:
    #         response = ai.chat.completions.create(
    #             messages=[
    #                 {
    #                     "role": "user",
    #                     "content": "Say this is a test",
    #                 }
    #             ],
    #             model="gpt-3.5-turbo",
    #         )

    #         print(response.choices[0])

    client.run(TOKEN)
