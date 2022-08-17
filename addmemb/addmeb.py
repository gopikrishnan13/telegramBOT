import asyncio
from telethon import TelegramClient, events
from telethon.tl.functions.messages import AddChatUserRequest
from telethon.tl.functions.messages import ImportChatInviteRequest

# Use your own values from my.telegram.org
api_id = 16305757
api_hash = 'fab5a363019d1f552e5ca3026ae06053'
session_name = 'anon'


async def main():
    client = TelegramClient(session_name, api_id, api_hash)
    await client.start()
    s = await client.get_entity('+918807411913')
    # await client.send_message(s, 'hello')
    await client.addChatUserRequest()
    # await client.edit_message('me', 'hello')
    # await client.get_me()
    # print(client.is_connected())
# await client.send_message('RED_7BOT', 'hello', '')


asyncio.run(main())
