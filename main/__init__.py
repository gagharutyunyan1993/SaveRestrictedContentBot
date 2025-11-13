#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=None, cast=int)
API_HASH = config("API_HASH", default=None)
BOT_TOKEN = config("BOT_TOKEN", default=None)
SESSION = config("SESSION", default=None)
FORCESUB = config("FORCESUB", default=None)
AUTH = config("AUTH", default=None, cast=int)

# Validate required environment variables
required_vars = {
    'API_ID': API_ID,
    'API_HASH': API_HASH,
    'BOT_TOKEN': BOT_TOKEN,
    'SESSION': SESSION,
    'AUTH': AUTH
}

missing_vars = [var_name for var_name, var_value in required_vars.items() if var_value is None]

if missing_vars:
    print("=" * 50)
    print("ERROR: Missing required environment variables!")
    print("=" * 50)
    for var in missing_vars:
        print(f"  ✗ {var} is not set")
    print("\nPlease set these variables in your .env file or environment.")
    print("Check README.md for instructions on how to get these values.")
    print("=" * 50)
    sys.exit(1)

try:
    bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN)
    print("✓ Telethon bot initialized successfully")
except Exception as e:
    print("=" * 50)
    print("ERROR: Failed to initialize Telethon bot!")
    print("=" * 50)
    print(f"Error details: {str(e)}")
    print("\nPossible causes:")
    print("  • Invalid BOT_TOKEN")
    print("  • Invalid API_ID or API_HASH")
    print("  • Network connection issues")
    print("=" * 50)
    sys.exit(1)

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID)

try:
    userbot.start()
    print("✓ Pyrogram userbot started successfully")
except Exception as e:
    print("=" * 50)
    print("ERROR: Failed to start Pyrogram userbot!")
    print("=" * 50)
    print(f"Error details: {str(e)}")
    print("\nPossible causes:")
    print("  • Invalid SESSION string")
    print("  • SESSION string has expired")
    print("  • Invalid API_ID or API_HASH")
    print("  • Account banned or restricted")
    print("\nHow to fix:")
    print("  1. Generate a new SESSION string using @SessionStringGeneratorZBot")
    print("  2. Update the SESSION variable in your .env file")
    print("  3. Make sure you're using the correct API_ID and API_HASH")
    print("=" * 50)
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)

try:
    Bot.start()
    print("✓ Pyrogram bot started successfully")
except Exception as e:
    print("=" * 50)
    print("ERROR: Failed to start Pyrogram bot!")
    print("=" * 50)
    print(f"Error details: {str(e)}")
    print("\nPossible causes:")
    print("  • Invalid BOT_TOKEN")
    print("  • Invalid API_ID or API_HASH")
    print("  • Bot token has been revoked")
    print("  • Network connection issues")
    print("\nHow to fix:")
    print("  1. Get a new bot token from @BotFather")
    print("  2. Update BOT_TOKEN in your .env file")
    print("=" * 50)
    sys.exit(1)
