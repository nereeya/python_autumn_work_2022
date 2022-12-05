import config
import telebot
from telebot import types
from telebot.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, InlineKeyboardButton
import random

token = "5887648421:AAGroc3oJgv6klTVnRBg45FUu3416DoFgTU"
bot = telebot.TeleBot(token)

first = ["Сегодня — идеальный день для новых начинаний.",
         "Оптимальный день для того, чтобы решиться на смелый поступок!",
         "Будьте осторожны, сегодня звёзды могут повлиять на ваше финансовое состояние.",
         "Лучшее время для того, чтобы начать новые отношения или разобраться со старыми.",
         "Плодотворный день для того, чтобы разобраться с накопившимися делами."]

second = ["Но помните, что даже в этом случае нужно не забывать про", "Если поедете за город, заранее подумайте про",
          "Те, кто сегодня нацелен выполнить множество дел, должны помнить про",
          "Если у вас упадок сил, обратите внимание на",
          "Помните, что мысли материальны, а значит вам в течение дня нужно постоянно думать про"]

second_add = ["отношения с друзьями и близкими.",
              "работу и деловые вопросы, которые могут так некстати помешать планам.",
              "себя и своё здоровье, иначе к вечеру возможен полный раздрай.",
              "бытовые вопросы — особенно те, которые вы не доделали вчера.",
              "отдых, чтобы не превратить себя в загнанную лошадь в конце месяца."]

third = ["Злые языки могут говорить вам обратное, но сегодня их слушать не нужно.",
         "Знайте, что успех благоволит только настойчивым, поэтому посвятите этот день воспитанию духа.",
         "Даже если вы не сможете уменьшить влияние ретроградного Меркурия, то хотя бы доведите дела до конца.",
         "Не нужно бояться одиноких встреч — сегодня то самое время, когда они значат многое.",
         "Если встретите незнакомца на пути — проявите участие, и тогда эта встреча посулит вам приятные хлопоты."]


@bot.message_handler(commands=['start'])
def send_welcome(message):
    start_menu = types.ReplyKeyboardMarkup(True, True, True, True)
    start_menu.row('Гороскоп на завтра', 'Интересные факты о знаках', 'Приложения')
    bot.reply_to(message,
                 "🌙Добро пожаловать!🌙\n ✨Только тут вы можете узнать самые точные предсказания ✨\n 🌜Выберите интересующий вас раздел🌛",
                 reply_markup=start_menu)


@bot.message_handler(commands=['stop'])
def bye(message):
    bot.reply_to(message, "Нам очень жаль, что вы нас покидаете!\n Мы будем скучать!")
    exit()


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    if message.text == "Гороскоп на завтра":
        bot.send_message(message.from_user.id, "я могу рассказать тебе твой гороскоп на завтра. ")
        keyboard = types.InlineKeyboardMarkup()
        key_oven = types.InlineKeyboardButton(text='Овен', callback_data='zodiac')
        keyboard.add(key_oven)
        key_telec = types.InlineKeyboardButton(text='Телец', callback_data='zodiac')
        keyboard.add(key_telec)
        key_bliznecy = types.InlineKeyboardButton(text='Близнецы', callback_data='zodiac')
        keyboard.add(key_bliznecy)
        key_rak = types.InlineKeyboardButton(text='Рак', callback_data='zodiac')
        keyboard.add(key_rak)
        key_lev = types.InlineKeyboardButton(text='Лев', callback_data='zodiac')
        keyboard.add(key_lev)
        key_deva = types.InlineKeyboardButton(text='Дева', callback_data='zodiac')
        keyboard.add(key_deva)
        key_vesy = types.InlineKeyboardButton(text='Весы', callback_data='zodiac')
        keyboard.add(key_vesy)
        key_scorpion = types.InlineKeyboardButton(text='Скорпион', callback_data='zodiac')
        keyboard.add(key_scorpion)
        key_strelec = types.InlineKeyboardButton(text='Стрелец', callback_data='zodiac')
        keyboard.add(key_strelec)
        key_kozerog = types.InlineKeyboardButton(text='Козерог', callback_data='zodiac')
        keyboard.add(key_kozerog)
        key_vodoley = types.InlineKeyboardButton(text='Водолей', callback_data='zodiac')
        keyboard.add(key_vodoley)
        key_ryby = types.InlineKeyboardButton(text='Рыбы', callback_data='zodiac')
        keyboard.add(key_ryby)
        bot.send_message(message.from_user.id, text='Выбери свой знак зодиака', reply_markup=keyboard)
    if message.text == "Интересные факты о знаках":
        bot.send_message(message.from_user.id, "Для начала узнаем общие факты про стихии")
        keyboard = types.InlineKeyboardMarkup()
        key_ogon = types.InlineKeyboardButton(text='Огонь', callback_data='ogon')
        keyboard.add(key_ogon)
        key_zemla = types.InlineKeyboardButton(text='Земля', callback_data='zemla')
        keyboard.add(key_zemla)
        key_voda = types.InlineKeyboardButton(text='Вода', callback_data='voda')
        keyboard.add(key_voda)
        key_vozduh = types.InlineKeyboardButton(text='Воздух', callback_data='vozduh')
        keyboard.add(key_vozduh)
        bot.send_message(message.from_user.id, text='Выбери стихию твоего знака зодиака', reply_markup=keyboard)
    elif message.text == "Приложения":
        one_markup = types.InlineKeyboardMarkup(row_width=1)
        keyboard = types.InlineKeyboardMarkup(row_width=1)
        itemboo = types.InlineKeyboardButton("Проверка на совместимость", callback_data='bad2')
        itemboo1 = types.InlineKeyboardButton("Узнать свою удачу на экзамене", callback_data='bad4')

        keyboard.add(itemboo, itemboo1)

        bot.send_message(message.chat.id,
                         "{0.first_name}, окей, смотри, что у нас есть тут:".format(message.from_user),
                         reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: call.data in ['bad2', 'good3', 'bad4'])  # Мероприятия
def callback_one(call):
    if call.message:
        if call.data == 'bad2':  # Совместимость
            photo = open('pp.jpeg', 'rb')
            bot.send_photo(call.message.chat.id, photo)
            bot.send_message(call.message.chat.id, "Но главное это ваши чувства!!")

        elif call.data == 'bad4':  # Проведённые мероприятия
            bot.send_message(call.message.chat.id, "100% Вы все сдадите!")


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "zodiac":
        msg = random.choice(first) + ' ' + random.choice(second) + ' ' + random.choice(second_add) + ' ' + random.choice(third)

        bot.send_message(call.message.chat.id, msg)
    elif call.data == "ogon":
        with open('Ogon.txt', 'r', encoding='utf-8') as f:
            x = f.read()
            bot.send_message(call.message.chat.id, x)
    elif call.data == "zemla":
        with open('zemla.txt', 'r', encoding='utf-8') as f:
            y = f.read()
            bot.send_message(call.message.chat.id, y)
    elif call.data == "vozduh":
        with open('vozduh.txt', 'r', encoding='utf-8') as f:
            a = f.read()
            bot.send_message(call.message.chat.id, a)
    elif call.data == "voda":
        with open('voda.txt', 'r', encoding='utf-8') as f:
            b = f.read()
            bot.send_message(call.message.chat.id, b)




bot.polling(none_stop=True, interval=0)
