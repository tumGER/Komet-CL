import discord
from discord.ext import commands
from helpers.checks import check_if_staff
from helpers.userlogs import userlog


class ModNote:
    def __init__(self, bot):
        self.bot = bot

    @commands.guild_only()
    @commands.check(check_if_staff)
    @commands.command(aliases=["addnote"])
    async def note(self, ctx, target: discord.Member, *, note: str = ""):
        """Adds a note to a user, staff only."""
        userlog(target.id, ctx.author, note,
                "notes", target.name)
        await ctx.send(f"{target.mention}: noted!")

    @commands.guild_only()
    @commands.check(check_if_staff)
    @commands.command(aliases=["addnoteid"])
    async def noteid(self, ctx, target: int, *, note: str = ""):
        """Adds a note to a user by userid, staff only."""
        userlog(target, ctx.author, note,
                "notes")
        await ctx.send(f"{target.mention}: noted!")


def setup(bot):
    bot.add_cog(ModNote(bot))