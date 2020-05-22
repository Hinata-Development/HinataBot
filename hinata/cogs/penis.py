from discord.ext import commands
import discord, random

class Penis(commands.Cog):
    def __init__(self, hinata):
        self.hinata = hinata
        self.privileged_ids = [206696404347781120, 600781202617663617, 344163032433426442]

        self.min_length = 2
        self.max_length = 6

    def calculate_penis(self, user):
        if user.id in self.privileged_ids:
            return f"8{'='*10}D"
        else:
            return f"8{'='*random.randint(self.min_length, self.max_length)}D"

    @commands.command(help="Penis size.")
    async def penis(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.message.author

        embed = discord.Embed(title=f"Hinata · {member.name}'s Penis Length", description=self.calculate_penis(member), colour=14522759)
        embed.set_footer(text="This is 100% accurate.")
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Penis(bot))