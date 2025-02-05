# (©) iBOX TV

from aiohttp import web
from plugins import web_server

import pyromod.listen
import asyncio
from pyrogram import Client
from pyrogram.enums import ParseMode
import sys
from datetime import datetime

from config import API_HASH, APP_ID, LOGGER, TG_BOT_TOKEN, TG_BOT_WORKERS, FORCE_SUB_CHANNEL, FORCE_SUB_CHANNEL2, CHANNEL_ID, PORT

class Bot(Client):
    def __init__(self):
        super().__init__(
            name="Bot",
            api_hash=API_HASH,
            api_id=APP_ID,
            plugins={"root": "plugins"},
            workers=TG_BOT_WORKERS,
            bot_token=TG_BOT_TOKEN
        )
        self.LOGGER = LOGGER

    async def start(self):
        await super().start()
        usr_bot_me = await self.get_me()
        self.uptime = datetime.now()

        if FORCE_SUB_CHANNEL:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL)).invite_link
                self.invitelink = link
            except Exception as a:
                self.LOGGER(__name__).warning(f"⚠️ Error: {a}")
                self.LOGGER(__name__).warning("❌ Bot can't export invite link from Force Sub Channel!")
                self.LOGGER(__name__).warning(f"🔍 Double-check FORCE_SUB_CHANNEL: {FORCE_SUB_CHANNEL}")
                self.LOGGER(__name__).info("📌 Bot Stopped. Contact Support: https://t.me/iBox_TV")
                sys.exit()

        if FORCE_SUB_CHANNEL2:
            try:
                link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                if not link:
                    await self.export_chat_invite_link(FORCE_SUB_CHANNEL2)
                    link = (await self.get_chat(FORCE_SUB_CHANNEL2)).invite_link
                self.invitelink2 = link
            except Exception as a:
                self.LOGGER(__name__).warning(f"⚠️ Error: {a}")
                self.LOGGER(__name__).warning("❌ Bot can't export invite link from Force Sub Channel 2!")
                self.LOGGER(__name__).warning(f"🔍 Double-check FORCE_SUB_CHANNEL2: {FORCE_SUB_CHANNEL2}")
                self.LOGGER(__name__).info("📌 Bot Stopped. Contact Support: https://t.me/iBox_TV")
                sys.exit()

        try:
            db_channel = await self.get_chat(CHANNEL_ID)
            self.db_channel = db_channel
            test = await self.send_message(chat_id=db_channel.id, text="Test Message")
            await asyncio.sleep(3)
            await test.delete()
        except Exception as e:
            self.LOGGER(__name__).warning(f"⚠️ Error: {e}")
            self.LOGGER(__name__).warning(f"❌ Ensure bot is an admin in the DB Channel {CHANNEL_ID}")
            self.LOGGER(__name__).info("📌 Bot Stopped. Contact Support: https://t.me/iBox_TV")
            sys.exit()

        self.set_parse_mode(ParseMode.HTML)
        self.LOGGER(__name__).info(f"✅ Bot Running Successfully!\n🌟 Created by https://t.me/iBox_TV")
        self.username = usr_bot_me.username

        # Web Response Setup
        app = web.AppRunner(await web_server())
        await app.setup()
        bind_address = "0.0.0.0"
        await web.TCPSite(app, bind_address, PORT).start()

    async def stop(self, *args):
        await super().stop()
        self.LOGGER(__name__).info("🚫 Bot Stopped.")

    async def send_temp_message(self, chat_id, text):
        """Send a message that auto-deletes after 5 seconds"""
        msg = await self.send_message(chat_id=chat_id, text=text)
        await asyncio.sleep(5)
        await msg.delete()

    async def send_temp_file(self, chat_id, msg):
        """Send a file that auto-deletes after 5 seconds"""
        sent_msg = await msg.copy(chat_id=chat_id)
        await asyncio.sleep(5)
        await sent_msg.delete()

