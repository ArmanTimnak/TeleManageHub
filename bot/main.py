import logging, os, httpx, json

from dotenv import load_dotenv
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from handlers import all_handlers

# Load environment variables
load_dotenv()
bot_token = os.getenv("BOT_TOKEN")

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"Welcome to TeleManageHub! 🤖 \n\nYour ultimate Telegram companion for effortless group and channel management. Type /help to dive into a world of features.\n\nLet's enhance your Telegram experience! 🚀",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")

def main() -> None:
    application = Application.builder().token(bot_token).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("help", help_command))

    for handler in all_handlers:
        if len(handler) == 2:
            application.add_handler(
                handler[0],
                handler[1]
            )
        else:
            application.add_handler(
                handler[0]
            )
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()