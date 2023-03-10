# MIT License
#
# Copyright (c) 2023 AnonymousX1025
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

from pyrogram import filters
from pyrogram.types import Message
from pytgcalls.types import AudioPiped, HighQualityAudio

from FallenMusic import BOT_USERNAME, app, fallendb, pytgcalls
from FallenMusic.Helpers import _clear_, admin_check, buttons, close_key, gen_thumb


@app.on_message(filters.command(["skip", "next"]) & filters.group)
@admin_check
async def skip_str(_, message: Message):
    try:
        await message.delete()
    except:
        pass
    get = fallendb.get(message.chat.id)
    if not get:
        try:
            await _clear_(message.chat.id)
            await pytgcalls.leave_group_call(message.chat.id)
            await message.reply_text(
                text=f"โป ๐๐๐๐ ๐๐ช๐ฆ ๐๐๐๐ ๐๐๐ช๐ ๐๐๐ฅบ\nโ \nโสส : {message.from_user.mention} ๐ฅ\n\n**ยป ษดแด แดแดสแด วซแดแดแดแดแด แดสแดแดแดs ษชษด** {message.chat.title}, **๐๐๐๐๐๐ช๐ ๐๐?๐ง๐ ๐ช๐?๐ฆ .**",
                reply_markup=close_key,
            )
        except:
            return
    else:
        title = get[0]["title"]
        duration = get[0]["duration"]
        file_path = get[0]["file_path"]
        videoid = get[0]["videoid"]
        req_by = get[0]["req"]
        user_id = get[0]["user_id"]
        get.pop(0)

        stream = AudioPiped(file_path, audio_parameters=HighQualityAudio())
        try:
            await pytgcalls.change_stream(
                message.chat.id,
                stream,
            )
        except:
            await _clear_(message.chat.id)
            return await pytgcalls.leave_group_call(message.chat.id)

        await message.reply_text(
            text=f"โป แดแดษดแด สแดแด ๐ฅบ\nโ \nโสส : {message.from_user.mention} ๐ฅ",
            reply_markup=close_key,
        )
        img = await gen_thumb(videoid, user_id)
        return await message.reply_photo(
            photo=img,
            caption=f"**โป sแดแดสแดแดแด sแดสแดแดแดษชษดษข**\n\nโฃ **แดษชแดสแด :** [{title[:27]}](https://t.me/{BOT_USERNAME}?start=info_{videoid})\nโฃ **แดแดสแดแดษชแดษด :** `{duration}` แดษชษดแดแดแดs\nโฃ **สแดวซแดแดsแดแดแด สส :** {req_by}",
            reply_markup=buttons,
        )
