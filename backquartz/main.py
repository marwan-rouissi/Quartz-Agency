import openai
from craiyon import Craiyon
import json
import requests
import random

def createChannel(token: str,server_id: str, parent_id: str, name: str):
    return json.loads(requests.post("https://discord.com/api/v9/guilds/"+server_id+'/channels', 
                                    headers={'authorization': token, 'content-type':'application/json'},
                                    json={"type":0, "name":name,"permission_overwrites":[],"parent_id":parent_id}).content.decode('utf-8'))['id']

def deleteChannel(token: str, channel_id: str):
    requests.delete("https://discord.com/api/v9/channels/"+channel_id, headers={'authorization': token})

def postMessage(token: str, channel_id: str, message: str):
    requests.post("https://discord.com/api/v9/channels/"+channel_id+"/messages",
                  headers={'authorization': token, 'content-type': 'application/json'}, json={'content':message})

def createIntegration(token: str, server_id: str, bot_id: str, channel_id: str, command_id: str, command_name: str, command_version: str, option=[]):
    head = {'authorization': token, 'content-type': 'application/json'}
    data = {"application_id": bot_id,"channel_id": channel_id,"data"
            :{"id": command_id,"name": command_name,"options": [],"version": command_version},"guild_id": server_id,"session_id": "a","type": 2}
    requests.post("https://discord.com/api/v9/interactions", headers=head, json=data)



text = ""
textOut = ""
geneImg = ""
geneImgOut = ""
hashTag = []


inPut = [text, geneImg]
outPut = [textOut,geneImgOut, []]


token = "MTEwNjUzODMxNjg5MzAwMzc4Ng.G0orL-.KsHREPHRaIaXFloGqgCT3m41sZF_mj5nOXYKk0"
server_id = "1113874867276742688"
parent_id = "1113942565633400992"
name = "pending-command"

text = "Pollution liée aux confinements due au covid19"
liste = ["",]
for a in text:
    if a == " ":
        liste.append("")
    else:
        liste[-1] += a
for b in liste:
    if len(b)<=3:
        liste.remove(b)
openai.api_key = "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"

startPrompt = "Fait moi un article de " + str(len(liste)//10 + 1) + " paragraphes sur : "
prompt = startPrompt + text + " Fait ressortir les mots clés a la fin"

print(prompt)

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo", 
  messages=[{"role": "user", "content": prompt}]
)
textOut = completion["choices"][0]["messages"]["content"]
for a in range(len(textOut)):
    if textOut[a] == "\n":
        Target = a
start = 0
textOut = textOut.replace(textOut[a:],"")
keyWord = textOut[a:].replace("Mots-clés : ", "")

for charset in range(len(keyWord)):
    if keyWord[charset] == ",":
        hashTag.append(keyWord[start:charset])
        start = charset+2
    if keyWord[charset] == ".":
        hashTag.append(keyWord[start:])
for j in range(len(hashTag)):
    hashTag[j].replace(" ", "_")
if geneImg != "":
    channel_id = createChannel(token, server_id, parent_id, name)
    #postMessage(token, channel_id, textOut)
