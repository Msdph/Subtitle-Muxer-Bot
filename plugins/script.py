from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

class Script(object):



    START_TEXT = """
سلام {} 👋

من یه زیرنویس زن هستم

من می توانم هر فایل srt یا ass را در فایل یا ویدیو بچسبانم

از دستور راهنما استفاده کنید تا بدانید چگونه از من استفاده کنید

Made With 💕 By @Tellybots_4u
"""
    HELP_TEXT = """
توصیه میشود وقتی : 
➠ از Hardmux وقتی زمان زیادی داری

توصیه میشود وقتی : 
➠ از Softmux وقتی میخوای سریع باشه

Softmux
➠ Send /softmux to add Subtitle Softly in it

HardMux
➠ Send /hardmux to add Subtitle hardly in it 

Made With 💕 By @KenzoMovie
"""
    ABOUT_TEXT = """
 **🤖 Bot :** Subtitle KenzoMovie\n
 **👥 Channel :** [KenzoMovie](https://telegram.me/KenzoMovie)\n

"""
    START_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🤖 Update Channel', url='https://telegram.me/KenzoMovie'),
        InlineKeyboardButton('💬 Support Group', url='https://telegram.me/KenzoMovie')
        ],[
        InlineKeyboardButton('❔ راهنما', callback_data='help'),
        InlineKeyboardButton('⛔ بستن', callback_data='close')
        ]]
    )
    HELP_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 خانه', callback_data='home'),
        InlineKeyboardButton('👲 درباره', callback_data='about'),
        InlineKeyboardButton('⛔ بستن', callback_data='close')
        ]]
    )
    ABOUT_BUTTONS = InlineKeyboardMarkup(
        [[
        InlineKeyboardButton('🏡 خانه', callback_data='home'),
        InlineKeyboardButton('❔ راهنما', callback_data='help'),
        InlineKeyboardButton('⛔ بستن', callback_data='close')
        ]]
    )
