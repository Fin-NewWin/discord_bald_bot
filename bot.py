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
        # name = "Pho King-eboy"
        name = ctx.message.content.replace("!opgg", "").lstrip(" ")
        print(name)
        responses = opggapi.retrieve_rank("na", name)
        print(responses)
        if responses:
            url = str(responses[1]).replace(" ", "%20")
            embed = discord.Embed()
            embed.set_author(
                name=name.replace("-", "#"),
                url=url,
                # icon_url=responses[0],
            )
            embed.set_thumbnail(url=responses[0])
            embed.add_field(name="", value="LV. " + str(responses[2]), inline=False)
            embed.add_field(
                name="Ranked Solo/Duo",
                value=str(responses[3])
                + "\n"
                + str(responses[4])
                + "\n"
                + str(responses[5]),
                inline=False,
            )

            embed.add_field(
                name="Ranked Flex",
                value=str(responses[6])
                + "\n"
                + str(responses[7])
                + "\n"
                + str(responses[8]),
                inline=False,
            )
            await ctx.send(embed=embed)
        else:
            await ctx.send("User not found. Please input as `!opgg username-1234`")

    @client.command()
    async def FTD(ctx):  # FTD = "F**k the dealer (card game)"
        await ctx.send("FTD")
        message = await ctx.send(
            "Players join within 10 seconds by reacting with a thumbs up"
        )
        thumbs_up = "👍"

        def check(reaction, user):
            return user == ctx.author and str(reaction.emoji) == thumbs_up

        ace = await ctx.send("Vote Ace as 1 or 14")
        await message.add_reaction(thumbs_up)

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
