from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboards.keyboard as kb

from service.services import get_random_answer, get_winner

rout = Router()

@rout.message(F.text.lower().in_(['start', 'let\'s play', 'let\'s start', 'game', 'play']))
async def start_proc(message: Message):
    await message.answer('Great! Make your choice!', 
                         reply_markup=kb.game_kb)

@rout.message(F.text.in_(['Rock', 'Paper', 'Scissors']))
async def game_proc(message: Message):
    bot_ans: str = get_random_answer()
    user_ans: str = message.text
    await message.answer(text=f'Bot - {bot_ans}\n\nYou - {user_ans}\n\n{get_winner(user_ans, bot_ans)}')
    await message.answer('Do you want to play again?', 
                         reply_markup=kb.menu_kb)

@rout.message(F.text.lower().in_(['quit', 'cancel', 'stop']))
async def stop_proc(message: Message):
    await message.answer('If you ever want to play again just text me or open keyboard and press \'Start\' :)',
                         reply_markup=kb.menu_kb)

@rout.message()
async def other_proc(message: Message):
    await message.answer('I am a pretty limited bot\nLet\'s just play the game?')