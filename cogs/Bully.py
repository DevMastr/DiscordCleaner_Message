import discord
import os,time
import json
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

def escrever_json(dados):
    with open('dados.json', 'w', encoding='utf8') as f:
        json.dump(dados, f, ensure_ascii=False, sort_keys=True, indent=4, separators=(',', ':'))


def ler_json(arq_json):
    with open(arq_json, 'r', encoding='utf8') as f:
        return json.load(f)


class Target(commands.Cog):
    def __init__(self,client):
        self.client = client
        

    @commands.command()
    async def target(self,message,member_id=None):
        if member_id == None:
            os.system("cls")
            print(banner)
            print('\n| Syntaxe: .target "ID de um Membro" |\n\nNão sabe encontrar o ID?, Digite: .help_id')
            return 0
        os.system("cls")
        print(banner)
        alvo = {"member_id": member_id}
        escrever_json(alvo)
        print(f"{'-'*10}\nAlvo Selecionado\nTarget Ligado")
        await message.message.delete()

    @commands.Cog.listener()
    async def on_message(self,message):
        try:
            data = ler_json('dados.json')
            if message.author.id == self.client.user.id:
                if message.content == "targetOFF":
                    print(f"Target Desativado\n{'-'*10}")
                    os.remove('dados.json')
                    await message.message.delete()
            if message.author.id == int(data['member_id']):
                await message.channel.last_message.delete()
        except:
            pass


        

    
        
def setup(client):
    client.add_cog(Target(client))