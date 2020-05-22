from discord.ext import commands
import discord

class About(commands.Cog):
    def __init__(self, hinata):
        self.hinata = hinata

    @commands.command(help="About Hinata.")
    async def about(self, ctx):
        embed = discord.Embed(title="Hinata · About", description="A bot made for fun.", colour=14522759)
        embed.set_thumbnail(url=self.hinata.user.avatar_url)
        embed.add_field(name="Servers", value=len(self.hinata.guilds), inline=True)
        embed.add_field(name="Members", value=len(self.hinata.users), inline=True)
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(About(bot))