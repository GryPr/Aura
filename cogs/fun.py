import discord
from discord.ext import commands
import random


class Fun(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command()
    async def dab(self, ctx, user: discord.Member = None):
        # Checks if an argument is provided. If there is no argument, outputs author.
        if user:
            target = user
        else:
            target = ctx.author
        dab_images = [
            'https://i.imgur.com/Y0ZfhYv.jpg',
            'https://i.imgur.com/f2IRUHh.jpg',
            'https://i.imgur.com/dTztqJ8.jpg',
            'https://i.imgur.com/VcRn48o.jpg',
            'https://i.imgur.com/MFLFhw3.png',
            'https://i.imgur.com/HXtHTAa.jpg',
            'https://i.imgur.com/VEjxXxs.png',
            'https://i.imgur.com/5IgMBvG.jpg'
        ]
        embed = discord.Embed(title=f'Get dabbed on {target.name}!')
        embed.set_image(url=f'{random.choice(dab_images)}')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(Fun(client))