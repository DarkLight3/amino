import amino
import json
import amino
import random
import time
from google_trans_new import google_translator  
from gtts import gTTS
import os
import requests
import threading
import re
from threading import Thread
from threading import Timer
#variables
hp = ("""[C]︵ ⠄︵ ⠄︵
[C]꒷꒦ ▸ ▹ ▸ ꗃ 𖥻𝗪𝗘𝗟𝗖𝗢𝗠𝗘 𖥦 ᵎ ❟
[bci]|𝖧𝖾𝗅𝗉.
[C]𔘓   ꗃ ∶ ∶   ⟮⛓⟯  𔒩   ⩇∶⩇ ❟   𖥦    ༶ 

[C]
[C]𖤐 : c ū r s ē d ! ⇘ ⇘ ﹙𖤛﹚﹫ usser  𖥍
[C]
[C]i t ' s  ﹙҂﹚ h u r t s  ⨳  L î ē s ！⛓︎ ꒷꒦

[ciu]Es un bot de divisiones lo cual es un proyecto el cual esta en proceso si no funciona es por que se le estan pidiendo nuevos comandos o cosas.

[Ic]Todo tipo de comandos se usa con cierta cosas.

[Ciu]Ejemplos.

[ic]#help 
[ic]#ping

[ciu]- Bot-zack -(Dueño).

[ciu]help= te dice que comandos tiene el bot 
[ciu]ping= dice pong! 
[ciu]onichan= manda un audio diciendo onichan  (mantenimiento).

[ciu]Trad = traduce el mensaje que quieras de cualquier 
[ciu]idioma al español 
[C]𔘓   ꗃ ∶ ∶   ⟮⛓⟯  𔒩   ⩇∶⩇ ❟   𖥦    ༶ 
[ciu]info = te dice tu informacion 
[ciu]comment = comenta en tu muro 
[ciu]kill= mata al usuario que quieras 
[ci]arrepientete = arrepientete marrano OwO 
[C]𔘓   ꗃ ∶ ∶   ⟮⛓⟯  𔒩   ⩇∶⩇ ❟   𖥦    ༶ 
[ciu]di= dice lo que quieras  
[cui]askme= preguntame algo  
[ciu]Voz= dime que quieres que diga por audio OwO

[Ciu]‹  ꗃ .﹙bye bye﹚⋆  i  ṅ e v̶ e r  –  d i ė

[Ciu]Todo tipo de comandos o nuevas ideas en procesos.

[Ciu]Bot Hecho por zack (https://aminoapps.com/u/Zack321668522911)
[C]╰────────────────╯""")
askme =("Por que si.","Claro.","Tal ves.","Si.","Nunca.","Tu mama.","Claro que no, no haria eso.")
#login
with open('./config.json') as cjson:
    config = json.load(cjson)
    print("Bot Online.")

client = amino.Client()

ea = config["email"]
pa = config["passwd"]
comid = config["comuid"]
prefix = config["prefix"]

client.login(ea, pa)

def reconsocketloop():
    while (1):
        shandle = clienteAmino.socket
        print(threading.active_count())
        shandle.close()
        shandle.start()
        time.sleep(480)

subclient = amino.SubClient(comId=comid, profile=client.profile)
@client.callbacks.event("on_text_message")
def on_text_message(data):
    print(f"{data.message.author.nickname}: {data.message.content}")
    if data.message.content.lower().startswith(f'{prefix}ping'):
        subclient.send_message(message="Pong!", chatId=data.message.chatId)

    if data.message.content.lower().startswith(f'{prefix}info'):
        u1 = subclient.get_user_info(data.message.author.userId)
        u2 = data.message.author.userId
        u3 = data.message.author.nickname
        u4 = u1.followersCount
        u5 = u1.followingCount
        u6 = data.message.author.reputation
        u7 = data.message.author.level
        u8 = u1.createdTime
        u9 = u1.onlineStatus
        u10 = u1.blogsCount
        subclient.send_message(message=f'\n\n[bcui]Info de {u3} \n\n[ci]Nickname:{u3} \n\n[ci]Id={u2} \n\n[ci]Reputacion: {u6} \n\n[ci]nivel:{u7} \n\n[ci]Seguidores: {u4} \n\n[ci]Siguiendo: {u5} \n\n[ci]Creacion de la cuenta:{u8} \n\n[ci]Online:{u9}   \n\n[ci]blogsCount:{u10}', chatId=data.message.chatId)
        
    if data.message.content.lower().startswith(f'{prefix}di'):
        objChat=subclient.get_chat_messages(chatId=data.message.chatId)
        UltMssg=objChat.content[0]
        res=UltMssg.replace("#di", "", 1)
        u1 = subclient.get_user_info(data.message.author.userId)
        u2 = u1.nickname
        subclient.send_message(message=f"{u2}:{res}", chatId=data.message.chatId)

    if data.message.content.lower().startswith(f'{prefix}voz'):
        objChat=subclient.get_chat_messages(chatId=data.message.chatId)
        UltMssg=objChat.content[0]
        res=UltMssg.replace("#voz", "", 1)
        tts = gTTS(f"{res}",lang="es",tld='es')
        tts.save("Voz.mp3")
        with open ("Voz.mp3", "rb") as file:
            subclient.send_message(chatId=data.message.chatId, file=file, fileType="audio")
        try:
            os.remove("Voz.mp3")
        except:pass

    if data.message.content.lower().startswith(f'{prefix}tra'):
        objChat=subclient.get_chat_messages(chatId=data.message.chatId)
        UltMssg=objChat.content[0]
        res=UltMssg.replace("#tra", "", 1)
        translator = google_translator()
        translate_text = translator.translate(str(f"{res}"),lang_tgt='es')
        subclient.send_message(message=translate_text,chatId=data.message.chatId,messageType=0)

    if data.message.content.lower().startswith(f'{prefix}comment'):
        objChat=subclient.get_chat_messages(chatId=data.message.chatId)
        UltMssg=objChat.content[0]
        u2 = data.message.author.userId
        res=UltMssg.replace("#comment", "", 1)
        subclient.comment(message=f"{res}",userId=data.message.author.userId)

    if data.message.content.lower().startswith(f'{prefix}help'):
        subclient.send_message(message= hp, chatId=data.message.chatId)

    if data.message.content.lower().startswith(f'{prefix}askme'):
        subclient.send_message(message=random.choice(askme), chatId=data.message.chatId)

    if data.message.content.lower().startswith(f'{prefix}comment'):
        subclient.send_message(message="Revisa tu muro OwO", chatId=data.message.chatId)

@client.callbacks.event("on_group_member_join")
def on_group_member_join(data):
    u1 = subclient.get_user_info(data.message.author.userId).nickname
    subclient.send_message(message=f'Bienvenido {u1}! espero te la pases genial en el chat.', chatId=data.message.chatId)
    subclient.start_chat(userId=data.message.author.userId, message="a prueba")

@client.callbacks.event("on_group_member_leave")
def on_group_member_leave(data):
    subclient.send_message(message='[Ci]Adios cuidate xD', chatId=data.message.chatId)
reconsocketloop
