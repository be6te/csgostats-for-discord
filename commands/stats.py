import discord
from discord.ext import commands
from core.APIRequests import RequestAPI
from core.scraper import scraperw
from core.ranks import csgo_ranks
scrape = scraperw()
request_api = RequestAPI()

class csgo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command()
    async def tracker(self, ctx, url, contx: str=None):
        searching = discord.Embed(
            color = 0x313338,
            description=':mag: Searching: `{}`'.format(url)
        )
        try:
            data = request_api.CSGOStats(final_url=url)

            if data == False:
                embed = discord.Embed(
                    color = 0x313338,
                    description = 'This account has no registered matches.'
                )
                return await ctx.send(embed=embed)

            steamid = request_api.GetSteamID(url=url)
            steam_name = scrape.PlayerName(f'https://csgostats.gg/player/{steamid}').split('<div id="player-name">')[0]
            steam_avatar = request_api.AvatarURL(user=steamid)
            
            embed = discord.Embed(
                title = f'{steam_name}',
                color = 0x313338
            )
            embed.add_field(name='K/D:', value=data['overall']['kpd'], inline=True)
            embed.add_field(name='HLTV Rating:', value=data['overall']['rating'], inline=True)
            embed.add_field(name='Headshot Accuracy:', value=f"{data['overall']['hs']}%", inline=True)
            embed.add_field(name='ADR:', value=f"{data['overall']['adr']}%", inline=True)
            embed.add_field(name='Win Rate:', value=f"{data['overall']['wr']}%", inline=True)
            embed.add_field(name='Clutch Success:', value=f"1v1: {data['overall']['1v1']}% | 1v2: {data['overall']['1v2']}% | 1v3: {data['overall']['1v3']}% | 1v4: {data['overall']['1v4']}% | 1v5: {data['overall']['1vX']}%", inline=True)
            embed.add_field(name='Matchmaking Played:', value=f"{data['totals']['overall']['games']}", inline=True)
            embed.add_field(name='Matchmaking Wins:', value=f"{data['totals']['overall']['wins']}", inline=True)
            embed.add_field(name='Matchmaking Losses:', value=f"{data['totals']['overall']['losses']}", inline=True)
            embed.add_field(name='Rounds Played:', value=f"{data['totals']['overall']['rounds']}", inline=True)
            embed.add_field(name='Total Headshots:', value=f"{data['totals']['overall']['HS']}", inline=True)
            embed.add_field(name='Total Damage:', value=f"{data['totals']['overall']['dmg']}", inline=True)
            embed.add_field(name='Competitive Wins', value=f"{data['comp_wins']}", inline=True)
            file = discord.File(f'ranks/{data["rank"]}.png', filename=f'{data["rank"]}.png')
            
            try:
                best_rank = csgo_ranks[data['rank']]
            except:
                best_rank = 'Unknown'
            try:
                current_rank = csgo_ranks[data['best']['rank']]
            except:
                current_rank = 'Unknown'
                
            embed.set_thumbnail(url=f'attachment://{data["rank"]}.png')
            embed.set_footer(text=f"ID: {steamid} | Current Rank: {best_rank} | Peak Rank: {current_rank} | Powered by csgostats.gg", icon_url=steam_avatar)
            await ctx.send(file=file, embed=embed)
        except:
            embed = discord.Embed(
                color = 0xff0008,
                description='Ooops, I think this account is private or an error occurred.'
            )
            await ctx.send(embed=embed)

async def setup(bot):
    await bot.add_cog(csgo(bot=bot))