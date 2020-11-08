import telebot

WeatherBot = telebot.TeleBot('1382011405:AAFAVt71bbOvqz5JsLUkpWqdn2Kt_BcbKc0')

@WeatherBot.message_handler(func = lambda message: True)
def weather(message):
    #x, y = map(int, message.text.split())
    #WeatherBot.reply_to(message, str(x+y))
    if message.text == 'write':
        data = 'hui'
        WeatherBot.reply_to(message, 'data saved')
    if message.text == 'read':
        WeatherBot.reply_to(message, data)

    # if message.text == '/start':
    #     WeatherBot.reply_to(message, 'Давай посчитаем!')
    # elif message.text == 'Привет' or message.text == 'Привет!':
    #     WeatherBot.reply_to(message, 'Здорово, ' + str(message.from_user.first_name)+'!')
    # elif message.text == 'Москва':
    #     WeatherBot.reply_to(message, 'Сейчас отличная погода!')
    # elif message.text == 'Москва завтра':
    #     WeatherBot.reply_to(message, 'Завтра еще лучше')
    # else:
    #     WeatherBot.reply_to(message, 'Я тебя не понял')

WeatherBot.polling()