import discord

client = discord.Client()
LANGS = {}

@client.event
async def on_ready():
    emoji_guild = discord.utils.get(client.guilds, id=984878971172835359)
    for emoji in emoji_guild.emojis:
        for lang in emoji.name.split('X'):
            LANGS[lang] = emoji
    print(LANGS)

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    text = message.content
    for lang in LANGS:
        code = lang if lang != 'c_' else 'c'
        start, end = text.find(f'```{code}'), text.rfind('```')
        if start == -1 or start >= end: continue
        await message.add_reaction(LANGS[lang])
        break

client.run('OTg0MjMzNzQ1ODM2MDMyMDMw.GPqRSn.wGNfYEJOlWlR7Ax-udRcI7NNrdMVbnpfF90oec')
