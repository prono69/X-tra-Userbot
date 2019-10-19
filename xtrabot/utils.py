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

async def answer(event, text, **args):
    call = args.get("call", "edit")
    actions = {"edit": event.edit, "reply": event.reply, "respond": event.respond}
    action = actions[call]
    if event.reply_to_msg_id:
        reply_to_id = event.reply_to_msg_id
    if len(text) > 4095:
        with io.BytesIO(str.encode(text)) as out_file:
            out_file.name = "result.txt"
            await event.client.send_file(
                event.chat_id,
                out_file,
                force_document=True,
                allow_cache=False,
                caption=cmd,
                reply_to=reply_to_id
            )
            await event.delete()
    else:
        tmp = await action(text)
        return tmp
