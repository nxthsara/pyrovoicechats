from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>Hey {message.from_user.first_name} 👋🏻</b>
I Can Play In Your Voice Chats :)""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Website 📩", url="https://candase.cf"
                    ),
                    InlineKeyboardButton(
                        "Channel 🔈", url="https://t.me/candasee"
                    )
                ]
            ]
        )
    )


@Client.on_message(
    filters.command("start")
    & filters.group
    & ~ filters.edited
)
async def start(client: Client, message: Message):
    await message.reply_text(
        "Do You Want To Search For A YouTube Video 💁🏻‍♂️",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No", callback_data="close"
                    )
                ]
            ]
        )
    )
