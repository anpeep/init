from dotenv import dotenv_values
from discord import Intents, Message
from discord.ext import commands

config = dotenv_values(".env")
intents = Intents.default()
intents.message_content = True
client = commands.Bot(command_prefix="!", intents=intents)


@client.event
async def on_ready():
    print(f"{client.user} is now running!")


@client.event
async def on_message(message: Message):
    if message.author == client.user:
        return

    if message.content.startswith("!"):
        await client.process_commands(message)
        return


def main():
    token = config.get("TOKEN")
    if token is None:
        raise ValueError("loo fail nimega .env ja pane sinna BOT_TOKEN=isiklik Discord Developer Portal token")
    client.run(token)


if __name__ == "__main__":
    main()
