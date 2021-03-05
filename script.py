import telebot
from telebot import types


bot = telebot.TeleBot("1657434198:AAHavyv_LqK9JuR4McDFEpiC4NeUHbTHEso")


@bot.message_handler(content_types=['text'])
def series(message):
    textepisode = 'Блич серия ' + str(message.text)
    series.episodes = int(message.text)
    episodevideo =   str(series.episodes) + '.mp4'
    
    markup = types.InlineKeyboardMarkup()
    item1 = types.InlineKeyboardButton(text='Следующая серия', callback_data='next')
    item2 = types.InlineKeyboardButton(text='Предыдущая серия', callback_data='prev')
    markup.add(item2, item1)
    video = open(episodevideo, 'rb')
    bot.send_video(message.chat.id, video, supports_streaming=True)
    bot.send_message(message.chat.id, textepisode , reply_markup=markup)
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.data == 'next':
        series.episodes = int(series.episodes) + 1
    elif call.data == 'prev':
        series.episodes = int(series.episodes) - 1
bot.polling(none_stop=True)