# (©) Codexbotz

from pyrogram import __version__
from bot import Bot
from config import OWNER_ID
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton, CallbackQuery

@Bot.on_callback_query()
async def cb_handler(client: Bot, query: CallbackQuery):
    data = query.data

    if data == "about":
        await query.message.edit_text(
            text=(
                "🎬 <b>Welcome to K-ZEN TV!</b>\n\n"
                "🥇 **Home for all your favorite & latest Movies & TV Shows**\n"
                "🔹 Stay updated with the **latest movies & series**\n"
                "🔹 Search and discover content **effortlessly**\n"
                "🔹 Get **exclusive updates & recommendations**\n\n"
                "💡 **Our Community & Updates:**\n"
                "🕴🏼 <b>Owner:</b> <a href='tg://user?id={OWNER_ID}'>K-Zen TV</a>\n"
                "📺 <b>Updates:</b> <a href='https://t.me/K_ZenTv'>K-Zen TV</a>\n"
                "🍿 <b>Movies Channel:</b> <a href='https://t.me/K_ZenMovies'>K-ZEN MOVIES</a>\n"
                "🌍 <b>Community:</b> <a href='https://t.me/+npjbj_z59uYyZTM0'>Request Series</a>\n"
                "🔎 <b>Movie Search Chat:</b> <a href='https://t.me/+bc4ZizsFnoZjYzU0'>K-Zen Movie Requests</a>\n\n"
                "✨ **Enjoy a seamless movie experience with us!** 🍿🎥"
            ).format(OWNER_ID=OWNER_ID),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton("🎬 Explore Movies", url="https://t.me/K_ZenMovies"),
                        InlineKeyboardButton("📢 Latest Updates", url="https://t.me/K_ZenTv")
                    ],
                    [
                        InlineKeyboardButton("❌ Close", callback_data="close")
                    ]
                ]
            )
        )

    elif data == "close":
        # Smooth exit with a confirmation message
        await query.message.edit_text(
            "❌ <b>Closed.</b>\n\n"
            "Need help? Use /help anytime! 🚀",
            disable_web_page_preview=True
        )

# ⋗ Telegram - @K_ZenTv

# 🎉 Credit: Github - @K_ZenTv
# 📢 Special Thanks to K-ZEN TV for support!
# 🛠 For any issues, contact @K_ZenTv | Community: @K_ZenTv
