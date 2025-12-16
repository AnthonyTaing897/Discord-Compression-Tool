import discord
import sqlite3
from discord.ext import commands
from dotenv import load_dotenv
from server import webhookReceiver

import os

# Load command list cog
from cmds.commandGog import commandGog

# client Token
load_dotenv()
token = os.getenv('DISCORD_TOKEN')
if not token:
    raise EnvironmentError('DISCORD_TOKEN not set in environment')


# client Intent
intents = discord.Intents.default()
intents.message_content = True

# Set up Command Prefix and Intents
client = commands.Bot(command_prefix = '%', intents = intents)
connection = None

# Event: client is ready
@client.event
async def on_ready():
    #initalise the database connection and clear previous sessions
    connection = sqlite3.connect('Discord_Bot\DB\database.db')
    cursor = connection.cursor()
    cursor.execute("""DROP TABLE IF EXISTS sessions""")
    cursor.execute("""CREATE TABLE IF NOT EXISTS sessions (session_id TEXT PRIMARY KEY, session_code TEXT UNIQUE, user_id TEXT, start_time TIMESTAMP)""")  
    connection.commit()
    cursor.close()
    
    await client.add_cog(commandGog(client = client, connection = connection))

    

    webhookReceiver.init_webhook_reciever(client)
    print(f"The {client.user.name} is ready to compress")

@client.event
async def on_disconnect():
    connection.close()


if __name__ == "__main__":
    
    # Run the client (Leave this at the end of the file)
    client.run(token)