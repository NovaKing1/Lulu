# (©) K-ZEN TV

import os
import logging
from logging.handlers import RotatingFileHandler

# =================== BOT CONFIGURATION =================== #

# Bot Username
BOT_USERNAME = os.environ.get("BOT_USERNAME", "default_bot_username")

# Permanent Heroku App URL (For Redirection)
HEROKU_APP_URL = os.environ.get("HEROKU_APP_URL", "https://your-app.herokuapp.com")

# Telegram Bot Token (@BotFather)
TG_BOT_TOKEN = os.environ.get("TG_BOT_TOKEN", "")

# Telegram API Credentials (from my.telegram.org)
APP_ID = int(os.environ.get("APP_ID", "23562561"))
API_HASH = os.environ.get("API_HASH", "a7974b5ef6b47b6457dc5ddb568e5ce7")

# Database Configuration
DB_URI = os.environ.get("DATABASE_URL", "")
DB_NAME = os.environ.get("DATABASE_NAME", "KZENDB")

# Channel & Owner Details
CHANNEL_ID = int(os.environ.get("CHANNEL_ID", ""))
OWNER = os.environ.get("OWNER", "Roverxstar")
OWNER_ID = int(os.environ.get("OWNER_ID", "7106166920"))

# Bot Working Port
PORT = int(os.environ.get("PORT", "8030"))

# Bot Workers (for handling multiple requests)
TG_BOT_WORKERS = int(os.environ.get("TG_BOT_WORKERS", "4"))

# Force Subscription Channels (if enabled)
FORCE_SUB_CHANNEL = int(os.environ.get("FORCE_SUB_CHANNEL", "-1002311266823"))
FORCE_SUB_CHANNEL2 = int(os.environ.get("FORCE_SUB_CHANNEL2", "-1002311266823"))

# Admins List
try:
    ADMINS = [OWNER_ID]  # Always include the owner as admin
    ADMINS.extend([int(x) for x in os.environ.get("ADMINS", "7371865855").split()])
except ValueError:
    raise Exception("❌ ERROR: Your Admins list does not contain valid integers.")

# =================== BOT UI MESSAGES =================== #

# Start Message (Optimized for TV Show Fetching)
START_MSG = os.environ.get(
    "START_MESSAGE",
    "<b>👋 Hello, {first}!</b>\n\n"
    "I am <b>K-Zen TV File Share Bot</b>. 📺\n"
    "Click on the <b>Season</b> or <b>Episode</b> buttons sent by the admin to fetch your favorite TV shows! 🎬"
)

# Force Subscription Message (Fixed Spacing & "Try Again" Button)
FORCE_MSG = os.environ.get(
    "FORCE_SUB_MESSAGE",
    "👋 <b>Hello, {first},</b>\n\n"
    "<i>To continue using me, you must join our channels below.</i> 👇\n\n"
    "📢 <b>Join, then tap 'Try Again' to access your requested file.</b>"
)

# Custom Caption for Forwarded Files (Optional)
CUSTOM_CAPTION = os.environ.get("CUSTOM_CAPTION", None)

# File Protection (Prevents forwarding files outside the bot)
PROTECT_CONTENT = os.environ.get("PROTECT_CONTENT", "False").lower() == "true"

# Disable Share Button for Channel Posts
DISABLE_CHANNEL_BUTTON = os.environ.get("DISABLE_CHANNEL_BUTTON", "False").lower() == "true"

# Bot Stats Message
BOT_STATS_TEXT = "<b>📊 BOT UPTIME:</b>\n{uptime}"

# Unauthorized Access Response
USER_REPLY_TEXT = "🚫 **Permission Denied!** Only bot owners can execute this command."

# =================== LOGGING CONFIGURATION =================== #

LOG_FILE_NAME = "filesharingbot.log"

logging.basicConfig(
    level=logging.INFO,
    format="[%(asctime)s - %(levelname)s] - %(name)s - %(message)s",
    datefmt='%d-%b-%y %H:%M:%S',
    handlers=[
        RotatingFileHandler(LOG_FILE_NAME, maxBytes=50_000_000, backupCount=10),
        logging.StreamHandler()
    ]
)

logging.getLogger("pyrogram").setLevel(logging.WARNING)

def LOGGER(name: str) -> logging.Logger:
    """Returns a configured logger instance."""
    return logging.getLogger(name)
