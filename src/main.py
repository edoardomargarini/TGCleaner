import os
import platform
from telethon import TelegramClient
import asyncio
from flask import Flask, render_template

flask_app = Flask('TGCleaner')

dialogs_raw = []
api_id = 12345
api_hash = 'abcdefghi'
client = TelegramClient('my', api_id, api_hash)

ASCII_art = """\
      _____ ___  ___ _
     |_   _/ __|/ __| |___ __ _ _ _  ___ _ _
       | || (_ | (__| / -_) _` | ' \/ -_) '_|
       |_| \___|\___|_\___\__,_|_||_\___|_|
    """

def clear_console():
    if platform.system() == "Windows":
        os.system('cls')
    else:
        os.system('clear')
@flask_app.route('/')
def index():
    dialogs = {
        'chats': [],
        'groups': [],
        'channels': []
    }

    for dialog in dialogs_raw:
        if dialog.is_user:
            dialogs['chats'].append(dialog)
        elif dialog.is_group:
            dialogs['groups'].append(dialog)
        elif dialog.is_channel:
            dialogs['channels'].append(dialog)
    print(dialogs['chats'][0])
    return render_template('home.html', dialogs=dialogs)


def request_api_credentials(api_id, api_hash):
    try:
        api_id = int(input("Insert your API_ID: "))
    except ValueError:
        print("API_ID must be an integer number.")
        return

    api_hash = input("Insert your API_HASH: ")
    print("Remember to put the phone's prefix (ex. +39)")
async def main():
    clear_console()
    print(ASCII_art)

    print("Visit https://docs.telethon.dev/en/stable/basic/signing-in.html for more information on how to obtain free Telegram API credentials.")

    #request_api_credentials(api_id, api_hash)

    # Crea una sessione per il client

    try:
        # Avvia il client
        await client.start()
        clear_console()
        me = await client.get_me()
        print(f'Logged in as {me.username}')
        print("Starting Server...")

        async for dialog in client.iter_dialogs():
            dialogs_raw.append(dialog)

        flask_app.run(debug=False, host='localhost', port=5123)

    

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Chiudi la connessione
        await client.disconnect()


if __name__ == "__main__":
    # Esegui la funzione main() in un loop di evento asyncio
    asyncio.run(main())
