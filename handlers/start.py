from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


@Client.on_message(
    filters.command("start")
    & filters.private
    & ~ filters.edited
)
async def start_(client: Client, message: Message):
    await message.reply_text(
        f"""<b>👋🏻 Hi {message.from_user.first_name}!</b>

I am Powerful Bot Of @teamdanishbaba , lets you play music in your Telegram groups voice chat.
😁🔥. 

To play music This bot and @danishbabamusic in ur group.

Use the buttons below to know more about me.""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "My creator", url="https://t.me/teamdanishbaba"
                    )
                ],
                [
                    InlineKeyboardButton(
                        "💬 Group", url="https://t.me/joinchat/ZZUcbt3PDLllZGI9"
                    ),
                    InlineKeyboardButton(
                        "channel", url="https://t.me/whitedevilot"
                    ),
                    InlineKeyboardButton(
                        "Commands", url="https://telegra.ph/tgvcrobot-vctgassistant-04-12" )
                ],
                [
                    InlineKeyboardButton(
                        "Donate The Creator", url="https://t.me/teamdanishbaba"
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
        "💁🏻‍♂️ Do you want to search for a YouTube video?",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "✅ Yes", switch_inline_query_current_chat=""
                    ),
                    InlineKeyboardButton(
                        "No ❌", callback_data="close"
                    )
                ]
            ]
        )
    )
