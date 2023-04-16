from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def botplaylist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Personal",
                callback_data="get_playlist_playmode",
            ),
            InlineKeyboardButton(
                text="Global", callback_data="get_top_playlists"
            ),
        ],
        [
            InlineKeyboardButton(
                text="Close", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Top 10 Playlists", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="Personal", callback_data="SERVERTOP user"
            )
        ],
        [
            InlineKeyboardButton(
                text="Global", callback_data="SERVERTOP global"
            ),
            InlineKeyboardButton(
                text="Group's", callback_data="SERVERTOP chat"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="Close", callback_data="close"
            ),
        ],
    ]
    return buttons


def get_playlist_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Audio", callback_data="play_playlist a"
            ),
            InlineKeyboardButton(
                text="Video", callback_data="play_playlist v"
            ),
        ],
        [
            InlineKeyboardButton(
                text="ʙᴀᴄᴋ", callback_data="home_play"
            ),
            InlineKeyboardButton(
                text="Close", callback_data="close"
            ),
        ],
    ]
    return buttons


def top_play_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Top 10 Playlists", callback_data="SERVERTOP"
            )
        ],
        [
            InlineKeyboardButton(
                text="Personal", callback_data="SERVERTOP Personal"
            )
        ],
        [
            InlineKeyboardButton(
                text="Global", callback_data="SERVERTOP Global"
            ),
            InlineKeyboardButton(
                text="Group's", callback_data="SERVERTOP Group"
            )
        ],
        [
            InlineKeyboardButton(
                text="Back", callback_data="get_playmarkup"
            ),
            InlineKeyboardButton(
                text="Close", callback_data="close"
            ),
        ],
    ]
    return buttons


def failed_top_markup(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="Back",
                callback_data="get_top_playlists",
            ),
            InlineKeyboardButton(
                text="Close", callback_data="close"
            ),
        ],
    ]
    return buttons


def warning_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Delete",
                    callback_data="delete_whole_playlist",
                ),
            ],
            [
                InlineKeyboardButton(
                    text="Back",
                    callback_data="del_back_playlist",
                ),
                InlineKeyboardButton(
                    text="Close",
                    callback_data="close",
                ),
            ],
        ]
    )
    return upl


def close_markup(_):
    upl = InlineKeyboardMarkup(
        [
            [
                InlineKeyboardButton(
                    text="Close",
                    callback_data="close",
                ),
            ]
        ]
    )
    return upl
