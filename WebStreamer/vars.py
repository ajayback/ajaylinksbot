# (c) @AvishkarPatil | @EverythingSuckz

from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()


class Var(object):
    API_ID = int(getenv('API_ID','9002178'))
    API_HASH = str(getenv('API_HASH','a315441ae0890980db3be9d404bc3c59'))
    BOT_TOKEN = str(getenv('BOT_TOKEN','5493121282:AAHLtEZXfZodIKvIOFHPphERRss7tZl3Wc8'))
    SESSION_NAME = str(getenv('SESSION_NAME', 'AviStreamBot'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL','-1001622288261'))
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    OWNER_ID = int(getenv('OWNER_ID', '953267481'))
    NO_PORT = bool(getenv('NO_PORT', True))
    FQDN = str(getenv('FQDN', 'ajaybackup.github.io/Kaali-Linux'))
    URL = "https://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL','mongodb+srv://Ajaybackup235:Ajay1323@cluster0.nprpuiy.mongodb.net/?retryWrites=true&w=majority'))
    PING_INTERVAL = int(getenv('PING_INTERVAL', '500'))
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', None))
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "-1001296894100")).split()))
