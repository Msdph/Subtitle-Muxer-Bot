from pyrogram import Client, filters
from helper_func.progress_bar import progress_bar
from helper_func.dbhelper import Database as Db
from helper_func.mux import softmux_vid, hardmux_vid, softremove_vid
from config import Config
import time
import os
from database.adduser import AddUser
db = Db()
from plugins.forcesub import handle_force_subscribe
@Client.on_message(filters.command('softmux') & filters.private)
async def softmux(client, message):
    await AddUser(client, message)
    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(client, message)
      if fsub == 400:
        return
    chat_id = message.from_user.id
    og_vid_filename = db.get_vid_filename(chat_id)
    og_sub_filename = db.get_sub_filename(chat_id)
    text = ''
    if not og_vid_filename :
        text += 'اول فیلم رو بفرست\n'
    if not og_sub_filename :
        text += 'فایل زیرنویس رو بفرست!'

    if not (og_sub_filename and og_vid_filename) :
        await client.send_message(chat_id, text)
        return

    text = '👻 سافتساب زود انجام میشه یکم صبر کن  . . . '
    sent_msg = await client.send_message(chat_id, text)

    softmux_filename = await softmux_vid(og_vid_filename, og_sub_filename, sent_msg)
    if not softmux_filename:
        return

    final_filename = db.get_filename(chat_id)
    os.rename(Config.DOWNLOAD_DIR+'/'+softmux_filename,Config.DOWNLOAD_DIR+'/'+final_filename)
    
    start_time = time.time()
    try:
        await client.send_document(
                chat_id,
                progress = progress_bar, 
                progress_args = (
                    'Uploading your File!',
                    sent_msg,
                    start_time
                    ), 
                document = os.path.join(Config.DOWNLOAD_DIR, final_filename),
                caption = final_filename
                )
        text = 'فایل با موفقیت آپلود شد!\nکل زمان صرف شده : {} ثانیه'.format(round(time.time()-start_time))
        await sent_msg.edit(text)
    except Exception as e:
        print(e)
        await client.send_message(chat_id, 'هنگام آپلود فایل خطایی رخ داد!\nبرای جزئیات خطا، گزارش ها را بررسی کنید!')

    path = Config.DOWNLOAD_DIR+'/'
    os.remove(path+og_sub_filename)
    os.remove(path+og_vid_filename)
    try :
        os.remove(path+final_filename)
    except :
        pass

    db.erase(chat_id)


@Client.on_message(filters.command('hardmux') & filters.private)
async def hardmux(bot, message, cb=False):
    await AddUser(bot, message)
    if Config.UPDATES_CHANNEL:
      fsub = await handle_force_subscribe(bot, message)
      if fsub == 400:
        return
    me = await bot.get_me()
    
    chat_id = message.from_user.id
    og_vid_filename = db.get_vid_filename(chat_id)
    og_sub_filename = db.get_sub_filename(chat_id)
    text = ''
    if not og_vid_filename :
        text += 'اول فیلم رو بفرست\n'
    if not og_sub_filename :
        text += 'فایل زیرنویس رو بفرست!'
    
    if not (og_sub_filename or og_vid_filename) :
        return await bot.send_message(chat_id, text)
    
    text = '👻 هارد ساب خیلی طول میکشه زیاد صبر کن . . . '
    sent_msg = await bot.send_message(chat_id, text)

    hardmux_filename = await hardmux_vid(og_vid_filename, og_sub_filename, sent_msg)
    
    if not hardmux_filename:
        return
    
    final_filename = db.get_filename(chat_id)
    os.rename(Config.DOWNLOAD_DIR+'/'+hardmux_filename,Config.DOWNLOAD_DIR+'/'+final_filename)
    

    start_time = time.time()
    try:
        await bot.send_video(
                chat_id,
                progress = progress_bar, 
                progress_args = (
                    'Uploading your File!',
                    sent_msg,
                    start_time
                    ), 
                video = os.path.join(Config.DOWNLOAD_DIR, final_filename),
                caption = final_filename
                )
        text = 'فایل با موفقیت آپلود شد!\nکل زمان صرف شده : {} ثانیه'.format(round(time.time()-start_time))
        await sent_msg.edit(text)
    except Exception as e:
        print(e)
        await client.send_message(chat_id, 'هنگام آپلود فایل خطایی رخ داد!\nبرای جزئیات خطا، گزارش ها را بررسی کنید!')
    
    path = Config.DOWNLOAD_DIR+'/'
    os.remove(path+og_sub_filename)
    os.remove(path+og_vid_filename)
    try :
        os.remove(path+final_filename)
    except :
        pass
    db.erase(chat_id)




