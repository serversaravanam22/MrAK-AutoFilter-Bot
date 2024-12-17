import os
import re
import logging
from os import getenv
from Script import script

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Regex pattern to match numeric IDs
id_pattern = re.compile(r'^.\d+$')

def is_enabled(value, default):
    """Helper function to convert string to boolean."""
    if value.lower() in ["true", "yes", "1", "enable", "y"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "n"]:
        return False
    else:
        return default

# Check and fetch critical environment variables
def get_env_variable(var_name, default=None, required=True):
    """Fetches an environment variable or returns default if not found. Logs if required is True."""
    value = os.environ.get(var_name, default)
    if required and value is None:
        logger.error(f"Error: {var_name} is not set!")
        exit(1)
    return value

# Bot information
SESSION = get_env_variable('SESSION', 'Media_search')
API_ID = int(get_env_variable('API_ID', '20902603'))
API_HASH = get_env_variable('API_HASH', '79e5caa103a9e9fb0183390b4800845d')
BOT_TOKEN = get_env_variable('BOT_TOKEN', "7358459130:AAFG4DwbmI5rfyN9LMB410nEsYmgsZig5EE")

# Bot settings
CACHE_TIME = int(get_env_variable('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(get_env_variable('USE_CAPTION_FILTER', True))

PICS = get_env_variable('PICS', 'https://envs.sh/kwZ.jpg https://envs.sh/kw5.jpg https://envs.sh/kwG.jpg https://envs.sh/kwY.jpg https://envs.sh/kwC.jpg ').split() # Sample PIC
NOR_IMG = get_env_variable("NOR_IMG", "https://envs.sh/kw1.jpg")
MELCOW_VID = get_env_variable("MELCOW_VID", "https://envs.sh/kwU.jpg")
SPELL_IMG = get_env_variable("SPELL_IMG", "https://envs.sh/kwv.jpg")
SUBSCRIPTION = get_env_variable('SUBSCRIPTION', 'https://envs.sh/kwl.jpg')
CODE = get_env_variable('CODE', '0')

# Stream link shortener
STREAM_SITE = get_env_variable('STREAM_SITE', 'publicearn.com')
STREAM_API = get_env_variable('STREAM_API', 'bcb93413e5dd9aaf092ab03269420e6f928aae2c')
STREAMHTO = get_env_variable('STREAMHTO', 'https://t.me/sasukemovieschannel')

# Referral and premium settings
REFERAL_COUNT = int(get_env_variable('REFERAL_COUNT', '225'))
REFERAL_PREMEIUM_TIME = get_env_variable('REFERAL_PREMEIUM_TIME', '1month')
PREMIUM_LOGS = int(get_env_variable('PREMIUM_LOGS', '-1002271986248'))

# Admins, Channels & Users
USERNAME = get_env_variable("USERNAME", "https://t.me/Cr3atives_Cortex")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in get_env_variable('ADMINS', '6283322330').split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in get_env_variable('CHANNELS', '-1002439384019').split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in get_env_variable('AUTH_USERS', '6283322330').split()]
AUTH_USERS = auth_users + ADMINS if auth_users else []
PREMIUM_USER = [int(user) if id_pattern.search(user) else user for user in get_env_variable('PREMIUM_USER', '6283322330').split()]
auth_channel = get_env_variable('AUTH_CHANNEL', '-1002397984715')
AUTH_CHANNEL = int(auth_channel) if auth_channel and id_pattern.search(auth_channel) else None
support_chat_id = get_env_variable('SUPPORT_CHAT_ID', '-1002328454530')
SUPPORT_CHAT_ID = int(support_chat_id) if support_chat_id and id_pattern.search(support_chat_id) else None

# MongoDB information
DATABASE_URI = get_env_variable('DATABASE_URI', "mongodb+srv://Mastersender:17032008@cluster0.dt8i8.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
DATABASE_NAME = get_env_variable('DATABASE_NAME', "Cluster0")
COLLECTION_NAME = get_env_variable('COLLECTION_NAME', 'Telegram_files')

# Shortener configuration
VERIFY = bool(get_env_variable('VERIFY', False))
HOWTOVERIFY = get_env_variable('HOWTOVERIFY', '0')
SHORTLINK_URL = get_env_variable('SHORTLINK_URL', 'publicearn.com')
SHORTLINK_API = get_env_variable('SHORTLINK_API', 'bcb93413e5dd9aaf092ab03269420e6f928aae2c')
IS_SHORTLINK = bool(get_env_variable('IS_SHORTLINK', True))

# Miscellaneous
WCHNL = get_env_variable('WCHNL', 'https://whatsapp.com/channel/0029Vaz8vJlDp2QBlKE0Ys1d')
WRM = get_env_variable('WRM', 'https://t.me/sasukeweeklyrelease')
DELETE_CHANNELS = [int(dch) if id_pattern.search(dch) else dch for dch in get_env_variable('DELETE_CHANNELS', '0').split()]
MAX_B_TN = get_env_variable("MAX_B_TN", "5")
MAX_BTN = is_enabled(get_env_variable('MAX_BTN', "True"), True)
PORT = get_env_variable("PORT", "8080")
GRP_LNK = get_env_variable('GRP_LNK', 'https://t.me/+VjiNsUiEbsozNGY1')
CHNL_LNK = get_env_variable('CHNL_LNK', 'https://t.me/+Fmo0FrJ_iH8zMjQ9')
TUTORIAL = get_env_variable('TUTORIAL', 'https://t.me/MrAK_LinkZz/5')
IS_TUTORIAL = bool(get_env_variable('IS_TUTORIAL', True))
MSG_ALRT = get_env_variable('MSG_ALRT', 'Hello Nanbha and Nanbis ❤️')
LOG_CHANNEL = int(get_env_variable('LOG_CHANNEL', '-1002363029859'))

# Online stream and download settings
NO_PORT = bool(get_env_variable('NO_PORT', False))
APP_NAME = None
if 'DYNO' in os.environ:
    ON_HEROKU = True
    APP_NAME = get_env_variable('APP_NAME', 'sasukemoviesbot.koyeb.app/')
else:
    ON_HEROKU = False
BIND_ADRESS = getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0')
FQDN = getenv('FQDN', BIND_ADRESS) if not ON_HEROKU or getenv('FQDN') else APP_NAME+'.herokuapp.com'
URL = "https://{}/".format(FQDN) if ON_HEROKU or NO_PORT else "https://{}/".format(FQDN, PORT)

SLEEP_THRESHOLD = int(get_env_variable('SLEEP_THRESHOLD', '60'))
WORKERS = int(get_env_variable('WORKERS', '4'))
SESSION_NAME = get_env_variable('SESSION_NAME', 'LazyBot')
MULTI_CLIENT = False

# Log configuration
logger.info("Current Customized Configurations:")
logger.info(f"IMDB Results: {'Enabled' if IMDB else 'Disabled'}")
logger.info(f"Spell Check Mode: {'Enabled' if SPELL_CHECK_REPLY else 'Disabled'}")
logger.info(f"MAX_BTN: {MAX_BTN}")
logger.info(f"Custom File Caption: {CUSTOM_FILE_CAPTION if CUSTOM_FILE_CAPTION else 'Default Caption'}")

# Make sure to validate all critical settings here
if not BOT_TOKEN or not API_ID:
    logger.error("Critical error: BOT_TOKEN or API_ID is missing. Exiting.")
    exit(1)
