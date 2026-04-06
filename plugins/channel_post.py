
from pyrogram import Client, filters
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

CHANNEL_ID = -1001234567890  # change

def setup_channel_post(app: Client):

    @app.on_message(filters.private & (filters.document | filters.video | filters.audio))
    async def auto_post(client, message):
        file_id = message.document.file_id if message.document else message.video.file_id if message.video else message.audio.file_id

        buttons = InlineKeyboardMarkup([
            [InlineKeyboardButton("📥 Download Tutorial", url="https://your-shortner-link.com")],
            [InlineKeyboardButton("💎 Premium Download", url="https://your-shortner-link.com/premium")]
        ])

        sent = await client.send_cached_media(
            chat_id=CHANNEL_ID,
            file_id=file_id,
            caption="📦 New File Uploaded",
            reply_markup=buttons
        )

        await message.reply("✅ File posted to channel!")

    @app.on_callback_query()
    async def verify_and_send(client, callback_query):
        # dummy verify
        await callback_query.message.reply("✅ Verified! Sending file...")
        
