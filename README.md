# Шаблон inline-кнопок
Лично мне нужны были для чат-бота ... Всё интуитивно просто написал, комментарии в коде и здесь кратко опишу.

Создаем функцию под названием 'panel' в ней через метод 'InlineKeyboardMarkup' создаем клавиатуру. В 'action' указываем индивидуальный ключ для каждой кнопки.
> return types.InlineKeyboardMarkup().row(types.InlineKeyboardButton('Текст_кнопки', callback_data=vote_cb.new(action='ключ')),)

Создаем обработчик каманды, в моем случае '/panel' .
> @dp.message_handler(commands=['panel'])

В ней методом 'message.reply' отвечаем на сообщение и ввыводи клавиатуру 'reply_markup' которую поместили в функцию 'panel()'
> await message.reply('Панель управления', reply_markup=panel())

Каждую новую кнопку необходимо добавить в обработчик (в конце списка дописать) 
> @dp.callback_query_handler(vote_cb.filter(action=['кнопка1','кнопка2','кнопка3']))

В дальнейшем, через 'if/elif' прописать действия за которые отвечает каждая кнопка.
> if callback_data_action == 'кнопка1':

Есть два (на мое мнение) важных/удобных метода. Это удаление сообщение и редактирование сообщения. Айди чата 'chat_id', айди сообщения 'msg_id' которое нужно удалить/изменить
> await bot.delete_message(chat_id, msg_id).
> 
> await bot.edit_message_text('Сообщение', chat_id, msg_id,).

Очень удобно через метод 'edit_message_text' изменять текст сообщения при этом влаживать новые кнопки, расширяя функционал и возможности вашего бота. Как то так ...

---

> Мои контакты [Instagram](https://www.instagram.com/just.gray) / [Telegram](https://t.me/justgrayy)
