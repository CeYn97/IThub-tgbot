from flask import Flask, request
import telebot
from telegram.constants import ParseMode
from telebot import types
import time

secret = 'd484237c-d2d5-408c-813b-cd3abedebadf'
bot = telebot.TeleBot("6757794432:AAGia_ydDYQ1qHzQwzq7AYsRkVJJL82mYKg", threaded=False)

bot.remove_webhook()
time.sleep(1)
bot.set_webhook(url="https://CeYn97.pythonanywhere.com/{}".format(secret))

app = Flask(__name__)

@app.route('/{}'.format(secret), methods=["POST"])
def webhook():
    bot.process_new_updates([telebot.types.Update.de_json(request.stream.read().decode("utf-8"))])
    print("Message")
    return "ok", 200

# @bot.message_handler(commands=['start'])
# def start(message):
#     send_menu(message)
#     keyboard = telebot.types.ReplyKeyboardMarkup(True, True)
#     bot.send_message(message.chat.id, "Выбирите действие:", reply_markup=keyboard)

@bot.message_handler(commands=['start'])
def send_menu(message):
    menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    menu_markup.add(types.KeyboardButton("Часто задаваемые вопросы"))
    menu_markup.add(types.KeyboardButton("Задать вопрос"))
    bot.send_message(message.chat.id, "Я - виртуальный студент колледжа IThub 👋🏼\n \nГотов ответить на твои вопросы 🤗\n \nЧто тебя интересует?", reply_markup=menu_markup)

# def send_menu(message):
#     menu_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
#     menu_markup.add(types.KeyboardButton("Часто задаваемые вопросы"))
#     menu_markup.add(types.KeyboardButton("Задать вопрос"))
#     bot.send_message(message.chat.id, "Я - виртуальный студент колледжа IThub 👋🏼\n \nГотов ответить на твои вопросы 🤗\n \nЧто тебя интересует?", reply_markup=menu_markup)
#

@bot.message_handler(func=lambda message: message.text == "Часто задаваемые вопросы")
def frequently_asked_questions(message):
    faq_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    faq_markup.add(types.KeyboardButton("Все про поступление"))
    faq_markup.add(types.KeyboardButton("Все про документы для поступления"))
    faq_markup.add(types.KeyboardButton("Все про колледж"))
    faq_markup.add(types.KeyboardButton("Контакты"))
    faq_markup.add(types.KeyboardButton("Назад в меню"))
    bot.send_message(message.chat.id, "Выберите интересующий вопрос:", reply_markup=faq_markup)

@bot.message_handler(func=lambda message: message.text == "Все про поступление")
def subtopics_asked_questions(message):
    faq_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    faq_markup.add(types.KeyboardButton("Как поступить?"))
    faq_markup.add(types.KeyboardButton("Сколько стоит обучение?"))
    faq_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "Выберите интересующий вопрос:", reply_markup=faq_markup)

@bot.message_handler(func=lambda message: message.text == "Все про колледж")
def subtopics_asked_questions(message):
    faq_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    faq_markup.add(types.KeyboardButton("Где проходят занятия?"))
    faq_markup.add(types.KeyboardButton("Период обучения"))
    faq_markup.add(types.KeyboardButton("Документ выпускника"))
    faq_markup.add(types.KeyboardButton("Военная служба"))
    faq_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "Выберите интересующий вопрос:", reply_markup=faq_markup)

@bot.message_handler(func=lambda message: message.text == "Все про документы для поступления")
def subtopics_asked_questions(message):
    faq_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    faq_markup.add(types.KeyboardButton("Основные документы"))
    faq_markup.add(types.KeyboardButton("Военная служба"))
    faq_markup.add(types.KeyboardButton("Материнский капитал"))
    faq_markup.add(types.KeyboardButton("Льготники"))
    faq_markup.add(types.KeyboardButton("Иностранцам"))
    faq_markup.add(types.KeyboardButton("Перевод в ITHub"))
    faq_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "Выберите интересующий вопрос:", reply_markup=faq_markup)

@bot.message_handler(func=lambda message: message.text == "Контакты")
def ask_question111(message):
    faq_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    faq_markup.add(types.KeyboardButton("Контакты колледжа"))
    faq_markup.add(types.KeyboardButton("Написать меннеджеру"))
    faq_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "Выберите интересующий вопрос:", reply_markup=faq_markup)

@bot.message_handler(func=lambda message: message.text == "Задать вопрос")
def ask_question(message):
    faq_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    faq_markup.add(types.KeyboardButton("Контакты колледжа"))
    faq_markup.add(types.KeyboardButton("Написать меннеджеру"))
    faq_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "Выберите интересующий вопрос:", reply_markup=faq_markup)



@bot.message_handler(func=lambda message: message.text == "Контакты колледжа")
def ask_question(message):
    bot.send_message(message.chat.id, "Если у вас остались вопросы на которые мы не смогли ответить здесь, то всегда для вас есть контактная информация колледжа:\n \nЭл. почта: info@spb.ithub.ru\n \nТелефон: +7 (812) 210-91-28\n \nОфис: Аптекарский пр-т, д. 2, лит, 3, пом. 10Н, 6 минут пешком от м. Петроградская\n \nhttps://t.me/ceYnnnnn - Наш менеджер Алиса")

@bot.message_handler(func=lambda message: message.text == "Написать меннеджеру")
def ask_question(message):
    bot.send_message(message.chat.id, "ю")


@bot.message_handler(func=lambda message: message.text == "Как поступить?")
def queshion1(message):
    subtopic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    subtopic_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "1) Подать заявку на поступление и необходимые документы для оформления договора на Дне открытых дверей, на сайте в разделе <a href='https://spb.ithub.ru/#rec614944177'>«Приёмная комиссия». </a> Лично в офисе приёмной комиссии\n \n2) С сопровождением менеджеров приёмной комиссии, согласовать договор онлайн и подписать через сервис nopaper.ru или лично при оплате материнским/региональным капиталом\n \n3) Оплатить обучение по реквизитам, указанным в договоре\n \n4) Предоставить документы для зачисления и формирования личного дела по списку",parse_mode=ParseMode.HTML),

@bot.message_handler(func=lambda message: message.text == "Сколько стоит обучение?")
def queshion2(message):
    subtopic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    subtopic_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "Стоимость обучения - 280’000/учебный год\n \n🟣Оплата возможна:\nза весь период,\nза год (280’000),\nза семестр (140’000), \nа так же ежемесячная (29’000).\n \n❗️При оплате всего периода обучения действует скидка.\n❗️<a href='https://drive.google.com/file/d/1-1M1OFn-fKnkPpV9B1Iz9RGqVobYGTT0/view'>Предусмотрена программа лояльности.</a>\n \n🟣Оплатить учебу можно:\n- собственными средствами,\n- материнским (семейным) капиталом,\n- <a href='https://drive.google.com/file/d/1-1M1OFn-fKnkPpV9B1Iz9RGqVobYGTT0/view'>образовательным кредитом с господдержкой</a>", parse_mode=ParseMode.HTML)

@bot.message_handler(func=lambda message: message.text == "Где проходят занятия?")
def queshion3(message):
    subtopic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    subtopic_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "● Обучение проходит офлайн на территории технопарка Ленполиграфмаш.\n● Адрес: Аптекарский пр-т, д. 2, лит, 3, пом. 10Н, 6 минут пешком от м. Петроградская\n \n● Занятия проводятся по расписанию: \n1 пара 10:00 – 11:30, 10 мин. перерыв\n2 пара 11:40 – 13:10\nОБЕД с 13:10 – 14:00\n3 пара 14:00 – 15:30, 10 мин перерыв\n4 пара 15:40 – 17:10, 10 мин перерыв\n5 пара 17:20 – 18:50\n \n● Каникулы: период новогодних и майских праздников, июль и август", reply_markup=subtopic_markup)

@bot.message_handler(func=lambda message: message.text == "Период обучения")
def queshion4(message):
    subtopic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    subtopic_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "● Обучение на базе 9 класса длится 3 года 10 месяцев\n \n● Обучение на базе 11 класса длится 2 года 10 месяцев", parse_mode=ParseMode.HTML)

@bot.message_handler(func=lambda message: message.text == "Документ выпускника")
def queshion5(message):
    subtopic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    subtopic_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "По окончанию обучения выпускник колледжа IThub получает:\n \n🟣Диплом государственного образца о среднем профессиональном образовании по выбранной специальности\n \n🟣Диплом о профессиональной переподготовке по выбранной бизнес-роли", reply_markup=subtopic_markup)

@bot.message_handler(func=lambda message: message.text == "Военная служба")
def queshion6(message):
    subtopic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    subtopic_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "Отсрочка предоставляется в соответствии с Федеральным законом от 28.03.1998 N 53-ФЗ (ред. от 23.03.2024) «О воинской обязанности и военной службе»\n \nЛьготы предоставляются в соответствии <a href='https://drive.google.com/file/d/1-1M1OFn-fKnkPpV9B1Iz9RGqVobYGTT0/view'>«программой лояльности»</a> при предоставлении подтверждающего документа.", parse_mode=ParseMode.HTML)

@bot.message_handler(func=lambda message: message.text == "Военная служба")
def queshion9(message):
    subtopic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    subtopic_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "Отсрочка предоставляется в соответствии с Федеральным законом от 28.03.1998 N 53-ФЗ (ред. от 23.03.2024) «О воинской обязанности и военной службе»\n \nЛьготы предоставляются в соответствии <a href='https://drive.google.com/file/d/1-1M1OFn-fKnkPpV9B1Iz9RGqVobYGTT0/view'>«программой лояльности»</a> при предоставлении подтверждающего документа.", parse_mode=ParseMode.HTML)

@bot.message_handler(func=lambda message: message.text == "Основные документы")
def queshion7(message):
    subtopic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    subtopic_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "● Для оформления договора необходимы:\n \n1) Паспорт родителя и абитуриента\n(или только абитуриента, если ему 18 лет и родитель не планирует делать налоговый вычет до достижения ребенком 23 лет), развороты с фото и с регистрацией\n \n2) Cнилс абитуриента\n \n3) Документ об образовании с приложением — аттестат или диплом\n \n4) В дополнение в зависимости от индивидуальной ситуации:\nиные документы (см. вопросы ниже)\n \n5) Сканы вышеперечисленных документов\n \n------------------------------------------------------\n \n● Для зачисления в колледж и формирования личного дела, после подписания договора и оплаты, потребуются:\n \n1) Оригинал документа об образовании с приложением — аттестат или диплом\nСвидетельство о результатах ЕГЭ или ОГЭ не требуется\n \n2) Фото 3×4, 4 штуки любого цветового решения\n \n3) Военный билет или приписное свидетельство при наличии для юношей\n \n4) В зависимости от индивидуальной ситуации:\n \n● Скан государственного/регионального сертификата на материнский (семейный) капитал\n● Выписка об остатке средств материнского капитала\n● Скан удостоверения многодетной семьи\n● Справка об инвалидности\n● Справка о потере кормильца\n● Академическая справка о периоде обучения (при переводе из другой образовательной организации или филиала IThub)\n● Выписка из приказа об отчислении в связи с переводом (при переводе из другой образовательной организации или филиала IThub)\n● Медицинская справка формы 086/у\n● Иные документы", parse_mode=ParseMode.HTML)

@bot.message_handler(func=lambda message: message.text == "Материнский капитал")
def queshion8(message):
    subtopic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    subtopic_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "Для оформления договора, зачисления в колледж и формирования личного дела, при оплате материнским/семейным капиталом, в дополнение к основным документам потребуются:\n \n◯Cкан государственного/регионального сертификата на материнский (семейный) капитал\n \n◯Cкан выписки об остатке средств материнского/семейного капитала\n \n◯Расписка в получении запроса и иных документов (информации) от заявителя, после посещения МФЦ", parse_mode=ParseMode.HTML)

@bot.message_handler(func=lambda message: message.text == "Льготники")
def queshion9(message):
    subtopic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    subtopic_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "Для оформления договора, зачисления в колледж и формирования личного дела абитуриентов из многодетных семей, лиц с ограниченными возможностями или потерявших кормильца, в дополнение к основным документам потребуются:\n \n◯Cкан удостоверения многодетной семьи\n \n◯Cкан справки об инвалидности\n \n◯Cкан свидетельства о смерти кормильца\n \n◯Cкан свидетельства о рождении/признании отцовства/усыновлении", parse_mode=ParseMode.HTML)

@bot.message_handler(func=lambda message: message.text == "Иностранцам")
def queshion10(message):
    subtopic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    subtopic_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "Гражданам иностранных государств для оформления договора, зачисления в колледж и формирования личного дела потребуются основные документы с учетом особенностей:\n \n◯Все документы должны быть переведены на русский язык и легализованы (иметь апостиль, кроме стран, у которых есть договор о правовой помощи с РФ)\n \n◯Перевод должен быть заверен в установленном порядке\n \n◯При подаче документов необходимо предоставить документ, подтверждающий право законного нахождения абитуриента на территории РФ (регистрация, виза, ВНЖ, РВП или иной документ)", parse_mode=ParseMode.HTML)

@bot.message_handler(func=lambda message: message.text == "Перевод в ITHub")
def queshion10(message):
    subtopic_markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    subtopic_markup.add(types.KeyboardButton("Назад к вопросам"))
    bot.send_message(message.chat.id, "Для оформления договора, зачисления в колледж и формирования личного дела при переводе из другой образовательной организации или колледжа IThub, в дополнение к основным документам потребуются:\n \n◯Cкан и оригинал Академической справки о периоде обучения\n \n◯Выписка из приказа об отчислении в связи с переводом", parse_mode=ParseMode.HTML)


@bot.message_handler(func=lambda message: message.text == "Назад в меню")
def back_to_menu(message):
    send_menu(message)


@bot.message_handler(func=lambda message: message.text == "Назад к вопросам")
def back_to_questions(message):
    frequently_asked_questions(message)

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, "Я не понимаю вашего запроса. Пожалуйста, выберите один из пунктов меню.")

bot.polling()