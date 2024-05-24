# import datetime
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from commands import response, web

load_dotenv()


async def send_message(message, user_message, is_private):
    try:
        pass
        res = response.Responses(user_message)
        if res:
            (
                await message.author.send(res)
                if is_private
                else await message.channel.send(res)
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
        name = ctx.message.content.replace("!opgg", "").lstrip(" ")
        # print(name)
        res = web.OPGGApi.retrieve_rank("na", name)
        print(res)
        if res:
            url = str(res[1]).replace(" ", "%20")
            embed = discord.Embed()
            embed.set_author(
                name=name.replace("-", "#"),
                url=url,
                # icon_url=responses[0],
            )
            embed.set_thumbnail(url=res[0])
            embed.add_field(name="", value="LV. " + str(res[2]), inline=False)
            if res[3]:
                embed.add_field(
                    name="Ranked Solo/Duo",
                    value=str(res[3]) + "\n" + str(res[4]) + "\n" + str(res[5]),
                    inline=False,
                )
            else:
                embed.add_field(
                    name="Ranked Solo/Duo",
                    value="Unranked",
                    inline=False,
                )

            if res[6]:
                embed.add_field(
                    name="Ranked Flex",
                    value=str(res[6]) + "\n" + str(res[7]) + "\n" + str(res[8]),
                    inline=False,
                )
            else:
                embed.add_field(
                    name="Ranked Flex",
                    value="Unranked",
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
