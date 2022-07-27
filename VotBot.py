import telebot
from config import TOKEN, keys
from extensions import APIException, CryptoConverter

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def start_help(message: telebot.types.Message):
    text = 'Чтобы начать работу введите коменду: \n <сколько переводим>\
    <какую валюты переводим>\
    <в какую валюту переводим (по умолчанию рубль)>\
    \n Список доступнях валют команда /values'
    bot.reply_to(message, text)

@bot.message_handler(commands=['values'])
def echo_val(message: telebot.types.Message):
    text = 'Доступные валюты:'
    for i in keys.keys():
        text = '\n'.join((text, i, ))
    bot.reply_to(message, text)

@bot.message_handler(content_types='text')
def convert(message: telebot.types.Message):
    try:
        values = message.text.split(' ')
        if len(values) != 3 and len(values) != 2 :
            raise APIException('Нужно указать 3 параметра')
        else:
            if len(values) == 2:
                values.append('рубль')
            amount, quote, base  = values
            t_base = CryptoConverter.convetr(quote, base, amount)
    except APIException as e:
        bot.reply_to(message, f'Ошибка пользователя\n{e}')
    except Exception as e:
        bot.reply_to(message, f'Не удалось обработать команду\n{e}')
    else:
        text = f'Цена {amount} {quote} в {base} ровна {t_base * float(amount)}'
        bot.send_message(message.chat.id, text)

bot.polling()