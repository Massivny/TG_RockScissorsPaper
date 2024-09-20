import logging
import asyncio

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.types import BotCommand

from config_data.config import Config, load_config
from handlers import user_handlers, other_handlers
from keyboards.set_menu import set_main_menu

logger = logging.getLogger(__name__)
'''
async def set_main_menu(bot: Bot):
    main_menu_commands = [
        BotCommand(command='/help',
                   description='Avaliable commands and the game rules'),
        BotCommand(command='/stat',
                   description='View game statistics'),
        BotCommand(command='cancel',
                   description='Cancel the game')
    ]
    await bot.set_my_commands(main_menu_commands)
'''
async def main() -> None:
    logging.basicConfig(
        level=logging.INFO,
        format='%(filename)s:%(lineno)d #%(levelname)-8s '
               '[%(asctime)s] - %(name)s - %(message)s'
    )

    logger.info('Starting bot')

    config: Config = load_config()

    bot = Bot(config.tg_bot.token,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.include_router(user_handlers.rout)
    dp.include_router(other_handlers.rout)

    await set_main_menu(bot=bot)

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')

