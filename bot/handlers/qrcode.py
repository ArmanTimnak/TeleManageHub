import qrcode
import os
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

def generate_qr_code(data, filename):
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(data)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(filename)

async def qrcodeCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    args = context.args
    if len(args) == 0:
        await update.message.reply_text("Please provide a text to generate QR code.")
        return
    text = " ".join(args)
    filename = f"{text}.jpg"
    generate_qr_code(text, filename)
    caption = f'QR code for: "{text}"'
    await update.message.reply_photo(photo=open(filename, "rb"), caption=caption)
    os.remove(filename)


__handlers__ = [
    [
        CommandHandler(
            "qrcode",
            qrcodeCommand
        )
    ]
]