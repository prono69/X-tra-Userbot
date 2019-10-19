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

from xtrabot import UniSupport as uni, client, PPESupport as ppe
import re
from telethon import events
import sys
import importlib
from pathlib import Path

import xtrabot.compat.userbot as userb
import xtrabot.compat.uniborg as unib
import xtrabot.compat.uniborg.sql_helpers as sqlh

def start_module(shortname):
    path = Path(f"xtrabot/modules/{shortname}.py")
    name = "xtrabot.modules.{}".format(shortname)
    spec = importlib.util.spec_from_file_location(name, path)
    mod = importlib.util.module_from_spec(spec)
    try:
        mod.__dict__["start"](Module)
    except Exception as e:
        print(e)
        sys.modules["userbot.modules"] = userb
        sys.modules["userbot"] = userb
        sys.modules["uniborg"] = unib
        sys.modules["sql_helpers"] = sqlh
        mod.borg = uni.borg
        mod.Config = uni
        spec.loader.exec_module(mod)

class Module():
    def __init__(self, cls):
        try:
            cls()
        except Exception as e:
            print(e)


