from aiogram.types import (KeyboardButton, Message, ReplyKeyboardMarkup,
                           ReplyKeyboardRemove, KeyboardButtonPollType)
from aiogram.utils.keyboard import ReplyKeyboardBuilder

menu_kb_builder = ReplyKeyboardBuilder()
game_kb_builder = ReplyKeyboardBuilder()

start_but = KeyboardButton(text='Start')

cancel_but = KeyboardButton(text='Quit')

rock_but = KeyboardButton(text='Rock')

paper_but = KeyboardButton(text='Paper')

scissors_but = KeyboardButton(text='Scissors')

menu_buttons: list[KeyboardButton] = {
    start_but, cancel_but
}

menu_kb_builder.row(*menu_buttons, width=2)
menu_kb: ReplyKeyboardMarkup = menu_kb_builder.as_markup(resize_keyboard=True, 
                                                                   input_field_placeholder='Press the button' 
                                                                                           'to start the game',
                                                                   one_time_keyboard=True)

game_buttons: list[KeyboardButton] = {
    rock_but,
    paper_but,
    scissors_but
}

game_kb_builder.row(*game_buttons, width=1)
game_kb: ReplyKeyboardMarkup = game_kb_builder.as_markup(resize_keyboard=True,
                                                         one_time_keyboard=True)