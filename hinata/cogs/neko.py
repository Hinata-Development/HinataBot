from discord.ext import commands
import discord
import requests_async as requests

class Neko(commands.Cog):
    def __init__(self, hinata):
        self.hinata = hinata

    async def retrieve_neko(self):
        res = await requests.get("https://nekos.life/api/neko")
        return res.json()['neko']

    @commands.command(help="Neko!")
    async def neko(self, ctx):
        embed = discord.Embed(title="Hinata · Neko", colour=14522759)
        embed.set_image(url=await self.retrieve_neko())
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Neko(bot))