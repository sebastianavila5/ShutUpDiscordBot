import os
import discord
from keep_alive import keep_alive

client = discord.Client()

bad = {"Spectre"}

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  if message.author == client.user:
    return
  if message.content.startswith('$shutup'):
    await connect(message)
  if message.content.startswith('$shutdown'):
    await disconnect(message)

async def connect(message):
  if not message.author.voice:
    await message.channel.send('Must be in a voice channel to Shut Up!')
    return
  channel = message.author.voice.channel
  await channel.connect()

async def disconnect(message):
  if not client.voice_clients:
    await message.channel.send('How can I Shut Down if you never Shut Up?')
    return
  await client.voice_clients[0].disconnect()

@client.event
async def on_voice_state_update(member, before, after):
  if not after.channel:
    return
  if member.name in bad:
    await member.move_to(None)
  print(member.name)

keep_alive()
client.run(os.environ['TOKEN'])