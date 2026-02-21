import random
import os
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes

# Get token from Railway Variables
TOKEN = os.getenv("TOKEN")

# Random lists
moods = ["Happy 😄", "Sad 😢", "Angry 😡", "Sleepy 😴", "Focused 😎"]
works = ["Student 📚", "Gamer 🎮", "Shopkeeper 🏪", "Coder 💻", "Dreamer 🌙"]

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE):
    user = update.effective_user

    luck = random.randint(1, 100)
    mood = random.choice(moods)
    work = random.choice(works)
    age = random.randint(15, 35)

    premium_status = "Premium 💎" if user.is_premium else "Basic 👤"

    # Get profile photo
    photos = await context.bot.get_user_profile_photos(user.id)
    photo = photos.photos[0][0].file_id if photos.total_count > 0 else None

    text = f"""
●♡▬▬♡ ᑭʀᴏꜰɪʟᴇ ♡▬▬♡●

👇🏻

⸙     {user.full_name}
☑     @{user.username if user.username else "No Username"}
☼     {luck}%
✲     {mood}

┉┉┉┉┉┉┉┉┉┉┉┉┉┉┉

ᴡᴏʀᴋ - {work}
ᴀɢᴇ - {age}
ᴀᴄᴄᴏᴜɴᴛ ɪɴғᴏ - {premium_status}
ᴜsᴇʀ ʙɪᴏ - Not Set
ᴜsᴇʀ ɪᴅ - {user.id}

▁ ▂ ▄ ▅ ▆ ▇ ██ ▇ ▆ ▅ ▄ ▂ ▁

ᴛᴀᴘ ᴛʜᴇ ʙᴜᴛᴛᴏɴ ʙᴇʟᴏᴡ ᴛᴏ sᴇᴛ ʏᴏᴜʀ ᴘʀᴏғɪʟᴇ ɪɴғᴏ
"""

    keyboard = [
        [InlineKeyboardButton("⚙️ Set Profile", url=f"https://t.me/{context.bot.username}")]
    ]

    reply_markup = InlineKeyboardMarkup(keyboard)

    if photo:
        await update.message.reply_photo(photo=photo, caption=text, reply_markup=reply_markup)
    else:
        await update.message.reply_text(text, reply_markup=reply_markup)


if __name__ == "__main__":
    if not TOKEN:
        raise ValueError("TOKEN not found! Add it in Railway Variables.")

    app = ApplicationBuilder().token(TOKEN).build()
    app.add_handler(CommandHandler("profile", profile))

    print("Bot started successfully...")
    app.run_polling()
