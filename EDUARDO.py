import discord
import secret
import io
from random import *
import requests
import time
import asyncio
from datetime import datetime
import re
import os
import websockets
import aiohttp
import json
from googletrans import Translator
from io import BytesIO
from PIL import Image, ImageDraw, ImageFont, ImageOps


client = discord.Client()


COR = 0xffce0a
COR = 0x23ef90

token = secret.seu_token()
msg_id = None
msg_user = None

@client.event
async def on_ready():
    print('BOT ONLINE - Olá Mundo!')
    print(client.user.name)
    print("Nome do bot: {}".format(client.user.name))
    print("Logado em {} servidores".format(len(client.servers)))
    print(client.user.id)
    print('--------Eduardo-------')
    while True:
        script = "Online em " + str(len(client.servers)) + " servidores | " + str(len(set(client.get_all_members()))) + " usuários | " + str(len(set(client.get_all_channels()))) + " canais."
        await client.change_presence(game=discord.Game(name=script, url='https://www.twitch.tv/eduardokng', type=1))
        await asyncio.sleep(15)
        script2 = 'xy.ajuda ou xy.help para meus cmd'
        await client.change_presence(game=discord.Game(name=script2), status=discord.Status.dnd)
        await asyncio.sleep(15)

@client.event
async def on_message(message):
    if message.author.bot:
        return
 
    if message.content.startswith('xy.hug'):
        try:
            resultado = hug_gif()
            usuario = message.mentions[0]
            embed_kiss = discord.Embed(title="\n", description='{} Acabou de abraçar o(a) Usuario(a) {}!'.format(
                message.author.mention, usuario.mention), color=0x751975)
            embed_kiss.set_image(url=resultado)
            embed_kiss.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=embed_kiss)
        except:
            await client.send_message(message.channel, 'Você precisa mencionar um usuario para abraçar!')

    if message.content.lower().startswith('<@429376853162197002>'):
        await client.delete_message(message)
        await client.send_message(message.channel, "<:ping:450749734391644162> Vai fazer alguma coisa da vida, e para de ficar me mencionando <:REEEEE:450784770759065610>")

    if message.content.lower().startswith('xy.teste'):
        await client.delete_message(message)
        await client.send_message(message.channel, "__Olá Mundo, estou vivo!__")


    if message.content.lower().startswith('xy.sobre'):
        embed = discord.Embed(
            title="Quem sou eu?",
            color=0x03c3f5,
            description="Um bot criado para te ajudar em seu servidor;\n"
                        "Se tiver dúvida sobre mim use **xy.help|xy.ajuda** pra saber os meus comandos;\n"
                        "Se não conseguir ativar nenhum comando meu, entre em contato com o meu dono.", )
        embed.add_field(name='Estou online em', value='\n' + (str(len(client.servers))) + ' Servidores')
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('xy.votar'):
        await client.add_reaction(message, '✅')
        await client.add_reaction(message, '❌')

    elif message.content.lower().startswith('xy.avatar'):

        try:
            member = message.mentions[0]
            embed = discord.Embed(
                title="",
                color=0x03c3f5,
                description='[Click here](' + member.avatar_url + ') para acessar o link do avatar de {}! '.format(member.name))

            embed.set_image(url=member.avatar_url)
            await client.send_message(message.channel, embed=embed)

        except:
            member = message.author
            embed = discord.Embed(
                title='Your avatar'.format(member.name),
                color=0x03c3f5,
                description='[Click here](' + member.avatar_url + ') para acessar o link do seu Avatar  '.format(member.name))

            embed.set_image(url=member.avatar_url)
            await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('xy.ping'):
        timep = time.time()
        emb = discord.Embed(title='Aguarde...', color=0x009C7A)
        pingm0 = await client.send_message(message.channel, embed=emb)
        ping = time.time() - timep
        pingm1 = discord.Embed(title='Pong!', description='<:load:459496192192151554>Tempo de Resposta - %.01f segundos' % ping,
                               color=0x009C7A)
        await client.edit_message(pingm0, embed=pingm1)

    if message.content.startswith('xy.game'):
        if not message.author.id == "319253966586118146":
            return await client.send_message(message.channel, '❎ | Você não tem permisão para usar esse comando')
        game = message.content[7:]
        await client.delete_message(message)
        await client.change_presence(game=discord.Game(name=game, url='https://www.twitch.tv/eduardokng', type=1))
        await client.send_message(message.channel, "Meu status foi trocado para: " + game + "")
    
    if message.content.startswith('xy.watch'):
        if not message.author.id == "319253966586118146":
            return await client.send_message(message.channel, '❎ | Você não tem permisão para usar esse comando')
        game = message.content[9:]
        await client.delete_message(message)
        await client.change_presence(game=discord.Game(name=game, url='https://www.twitch.tv/eduardokng', type=3))
        await client.send_message(message.channel, "Meu status foi trocado para: " + game + "")

    if message.content.startswith('xy.listen'):
        if not message.author.id == "319253966586118146":
            return await client.send_message(message.channel, '❎ | Você não tem permisão para usar esse comando')
        game = message.content[10:]
        await client.delete_message(message)
        await client.change_presence(game=discord.Game(name=game, url='https://www.twitch.tv/eduardokng', type=2))
        await client.send_message(message.channel, "Meu status foi trocado para: " + game + "")

    elif message.content.lower().startswith('xy.userinfo'):
        try:
            user = message.mentions[0]
            server = message.server
            embedinfo = discord.Embed(title='Informações do usuário', color=0x03c3f5, )
            embedinfo.set_thumbnail(url=user.avatar_url)
            embedinfo.add_field(name='<:user:439213886865014784> Usuário:', value=user.name)
            embedinfo.add_field(name='<:usershield:458046233559433235> Apelido', value=user.nick)
            embedinfo.add_field(name='<:cracha:458046812037709836> ID:', value=user.id)
            embedinfo.add_field(name='<:entrada:458046233387204608> Entrou em:', value=user.joined_at.strftime("%d %b %Y às %H:%M"))
            embedinfo.add_field(name=":beginner:  Status:", value=user.status)
            embedinfo.add_field(name=':video_game: Jogando:', value=user.game)
            embedinfo.add_field(name='<:role:458048577114079234>Cargos:', value=([role.name for role in user.roles if role.name != "@everyone"]))
            await client.send_message(message.channel, embed=embedinfo)
        except ImportError:
            await client.send_message(message.channel, 'Buguei!')
        except:
            await client.send_message(message.channel, '<:perfilnegado:447911647303172106> | Mencione um usuário válido!')
        finally:
            pass

    if message.content.lower().startswith("xy.cargo"):
            embed1 = discord.Embed(
                title="_Escolha seu Cargo!_ ",
                color=0x03c3f5,
                description="- Otaku = 🈸\n"
                            "- Zueiro  =  🎉 \n"
                            "- Geek = 💎\n"
                            "- Nerd = 👓\n"
                            "- Artista = 🎨\n"
                            "- Gamer  = 🎮 \n"
							"- Depressivo = 😭\n", )

            botmsg = await client.send_message(message.channel, embed=embed1)

            await client.add_reaction(botmsg, "🈸")
            await client.add_reaction(botmsg, "🎉")
            await client.add_reaction(botmsg, "💎")
            await client.add_reaction(botmsg, "👓")
            await client.add_reaction(botmsg, "🎨")
            await client.add_reaction(botmsg, "🎮")
			await client.add_reaction(botmsg, "😭")
			
            global msg_id
            msg_id = botmsg.id

            global msg_user
            msg_user = message.author

    @client.event
    async def on_reaction_add(reaction, user):
        msg = reaction.message

        if reaction.emoji == "🈸" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Otaku", msg.server.roles)
            await client.add_roles(user, role)
            print("add")

        if reaction.emoji == "🎉" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Zueiro", msg.server.roles)
            await client.add_roles(user, role)
            print("add")

        if reaction.emoji == "💎" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Geek", msg.server.roles)
            await client.add_roles(user, role)
            print("add")

        if reaction.emoji == "👓" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Nerd", msg.server.roles)
            await client.add_roles(user, role)
            print("add")

        if reaction.emoji == "🎨" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Artista", msg.server.roles)
            await client.add_roles(user, role)
            print("add")

        if reaction.emoji == "🎮" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Gamer", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
		
		if reaction.emoji == "" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Depressivo", msg.server.roles)
            await client.add_roles(user, role)
            print("add")
			

    @client.event
    async def on_reaction_remove(reaction, user):
        msg = reaction.message

        if reaction.emoji == "🈸" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Otaku", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")

        if reaction.emoji == "🎉" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Zueiro", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")

        if reaction.emoji == "💎" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Geek", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")

        if reaction.emoji == "👓" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Nerd", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")

        if reaction.emoji == "🎨" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Artista", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")

        if reaction.emoji == "🎮" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Gamer", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")
		
		if reaction.emoji == "🈸" and msg.id == msg_id:  # and user == msg_user:
            role = discord.utils.find(lambda r: r.name == "Depressivo", msg.server.roles)
            await client.remove_roles(user, role)
            print("remove")
	

	
    if message.content.lower().startswith('xy.cair'):
        embed = discord.Embed(title='Eu vou cair fora mermão',
                              color=0x751975,
                              description='Um cara dizendo que vai cair fora',)
        embed.set_image(
            url="https://cdn.discordapp.com/attachments/436570816701005833/437316419110043668/tenor.gif")
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('xy.boa noite'):
        embed = discord.Embed(title="Boa noite 🌚", color=0x751975)
        await client.delete_message(message)
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith('xy.bom dia'):
        embed = discord.Embed(title="Bom dia 🌞", color=0x751975)
        await client.delete_message(message)
        await client.send_message(message.channel, embed=embed)

    elif message.content.lower().startswith('xy.serverinfo'):
        server = message.server
        embedserver = discord.Embed(
            title='Informações do Servidor',
            color=0x03c3f5,
            descripition='Essas são as informações\n')
        embedserver = discord.Embed(name="{} Server ".format(message.server.name), color=0x551A8B)
        embedserver.add_field(name=":busts_in_silhouette: Nome:", value=message.server.name, inline=True)
        embedserver.add_field(name=":crown:Dono:", value=message.server.owner.mention)
        embedserver.add_field(name=":id: ID:", value=message.server.id, inline=True)
        embedserver.add_field(name="Cargos:", value=len(message.server.roles), inline=True)
        embedserver.add_field(name=":family:Membros:", value=len(message.server.members), inline=True)
        embedserver.add_field(name=":date: Criado em:", value=message.server.created_at.strftime("%d %b %Y %H:%M"))
        embedserver.add_field(name="Emojis:", value=f"{len(message.server.emojis)}/100")
        embedserver.add_field(name=":flag_eu:Região:", value=str(message.server.region).title())
        embedserver.set_thumbnail(url=message.server.icon_url)
        embedserver.set_footer(text="By: IamEduardo#6790")
        await client.send_message(message.channel, embed=embedserver)

    if message.content.lower().startswith('xy.frases'):
        choice = random.randint(1,9)
        if choice == 1:
            await client.send_message(message.channel, 'É patetico desisitir de algo sem nem mesmo ter tentado" ')
        if choice == 2:
            await client.send_message(message.channel, ' Nós não sabemos que tipo de pessoas realmente somos até um momento antes da nossa morte. Assim que a morte vier abraçá-lo você perceberá o que você é ')
        if choice == 3:
            await client.send_message(message.channel, ' Quem diz que não pode ser feito nunca deve interromper aquele que está fazendo. ')
        if choice == 4:
            await client.send_message(message.channel, ' Pesadelos não duram para sempre. Um dia você acorda e eles se foram. ')
        if choice == 5:
            await client.send_message(message.channel, ' Com grandes poderes vem grandes responsabilidades. ')
        if choice == 6:
            await client.send_message(message.channel, 'Eles querem saber como realmente você é. Então mostra a parte ruim a eles e todos se afastam.')
        if choice == 7:
            await client.send_message(message.channel, 'As pessoas não podem ser perfeitas, todo o mundo acredita em sua própria mentira...')
        if choice == 8:
            await client.send_message(message.channel, 'Fácil é apagar todas as fotos, o difícil mesmo é apagar todos os momentos em que eu estive contigo')
        if choice == 9:
            await client.send_message(message.channel, 'A vida não te ensina a ser forte, ela te obriga a ser forte')


    elif message.content.lower().startswith('xy.help') or message.content.lower().startswith('xy.ajuda'):

        embedhelp = discord.Embed(
            title="**Ajuda do Galaxy**",
            color=0x03c3f5,
            description="Te enviei os meus comandos no seu DM, por favor olhe as suas mensagens diretas :mailbox_with_mail:!\n"
                        "**Meu Servidor de Suporte** \n"
                         "**https://discord.gg/CMKUyRu**\n"
                         "**Meus 2 websites**\n"
                        "https://wanted-dashboard-bot.jimdosite.com/ \n "
                        "https://galaxy-xy.glitch.me/\n"                  
                        "**Me invite para seu servidor**\n"
                        "https://goo.gl/R6Tn7K\n"
                        "**Fui desenvolvido em <:python:447909397276917760>**", )
        embedhelp.set_thumbnail(
            url='https://cdn.discordapp.com/attachments/436540739552542733/449274988378456064/ajuda.png')
        embedhelp.set_footer(text="By: IamEduardo#6790")
        msg =await client.send_message(message.channel, embed=embedhelp, content=message.author.mention)
        await client.add_reaction(msg, ':mail:450383163567374338')
        await client.add_reaction(msg, ':prize:447911648569720832')
        embedhelp = discord.Embed(
            title=":bookmark: Comandos",
            color=0x03c3f5,
            description="**Eu ainda estou em desenvolvimento mais tenho esses comandos que de alguma forma o ajudará**\n"
                        "**xy.teste**   | Comando para saber se estou funcionado em seu servidor \n"
                        "**xy.help e xy.ajuda**  | Irei lhe enviar essa mensagem de **Help**\n"
                        "**xy.sobre**  | Irei dizer um pouco sobre mim e irei mostrar minhas informaçoes atuais\n"
                        "**xy.userinfo**  | Irei lhe mostrar as informaçoes do usuario mencionado\n "
                        "**xy.serverinfo** |  Irei lhe enviar as informaçoes do servidor atual\n" 
                        "**xy.avatar**  | Irei lhe mandar o avatar do usuario mencionado\n"
                        "**xy.votar** (mensagem)| Irei enviar uma votação de :white_check_mark: ou :x: na sua mensagem\n"
                        "**xy.ping**  | Irei lhe responder com Pong! \n"
                        "xy.bom dia | Irei lhe dar um bom dia ensolarado \n"
                        "xy.boa noite | Irei lhe dar uma boa noite estrelada \n"
                        "**xy.invite** | Te mando o invite para me add no seu serve e também envio a você o meu server de suporte \n"
                        "xy.cair | Verá um cara caindo fora da treta\n"
                        "xy.hug | Para receber um abraço de um user basta escrever: xy.hug @User \n"
                        "xy.gif | Você pode pedir um gif que quiser, basta dar: xy.gif BTS(exemplo de gif) \n"
                        "Existem outros comandos, que só podem ser utilizados em meu suporte. ",)
        embedhelp.set_footer(text="By: IamEduardo⚡")
        await client.send_message(message.author, embed=embedhelp)

    elif message.content.lower().startswith('xy.invite'):

        embedinvite = discord.Embed(
            title="Aqui estão os meus convites!!",
            color=0x03c3f5,
            description="**Aqui está o convite para me adicionar no seu servidor ou meu servidor de suporte ;D**\n"
                        ":sos: Servidor de Suporte\n"
                        "https://goo.gl/Y4LsjF \n"
                        "Me convide para seu servidor\n"
                        "https://goo.gl/C17xKi", )
        await client.send_message(message.channel, embed=embedinvite)

    if message.content.lower().startswith('xy.dog'):
        async with aiohttp.get('https://random.dog/woof.json') as r:
            if r.status == 200:
                js = await r.json()
                canal = message.channel
                await client.delete_message(message)
                await client.send_message(canal, js['url'])


    if message.content.startswith('xy.uptime') or message.content.lower().startswith('xy.time'):
        await client.send_message(message.channel,
                                  ":alarm_clock: **Estou a {0} horas e {1} minutos online.**".format(hour, minutes,
                                                                                                    message.server))


    async def up_time():
        await client.wait_until_ready()
        global minutes
        minutes = 0
        global hour
        hour = 0
        while not client.is_closed:
            await asyncio.sleep(60)
            minutes += 1
            if minutes == 60:
                minutes = 0
                hour += 1

    client.loop.create_task(up_time())


    if message.content.startswith('xy.fale'):
        if message.author.id == '429376853162197002':
            return
        try:
            mensagem = message.content[7:]
            await client.send_message(message.channel, mensagem, tts=False)
            await client.delete_message(message)
            print('Fale on')
            print(mensagem)
        except:
            await client.send_message(message.channel, "Você precisa escrever algo para eu falar!")

    if message.channel == client.get_channel('449611356799369247'):
        await client.add_reaction(message, ":correto:447911578478706700")
        await client.add_reaction(message, ":errado:439213886047256577")

	

    elif message.content.lower().startswith("xy.eval"):
        if not message.author.id == '319253966586118146':
            return await client.send_message(message.channel, '<:aviso:447911820234194964>**Sem Permissão**')
        try:
            embedeval1 = discord.Embed(title='\n', description='\n')
            embedeval1.add_field(name='**:inbox_tray: Entrada**', value='`' + message.content[7:] + '`')
            embedeval1.add_field(name='**:outbox_tray: Saída**', value='`' + str(eval(message.content[7:])) + '`')
            await client.send_message(message.channel, embed=embedeval1)
            await client.add_reaction(message, ':correto:447911578478706700')

        except Exception as e:
            embedeval = discord.Embed(title='\n', description='\n')
            embedeval.add_field(name='**:inbox_tray: Entrada**', value='`' + message.content[7:] + '`')
            embedeval.add_field(name='**:outbox_tray: Saída**', value='`' + repr(e) + '`')
            await client.send_message(message.channel, embed=embedeval)
            await client.add_reaction(message, ':errado:439213886047256577')

    if message.content.startswith('xy.gif'):
        try:
            tag = message.content[6:]
            resultado = giphy_api(tag)
            embed_gif = discord.Embed(title="\n", description='\n', color=0x23ef90)
            embed_gif.set_image(url=resultado)
            embed_gif.set_footer(text=client.user.name, icon_url=client.user.avatar_url)
            await client.send_message(message.channel, embed=embed_gif)
        except:
            await client.send_message(message.channel, 'Não encontrei nenhuma gif para essa tag!')

    if message.content.lower().startswith('xy.emoji'):
        embed = discord.Embed(
            title='Todos os emojis do Galaxy',
            description='<:user:439213886865014784>; <:usuarionegado:447911609772539905>; <:pic:447909389278642201>; <:ID:439211809401208843>; <:errado:439213886047256577>; <:webdesign:439211554924396544>; <:errorbot:447911653774721026>; <:correto:439211809749336064>;\n'
                        '<:informao:459443407685681162>; <:hora1:459443848536522782>; <:termometro1:459443407547531274>; :cloud_rain: ; <:nuvem:459443407274770444>; \n'
                        '<a:rainbow_python:471032257713274901>; \n'



                        '\n'
                        '\n'
                        '\n'.format(message.author.mention),
            color=0x55ACEE
        )
        await client.send_message(message.channel, embed=embed)

    if message.content.lower().startswith("!tradutor"):
        try:
            msg = message.content[10:12]
            msg2 = message.content[13:]
            translator = Translator()
            traduzido = translator.translate(msg2, dest=msg).text
            nome = "Texto antes da tradução : ```" + msg2 + "```\nTexto traduzido : ```" + traduzido + "```"
            embed = discord.Embed(colour=0x009C7A)
            embed.add_field(name="Aqui está o texto traduzido que você pediu!⠀", value=nome)
            embed.set_thumbnail(url="https://cdn.discordapp.com/attachments/436540739552542733/459818415243395082/white-google-translate-512.png")
            embed.set_footer(text="Galaxy👑 2k18")
            await client.send_message(message.channel, embed=embed)
        except Exception as e:
            await client.send_message(message.channel, "Erro. Não é possível traduzir isso!")

    if message.content.lower().startswith('xy.clima'):
        try:
            s = message.content[7:]
            url = 'http://api.apixu.com/v1/current.json?key=7fa4b4027a2349e8b44114046182304&q=' + s
            r = requests.get(url)
            if r.status_code == 200:
                js = r.json()
                nome = js['location']['name']
                regiao = js['location']['region']
                pais = js['location']['country']
                zona = js['location']['tz_id']
                tempo = js['location']['localtime']
                att = js['current']['last_updated']

                temp = str(js['current']['temp_c']) + "°C"
                temp2 = str(js['current']['temp_f']) + "°F"
                tenp = str(js['current']['feelslike_c']) + "°C"
                tenp2 = str(js['current']['feelslike_f']) + "°F"

                icon = "http:" + str(js['current']['condition']['icon'])
                umi = str(js['current']['humidity']) + "%"
                vento = str(js['current']['wind_kph']) + "km/h"
                ventof = str(js['current']['wind_degree']) + "km/p"
                ventog = str(js['current']['wind_dir'])
                chuva = str(js['current']['precip_mm'])
                nuvem = str(js['current']['cloud'])
            aa = "\n🔹Cidade : " + nome + "\n🔹Região : " + regiao + "\n🔹País : " + pais
            bb = "\n🔹Fuso : " + zona + "\n🔹Local : " + tempo + "\n🔹Última atualização : " + att
            cc = "\n🔹Celsius : " + temp + "\n🔹Fahrenheit : " + temp2 + "\n🔹Sensação : " + tenp + "/" + tenp2
            dd = "\n🔹Nuvem : " + nuvem + "%\n🔹Quantidade : " + chuva + "mm\n🔹Umidade : " + umi
            ee = "\n🔹Velocidade : " + vento + "\n🔹Força: " + ventof + "\n🔹Direção : " + ventog + " [[String]](http://snowfence.umn.edu/Components/winddirectionanddegreeswithouttable3.htm)"
            embed = discord.Embed(colour=0x98ADE5)
            embed.add_field(name="<:informao:459443407685681162> Informação do Local", value=aa)
            embed.add_field(name="<:hora1:459443848536522782> Hora", value=bb)
            embed.add_field(name="<:termometro1:459443407547531274> Temperatura", value=cc)
            embed.add_field(name=":cloud_rain: Chuva", value=dd)
            embed.add_field(name="<:nuvem:459443407274770444> Vento", value=ee)
            embed.set_thumbnail(url=icon)
            embed.set_footer(text="Galaxy © 2k18")
            await client.send_message(message.channel, embed=embed)
        except:
            await client.send_message(message.channel, "Não foi possível localizar o status deste local.")

    elif message.content.lower().startswith('xy.py'):
        usermsgcod = message.content[5:]
        await client.send_message(message.channel,
                                  '<a:rainbow_python:471032257713274901> O {} enviou o segunte código:\n```python\n{} \n```'.format(
                                      message.author.mention, usermsgcod))
        await client.delete_message(message)\

    elif message.content.lower().startswith("xy.shelp"):
        # await client.delete_message(message)
        searchhelp = discord.Embed(title='Detalhes Sobre', color=0x1CF9FF, description='🔍Comandos de Search🔍')
        searchhelp.set_thumbnail(url="https://i.imgur.com/nrqRsbf.png")
        searchhelp.add_field(name='**Uso**', value='Parametros<> | Opcional []', inline=True)
        searchhelp.add_field(name='**xy.ggl**', value='`<pesquisa em texto> Faz uma busca no google`', inline=False)
        searchhelp.add_field(name='**xy.ytb**', value='`<pesquisa em texto> Faz uma busca no youtube`', inline=False)
        searchhelp.set_footer(
            text="Comando usado por {0} as {1} Hrs".format(message.author, time.time()),
            icon_url=message.author.avatar_url)
        search = await client.send_message(message.author, embed=searchhelp)
        await asyncio.sleep(30)
        await client.delete_message(search)

    elif message.content.lower().startswith("xy.ggl"):
        #  await client.delete_message(message)
        words = 'https://www.google.com/search?q=' + message.content[7:].strip().replace(' ', '+')
        await client.send_message(message.channel, words)

    elif message.content.lower().startswith("xy.ytb"):
        #  await client.delete_message(message)
        words = 'https://www.youtube.com/results?search_query=' + message.content[7:].strip().replace(' ', '+')
        await client.send_message(message.channel, words)

    if message.content.lower().startswith('xy.semoji'):
        try:
            msg = message.content[10:]
            emoji = discord.utils.get(client.get_all_emojis(), name=msg)
            embed = discord.Embed(title='Informação do Emoji: {}!'.format(emoji.name),
                                  description='Veja aqui as info deste emoji! ^^\n', color=0xF1C40F, timestamp=message.timestamp)
            embed.add_field(name='Nome do Emoji', value=emoji.name)
            embed.add_field(name='ID Do Emoji', value='{}'.format(emoji.id))
            embed.add_field(name='Link', value=(emoji.url))
            embed.add_field(name='Servidor', value='{}({})'.format(emoji.server.name, emoji.server.id))
            embed.add_field(name='Emoji upado em', value=emoji.created_at)
            embed.add_field(name='Uso', value=f'`<:{emoji.name}:{emoji.id}>`')
            embed.set_thumbnail(url=emoji.url)
            embed.set_footer(text="By: IamEduardo#6790")
            await client.send_message(message.channel, embed=embed)
        except:
            await client.send_message(message.channel, 'Emoji não existe ou não encontrado.')
	

def hug_gif():
    url = "http://anaaliceprojects.xyz/apis/hug.php"
    resposta = requests.get(url)
    resposta_json = json.loads(resposta.text)
    gif = resposta_json['url']
    return gif

def giphy_api(tag):
    url = 'http://api.giphy.com/v1/gifs/search?q={}&api_key=y3YKoN7TmXF4Czuuncm5iSsV13hpkH4S&limit=16'.format(tag)
    resposta = requests.get(url)
    resposta_json = json.loads(resposta.text)
    gif = resposta_json['data'][randrange(0,15)]['id']
    return 'https://media.giphy.com/media/{}/giphy.gif'.format(gif)

client.run(token)

