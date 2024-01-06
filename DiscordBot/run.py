from app.discord_bot.discord_api import botClient, discordToken

if __name__ == "__main__":
    botClient.run(discordToken)