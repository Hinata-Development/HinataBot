import discord
from discord.ext import commands

class EventHandler:
    def __init__(self, hinata):
        self.hinata = hinata
        self.ignored_errors = (commands.CommandNotFound, commands.UserInputError)

        @self.hinata.bot.event
        async def on_ready():
            await self.hinata.bot.change_presence(activity=discord.Game(name=f"{self.hinata.prefix}help"))
            print("[>] Hinata is ready!")

        @self.hinata.bot.event
        async def on_command_error(ctx, error):
            if isinstance(error, self.ignored_errors):
                return

            if isinstance(error, commands.MissingPermissions):
                embed = discord.Embed(title="Error! <a:HinataCry:710280345379143741>", colour=14522759)
                embed.description = f"Error! \n** Type: **{error}**"
                await ctx.send(embed=embed)

            if isinstance(error, commands.BotMissingPermissions):
                embed = discord.Embed(title="Error! <a:HinataCry:710280345379143741>", colour=14522759)
                embed.description = "I need permission to embed links to use this command!"
                embed.colour = 14522759
                await ctx.send(embed=embed)

            if isinstance(error, commands.NSFWChannelRequired):
                embed = discord.Embed(title="Error! <a:HinataCry:710280345379143741>", colour=14522759)
                embed.description = f"Unable to use **{self.hinata.prefix}{ctx.command}** in non **NSFW** channels!   \n\n Type: **{error}**"
                await ctx.send(embed=embed)


        print("[>] Loaded Events.")