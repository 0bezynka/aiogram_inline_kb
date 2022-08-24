import logging
import typing

from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.utils.callback_data import CallbackData
from aiogram.utils.exceptions import MessageNotModified

TOKEN = 'TOKEN'

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)


# Клавиатура при вызове каманды 'panel'
def panel():
    return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton('Просто кнопка', callback_data=vote_cb.new(action='prosto')),
        types.InlineKeyboardButton('Удалить', callback_data=vote_cb.new(action='del')),
    ).row(
        types.InlineKeyboardButton('Изменить', callback_data=vote_cb.new(action='change')),
        types.InlineKeyboardButton('кнопка', callback_data=vote_cb.new(action='tap4')),
        types.InlineKeyboardButton('кнопка', callback_data=vote_cb.new(action='tap4')),
    ).row(
        types.InlineKeyboardButton('Пример', callback_data=vote_cb.new(action='primer')),
    )

# Клавиатура для примера 'primer'
def primer():
	return types.InlineKeyboardMarkup().row(
        types.InlineKeyboardButton('Назад', callback_data=vote_cb.new(action='home')),
        types.InlineKeyboardButton('Вперед', callback_data=vote_cb.new(action='home')),
    )

# Каманда вызывающая панель '/panel'
@dp.message_handler(commands=['panel'])
async def cmd_panel(message: types.Message):
		await message.reply('Панель управления', reply_markup=panel())


vote_cb = CallbackData('vote', 'action')

# Все новые кнопки, а именно их " action='prosto' " необходимо добовлять в конце этого списка ...
@dp.callback_query_handler(vote_cb.filter(action=['prosto','del','change','primer', 'home', 'tap4']))# Сюда нужно дописывать 
async def callback_vote_action(query: types.CallbackQuery, callback_data: typing.Dict[str, str]):
    chat_id = (query.message.chat.id) # айди чата
    msg_id = (query.message.message_id) # айди сообщения
    
    await query.answer('Жмяк!') # Всплывающее сообщение
    callback_data_action = callback_data['action']

    if callback_data_action == 'prosto':
        await bot.send_message(chat_id,"Просто текст")
    
    elif callback_data_action == 'del':
        await bot.delete_message(chat_id, msg_id)
        # Удаление сообщения "msg_id" в нашем чате "chat_id"
        await bot.send_message(chat_id,"Сообщение удалено")
        # Отправка сообщения в наш чат "chat_id"
    
    elif callback_data_action == 'change':
        await bot.edit_message_text('Сообщение изменено\nЕсть возможность подключить кнопки к нему\nНажми на \'Пример\'', chat_id, msg_id,)
        # Изменяет сообщение
    
    elif callback_data_action == 'tap4':
        await bot.send_message(chat_id,"Что то другое ...")
        # Пустая кнопка ...

    elif callback_data_action == 'primer':
        await bot.edit_message_text('Много много много много много текста\nМного много много много много текста', chat_id, msg_id, reply_markup=primer())
        # Изменяет сообщение
        # Выводит новую клавиатуру "primer()"  
	
    elif callback_data_action == 'home':
        await bot.edit_message_text('Панель управления', chat_id, msg_id, reply_markup=panel())
        # Снова изменяет сообщение
        # Выводит старую клавиатуру "panel()"
    
# -----------------------------------------------------------------    
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
