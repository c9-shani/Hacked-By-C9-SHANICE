# C9-SHANI Telegram Bot
# Author: C9-SHANI
# Team: Black Hat Ethical Hackers
# King Of Hacking 👑

from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Updater, CommandHandler, CallbackQueryHandler, CallbackContext
import os

# Bot token set as environment variable
BOT_TOKEN = os.environ.get("BOT_TOKEN")

# ------------------ BUTTON MENU ------------------ #
def start(update: Update, context: CallbackContext):
    keyboard = [
        [InlineKeyboardButton("🌐 Website Tools", callback_data='website')],
        [InlineKeyboardButton("📁 File Tools", callback_data='file')],
        [InlineKeyboardButton("📥 Downloader", callback_data='downloader')],
        [InlineKeyboardButton("🤖 AI Assistant", callback_data='ai')],
        [InlineKeyboardButton("⚙️ Utilities", callback_data='utilities')],
        [InlineKeyboardButton("☪️ Islamic Tools", callback_data='islamic')]
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    update.message.reply_text(
        "🤖 Welcome to C9-SHANI Bot 🚀\n\n"
        "Choose a category:\n",
        reply_markup=reply_markup
    )

# ------------------ CALLBACK HANDLER ------------------ #
def button(update: Update, context: CallbackContext):
    query = update.callback_query
    query.answer()
    choice = query.data

    if choice == "website":
        query.edit_message_text(
            "🌐 Website Tools:\n"
            "1. Website Status Checker\n"
            "2. DNS Lookup\n"
            "3. Robots.txt Viewer\n"
            "4. Sitemap Finder\n"
            "5. SSL Certificate Checker\n\n"
            "Powered by C9-SHANI\nTeam Black Hat Ethical Hackers\nKing Of Hacking 👑"
        )
    elif choice == "file":
        query.edit_message_text(
            "📁 File Tools:\n"
            "- PDF → Image Converter\n"
            "- Image Compressor\n"
            "- File Size Checker\n"
            "- File Format Converter\n\n"
            "Powered by C9-SHANI\nTeam Black Hat Ethical Hackers\nKing Of Hacking 👑"
        )
    elif choice == "downloader":
        query.edit_message_text(
            "📥 Downloader Tools:\n"
            "- YouTube Video Downloader\n"
            "- Instagram Media Downloader\n"
            "- Audio Converter\n\n"
            "Powered by C9-SHANI\nTeam Black Hat Ethical Hackers\nKing Of Hacking 👑"
        )
    elif choice == "ai":
        query.edit_message_text(
            "🤖 AI Tools:\n"
            "- AI Chat Assistant\n"
            "- Text Generator\n"
            "- Code Helper\n"
            "- Language Translator\n\n"
            "Powered by C9-SHANI\nTeam Black Hat Ethical Hackers\nKing Of Hacking 👑"
        )
    elif choice == "utilities":
        query.edit_message_text(
            "⚙️ Utilities:\n"
            "- Reminder System\n"
            "- Weather Checker\n"
            "- Currency Converter\n\n"
            "Powered by C9-SHANI\nTeam Black Hat Ethical Hackers\nKing Of Hacking 👑"
        )
    elif choice == "islamic":
        query.edit_message_text(
            "☪️ Islamic Tools:\n"
            "- Daily Islamic Reminders\n"
            "- Quran Quotes\n\n"
            "Powered by C9-SHANI\nTeam Black Hat Ethical Hackers\nKing Of Hacking 👑"
        )

# ------------------ MAIN ------------------ #
def main():
    updater = Updater(BOT_TOKEN)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CallbackQueryHandler(button))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()