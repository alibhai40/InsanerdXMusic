import re
import os
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

# Get this value from my.telegram.org/apps
API_ID = int(getenv("21228632", None))
API_HASH = getenv("6973dee17a0b7f477886c6cabdc54174", None)

# Get your token from @BotFather on Telegram.
BOT_TOKEN = getenv("7225567107:AAGXnisspysxNjv6IcIaAj_ZVa0F1qFot88", None)

# Get your mongo url from cloud.mongodb.com
MONGO_DB_URI = getenv("mongodb+srv://xylahacer007:xylahacer007@insane.cjjuw.mongodb.net/?retryWrites=true&w=majority&appName=Insane", None)
MUSIC_BOT_NAME = getenv("insane_musicbot", None)
PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", 900))

# Chat id of a group for logging bot's activities
LOGGER_ID = int(getenv("-1002199009517", None))
LOG_GROUP_ID = int(getenv("-1002199009517", None))

# Get this value from @BRANDRD_ROBOT on Telegram by /id
OWNER_ID = int(getenv("7368528181", ))

## Fill these variables if you're deploying on heroku.
# Your heroku app name
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME")
# Get it from http://dashboard.heroku.com/account
HEROKU_API_KEY = getenv("HEROKU_API_KEY")

UPSTREAM_REPO = getenv(
    "UPSTREAM_REPO",
    "https://github.com/WCGKING/BrandrdXMusic",
)
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "main")
GIT_TOKEN = getenv(
    "GIT_TOKEN", None
)  # Fill this variable if your upstream repository is private

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/VP247_Updates")
SUPPORT_CHAT = getenv("SUPPORT_CHAT", "https://t.me/Tamil_VP247")

# Set this to True if you want the assistant to automatically leave chats after an interval
AUTO_LEAVING_ASSISTANT = bool(getenv("AUTO_LEAVING_ASSISTANT", False))

# Auto Gcast/Broadcast Handler (True = broadcast on , False = broadcast off During Hosting, Dont Do anything here.)
AUTO_GCAST = os.getenv("AUTO_GCAST")

# Auto Broadcast Message That You Want Use In Auto Broadcast In All Groups.
AUTO_GCAST_MSG = getenv("AUTO_GCAST_MSG", "")

# Get this credentials from https://developer.spotify.com/dashboard
SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "bcfe26b0ebc3428882a0b5fb3e872473")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "907c6a054c214005aeae1fd752273cc4")


# Maximum limit for fetching playlist's track from youtube, spotify, apple links.
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "25"))

SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION_LIMIT = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "2000"))

# Telegram audio and video file size limit (in bytes)
TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", 104857600))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", 1073741824))
# Checkout https://www.gbmb.org/mb-to-bytes for converting mb to bytes


# Get your pyrogram v2 session from @BRANDEDSTRINGSESSION_BOT on Telegram
STRING1 = getenv("BQFD7FgAWjV01x67HTKhYvz6aHB7zOnAvqMXfeHeeYpugtutqlh6QigmcPOJkHeXNFZ6t-4jqUhzsXp-NOfoUAh8QXxFSQyNc36D1aCy1Nwdm0oNzM1YQMYB6MVXnFpTSogV4tdpCM4GaLlf8G3D2XLruI8zxP94TIRdUpyvjzDwdJzfmj6iUj54peIGZ0GbPvDOGAxDXeSPc5kJQKlnye7gZGEsY9p-q-7uVzteanfsy4DNtuYDeA2g6tXkKbzsrjm8zUF6yKJrDqdia7wZcaOg90S64Z36FRGs0KLF_21LDxzpUbn5wdN3FrM5YxYYeJtgMbZ9z1nPdIUZGz23RIn3mpnWBQAAAAG3MtE1AA",  None)
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)


BANNED_USERS = filters.user()
adminlist = {}
lyrical = {}
votemode = {}
autoclean = []
confirmer = {}


START_IMG_URL = getenv(
    "START_IMG_URL", "https://envs.sh/bGI.jpg"
)
PING_IMG_URL = getenv(
    "PING_IMG_URL", "https://envs.sh/bGI.jpg"
)
PLAYLIST_IMG_URL = "https://te.legra.ph/file/14eb59ea7d31229d8d751.jpg"
STATS_IMG_URL = "https://te.legra.ph/file/4310ea5f523520b2b765b.jpg"
TELEGRAM_AUDIO_URL = "https://te.legra.ph/file/923c1faac33d8c70335dc.jpg"
TELEGRAM_VIDEO_URL = "https://te.legra.ph/file/6c66f8b192532fe758e82.jpg"
STREAM_IMG_URL = "https://te.legra.ph/file/ebc4dc6357be06e08a3ed.jpg"
SOUNCLOUD_IMG_URL = "https://te.legra.ph/file/d339f390ec168c19879c6.jpg"
YOUTUBE_IMG_URL = "https://te.legra.ph/file/ee0cd53ab73f08f4a3627.jpg"
SPOTIFY_ARTIST_IMG_URL = "https://te.legra.ph/file/5f9fb5bba66021c782d96.jpg"
SPOTIFY_ALBUM_IMG_URL = "https://te.legra.ph/file/affe0afec5c7ad63676a4.jpg"
SPOTIFY_PLAYLIST_IMG_URL = "https://te.legra.ph/file/3c446e8dee78ed0ca62ff.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(int(x) * 60**i for i, x in enumerate(reversed(stringt.split(":"))))


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))


if SUPPORT_CHANNEL:
    if not re.match("(?:http|https)://", SUPPORT_CHANNEL):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHANNEL url is wrong. Please ensure that it starts with https://"
        )

if SUPPORT_CHAT:
    if not re.match("(?:http|https)://", SUPPORT_CHAT):
        raise SystemExit(
            "[ERROR] - Your SUPPORT_CHAT url is wrong. Please ensure that it starts with https://"
        )
