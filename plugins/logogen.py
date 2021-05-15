# Copyright (C) 2020-2021 by casperteam@Github, < https://github.com/casperteam >.
#
# This file is part of < https://github.com/casperteam/cpbot > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/casperteam/blob/master/LICENSE >
#
# All rights reserved.

from bs4 import *
import shutil
import requests
import os
import base64
import sys
import random
import requests
from main_startup.core.decorators import cpbot_on_cmd
from main_startup.helper_func.basic_helpers import edit_or_reply, get_text





def download_images(images): 
    count = 0
    print(f"Total {len(images)} Image Found!") 
    if len(images) != 0:
        for i, image in enumerate(images):
            try:
                image_link = image["data-srcset"] 
            except: 
                try: 
                    image_link = image["data-src"] 
                except:
                    try:
                        image_link = image["data-fallback-src"] 
                    except:
                        try:
                            image_link = image["src"] 
                        except: 

                            pass
            try: 
                r = requests.get(image_link).content 
                try:

                    r = str(r, 'utf-8')
                except UnicodeDecodeError:
                    with open("logo@cpbotOT.jpg", "wb+") as f: 
                        f.write(r)
                    count += 1
            except: 
                pass


def mainne(name, typeo):
    url = f"https://www.brandcrowd.com/maker/logos?text={name}&searchtext={typeo}&searchService="
    r = requests.get(url) 
    soup = BeautifulSoup(r.text, 'html.parser') 
    images = soup.findAll('img') 
    random.shuffle(images)
    if images is not None:
       print("level 1 pass")
    download_images(images)


@cpbot_on_cmd(
    ["logogen"],
    is_official=False,
    cmd_help={
        "help": "Generate Logo With Given Name",
        "example": "{ch}logogen (logo text:type)",
    },
)
async def logogen(client, message):
    pablo = await edit_or_reply(message, "`Creating The Logo.....`")
    Godzilla = get_text(message)
    if not Godzilla:
        await pablo.edit("`Please Give Me A Valid Input. You Can Check Help Menu To Know More!`")
        return
    lmao = Godzilla.split(":", 1)
    try:
        typeo = lmao[1]
    except BaseException:
        typeo = "name"
        await pablo.edit(
             "Give name and type for logo Idiot. like `.logogen messi:football`")
    name = lmao[0]
    mainne(name, typeo)
    caption = "<b>Logo Generated By cpbot. Get cpbot From @cpbotOT<b>"
    pate = "logo@cpbotOT.jpg"
    await client.send_photo(message.chat.id, pate)
    try:
        os.remove(pate)
    except:
        pass
    await pablo.delete()



