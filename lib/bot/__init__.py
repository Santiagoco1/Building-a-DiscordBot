from datetime import datetime

from apscheduler.schedulers.asyncio import AsyncIOScheduler
from discord import Embed, File
from discord.ext.commands import Bot as BotBase

PREFIX = "/"
OWNER_IDS = [700777123261972513]

class Bot(BotBase):
    def __init__(self):
        self.PREFIX = PREFIX
        self.ready = False
        self.guild = None
        self.schedule = AsyncIOScheduler()

        super().__init__(command_prefix=PREFIX, owner_ids=OWNER_IDS)

    def run(self, version):
        self.VERSION = version

        with open("./lib/bot/token.0", "r", encoding="utf-8") as tf:
            self.TOKEN = tf.read()

        print("Running Bot... ")
        super().run(self.TOKEN, reconnect=True)

    async def on_connect(self):
        print("Bot Connected")

    async def on_disconnect(self):
        print("Bot Disconnected")

    async def on_ready(self):
        if not self.ready:
            self.ready = True
            self.guild = self.get_guild(753667457310261368)
            # self.guild = self.guild(753667457310261368)
            print("Bot Ready")

            channel = self.get_channel(753667457310261371)
            await channel.send("Now online!")

            embed = Embed(tittle="Now Online!", description="GLaDOS is now online.", colour=0xFF0000, timestamp=datetime.utcnow())
            fields = [("Name", "Value", True),
                      ("Another field", "This field is next to the other one", True),
                      ("A non-inline field", "This field will appear on it's own row", False)]
            for name, value, inline in fields:
                embed.add_field(name=name, value=value, inline=inline)
            embed.set_author(name="Aperture Science Laboratories", icon_url=self.guild.icon_url)
            embed.set_footer(text="This is a footer!")
            embed.set_thumbnail(url=self.guild.icon_url)
            embed.set_image(url=self.guild.icon_url)
            await channel.send(embed=embed)

            await channel.send(file=File("./data/images/ApertureLaboratories.png"))

        else:
            print("Bot Reconnected")

    async def on_message(self, message):
        pass

bot = Bot()
