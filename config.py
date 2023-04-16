import re
import sys
from os import getenv

from dotenv import load_dotenv
from pyrogram import filters

load_dotenv()

API_ID = int(getenv("API_ID", "26788480"))
API_HASH = getenv("API_HASH", "858d65155253af8632221240c535c314")

BOT_TOKEN = getenv("BOT_TOKEN", "5858600782:AAFtbxUVLd44CDq-mKfk8M-HpbTqBA3CxEQ")

MONGO_DB_URI = getenv("MONGO_DB_URI", "mongodb+srv://anicadeupload:anicade123@cluster0.z0a8l6k.mongodb.net/?retryWrites=true&w=majority")
LOG_GROUP_ID = int(getenv("LOG_GROUP_ID", "-1001652671967"))
MUSIC_BOT_NAME = getenv("MUSIC_BOT_NAME", "DOKI")

OWNER_ID = list(map(int, getenv("OWNER_ID", "6219768950").split()))

HEROKU_API_KEY = getenv("HEROKU_API_KEY", None)
HEROKU_APP_NAME = getenv("HEROKU_APP_NAME", None)

UPSTREAM_REPO = getenv("UPSTREAM_REPO", "")
UPSTREAM_BRANCH = getenv("UPSTREAM_BRANCH", "master")
GIT_TOKEN = getenv("GIT_TOKEN", None)

SUPPORT_CHANNEL = getenv("SUPPORT_CHANNEL", "https://t.me/DokiSupport")
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/DokiSupport")

SUPPORT_HEHE = SUPPORT_GROUP.split("me/")[1]

DURATION_LIMIT_MIN = int(getenv("DURATION_LIMIT", "180"))
SONG_DOWNLOAD_DURATION = int(getenv("SONG_DOWNLOAD_DURATION_LIMIT", "180"))

AUTO_LEAVING_ASSISTANT = getenv("AUTO_LEAVING_ASSISTANT", "False")
AUTO_LEAVE_ASSISTANT_TIME = int(
    getenv("ASSISTANT_LEAVE_TIME", "5400")
)

AUTO_DOWNLOADS_CLEAR = getenv("AUTO_DOWNLOADS_CLEAR", "True")

PRIVATE_BOT_MODE = getenv("PRIVATE_BOT_MODE", None)

YOUTUBE_DOWNLOAD_EDIT_SLEEP = int(getenv("YOUTUBE_EDIT_SLEEP", "5"))
TELEGRAM_DOWNLOAD_EDIT_SLEEP = int(getenv("TELEGRAM_EDIT_SLEEP", "3"))

SPOTIFY_CLIENT_ID = getenv("SPOTIFY_CLIENT_ID", "a85537ebcdd148beaf36e875fce7aab4")
SPOTIFY_CLIENT_SECRET = getenv("SPOTIFY_CLIENT_SECRET", "52b5bbaa7c5b400db1f6c48f501490a0")

VIDEO_STREAM_LIMIT = int(getenv("VIDEO_STREAM_LIMIT", "5"))
SERVER_PLAYLIST_LIMIT = int(getenv("SERVER_PLAYLIST_LIMIT", "50"))
PLAYLIST_FETCH_LIMIT = int(getenv("PLAYLIST_FETCH_LIMIT", "50"))

CLEANMODE_DELETE_MINS = int(getenv("CLEANMODE_MINS", "12"))

TG_AUDIO_FILESIZE_LIMIT = int(getenv("TG_AUDIO_FILESIZE_LIMIT", "104857600"))
TG_VIDEO_FILESIZE_LIMIT = int(getenv("TG_VIDEO_FILESIZE_LIMIT", "1073741824"))
# https://www.gbmb.org/mb-to-bytes

STRING1 = getenv("STRING_SESSION", "AQC_55teEDD2t-OOI1wHEqMiwYYngXpD5lX_yp6g3wH9SNjKNL73plxpHNl1vAeh9isdPioN9Sf-fgpA6YOPaNa_SftVTFvcN1ct7m7dtCrgbvS2vXvREFZjprXai5mmu7Oc0UKqXNZLMuFl3TR7a7ar7expt4__iETP1z3liit_wVvGwylJaljNU5bS7cN1B7VeufJZvlW2mmQOjolAi94SWZM9HQLWxPAKXPv1c3A3iciw-jrrS0qQ7QCWel8nNloWxew5V8fSgtHVUQqmBtgehnjgJ86ilMyGjAw3-u65NFEXInBBq4DIEQA2APlBg9636nMTVn_lCicHX70y9oXhAAAAAVbwES0A")
STRING2 = getenv("STRING_SESSION2", None)
STRING3 = getenv("STRING_SESSION3", None)
STRING4 = getenv("STRING_SESSION4", None)
STRING5 = getenv("STRING_SESSION5", None)

BANNED_USERS = filters.user()
YTDOWNLOADER = 1
LOG = 2
LOG_FILE_NAME = "doki.txt"
adminlist = {}
lyrical = {}
chatstats = {}
userstats = {}
clean = {}
autoclean = []


START_IMG_URL = getenv("START_IMG_URL", "https://graph.org/file/996958234f2421639d85b.jpg")

PING_IMG_URL = getenv(
    "PING_IMG_URL",
    "https://graph.org/file/b3e14e839a76568937def.jpg",
)

PLAYLIST_IMG_URL = "https://graph.org/file/a3804350cd55adf283622.jpg"

GLOBAL_IMG_URL = "https://graph.org/file/3e0e2de1c0e9dc43269e7.jpg"

STATS_IMG_URL = "https://graph.org/file/f60eb25b02fa06307081d.jpg"

TELEGRAM_AUDIO_URL = "https://graph.org/file/3e0e2de1c0e9dc43269e7.jpg"

TELEGRAM_VIDEO_URL = "https://graph.org/file/3e0e2de1c0e9dc43269e7.jpg"

STREAM_IMG_URL = "https://graph.org/file/82e478b5ad0e14b78fde3.jpg"

SOUNCLOUD_IMG_URL = "https://graph.org/file/82e478b5ad0e14b78fde3.jpg"

YOUTUBE_IMG_URL = "https://graph.org/file/82e478b5ad0e14b78fde3.jpg"

SPOTIFY_ARTIST_IMG_URL = "https://graph.org/file/82e478b5ad0e14b78fde3.jpg"

SPOTIFY_ALBUM_IMG_URL = "https://graph.org/file/ee0a9297d1744af715734.jpg"

SPOTIFY_PLAYLIST_IMG_URL = "https://graph.org/file/a3804350cd55adf283622.jpg"


def time_to_seconds(time):
    stringt = str(time)
    return sum(
        int(x) * 60**i
        for i, x in enumerate(reversed(stringt.split(":")))
    )


DURATION_LIMIT = int(time_to_seconds(f"{DURATION_LIMIT_MIN}:00"))
SONG_DOWNLOAD_DURATION_LIMIT = int(
    time_to_seconds(f"{SONG_DOWNLOAD_DURATION}:00")
)


if UPSTREAM_REPO:
    if not re.match("(?:http|https)://", UPSTREAM_REPO):
        print(
            "[ERROR] - Your UPSTREAM_REPO url is wrong. Please ensure that it starts with https://"
        )
        sys.exit()

if PING_IMG_URL:
    if PING_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", PING_IMG_URL):
            PING_IMG_URL = "https://graph.org/file/b3e14e839a76568937def.jpg"

if START_IMG_URL:
    if START_IMG_URL != "assets/Ping.jpeg":
        if not re.match("(?:http|https)://", START_IMG_URL):
            START_IMG_URL = "https://graph.org/file/996958234f2421639d85b.jpg"
