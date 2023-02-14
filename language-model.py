import discord
import openai
import constant
import asyncio # To get the exception

client = discord.Client(intents=discord.Intents.all())
TOKEN = constant.DISCORDTOKEN
openai.api_key = constant.OPENAPITOKEN
model_engine = "davinci"

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    
    if message.author == client.user:
        return
    if message.content == '!begin':

        await message.channel.send("Ask me anything")

        def check(msg):
            if(msg.author == message.author and msg.channel == message.channel):
                return msg
            else:
                return "Not valid"

        try:
            msg = await client.wait_for("message", check=check, timeout=30) # 30 seconds to reply
        except asyncio.TimeoutError:
            await message.send("Sorry, you didn't reply in time!")

        print("Message: " + message.content)

        response = "Test"
        
        response = open_ai_prompt(msg)


        await message.channel.send(response.choices[0].text)

    
        def open_ai_prompt(prompt):
            response = openai.Completion.create(
                engine=model_engine,
                prompt=msg,
                max_tokens=150,
                n=1,
                stop=None,
                temperature=0.5,
            )
            return response

client.run(TOKEN)
