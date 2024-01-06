from dotenv import load_dotenv
import discord
import os
from app.openai.openai import gptResponse

load_dotenv()

discordToken = os.getenv('DISCORD_TOKEN')

class DiscordBot(discord.Client):
    async def on_ready(self):
        print(f'{self.user} has connected to Discord!')

    async def on_message(self, message):
        if message.author == self.user:
            return

        if message.content == 'ping':
            await message.channel.send('pong')

        command, userMessage = None, None

        for text in ['/menabot']:
            if message.content.startswith(text):
                command = message.content.split(' ')[0]
                userMessage = message.content.replace(text, '')
                print(command, userMessage)
        
        if command == '/menabot':
            botResponse = gptResponse(prompt=userMessage)
            await message.channel.send(f"Response: {botResponse}")

intents = discord.Intents.default()
intents.message_content = True

botClient = DiscordBot(intents=intents)