from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import keyboards.keyboard as kb

rout = Router()

@rout.message(Command('start'))
async def start_cmd(message: Message):
    await message.answer(text=f'Hello there, {message.from_user.first_name}!\n'
                         f'Do you want to play the game?\n\n'
                         'If you have any questions about the game rules - '
                         'just type \'help\' to get information', 
                         reply_markup=kb.menu_kb
                        )
                         

@rout.message(Command('help'))
async def help_cmd(message: Message):
    await message.answer(f'The Game rules:\n\nRock beats Scissors, Scissors beats Paper, '
        f'and Paper beats Rock\n\nAvaliable commands:\n/help - rules '
        f'of the game and list of commands\n'
        f'/stat - view statistics\n\nLet\'s play?',
         reply_markup=kb.menu_kb
         )
    
@rout.message(Command('stat'))
async def stat_cmd(message: Message):
    await message.answer()