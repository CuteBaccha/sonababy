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

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

import config
from FallenMusic import BOT_USERNAME

close_key = InlineKeyboardMarkup(
    [[InlineKeyboardButton(text="✯💥𝗰𝗹𝗼𝘀𝗲💥✯", callback_data="close")]]
)


buttons = InlineKeyboardMarkup(
    [
        [
            InlineKeyboardButton(text="▷", callback_data="resume_cb"),
            InlineKeyboardButton(text="II", callback_data="pause_cb"),
            InlineKeyboardButton(text="‣‣I", callback_data="skip_cb"),
            InlineKeyboardButton(text="▢", callback_data="end_cb"),
        ]
    ]
)


pm_buttons = [
    [
        InlineKeyboardButton(
            text="💥𝗮𝗱𝗱 𝗸𝗿 𝗹𝗼 𝗯𝗮𝗯𝘆💥",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [InlineKeyboardButton(text="💥𝗰𝗼𝗺𝗺𝗮𝗻𝗱 𝗵𝗮𝗶 𝗱𝗲𝗸𝗼💥", callback_data="fallen_help")],
    [
        InlineKeyboardButton(text="💥 𝗯𝗮𝗯𝘆 𝗷𝗼𝗶𝗻 𝗸𝗿𝗹𝗼 💥", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="💥 𝗶𝘀𝗸𝗼 𝗯𝗵𝗶 𝗸𝗿 𝗹𝗼 𝗻𝗮💥", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="💥𝗿𝗲𝗽𝗼 𝗰𝗵𝗮𝗶𝘆𝗮💥", url="https://t.me/REPO_I"
        ),
        InlineKeyboardButton(text="💥𝗼𝘄𝗻𝗲𝗿 𝗵𝘂 𝗺𝗲💥", user_id=config.OWNER_ID),
    ],
]


gp_buttons = [
    [
        InlineKeyboardButton(
            text="💥𝗯𝗼𝘁 𝗮𝗱𝗱 𝗸𝗿 𝗹𝗼💥",
            url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
        )
    ],
    [
        InlineKeyboardButton(text="💥 𝗯𝗮𝗯𝘆 𝗷𝗼𝗶𝗻 𝗸𝗿𝗹𝗼💥", url=config.SUPPORT_CHANNEL),
        InlineKeyboardButton(text="💥𝘆𝗲 𝗯𝗵𝗶 𝗸𝗿𝗹𝗼 𝗷𝗼𝗶𝗻💥", url=config.SUPPORT_CHAT),
    ],
    [
        InlineKeyboardButton(
            text="🔷 𝕃𝔼 𝕃𝕆𝕆 🔷", url="https://github.com/CuteBaccha/sonababy"
        ),
        InlineKeyboardButton(text="💥𝗴𝗶𝗿𝗹 𝗰𝗿𝘂𝘀𝗵💥", user_id=config.OWNER_ID),
    ],
]


helpmenu = [
    [
        InlineKeyboardButton(
            text="💥𝘀𝗼𝗻𝗮 𝗺𝘂𝘀𝗶𝗰💥",
            callback_data="fallen_cb help",
        )
    ],
    [
        InlineKeyboardButton(text="💥𝘀𝗮𝘀𝘁𝗮 𝗼𝘄𝗻𝗲𝗿💥", callback_data="fallen_cb sudo"),
        InlineKeyboardButton(text="💥𝗿𝗲𝗮𝗹 𝗼𝘄𝗻𝗲𝗿💥", callback_data="fallen_cb owner"),
    ],
    [
        InlineKeyboardButton(text="💥𝗯𝗮𝗰𝗸💥", callback_data="fallen_home"),
        InlineKeyboardButton(text="💥𝗰𝗹𝗼𝘀𝗲💥", callback_data="close"),
    ],
]


help_back = [
    [InlineKeyboardButton(text="💥𝗷𝗼𝗶𝗻 𝗸𝗿 𝗹𝗼 𝗯𝗮𝗯𝘆💥", url=config.SUPPORT_CHAT)],
    [
        InlineKeyboardButton(text="💥𝗯𝗮𝗰𝗸💥", callback_data="fallen_help"),
        InlineKeyboardButton(text="💥𝗰𝗹𝗼𝘀𝗲💥", callback_data="close"),
    ],
]
