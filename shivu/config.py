class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5758713974"
    sudo_users = ["5758713974", "7011990425", "6264760837", "5527022252", "6384484443", "1850686769"]
    GROUP_ID = "-1002041586214"
    TOKEN = "7371780430:AAH3wBjiu4nRirz-A5U_L7beK97TmWicQSY"
    mongo_url = "mongodb+srv://vinamra523:duXNC3pKUddFNb1p@newbhainew.3ioyzuw.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL = ["https://telegra.ph/file/7e5398823512d307128a3.jpg", "https://telegra.ph/file/c45dcb207d81e97cb4f6a.jpg", "https://telegra.ph/file/0bc6d65878e8300fbf0f8.jpg", "https://telegra.ph/file/0afb45203ff162ee7227b.jpg"]
    SUPPORT_CHAT = "lustsupport"
    UPDATE_CHAT = "lustxUpdate"
    BOT_USERNAME = "lustXcatcherr_robot"
    CHARA_CHANNEL_ID = "-1002023474262"
    api_id = "20457610"
    api_hash = "b7de0dfecd19375d3f84dbedaeb92537"

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
