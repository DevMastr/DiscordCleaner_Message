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


class Color_Change(commands.Cog):
    def __init__(self,client):
        self.client = client


    @commands.command()
    async def color(self,message,cor=None):
        if cor == None:
            os.system("cls")
            await message.message.delete()
            print("""
As cores são:

0- Preto
1- Azul
2- Verde
3- Aqua
4- Vermelho
5- Roxo
6- Amarelo
7- Branca -- Default
8- Cinza
9- Azul-claro
a- verde-claro
b- Água-clara
c- Vermelho claro
d- Roxo claro
e- Amarelo-claro
f- Branco brilhante

Exemplo:
    Digite "color a"
""")
        else:
            await message.message.delete()
            os.system("cls")
            os.system(f"color {cor}")
            print(banner)
        

def setup(client):
    client.add_cog(Color_Change(client))