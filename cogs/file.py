import discord
from discord.ext import commands

banner = """
--------------------------------------------------------------------------------------
  _____  _                       _                                            
 |  __ \(_)                     | |                                           
 | |  | |_ ___  ___ ___  _ __ __| |                                           
 | |  | | / __|/ __/ _ \| '__/ _` |                                           
 | |__| | \__ \ (_| (_) | | | (_| |                                           
 |_____/|_|___/\___\___/|_|  \__,_|
    ____ ___                             __  __ 
  / ____|| |                            |  \/  |                               
 | |     | | ___  __ _ _ __   ___ _ __  | \  / | ___  ___ ___  __ _  __ _  ___ 
 | |     | |/ _ \/ _` | '_ \ / _ \ '__| | |\/| |/ _ \/ __/ __|/ _` |/ _` |/ _ \\
 | |____ | |  __/ (_| | | | |  __/ |    | |  | |  __/\__ \__ \ (_| | (_| |  __/
  \_____||_|\___|\__,_|_| |_|\___|_|    |_|  |_|\___||___/___/\__,_|\__, |\___|
                                                                    __/ |     
                                                                   |___/  
Author: Winaline  


>>> Para ver os Comandos, envie: (.help) em algum lugar no discord
           Todos os comandos devem ser enviados no Discord
--------------------------------------------------------------------------------------"""


class Example(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_connect(self):
        print(banner)
        print(f"\nLogado como: {self.client.user.name}")


def setup(client):
    client.add_cog(Example(client))
