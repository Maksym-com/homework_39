from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup


def dynamyc_kb(text_button):
    return InlineKeyboardMarkup(
        inline_keyboard=[
            [InlineKeyboardButton(text=text, callback_data=text) for text in text_button]
        ]
    )


Quest = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Для атаки мобів', callback_data='0'), InlineKeyboardButton(text='Для дерева', callback_data='1'), InlineKeyboardButton(text='Для камня', callback_data='2')],
    ]
)

Quest0 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Палки + камінь', callback_data='3'), InlineKeyboardButton(text='Палки + дошки', callback_data='4'), InlineKeyboardButton(text='Палка + дерево', callback_data='5')],
    ]
)

Quest1 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='3', callback_data='6'), InlineKeyboardButton(text='6', callback_data='7'), InlineKeyboardButton(text='7', callback_data='7')],
    ]
)

Quest2 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Так', callback_data='8'), InlineKeyboardButton(text='Так, якщо погодувати її', callback_data='9'), InlineKeyboardButton(text='Ні', callback_data='10')],
    ]
)

Quest3 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text="1-3 куска м'яса", callback_data='11'), InlineKeyboardButton(text="0-2 куска м'яса", callback_data='12'), InlineKeyboardButton(text="1-2 куска м'яса", callback_data='13')],
    ]
)

Quest4 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Залізні', callback_data='14'), InlineKeyboardButton(text="Дерев'яні", callback_data='15'), InlineKeyboardButton(text='Скляні', callback_data='16')],
    ]
)

Quest5 = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Кріпери', callback_data='17'), InlineKeyboardButton(text='Фантоми', callback_data='18'), InlineKeyboardButton(text='Зомбі', callback_data='19')],
    ]
)