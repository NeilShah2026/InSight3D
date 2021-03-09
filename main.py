#Imports
import discord
import os
import random
from keep_alive import keep_alive
import pyjokes
#test


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


  if message.content.startswith("!creators"):
    await message.channel.send('These Are My Creators: ')
    await message.channel.send('@Neil Shah #6469 & MehoB #1483')

  if message.content.startswith('!repo'):
    await message.channel.send('Ok, Here is The Link To My GitHub Repo: ')
    await message.channel.send('https://github.com/NeilShah2026/InSight3D')
  
  if message.content.startswith('!idea'):
    await message.channel.send('Here Is The Link To The Idea Sheet: ')
    await message.channel.send('https://docs.google.com/spreadsheets/d/1HHQMCAI5Cg4ul-GSQYx6t9xvcXBz8LBN0wKKHqi4h3E/edit?usp=sharing')
    
  if message.content.startswith('!test'):
    #This Does Nothing For Now, Just As A Place Holder
    await message.channel.send('All Systems Are Online')

    
  

keep_alive()
client.run(os.getenv('TOKEN'))
