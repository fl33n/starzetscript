from os import system, makedirs
from time import sleep
from random import choice

try:
    from pyrogram import Client, filters
except ImportError:
    system('pip3 install pyrogram')

user_id = input('Введи chat_id(@userinfobot): ')

try:
    makedirs('sessions')
except:
    pass

app = Client("sessions/session")
app.set_parse_mode("html")

@app.on_message(filters.all)
async def handler(client, message):
    try:
        user_mess = message.text

        if '.hearts' in message.text and message.from_user.id == user_id:
            hearts = '❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 '*25
            for heart in hearts.split(' '):
                sleep(1)
                await app.edit_message_text(message.chat.id, message.message_id, heart, disable_web_page_preview=True)
            await app.edit_message_text(message.chat.id, message.message_id, '<i>Сделать такую анимацию - @starzetscript</i>', disable_web_page_preview=True)

        elif '.hackchat' in message.text and message.from_user.id == user_id:
            for percent in range(100):
                s = f"[{(percent // 10) * '■'}"
                s += f"{(10 - (percent // 10)) * '○'}] "
                s += f"{percent}"
                await app.edit_message_text(message.chat.id, message.message_id, s, disable_web_page_preview=True)
                sleep(0.01)
            await app.edit_message_text(message.chat.id, message.message_id, '<b><u>Чат взломан!</u></b>\n\n<i>Сделать такую анимацию - @starzetscript</i>', disable_web_page_preview=True)

        elif '.help' in message.text and message.from_user.id == user_id:
            text = '🥷🏻 <b>Комманды бота:</b>\n\n<code>.hearts</code> - Анимация сердечек\n<code>.hackchat</code> - Взлом чата\n\n<i>Сделать такой же себе - @starzetscript</i>'
            await app.edit_message_text(message.chat.id, message.message_id, text, disable_web_page_preview=True)

    except Exception as e:
        pass

app.run()
