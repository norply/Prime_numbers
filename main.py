import telebot
token = "5928142015:AAF8FNlMUXlIGiNVHauiIYcVRuvqFUDnsSI"
numbers = []
a = 0
b = 0
bot = telebot.TeleBot(token)


@bot.message_handler(commands=['start'])
def start(message):
  bot.send_message(message.chat.id,'Этот бот предназначен для вывода простых чисел в заданном диапазоне. Введите левую границу диапазона.')


@bot.message_handler(content_types='text')
def message_a(message):
    global a
    a = int(message.text)
    mesg = bot.send_message(message.chat.id, 'Введите правую границу диапазона')
    bot.register_next_step_handler(mesg, message_b)


@bot.message_handler(content_types='text')
def message_b(message):
    global b
    b = int(message.text)
    for s in range(a, b + 1):
        for n in range(2, s):
            if s % n == 0:
                break
        else:
            numbers.append(s)
    bot.send_message(message.chat.id, 'Результат:')
    bot.send_message(message.chat.id, str(numbers))


bot.polling(none_stop=True)
