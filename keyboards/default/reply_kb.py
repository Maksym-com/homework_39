from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

text_button = [
        [['Для атаки мобів', 'Для дерева', 'Для камня']],
        [['Палки + камінь', 'Палки + дошки', 'Палка + дерево']],
        [['3', '6', '7']],
        [['Так', 'Так, якщо погодувати її', 'Ні']],
        [["1-3 куска м'яса", "0-2 куска м'яса", "1-2 куска м'яса"]],
        [['Залізні', "Дерев'яні", 'Скляні']],
        [['Кріпери', 'Фантоми', 'Зомбі']]
]

def dynamic_reply_kb(quiz_button):
    return ReplyKeyboardMarkup(
        keyboard=[
            [KeyboardButton(text=text) for text in row] for row in quiz_button
        ],
        resize_keyboard=True,
        one_time_keyboard=True
    )
