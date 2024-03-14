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
        name = "Pho King-eboy"
        responses = opggapi.retrieve_rank("na", name)
        if responses:
            url = str(responses[1]).replace(" ", "%20")

            embed = discord.Embed()
            embed.set_author(
                name=name.replace("-", "#"),
                url=url,
                # icon_url=responses[0],
            )
            # embed.set_thumbnail(url=responses[0])
            # embed.add_field(name="", value="LV. " + responses[4], inline=False)
            # embed.add_field(
            #     name="Ranked Solo/Duo",
            #     value=responses[1].title() + "\n" + responses[2] + " LP",
            #     inline=False,
            # )
            await ctx.send(embed=embed)
        else:
            await ctx.send("User not found.")

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
