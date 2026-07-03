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
PORT = int(os.getenv("PORT", "8000"))
WEBHOOK_URL = os.getenv("WEBHOOK_URL")  # Render URL e.g., https://your-app.onrender.com

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
    
    # Using HTML parse mode to prevent markdown crashes
    await update.message.reply_text(text=welcome_text, reply_markup=reply_markup, parse_mode="HTML")

def main() -> None:
    """Start the bot."""
    if not TOKEN:
        logger.error("No TOKEN found in environment variables!")
        return

    # Build the application
    application = Application.builder().token(TOKEN).build()

    # Register the /start command handler
    application.add_handler(CommandHandler("start", start))

    # Check if deploying to Render via Webhook or running locally via Polling
    if WEBHOOK_URL:
        logger.info(True)
        application.run_webhook(
            listen="0.0.0.0",
            port=PORT,
            url_path=TOKEN,
            webhook_url=f"{WEBHOOK_URL}/{TOKEN}"
        )
    else:
        logger.info("Starting local polling...")
        application.run_polling()

if __name__ == "__main__":
    main()
