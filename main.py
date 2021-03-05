#Imports
import discord
import os
import random
from keep_alive import keep_alive
import pyjokes

# Start Discord Client
client = discord.Client()

#Varuables
presence = discord.Activity(type=discord.ActivityType.watching, name='For !support')
live = print('We Have Logged In As {0.user}'.format(client))



# Discord Bot If Online Chck, See #Varuabe For More Info
@client.event
async def on_ready():
  presence
  live

#Start Client Check
@client.event
async def on_message(message):
  if message.author == client.user:
    return

  if message.content.startswith('!insight3d'):
    await message.channel.send('Ok, Here Is the Link For InSight3D: ')
    await message.channel.send('https://insight3d.tech/')

  if message.content.startswith('!joke'):
    await message.channel.send(pyjokes.get_joke())

  if message.content.startswith('!code'):
    await message.channel.send('Ok, To Format A Code, Follow This:')
    await message.channel.send('Please Note: Use The Back Ticks, It Is Located Under ESC')
    await message.channel.send('```py')
    await message.channel.send('Enter Your Code')
    await message.channel.send('```py')

  if message.content.startswith('!invite'):
    invite = await message.channel.create_invite(reason='Testing', max_age = 0, temporary = False)
    await message.channel.send(f'Invite link: {invite.url}')

  if message.content.startswith('!blog'):
    await message.channel.send('Ok, Here Is The Link To Our Blog: ')
    await message.channel.send('https://insight3d.tech/blog')


    if message.content.startswith("!creator"):
     await message.channel.send('@Neil ')

    
  

keep_alive()
client.run(os.getenv('TOKEN'))