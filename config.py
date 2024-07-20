# devggn
# Note if you are trying to deploy on vps then directly fill values in ("")

from os import getenv

API_ID = int(getenv("API_ID", "24906331"))
API_HASH = getenv("API_HASH", "866e8e4637fb269388b50202fb0f169c")
BOT_TOKEN = getenv("BOT_TOKEN", "7389659795:AAGNKQxX_2zCjoPkNRGDdMc65CAxySAaQpI")
OWNER_ID = list(map(int, getenv("OWNER_ID", "6486192717").split()))
MONGO_DB = getenv("MONGO_DB", "mongodb+srv://xohayet:xohayet123@cluster0.v1boian.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
LOG_GROUP = getenv("LOG_GROUP", "savereeee")
CHANNEL_ID = int(getenv("CHANNEL_ID", "-1001906326624"))
