#Используем библиотеку PyTelegramBotAPI 

import telebot
from telebot import types

TOKEN = '.................................'#Токен своего робота
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(m):
    keyboard = types.InlineKeyboardMarkup(row_width=2)
    itembtn1 = types.InlineKeyboardButton(text='💰 Пенсия', callback_data='💰 Пенсия')
    itembtn2 = types.InlineKeyboardButton(text='👨‍✈️ Денежное довольствие', callback_data='👨‍✈️ Денежное довольствие')
    itembtn3 = types.InlineKeyboardButton(text='✍️ Выслуга', callback_data='✍️ Выслуга')
    itembtn4 = types.InlineKeyboardButton(text='🏠 Жилищная субсидия', callback_data='🏠 Жилищная субсидия')
    keyboard.add(itembtn1, itembtn2, itembtn3, itembtn4)
    bot.send_message(m.chat.id, 'Привет!!!\n'
      'Выбери что хочешь расчитать', reply_markup=keyboard)

@bot.callback_query_handler(func=lambda c: True)
def inline(c):
    if c.data == '💰 Пенсия':
        bot.answer_callback_query(callback_query_id=c.id, show_alert=False, text="Выбран расчет пенсии!!!")
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Для расчета необходимо выбрать следующие данные',
            parse_mode='Markdown')
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        itembtn5 = types.InlineKeyboardButton(text='Тарифный разряд', callback_data='💰')
        itembtn6 = types.InlineKeyboardButton(text='Лётный класс', callback_data='👨‍✈️')
        itembtn7 = types.InlineKeyboardButton(text='Звание', callback_data='✍️')
        itembtn8 = types.InlineKeyboardButton(text='Надбавка за выслугу', callback_data='🏠')
        itembtn9 = types.InlineKeyboardButton(text='Размер пенсии в %', callback_data='🏠')
        itembtn10 = types.InlineKeyboardButton(text='Районный коэффициент', callback_data='🏠')
        itembtn11 = types.InlineKeyboardButton(text='Год выплаты пенсии', callback_data='🏠')
        itembtn12 = types.InlineKeyboardButton(text='🔙 Назад', callback_data='🔙 Назад')
        keyboard.add(itembtn5, itembtn6, itembtn7, itembtn8, itembtn9, itembtn10, itembtn11, itembtn12)
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=keyboard)
#Здесь идёт описание остальных пунктов меню...
#    elif c.data == '👨‍✈️ Денежное довольствие':
#        bot.edit_message_text(
#            chat_id=c.message.chat.id,
#            message_id=c.message.message_id,
#            text='Для расчета необходимо выбрать следующие данные',
#            parse_mode='Markdown')


#Пытаюсь создать кнопку назад, для перехода в основное меню, не получается!!!
@bot.callback_query_handler(func=lambda c: True)       
def inline(c):
    if c.data == '🔙 Назад':
        bot.answer_callback_query(callback_query_id=c.id, show_alert=False, text="Возврат в основное меню")
        bot.edit_message_text(
            chat_id=c.message.chat.id,
            message_id=c.message.message_id,
            text='Привет!!!\n' 'Выбери что хочешь расчитать',
            parse_mode='Markdown')
        keyboard = types.InlineKeyboardMarkup(row_width=2)
        itembtn13 = types.InlineKeyboardButton(text='💰 Пенсия', callback_data='💰 Пенсия')
        itembtn14 = types.InlineKeyboardButton(text='👨‍✈️ Денежное довольствие', callback_data='👨‍✈️ Денежное довольствие')
        itembtn15 = types.InlineKeyboardButton(text='✍️ Выслуга', callback_data='✍️ Выслуга')
        itembtn16 = types.InlineKeyboardButton(text='🏠 Жилищная субсидия', callback_data='🏠 Жилищная субсидия')
        keyboard.add(itembtn13, itembtn14, itembtn15, itembtn16)
        bot.edit_message_reply_markup(chat_id=c.message.chat.id, message_id=c.message.message_id, reply_markup=keyboard)
#    elif c.data == '👨‍✈️ Денежное довольствие':
#        bot.edit_message_text(
#            chat_id=c.message.chat.id,
#            message_id=c.message.message_id,
#            text='Для расчета необходимо выбрать следующие данные',
#            parse_mode='Markdown')

bot.polling()
