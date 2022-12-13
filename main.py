from discord.ext import commands
TOKEN = "MTA1MjMwNzk2MDc5MTA0NDI3Nw.G8S0Bz.E1eTbZesYN1CKOb6pbW8uIHnC1WjPk5fYpS6cA"

bot = commands.Bot(command_prefix="!")

@bot.event
async def on_ready():
    print(f'{bot.user} succesfully logged in!')

@bot.event
async def on_message(message):
    # Make sure the Bot doesn't respond to it's own messages
    if message.author == bot.user: 
        return
    
    if message.content == 'hello':
        await message.channel.send(f'Hi {message.author}')
    if message.content == 'bye':
        await message.channel.send(f'Goodbye {message.author}')

    await bot.process_commands(message)

bot.run(TOKEN)