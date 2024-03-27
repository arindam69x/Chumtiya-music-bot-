from typing import Union

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from IO import app


def help_pannel(_, START: Union[bool, int] = None):
    first = [InlineKeyboardButton(text=_["CLOSE_BUTTON"], callback_data=f"close")]
    second = [
        InlineKeyboardButton(
            text=_["BACK_BUTTON"],
            callback_data=f"settingsback_helper",
        ),
    ]
    mark = second if START else first
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["ADMINP"],
                    callback_data="help_callback hb1",
                ),
                InlineKeyboardButton(
                    text=_["AUTHP"],
                    callback_data="help_callback hb2",
                ),
                InlineKeyboardButton(
                    text=_["BROADP"],
                    callback_data="help_callback hb3",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["BLCP"],
                    callback_data="help_callback hb4",
                ),
                InlineKeyboardButton(
                    text=_["BLUP"],
                    callback_data="help_callback hb5",
                ),
                InlineKeyboardButton(
                    text=_["CPLAYP"],
                    callback_data="help_callback hb6",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["GBANP"],
                    callback_data="help_callback hb7",
                ),
                InlineKeyboardButton(
                    text=_["LOOPP"],
                    callback_data="help_callback hb8",
                ),
                InlineKeyboardButton(
                    text=_["IOP"],
                    callback_data="help_callback hb9",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["PINGP"],
                    callback_data="help_callback hb10",
                ),
                InlineKeyboardButton(
                    text=_["PLAYP"],
                    callback_data="help_callback hb11",
                ),
                InlineKeyboardButton(
                    text=_["SHUFFLEP"],
                    callback_data="help_callback hb12",
                ),
            ],
            [
                InlineKeyboardButton(
                    text=_["SEEKP"],
                    callback_data="help_callback hb13",
                ),
                InlineKeyboardButton(
                    text=_["SONGP"],
                    callback_data="help_callback hb14",
                ),
                InlineKeyboardButton(
                    text=_["SPEEDP"],
                    callback_data="help_callback hb15",
                ),
            ],
            mark,
        ]
    )
    return upl


def help_back_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text=_["BACK_BUTTON"],
                    callback_data=f"settings_back_helper",
                ),
            ]
        ]
    )
    return upl


def private_help_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text=_["S_B_4"],
                url=f"https://t.me/{app.username}?start=help",
            ),
        ],
    ]
    return buttons
