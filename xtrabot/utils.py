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
