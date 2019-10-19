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
from xtrabot.xtrautil import Module
from datetime import datetime

class Util(loader.Module):
    def __init__(self):
        self.name = "ping"
        super().__init__([self.ping, self.help])
        self.addxconfig("PING", "Pong!\n", "Defines Ping Message")

    async def ping(self, event):
        start = datetime.now()
        await utils.answer(event, self.xconfig["PING"][0])
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit("Pong!\n{}ms".format(ms))

    async def help(self, event):
        await utils.answer(event, "No help yet.")

Module(Util)
