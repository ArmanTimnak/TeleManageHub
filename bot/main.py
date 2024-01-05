import logging, os, httpx, json
import difflib
import glob
from os.path import dirname, basename, isfile, join
from dotenv import load_dotenv
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

from handlers import all_handlers

# Load environment variables
load_dotenv()
bot_token = os.getenv("BOT_TOKEN")
sudo_users = os.getenv("SUDO_USERS")
admin_group_id = os.getenv("ADMIN_GROUP_ID")

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)

logging.getLogger("httpx").setLevel(logging.WARNING)

logger = logging.getLogger(__name__)

modules = glob.glob(join(dirname(__file__), "handlers", "*.py"))
a = [basename(f)[:-3] for f in modules if isfile(f)
    and not f.endswith('__init__.py')]

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    user = update.effective_user
    await update.message.reply_html(
        f"Welcome to TeleManageHub! 🤖 \n\nYour ultimate Telegram companion for effortless group and channel management. Type /help to dive into a world of features.\n\nLet's enhance your Telegram experience! 🚀",
        reply_markup=ForceReply(selective=True),
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    await update.message.reply_text("Help!")

async def unknown(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
        command = update.message.text.strip()
        similar_commands = difflib.get_close_matches(command, a)
        if similar_commands:
            most_similar_command = similar_commands[0]
            await update.message.reply_text(f"Command not found! Did you mean /{most_similar_command}?")
        else:
            await update.message.reply_text("Command not found!")

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
    
    application.add_handler(MessageHandler(filters.ChatType.PRIVATE, unknown))
    
    application.run_polling(allowed_updates=Update.ALL_TYPES)


if __name__ == "__main__":
    main()
