from doki.core.bot import DokiBot
from doki.core.dir import dirr
from doki.core.git import git
from doki.core.userbot import Userbot
from doki.misc import dbb, heroku, sudo
from doki import ClientSession

from .logging import LOGGER


dirr()

git()

dbb()

heroku()

sudo()

# Clients
app = DokiBot()

userbot = Userbot()


from .platforms import *

YouTube = YouTubeAPI()
Carbon = CarbonAPI()
Spotify = SpotifyAPI()
Apple = AppleAPI()
Resso = RessoAPI()
SoundCloud = SoundAPI()
Telegram = TeleAPI()

aiohttpsession = ClientSession()
