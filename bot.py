import os
import logging
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, ContextTypes

# Enable logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

# Constants
TOKEN = os.getenv("TOKEN")

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    """Sends a message with inline buttons when the command /start is issued."""
    welcome_text = (
        "Welcome to <b>DeRealDegen Bot</b>! 🚀\n\n"
        "We track the markets, hunt the alpha, and bring you the latest crypto updates "
        "before they hit the mainstream.\n\n"
        "Stay connected with the movement using the buttons below: 👇"
    )

    # Inline Keyboard Buttons using HTML safely
    keyboard = [
        [
            InlineKeyboardButton("📢 Telegram Channel", url="https://t.me/Derealdegen")
        ],
        [
            InlineKeyboardButton("📸 Instagram", url="https://www.instagram.com/olayin__01?igsh=c3hyaGtlcGpkYmtu"),
            InlineKeyboardButton("🎵 TikTok", url="https://www.tiktok.com/@jamiielin?is_from_webapp=1&sender_device=pc")
        ]
    ]
    
    reply_markup = InlineKeyboardMarkup(keyboard)
    
    # Using HTML parse mode to prevent formatting crashes
    await update.message.reply_text(text=welcome_text, reply_markup=reply_markup, parse_mode="HTML")

def main() -> None:
    """Start the bot using polling as a continuous background worker."""
    if not TOKEN:
        logger.error("No TOKEN found in environment variables!")
        return

    # Build the application
    application = Application.builder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Continuous long-polling perfect for background workers
    logger.info("DeRealDegen Bot worker starting polling...")
    application.run_polling()

if __name__ == "__main__":
    main()
