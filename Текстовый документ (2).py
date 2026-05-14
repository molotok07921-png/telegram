import telebot

TOKEN = "8780318044:AAG9e3XO3dUi6IZCO34B8DYsvQY3Umq_BXQ"

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "Привет, бот работает ✅")

print("Бот запущен")

bot.infinity_polling()