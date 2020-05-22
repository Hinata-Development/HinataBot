from discord.ext import commands
import discord

import requests_async as requests

class Anal(commands.Cog):
    def __init__(self, hinata):
        self.hinata = hinata

    async def retrieve_anal(self):
        res = await requests.get("https://nekos.life/api/v2/img/anal")
        return res.json()['url']

    @commands.is_nsfw()
    @commands.command(help="Anal!")
    async def anal(self, ctx):
        embed = discord.Embed(title="Hinata · Anal", colour=14522759)
        embed.set_image(url=await self.retrieve_anal())
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Anal(bot))