from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

def text_to_morse(text):
    morse_code = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
        'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
        'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.', '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-', '&': '.-...',
        ':': '---...', ';': '-.-.-.', '=': '-...-', '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.', '$': '...-..-', '@': '.--.-.',
        ' ': '/'
    }

    morse_text = ''
    for char in text.upper():
        if char in morse_code:
            morse_text += morse_code[char] + ' '
        else:
            morse_text += char + ' '

    return morse_text.strip()

async def morseCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    text = context.args
    if not text:
        await update.message.reply_text(
            "🪪 Please provide some text to convert to morse code.",
            parse_mode="MarkdownV2"
        )
        return
    else:
        text = " ".join(text)
        morse_text = text_to_morse(text)
        await update.message.reply_text(
            f"🪪 Morse code for `{text}` is:\n\n"
            f"`{morse_text}`",
            parse_mode="MarkdownV2"
        )

__handlers__ = [
    [
        CommandHandler(
            "morse",
            morseCommand
        )
    ]
]
