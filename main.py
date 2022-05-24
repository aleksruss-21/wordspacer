# -*- coding: utf-8 -*-

import telebot
import make_bot
import pandas as pd


TOKEN = "TOKEN TG BOT"
bot = telebot.TeleBot(TOKEN, parse_mode=None)
message_id = 0

@bot.message_handler(commands=['start'])
def send_welcome(message):
    bot.send_message(message.chat.id, f"{message.chat.first_name}, привет! Напиши любую фразу, чтобы украсить текст.")
    dict_base = {
        "id": [message.chat.id],
        "username": [message.chat.username],
        "first_name": [message.chat.first_name],
        "last_name": [message.chat.last_name],
    }
    db = pd.read_csv("database/base.csv")
    if message.chat.id not in set(db.id):
        new_id = pd.DataFrame.from_dict(dict_base)
        new_id.to_csv("database/base.csv", mode="a", header=False)


@bot.message_handler(func=lambda message: True)
def message_upd(message):
    global message_id
    if len(message.text) < 3:
        bot.send_message(message.chat.id, "Текст сообщения должен состоять из трех или более символов.")
    elif len(message.text) > 14:
        bot.send_message(message.chat.id, "В тексте не может быть более 14 символов.")
    else:
        make_bot.make_text(message, message_id)
        with open(f"users/{message.chat.id}/text1.txt") as word_upd:
            new_message = word_upd.read()
            bot.send_message(message.chat.id, new_message)

        with open(f"users/{message.chat.id}/text2.txt") as word_upd:
            new_message = word_upd.read()
            bot.send_message(message.chat.id, new_message)

        with open(f"users/{message.chat.id}/text3.txt") as word_upd:
            new_message = word_upd.read()
            bot.send_message(message.chat.id, new_message)

        with open(f"users/{message.chat.id}/text4.txt") as word_upd:
            new_message = word_upd.read()
            bot.send_message(message.chat.id, new_message)

        with open(f"users/{message.chat.id}/text5.txt") as word_upd:
            new_message = word_upd.read()
            bot.send_message(message.chat.id, new_message)

        with open(f"users/{message.chat.id}/text6.txt") as word_upd:
            new_message = word_upd.read()
            bot.send_message(message.chat.id, new_message)
        message_id += 1
        print(f"Количество отправленных сообщений: {message_id}")


bot.infinity_polling()
