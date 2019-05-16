import discord
import asyncio
from database import Db


class Uwu(discord.Client):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.redis_url = kwargs.get('redis_url')
        self.mongo_url = kwargs.get('mongo_url')
        self.loop = asyncio.get_event_loop()
        self.db = Db(self.redis_url, self.mongo_url, self.loop)

    async def on_ready(self):

        print('Logged on as', self.user)

        game = discord.Game("v1.0.0")
        await self.change_presence(status=discord.Status.dnd, activity=game)

    async def on_message(self, message):

        if message.content == ".daddy":
            if message.channel.id != 578399914187554857:
                await message.channel.send(
                    "<@552309563794128898> *is my creator and daddy*")

        if message.channel.id == 578399914187554857:
            if message.author == self.user:
                await message.delete(delay=7)

        if message.channel.id == 578399914187554857:
            print("boop")
            if message.author != self.user:
                print("boop2")
                await message.delete()

                redis = await self.db.get_storage(server=message.guild)

                value = await redis.get(key=str(message.author.id))

                print(value)

                if value == None:
                    await message.channel.send("*Successfully sent confession*")

                    await redis.set(key=str(message.author.id),
                                    value="derp", expire=300)

                    channel2 = self.get_channel(578399807652102144)

                    embed = discord.Embed(
                        title='Confession',
                        description=message.content,
                    )

                    embed.set_footer(text="All confessions are anonymous.")

                    await channel2.send(embed=embed)
                else:
                    await message.channel.send('*Please wait 5 mins before sending another confession*')
