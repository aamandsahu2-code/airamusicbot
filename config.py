import random
import string
import os
from os import getenv
import time
import pymongo
from telethon import TelegramClient, events, Button
from pyrogram import Client, filters
from thumbnails import *
from fonts import *

# =====================================================
# 🔥 AIRA MUSIC BOT - Updated Config (English Theme) 🔥
# =====================================================

# Use getenv for all sensitive/configurable values
API_ID = int(os.getenv("API_ID", "2040"))
API_HASH = os.getenv("API_HASH", "b18441a1ff607e10a989891a5462e627")
STRING_SESSION = os.getenv("STRING_SESSION", "")
GROUP = os.getenv("GROUP", "nub_coder_s")
CHANNEL = os.getenv("CHANNEL", "nub_coders")
BOT_TOKEN = os.getenv("BOT_TOKEN", "")
OWNER_ID = int(os.getenv("OWNER_ID", "6076474757"))
LOGGER_ID = os.getenv("LOGGER_ID", None)
mongodb = os.getenv("MONGODB_URI", "mongodb+srv://nubcoders:nubcoders@music.8rxlsum.mongodb.net/?retryWrites=true&w=majority&appName=music")

# 🎵 AIRA THEME CONFIGURATION 🔥
AIRA_THEME = getenv("AIRA_THEME", "True").lower() == "true"
AIRA_START_IMG = getenv("AIRA_START_IMG", "aira_start.jpg")
AIRA_STICKER = getenv("AIRA_STICKER", "aira_sticker.webp")

# Welcome Messages (English)
WELCOME_MSG_EN = """
✨ **Aira Music Bot** ✨
Premium Voice Chat Music Player 🎵

🔥 **Quick Start:**
• Reply song → `/play`
• Search: `/play song name` 
• Video: `/vplay`

💖 **Premium Features:**
• HD 720p Video Streaming
• Smart Queue System
• Auto Assistant Join
• Seek & Loop Controls

👑 **Add to Group:** t.me/{bot_username}?startgroup=true
"""

PLAY_MSG_EN = """
🎵 **✨ Aira is Playing ✨**

🎤 **{title}**
⏱️ `{duration}`
👤 **by** {user}
🔗 [Watch]({url})

📊 **Queue:** `{queue_count}` songs
💖 **Powered by Aira Music**
"""

QUEUE_EMPTY_EN = "💔 **Queue is Empty!**\nAdd some songs first! 🎵"

# Working directory
ggg = os.getcwd()

# Track start time for uptime
StartTime = time.time()

# Global lists/dicts (Music Bot Essentials)
playing = {}
queues = {}
played = {}
active = []
AUTH = {}
BLOCK = []
SUDO = []
spam_chats = []

# MongoDB Connection
mongo_client = pymongo.MongoClient(mongodb)
db = mongo_client['voice']
user_sessions = db['user_sessions']
collection = db["users"]

# Bot username for dynamic links (will be set after client start)
BOT_USERNAME = ""

print("🎵 Aira Music Bot Config Loaded Successfully!")
print(f"✨ Theme Enabled: {AIRA_THEME}")
print(f"📁 Working Directory: {ggg}")
print("🚀 Ready to Rock! 💖")
