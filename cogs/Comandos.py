import discord
import os
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


class Help(commands.Cog):
    def __init__(self,client):
        self.client = client

    
    @commands.command()
    async def help(self,message):
        await message.message.delete()
        os.system("cls")
        print(banner)
        print("""

>>> Marca uma pessoa para não conseguir digitar ( em Servidores)
        que Você tenha Permissão de Apagar Mensagens:

        ___________________________________
        |                                  |
        | Marcar: .target "ID de um membro"|
        |                                  |
        |       Desmarcar: targetOFF       |
        |__________________________________|


>>> Caso não Saiba pegar o ID de um usuário: .help_id;

>>> Apagar suas próprias mensagens DM/Servidores: .clean;

>>> Mudar a cor do CMD: .color;

>>> Limpar o CMD: .cmd;
        """)


def setup(client):
    client.add_cog(Help(client))