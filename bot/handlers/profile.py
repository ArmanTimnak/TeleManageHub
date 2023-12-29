from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

async def profile(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    if update.effective_user.is_premium:
        premium = "Yes"
    else:
        premium = "No"
    
    await update.message.reply_text(
        "🪪 Your profile info:\n\n"
        f"🆔 ID: `{update.effective_user.id}`\n"
        f"👨 Name: `{update.effective_user.full_name}`\n"
        f"🏷️ Username: @{update.effective_user.username}\n"
        f"🈳 Language: `{update.effective_user.language_code}`\n"
        f"🌟 Premium User: {premium}\n"
        f"🔗 Profile Link: [{update.effective_user.full_name}](t.me/{update.effective_user.username})",
        parse_mode="MarkdownV2"
    )

__handlers__ = [
    [
        CommandHandler(
            "profile",
            profile
        )
    ]
]