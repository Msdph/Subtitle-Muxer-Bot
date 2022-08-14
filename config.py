
import os

class Config:

    BOT_TOKEN = os.environ.get('BOT_TOKEN', '5237219444:AAG6KaHe8_IbNrDquzE1Rq2Zwwlx2cyg7bo')
    APP_ID = os.environ.get('APP_ID', 2669389)
    API_HASH = os.environ.get('API_HASH', '59f112100d19186dc03cd93fb7f2904a')

    #comma seperated user id of users who are allowed to use

    DOWNLOAD_DIR = 'downloads'
    OWNER_ID = int(os.environ.get("OWNER_ID", 664738081))
    UPDATES_CHANNEL = os.environ.get("UPDATES_CHANNEL", None)  
    # your telegram id
    # database session name, example: xurluploader
    SESSION_NAME = os.environ.get("SESSION_NAME", "test")
    # database uri (mongodb)
    DATABASE_URL = os.environ.get("DATABASE_URL", "mongodb+srv://masoudbiatomoviez:12345678VB@cluster0.jigze.mongodb.net/Cluster0?retryWrites=true&w=majority")
    LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL", "-1001684448513"))
    BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
    DOWNLOAD_LOCATION = "./DOWNLOADS"
