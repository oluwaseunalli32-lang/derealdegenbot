import os
import logging
from telegram import (
    Update,
    InlineKeyboardButton,
    InlineKeyboardMarkup,
)
from telegram.ext import (
    Application,
    CommandHandler,
    ContextTypes,
)

# --------------------------------------------------
# Logging
# --------------------------------------------------
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

# --------------------------------------------------
# Environment Variable
# --------------------------------------------------
TOKEN = os.getenv("TOKEN")


# --------------------------------------------------
# /start
# --------------------------------------------------
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [
            InlineKeyboardButton(
                "📢 Telegram Channel",
                url="https://t.me/Derealdegen"
            )
        ],
        [
            InlineKeyboardButton(
                "ℹ️ About",
                callback_data="about"
            ),
            InlineKeyboardButton(
                "❓ Help",
                callback_data="help"
            )
        ],
        [
            InlineKeyboardButton(
                "📸 Instagram",
                url="https://www.instagram.com/olayin__01?igsh=c3hyaGtlcGpkYmtu"
            ),
            InlineKeyboardButton(
                "🎵 TikTok",
                url="https://www.tiktok.com/@jamiielin?is_from_webapp=1&sender_device=pc"
            )
        ]
    ]

    await update.message.reply_text(
        text=(
            "<b>Welcome to DeRealDegen Bot</b>\n\n"
            "Access the official DeRealDegen community and social channels.\n\n"
            "Use the buttons below to explore available resources."
        ),
        parse_mode="HTML",
        reply_markup=InlineKeyboardMarkup(keyboard),
    )


# --------------------------------------------------
# /about
# --------------------------------------------------
async def about(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        (
            "<b>About DeRealDegen</b>\n\n"
            "This bot provides access to the official DeRealDegen community "
            "and social media accounts.\n\n"
            "Follow our official channels to receive community updates and announcements."
        ),
        parse_mode="HTML",
    )


# --------------------------------------------------
# /help
# --------------------------------------------------
async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        (
            "<b>Available Commands</b>\n\n"
            "/start - Open the main menu\n"
            "/about - Learn about DeRealDegen\n"
            "/help - View available commands"
        ),
        parse_mode="HTML",
    )


# --------------------------------------------------
# Callback Buttons
# --------------------------------------------------
async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    if query.data == "about":
        await query.edit_message_text(
            (
                "<b>About DeRealDegen</b>\n\n"
                "This bot provides access to the official DeRealDegen community "
                "and social media accounts.\n\n"
                "Use the Telegram Channel button to join the community."
            ),
            parse_mode="HTML",
        )

    elif query.data == "help":
        await query.edit_message_text(
            (
                "<b>Help</b>\n\n"
                "Use the available buttons to access official DeRealDegen resources.\n\n"
                "Commands:\n"
                "/start\n"
                "/about\n"
                "/help"
            ),
            parse_mode="HTML",
        )


# --------------------------------------------------
# Main
# --------------------------------------------------
def main():
    if not TOKEN:
        logger.error("TOKEN environment variable not found.")
        return

    app = Application.builder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("about", about))
    app.add_handler(CommandHandler("help", help_command))

    from telegram.ext import CallbackQueryHandler

    app.add_handler(CallbackQueryHandler(button_handler))

    logger.info("DeRealDegen Bot is running...")

    app.run_polling()


if __name__ == "__main__":
    main()
