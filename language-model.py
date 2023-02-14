import discord
import openai
import constant

client = discord.Client(intents=discord.Intents.default())
TOKEN = constant.DISCORDTOKEN
openai.api_key = constant.OPENAPITOKEN
model_engine = "ChatGPT"

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    if message.content == '!trick':
        prompt = message.content[4:]
        response = openai.Completion.create(
            engine=model_engine,
            prompt=prompt,
            max_tokens=150,
            n=1,
            stop=None,
            temperature=0.5,
        )
        await message.channel.send(response.choices[0].text)

client.run(TOKEN)
