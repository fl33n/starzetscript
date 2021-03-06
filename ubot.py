from os import system, makedirs
from time import sleep
from random import choice

try:
    from pyrogram import Client, filters
except ImportError:
    system('pip3 install pyrogram')
    from pyrogram import Client, filters

try:
    makedirs('sessions')
except:
    pass

app = Client("sessions/session", 6309881, '0e1e408300ff1b4703dda93c4eaeb67f')
app.set_parse_mode("html")

@app.on_message(filters.me)
async def handler(client, message):
    try:
        if '.hearts' in message.text:
            hearts = '❤️ 🧡 💛 💚 💙 💜 🖤 🤍 🤎 '*25
            for heart in hearts.split(' '):
                sleep(1)
                await app.edit_message_text(message.chat.id, message.message_id, heart, disable_web_page_preview=True)
            await app.edit_message_text(message.chat.id, message.message_id, '<i>Сделать такую анимацию - @starzetscript</i>', disable_web_page_preview=True)

        elif '.hackchat' in message.text:
            for percent in range(100):
                s = f"[{(percent // 10) * '■'}"
                s += f"{(10 - (percent // 10)) * '○'}] "
                s += f"{percent}"
                await app.edit_message_text(message.chat.id, message.message_id, s, disable_web_page_preview=True)
                sleep(0.01)
            await app.edit_message_text(message.chat.id, message.message_id, '<b>Чат взломан!</b>\n\n<i>Сделать такую анимацию - @starzetscript</i>', disable_web_page_preview=True)

        elif '.test' in message.text:
            tochki = ''
            for i in range(3):
                tochki += '.'
                await app.edit_message_text(message.chat.id, message.message_id, f'<i>Определяем</i>{tochki}', disable_web_page_preview=True)
            ls = list(range(0,100))
            await app.edit_message_text(message.chat.id, message.message_id, f'<b>Вы гей на {choice(ls)}%!</b>\n\n<i>Сделать такую анимацию - @starzetscript</i>', disable_web_page_preview=True)

        elif '.help' in message.text:
            text = '🥷🏻 <b>Комманды бота:</b>\n\n<code>.hearts</code> - Анимация сердечек\n<code>.hackchat</code> - Взлом чата\n<code>.test</code> - Тест?\n\n<i>Сделать такой же себе - @starzetscript</i>'
            await app.edit_message_text(message.chat.id, message.message_id, text, disable_web_page_preview=True)
    except Exception as e:
        pass

app.run()