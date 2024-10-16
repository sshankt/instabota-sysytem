from instabot import Bot
import os

# Load environment variables securely
USERNAME = os.getenv("INSTA_USERNAME")  
PASSWORD = os.getenv("INSTA_PASSWORD")  

# Initialize the bot
bot = Bot()


if USERNAME and PASSWORD:
    # Login to Instagram
    bot.login(username=USERNAME, password=PASSWORD)
    
    # Follow a user
    bot.follow("codewithharry")
else:
    print("Error: Instagram username or password not set in environment variables")
