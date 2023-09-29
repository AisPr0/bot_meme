import config
import telebot
import random

from pars import Pars
import time

bot = telebot.TeleBot(config.token)



@bot.message_handler(content_types=["text"])
def repeat_all_messages(message):
    m = bot.send_message(message.chat.id, "обработка... ")
    bot.edit_message_text(chat_id=m.chat.id, message_id=m.message_id, text=f"{m.text} {random.randint(1, 20)}%")


    time.sleep(2)
    bot.edit_message_text(chat_id=m.chat.id, message_id=m.message_id, text=f"{m.text} {random.randint(20, 50)}%")
    # ищем meme png
    id = message.text
    pars = Pars(id)
    pars0 = pars.str1
    bot.edit_message_text(chat_id=m.chat.id, message_id=m.message_id, text=f"{m.text} {random.randint(50, 80)}%")
    par = 'bot.send_media_group(message.chat.id,[' + pars0 + '])'
    bot.edit_message_text(chat_id=m.chat.id, message_id=m.message_id, text=f"{m.text} {random.randint(80, 99)}%")
    # задержка
    time.sleep(3)
    bot.edit_message_text(chat_id=m.chat.id, message_id=m.message_id, text=f"Готово! 100%")
    # кнопки
    m = telebot.types.ReplyKeyboardMarkup(resize_keyboard=True)
    btn1 = telebot.types.KeyboardButton("Собака")
    btn2 = telebot.types.KeyboardButton("Кот")
    btn3 = telebot.types.KeyboardButton(message.text)
    m.add(btn1, btn2, btn3)

    # приветствие
    bot.send_message(message.chat.id, text="Привет {0.first_name}!".format(message.from_user), reply_markup=m)
    bot.send_message(message.chat.id, message.text)
    # картинки meme
    if pars0 != 'err':
        #print(pars0)
        try:
            eval(par)
        except telebot.apihelper.ApiTelegramException:
            bot.edit_message_text(chat_id=m.chat.id, message_id=m.message_id, text=f"=( мне бан")
    else:
        bot.send_message(message.chat.id, text="_=( нет meme_", parse_mode="Markdown")
    # картинки meme

if __name__ == '__main__':
     bot.infinity_polling()


