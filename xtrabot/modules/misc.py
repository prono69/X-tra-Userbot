#    X-tra-Telegram (userbot for telegram)
#    Copyright (C) 2019-2019 The Authors

#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.

#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.

#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <https://www.gnu.org/licenses/>.

from xtrabot import loader, utils
from xtrabot.xtrautil import start_module, Module
from pathlib import Path

class Misc(loader.Module):
    def __init__(self):
        self.name = "misc"
        super().__init__(self.install)
        self.addxconfig("installed message", "Yay, {shortname} has been added to your modules!!", "the message to the left is the one pops up when the module is installed")
        self.addxconfig("directory", "xtrabot/modules/", "is the modules directory")

    async def install(self, event):
        reply = await event.get_reply_message()
        text = await event.reply("Processing...")
        hmm = await event.client.download_media(reply, self.xconfig["directory"])
        path = Path(hmm)
        try:
            start_module(path.stem.replace(".py", ""))
        except Exception as e:
            await utils.answer(text, str(e), call="edit")
            return
        else:
            await utils.answer(text, (self.xconfig["installed message"]).format(path.stem.replace(".py", "")), call="edit")

Module(Misc)
