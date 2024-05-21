from aiogram import Bot, Dispatcher, types, executor
from config import TELEGRAM_TOKEN

bot = Bot(token=TELEGRAM_TOKEN)
dp = Dispatcher(bot)

async def set_commands(bot: Bot):
    commands = [
        types.BotCommand(command = '/start', description = 'Команда для того, чтобы запустить бота'),
        types.BotCommand(command = '/help', description = 'Команда для того, чтобы узнать, с чем может помочь бот'),
        types.BotCommand(command ='/product', description ='Каталог товаров'),
    ]
    await bot.set_my_commands(commands)


@dp.message_handler(commands= 'start')
async def start(message: types.Message):
    await message.reply('Привет')

@dp. message_handler(commands= 'help')
async def help(message: types.Message):
    await message.reply('Я могу помочь тебе с...')

@dp. message_handler(commands= 'product')
async def product(message: types.Message):
    await message.reply('У нас есть...')

@dp. message_handler()
async def echo(message:types.Message):
    await message.answer(message.text)

async def on_startup(dispatcher):
    await set_commands(dispatcher.bot)

if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True, on_startup= on_startup)



