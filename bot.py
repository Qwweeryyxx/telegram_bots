import telebot
from config import TOKEN
from texts import text
import webbrowser

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=["start"])
def start(message):
    print("кто-то ввёл /start")
    bot.send_message(message.chat.id, f"Привет {message.from_user.first_name}")
    print(message)


@bot.message_handler(commands=["profile"])
def profile(message):
    print("кто-то ввёл /profile")
    bot.reply_to(message, f"""вот ваш профиль 👥\n
ваше имя: {message.from_user.first_name}
ваш ник @{message.from_user.username}
ваш ID: {message.id}
код языка: {message.from_user.language_code}
premium: {message.from_user.is_premium}""")

@bot.message_handler(commands=['help'])
def help(message):
    print("кто-то ввёл /help")
    bot.send_message(message.chat.id, text[1])

@bot.message_handler(commands=["browser"])
def browser(message):
    print("кто-то ввёл /browser")
    bot.send_message(message.chat.id, text[2])
    webbrowser.open("www.google.com")
    

@bot.message_handler(commands=['audio'])
def audio(message):
    print("кто-то ввёл /audio")
    bot.reply_to(message, text[4])


@bot.message_handler()
def chat(message):
    if message.text.lower() == "привет":
        print("кто-то поздаровался!")
        bot.reply_to(message, "Приветики мой дорогой друг!")
    elif message.text.lower() == "как дела" or "как дела?":
        bot.reply_to(message, "У меня всё ПРОСТО ПРЕВОСХОДНО!\n Сам как?)")
    else:
        bot.reply_to(message, "!!!ERROR!!!")

bot.polling(none_stop=True)