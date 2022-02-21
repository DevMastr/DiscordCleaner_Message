import os
from discord.ext import commands


class Help_ID_Target(commands.Cog):
    def __init__(self,client):
        self.client = client
    
    @commands.command()
    async def help_id(self,message):
        os.system("start https://www.arcanth.net/forum/threads/como-copiar-id-de-mensagens-usuarios-e-servidor-explicacao-sobre.2005/")
        await message.message.delete()
        return 1


def setup(client):
    client.add_cog(Help_ID_Target(client))