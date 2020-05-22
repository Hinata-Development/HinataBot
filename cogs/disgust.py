from discord.ext import commands
import discord
import requests_async

class Disgust(commands.Cog):
    def __init__(self, hinata):
        self.hinata = hinata
        self.url = "http://95.217.232.67/hinataapi/disgust?avatarurl="

    @commands.command(help="Disgust command.")
    async def disgust(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        avatar_url = member.avatar_url_as(format="png")
        req = await requests_async.get(f"{self.url}{avatar_url}")

        embed = discord.Embed(title="Hinata · Disgust", colour=14522759)
        embed.set_image(url=req.json()['url'])
        embed.set_footer(text="h?disgust [@member]")
        await ctx.send(embed=embed)


def setup(bot):
    bot.add_cog(Disgust(bot))