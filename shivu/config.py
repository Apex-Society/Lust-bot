class Config(object):
    LOGGER = True

    # Get this value from my.telegram.org/apps
    OWNER_ID = "5758713974"
    sudo_users = "5758713974" ,"6679467894", "1837623818", "6916220465", "6494814225", "5079126270", "7350197183", "5138772561", "1440712150"
    GROUP_ID = -1002190080867
    TOKEN = "6656009300:AAGgaIl9uJ438ZVpLP1R5k5_fs3piACUqiU"
    mongo_url = "mongodb+srv://tiwarireeta004:peqxLEd36RAg7ors@cluster0.furypd3.mongodb.net/?retryWrites=true&w=majority"
    PHOTO_URL =["https://te.legra.ph/file/161e4748aff1915cf21f0.jpg", "https://te.legra.ph/file/0c0dd1968dfb3963275dd.jpg"]
    SUPPORT_CHAT = "ApeX_Chats"
    UPDATE_CHAT = "ApeX_Chats"
    BOT_USERNAME = "GUESSEM_ALL_BOT"
    CHARA_CHANNEL_ID = "-1002190080867"
    api_id = 24074986
    api_hash = "f4f6272a85d0e50e39a24cb378be118d"
    

    
class Production(Config):
    LOGGER = True


class Development(Config):
    LOGGER = True
