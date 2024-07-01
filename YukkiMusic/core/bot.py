#
# Copyright (C) 2024 by TheTeamVivek@Github, < https://github.com/TheTeamVivek >.
#
# This file is part of < https://github.com/TheTeamVivek/YukkiMusic > project,
# and is released under the "GNU v3.0 License Agreement".
# Please see < https://github.com/TheTeamVivek/YukkiMusic/blob/master/LICENSE >
#
# All rights reserved.
#

import sys
from pyrogram import Client
from pyrogram.enums import ChatMemberStatus
from pyrogram.types import BotCommand
import config

from ..logging import LOGGER


class YukkiBot(Client):
    def __init__(self):
        LOGGER(__name__).info(f"Starting Bot")
        super().__init__(
            "YukkiMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        get_me = await self.get_me()
        self.username = get_me.username
        self.id = get_me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.mention = self.me.mention

        try:
            await self.send_message(
                config.LOG_GROUP_ID,
                text=f"<u><b>» {self.mention} 𝙰𝙻𝙴𝙼 𝙼𝚄̈𝚉𝙸̇𝙺 𝙱𝙰𝚂̧𝙻𝙰𝙳𝙸 :</b><u>\n\n𝙸𝙳 : <code>{self.id}</code>\n𝙰𝙳𝙸 : {self.name}\n𝙺𝚄𝙻𝙻𝙰𝙽𝙸𝙲𝙸 𝙰𝙳𝙸 : @{self.username}",
            )
        except:
            LOGGER(__name__).error(
                "Bot has failed to access the log Group. Make sure that you have added your bot to your log channel and promoted as admin!"
            )
            sys.exit()
        if config.SET_CMDS:
            try:
                await self.set_bot_commands(
                    [
                        BotCommand("help", "Yardım Menüsünü Açar"),
                        BotCommand("ping", "Yaşıyormuyum?"),
                        BotCommand("play", "Parça Oynatmaya Başlar"),
                        BotCommand("skip", "Listedeki Diğer Parçaya Geçer"),
                        BotCommand("pause", "Yayını Duraklatır"),
                        BotCommand("resume", "Parça Oynatmaya Devam Eder"),
                        BotCommand("end", "Yayını Sonlandırır"),
                        BotCommand("shuffle", "Parça Listesini Karıştırır"),
                        BotCommand(
                            "playmode",
                            "Aʟʟᴏᴡs ʏᴏᴜ ᴛᴏ ᴄʜᴀɴɢᴇ ᴛʜᴇ ᴅᴇғᴀᴜʟᴛ ᴘʟᴀʏᴍᴏᴅᴇ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ",
                        ),
                        BotCommand(
                            "settings",
                            "Oᴘᴇɴ ᴛʜᴇ sᴇᴛᴛɪɴɢs ᴏғ ᴛʜᴇ ᴍᴜsɪᴄ ʙᴏᴛ ғᴏʀ ʏᴏᴜʀ ᴄʜᴀᴛ.",
                        ),
                    ]
                )
            except:
                pass
        else:
            pass
        a = await self.get_chat_member(config.LOG_GROUP_ID, self.id)
        if a.status != ChatMemberStatus.ADMINISTRATOR:
            LOGGER(__name__).error("Please promote Bot as Admin in Logger Group")
            sys.exit()
        if get_me.last_name:
            self.name = get_me.first_name + " " + get_me.last_name
        else:
            self.name = get_me.first_name
        LOGGER(__name__).info(f"𝙰𝙻𝙴𝙼 𝙼𝚄̈𝚉𝙸̇𝙺 𝙱𝙰𝚂̧𝙻𝙰𝙳𝙸 as {self.name}")
