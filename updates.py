import discord
from discord.ext import commands

class updates:
    """Show Compelled's Latest Updates"""

    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def updates(self):
        """Show Compelled's Latest Updates"""

        embed = discord.Embed(title=":fire: Compelled Updates :fire:", description=":regional_indicator_u::regional_indicator_p::regional_indicator_d::regional_indicator_a::regional_indicator_t::regional_indicator_e::regional_indicator_s:", color=0x00ff00)
        embed.add_field(name=":white_check_mark: Added the Ping command.", value=" **.ping**")
        embed.add_field(name=":white_check_mark: Added the Support Application Command.", value=" **.apply**", inline=False)
        embed.add_field(name=":white_check_mark: Added the Updates command to show this message.", value=" **.updates**", inline=False)
        embed.add_field(name=":white_check_mark: Added the Partnership command.", value=" **.partner**", inline=False)
        embed.add_field(name=":white_check_mark: Added the Dueling command.", value=" **.duel**", inline=False)
        embed.add_field(name=":white_check_mark: Fixed all commands including gif and audio functions.", value="**.help**", inline=False)
        embed.add_field(name=":white_check_mark: Fixed a couple bugs", value="**.help**", inline=False)
        embed.add_field(name=":x: There are no more updates to list, please check back later.", value=":wave:", inline=False)
        await self.bot.say(embed=embed)



def setup(bot):
    bot.add_cog(updates(bot))
