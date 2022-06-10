import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('TOKEN')

client = discord.Client()

LANGS = ['javascript', 'js', 'java', 'cpp', 'c++', 'csharp', 'cs', 'c_', 'golang', 'go', 'kotlin', 'kt', 'php', 'python', 'py', 'ruby', 'rust', 'swift', 'ts', 'typescript', 'scala']
REACTS = {}

@client.event
async def on_ready():
    emoji_guild = discord.utils.get(client.guilds, id=984878971172835359)
    for emoji in emoji_guild.emojis:
        for lang in emoji.name.split('X'):
            REACTS[lang] = emoji
            if lang == 'cpp': REACTS['c++'] = emoji

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    text = message.content
    for lang in LANGS:
        code = lang if lang != 'c_' else 'c'
        start, end = text.find(f'```{code}'), text.rfind('```')
        if start == -1 or start >= end: continue
        await message.add_reaction(REACTS[lang])
        break

client.run(TOKEN)
