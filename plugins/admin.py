# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#

from pyrogram import Client, filters
from datetime import datetime, timedelta
from database.db_premium import add_premium_user, remove_premium_user
from config import ADMINS

# ✅ ADD PREMIUM
@Client.on_message(filters.command("addpremium") & filters.user(ADMINS))
async def add_premium(client, message):
    try:
        user_id = int(message.text.split(" ")[1])
        days = int(message.text.split(" ")[2])

        expire_date = datetime.now() + timedelta(days=days)

        await add_premium_user(user_id, expire_date)

        await message.reply_text(
            f"✅ User `{user_id}` ko {days} days ka PREMIUM de diya gaya"
        )

    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")


# ❌ REMOVE PREMIUM
@Client.on_message(filters.command("removepremium") & filters.user(ADMINS))
async def remove_premium(client, message):
    try:
        user_id = int(message.text.split(" ")[1])

        await remove_premium_user(user_id)

        await message.reply_text(
            f"❌ User `{user_id}` ka PREMIUM remove kar diya gaya"
        )

    except Exception as e:
        await message.reply_text(f"❌ Error: {e}")

# Don't Remove Credit @CodeFlix_Bots, @rohit_1888
# Ask Doubt on telegram @CodeflixSupport
#
# Copyright (C) 2025 by Codeflix-Bots@Github, < https://github.com/Codeflix-Bots >.
#
# This file is part of < https://github.com/Codeflix-Bots/FileStore > project,
# and is released under the MIT License.
# Please see < https://github.com/Codeflix-Bots/FileStore/blob/master/LICENSE >
#
# All rights reserved.
#
