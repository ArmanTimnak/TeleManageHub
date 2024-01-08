import pytz
import requests
import json
from telegram import ForceReply, Update
from telegram.ext import Application, CommandHandler, ContextTypes, MessageHandler, filters

def getData(country, endpoints=None):
    if endpoints:
        endpoint_str = ",".join(endpoints)
        data = requests.get(f"https://restcountries.com/v3.1/alpha/{country}?fields={endpoint_str}").json()
        return data
    else:
        data = requests.get(f"https://restcountries.com/v3.1/alpha/{country}").json()
        return data

async def countryCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    country = context.args
    if not country:
        await update.message.reply_text(
            "🪪 Please provide a country code to get information about it.",
            parse_mode="MarkdownV2"
        )
        return
    else:
        country = " ".join(country)
        data = getData(country, ["name", "capital", "region", "subregion", "population", "area", "languages", "currencies"])
        if "status" in data:
            await update.message.reply_text(
                "🪪 Country not found! Please provide a valid country code."
            )
            return
        else:
            name = data["name"]["common"]
            capital = data["capital"][0]
            region = data["region"]
            subregion = data["subregion"]
            population = data["population"]
            area = data["area"]
            languages = ", ".join(data["languages"])
            currencies = ", ".join(data["currencies"])
            await update.message.reply_text(
                f"🪪 Information about `{name}`:\n\n"
                f"🏛️ Capital: `{capital}`\n"
                f"🌐 Region: `{region}`\n"
                f"🌐 Subregion: `{subregion}`\n"
                f"👥 Population: `{population}`\n"
                f"🗺️ Area: `{area} km²`\n"
                f"🗣️ Languages: `{languages}`\n"
                f"💰 Currencies: `{currencies}`\n",
                parse_mode="MarkdownV2"
            )

__handlers__ = [
    [
        CommandHandler(
            "country",
            countryCommand
        )
    ]
]
