import json
import random
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters


def get_random_quote(author):
    with open('bot/data/quotes.json', 'r', encoding='utf-8') as file:
        data = json.load(file)

    if author is None:
        quotes = data['quotes']
        quote = random.choice(quotes)
        return f"{quote['quote']} - {quote['author']}"
    else:
        quotes = [quote for quote in data['quotes'] if quote['author'].lower() == author.lower()]
        if quotes:
            quote = random.choice(quotes)
            return f"{quote['quote']} - {quote['author']}"
        else:
            return f"No quotes found for author: {author}"

async def quoteCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) == 0:
        await update.message.reply_text(get_random_quote(None))
    else:
        author = " ".join(args)
        await update.message.reply_text(get_random_quote(author))

__handlers__ = [
    [
        CommandHandler(
            "quote",
            quoteCommand
        )
    ]
]