from telegram import (
    InlineKeyboardMarkup, InlineKeyboardButton,
)

inline_keyboard = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='DAILY', callback_data='type:daily'), InlineKeyboardButton(text='WEEKLY', callback_data='type:weekly')],
        [InlineKeyboardButton(text='MONTHLY', callback_data='type:monthly'), InlineKeyboardButton(text='ALL DATA', callback_data='type:all')]
    ]
)