# !/usr/bin/env python3
# -*- coding: utf-8 -*-
# Name     : inline-tube-mate [ Telegram ]
# Repo     : https://github.com/m4mallu/inine-tube-mate
# Author   : Renjith Mangal [ https://t.me/space4renjith ]

from urllib.parse import quote
from presets import Presets
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

start_btn = [
    [
        InlineKeyboardButton('Visualizar a Thumb', callback_data='view_btn'),
        InlineKeyboardButton('Apagar a Thumb', callback_data='del_btn')

    ],
    [
        InlineKeyboardButton('Ajuda?', callback_data='help_btn'),
        InlineKeyboardButton('Suporte', url='t.me/RMProjects')
    ],
    [
        InlineKeyboardButton('Fechar', callback_data='close_btn'),
        InlineKeyboardButton('Pesquisa Inline', switch_inline_query_current_chat='')
    ]
]


del_thumb = [
    [
        InlineKeyboardButton("Apagar THUMB", callback_data="thumb_del_conf_btn"),
        InlineKeyboardButton("Voltar", callback_data="a_back_btn")
    ]
]

join_channel = [
    [
        InlineKeyboardButton('⚙ Entre', url='https://telegram.me/GR4V3_S4D_CRAZZY'),
        InlineKeyboardButton('Pesquisar via inline', switch_inline_query_current_chat='')
    ]
]


back_button = [
    [
        InlineKeyboardButton('⬅️ Voltar', callback_data='back_btn')
    ]
]

close_button = [
    [
        InlineKeyboardButton('❌ Fechar', callback_data='close_btn'),
        InlineKeyboardButton('Voltar o inicial', callback_data='home_btn')
    ]
]

cancel_button = [
    [
        InlineKeyboardButton('Cancelar', callback_data='cancel_btn')
    ]
]

prompt_thumb_btn = [
    [
        InlineKeyboardButton('Sim', callback_data='set_thumb_btn'),
        InlineKeyboardButton('Não', callback_data='close_btn')
    ]
]

reply_markup_cancel = InlineKeyboardMarkup(cancel_button)
reply_markup_close = InlineKeyboardMarkup(close_button)
reply_markup_back = InlineKeyboardMarkup(back_button)
reply_markup_join = InlineKeyboardMarkup(join_channel)
reply_markup_del_thumb = InlineKeyboardMarkup(del_thumb)
reply_markup_start = InlineKeyboardMarkup(start_btn)
reply_markup_thumb = InlineKeyboardMarkup(prompt_thumb_btn)

def get_reply_markup(username):
    url = 't.me/share/url?url=' + quote(Presets.SHARE_BUTTON_TEXT.format(username=username))
    buttons = [[InlineKeyboardButton('Share bot', url=url),
                InlineKeyboardButton("Search Inline", switch_inline_query_current_chat='')]]
    reply_markup_share = InlineKeyboardMarkup(buttons)
    return reply_markup_share
