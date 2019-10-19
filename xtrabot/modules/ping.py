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

from xtrabot import loader
from xtrabot.xtrautil import Module
from datetime import datetime

class Ping(loader.Module):
    def __init__(self):
        self.name = "ping"
        super().__init__([self.ping, self.aboutping])
        self.addxconfig("PING", "Pong!\n", "Defines Ping Message")

    async def ping(self, event):
        start = datetime.now()
        await event.edit(self.xconfig["PING"])
        end = datetime.now()
        ms = (end - start).microseconds / 1000
        await event.edit("Pong!\n{}ms".format(ms))

    async def aboutping(self, event):
        abbout = (self.xconfig["PING"]).about()
        await event.edit(abbout)

Module(Ping)
