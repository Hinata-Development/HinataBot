from discord.ext import commands
import discord
import requests_async

class Kiss(commands.Cog):
    def __init__(self, hinata):
        self.hinata = hinata

    async def retrieve_kiss(self):
        res = await requests_async.get("https://nekos.life/api/kiss")
        return res.json()['url']

    @commands.command(help="Kiss!")
    async def kiss(self, ctx, member: discord.Member = None):
        if not member:
            await ctx.send(f"Must Include a member! {ctx.author.mention}")
        else:
            embed = discord.Embed(title="Hinata · Kiss", colour=14522759)
            kiss = await self.retrieve_kiss()
            embed.set_image(url=kiss)

            name = "themselves!" if member is ctx.message.author else member.name

            embed.description = f"{ctx.author.name} **kissed** {name}"
            embed.set_footer(text=f"h?kiss [@member]")
            await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Kiss(bot))