import os
import platform
from telethon import TelegramClient
import asyncio

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

    api_id = 123456
    api_hash = "default"
    #request_api_credentials(api_id, api_hash)

    # Crea una sessione per il client
    client = TelegramClient('my', api_id, api_hash)

    try:
        # Avvia il client
        await client.start()
        clear_console()
        print("Client started successfully.")

        # Stampa il tuo numero di telefono per confermare la connessione
        me = await client.get_me()
        print(f'Logged in as {me.username}')

        dialogs = []
        async for dialog in client.iter_dialogs():
            dialogs.append(dialog)

        print(f"{len(dialogs)} dialogs found")
        print("Chats")
        for chat in dialogs:
            if chat.is_user:
                if chat.title != '':
                    print(f"Name: {chat.title}")
                else:
                    print("Name: Deleted Account")

        print("Groups")
        for group in dialogs:
            if group.is_group:
                print(f"Title: {group.title}, Name: {group.name}")

        print("Channels")
        for channel in dialogs:
            if channel.is_channel:
                print(f"Title: {channel.title}, Name: {channel.name}")

    except Exception as e:
        print(f"An error occurred: {e}")

    finally:
        # Chiudi la connessione
        await client.disconnect()


if __name__ == "__main__":
    # Esegui la funzione main() in un loop di evento asyncio
    asyncio.run(main())
