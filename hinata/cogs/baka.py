from discord.ext import commands
import discord
import requests_async as requests

class Baka(commands.Cog):
    def __init__(self, hinata):
        self.hinata = hinata

    async def retrieve_baka(self):
        res = await requests.get("https://nekos.life/api/v2/img/baka")
        return res.json()['url']

    @commands.command(help="Baka!")
    async def baka(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send(f"Must Include a member! {ctx.author.mention}")
        else:
            embed = discord.Embed(title="Hinata · Baka", colour=14522759)
            embed.set_image(url=await self.retrieve_baka())
            embed.description = f"{ctx.author.name} **called** {member.name} **a BAKA!** :("
            embed.set_footer(text=f"h?baka [@member]")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Baka(bot))