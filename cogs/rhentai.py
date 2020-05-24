from discord.ext import commands
import discord
import requests

class Rhentai(commands.Cog):
    def __init__(self, hinata):
        self.hinata = hinata

    def retrieve_rhentai(self):
        res = requests.get("https://nekos.life/api/v2/img/Random_hentai_gif")
        return res.json()['url']

    @commands.is_nsfw()
    @commands.command(help="Rhentai!")
    async def rhentai(self, ctx):
        embed = discord.Embed(title="Hinata - Rhentai", colour=14522759)
        embed.set_image(url=self.retrieve_rhentai())
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Rhentai(bot))