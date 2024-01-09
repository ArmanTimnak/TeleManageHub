import requests
from telegram import Update
from telegram.ext import CommandHandler, ContextTypes

def getData(country, endpoints=None):
    if endpoints:
        endpoint_str = ",".join(endpoints)
        data = requests.get(f"https://restcountries.com/v3.1/alpha/{country}?fields={endpoint_str}").json()
    else:
        data = requests.get(f"https://restcountries.com/v3.1/alpha/{country}").json()
    return data


async def countryCommand(update: Update, context: ContextTypes.DEFAULT_TYPE) -> None:
    country = context.args[0]
    endpoint = context.args[1] if len(context.args) == 2 else None

    if not country:
        await update.message.reply_text(
            "🪪 Please provide a country code to get information about it.",
            parse_mode="MarkdownV2"
        )
        return
    elif len(context.args) == 1:
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
    
    elif endpoint:
        data = getData(country, [endpoint])
        
        if "status" in data:
            await update.message.reply_text(
                "🪪 Country not found! Please provide a valid country code."
            )
            return

        else:
            name = data["name"]["common"]

            if endpoint == "name":
                data = data["name"]["common"]
            elif endpoint == "capital":
                data = data["capital"][0]
            elif endpoint == "languages":
                data = ", ".join(data["languages"])
            elif endpoint == "currencies":
                data = ", ".join(data["currencies"])
            else:
                data = data[endpoint]

            if endpoint == "name":
                endpoint_emoji = "🪪"
            elif endpoint == "capital":
                endpoint_emoji = "🏛️"
            elif endpoint == "region":
                endpoint_emoji = "🌐"
            elif endpoint == "subregion":
                endpoint_emoji = "🌐"
            elif endpoint == "population":
                endpoint_emoji = "👥"
            elif endpoint == "area":
                endpoint_emoji = "🗺️"
            elif endpoint == "languages":
                endpoint_emoji = "🗣️"
            elif endpoint == "currencies":
                endpoint_emoji = "💰"
            
            endpoint = endpoint.title()
            await update.message.reply_text(
                f"🪪 Information about `{name}`:\n\n"
                f"{endpoint_emoji} {endpoint}: `{data}`\n",
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