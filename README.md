# TeleManageHub

TeleManageHub is a bot that provides various functionalities such as handling country information, Morse code conversion, user profile management, QR code generation, and quote sharing.

## Features

- Country Information: Fetches and provides information about different countries. Implemented in [`country.py`](bot/handlers/country.py).
- Morse Code Conversion: Converts normal text to Morse code and vice versa. Implemented in [`morse.py`](bot/handlers/morse.py).
- User Profile Management: Handles user profile information. Implemented in [`profile.py`](bot/handlers/profile.py).
- QR Code Generation: Generates QR codes. Implemented in [`qrcode.py`](bot/handlers/qrcode.py).
- Quote Sharing: Shares interesting quotes. Implemented in [`quote.py`](bot/handlers/quote.py).

## Data

The bot uses data from the following files:

- `facts.json`: Contains various facts used by the bot. Located in [`bot/data/facts.json`](bot/data/facts.json).
- `quotes.json`: Contains quotes used by the bot. Located in [`bot/data/quotes.json`](bot/data/quotes.json).

More information about the data sources can be found in the [`SOURCES.md`](bot/data/SOURCES.md) file.

## Usage

To use the bot, run the `main.py` file in the `bot` directory:

## Contributing

We welcome contributions! Please see the [`CONTRIBUTING.md`](CONTRIBUTING.md) file for more details.

## Code of Conduct

We expect contributors to follow our code of conduct, which can be found in the [`CODE_OF_CONDUCT.md`](CODE_OF_CONDUCT.md) file.

## Style Guide

We follow a specific style guide for this project. You can find it in the [`STYLEGUIDE.md`](STYLEGUIDE.md) file.

## License

This project is licensed under the MIT License. See the [`LICENSE`](LICENSE) file for more details.

