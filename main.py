import discord
import random

#Chase was here


TOKEN = input("TOKEN: ")

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    username = str(message.author).split('#')[0]
    user_message = str(message.content)
    channel = str(message.channel.name)
    print(f'{username}: {user_message} ({channel})')

    if message.author ==client.user:
        return
    if message.channel.name == 'pokemon-go-bot-info':
        if user_message.lower() == 'status':
            await message.channel.send(f'Hello {username}, Big Brother is online.')
            return
        elif user_message.lower() == 'bye':
            await message.channel.send(f'See you later {username}!')
            return
        elif user_message.lower() == '!random':
            response = f' This is your random number: {random.randrange(10000)}'
            await message.channel.send(response)
            return

    if user_message.lower() == '!anywhere':
        await message.channel.send('Ths can be used anywhere!')
        return


client.run(TOKEN)
