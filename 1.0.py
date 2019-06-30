import telebot
from telebot import types

bot = telebot.TeleBot("757538090:AAFs2f9c9wyBtoqnm_XAMV8pUyvdhaRwgdM")


@bot.message_handler(commands=['start', 'help'])
def handle_start_help(message):
        user_markup = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup.row('Так \U0001F44D')
        user_markup.row('Ні \U0001F6AB')
        bot.send_message(message.from_user.id, "Доброго дня Ви є працівником охорони здоров'я \U00002753", reply_markup =user_markup)
@bot.message_handler(content_types=['text'])
def start_message(message):
    if message.text == 'Ні \U0001F6AB':
        user_start = telebot.types.ReplyKeyboardMarkup(True, True)
        user_start.row('/start')
        bot.send_message(message.from_user.id, "Вибачте за незручності,\n незаймайтесь самолікування, \n краще зверніться до лікаря.")
        bot.send_sticker(message.from_user.id,'CAADAgADHwoAAm4y2AABT5F3OcPvHcYC') 
        bot.send_message(message.from_user.id, "Щоб почати спочатку натисніть '/start'", reply_markup =user_start)


    elif message.text == 'Так \U0001F44D':
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='Гайдлайн з АГ 2018', url='https://hypertension.at.ua/_ld/0/36__AG_5-61-2018-p.pdf')
        markup.add(btn_my_site)
        user_markup1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_markup1.row('\U00002705 Продовжити')
        bot.send_sticker(message.from_user.id, 'CAADAgADAwADgNKDIhraFYXo9HB7Ag' )
        bot.send_message(message.from_user.id, "\U00002705 Інформація призначена тільки для порад, відповідно рекомендацій " + \
                         "Європейського товариства кардіологів 2018 року з лікування артеріальної гіпертензії.") 
        bot.send_message(message.from_user.id,"\U00002705 Даний телеграм бот " + \
                         "містить лише  основну" + \
                         " інформацію, щодо діагностики" + \
                         ' і лікування артеріальної гіпертензії.', reply_markup =user_markup1)
        bot.send_message(message.from_user.id,"\U00002705 Більш детальну інформацію ви" + \
                         " можете знайти за посиланням:",reply_markup = markup)    
    elif message.text == '\U00002705 Продовжити':
        user_no_hd = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd.row('\U0001F50D Скринінг і діагностика')
        user_no_hd.row('\U0001F6A9 Початок медикаментозного лікування')
        user_no_hd.row('\U0001F4CA Схеми лікування')
        user_no_hd.row('\U0001F3AF Цільові рівні АТ')
        user_no_hd.row('\U00002764 Гіпертензія при спеціальних станах')
        user_no_hd.row('\U0001F34F Модифікація способу життя')
        user_no_hd.row('\U0001F48A Антигіпертензивні препарати')
        bot.send_message(message.from_user.id, "Виберіть відповідний розділ:", reply_markup =user_no_hd)

    elif message.text == '\U0001F4A3 ОГУОМ':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 ОГУОМ – Обумовлені Гіпертензією Ураження Органів Мішеней.\n\nБазові тести для скринінгу ОГУОМ: \n\n\U0000270F ЕКГ у 12 відведеннях:\nСкринінг для виявлення ГЛШ та інших можливих аномалій серця, а також документування пульсу та серцевого ритму \n\n\U0000270F Співвідношення альбуміну та креатиніну в сечі: \n Виявити підвищення екскреції альбуміну, що свідчить про можливе захворювання нирок \n\n\U0000270F Креатинін крові та рШКФ \n Виявити можливе захворювання нирок \n\n\U0000270F Фундоскопія \n Виявити гіпертензивну ретинопатію, особливо у пацієнтів з гіпертензією 2-го або 3-го ступеня \n\n\U0000270F Ехокардіографія \n Оцінити структуру і функцію серця, коли ця інформація може вплинути на прийняття рішення про лікування \n\n\U0000270F УЗД сонної артерії \n Визначити наявність бляшки або стенозу в каротидних артеріях, зокрема в пацієнтів з цереброваскулярним захворюванням або судинними захворюваннями. \n Ультразвукове дослідження органів черевної порожнини та допплерографія \n\U0001F6A9 Оцінити розмір та структуру нирки (наприклад, рубцювання) і виключити обструкцію сечовивідних шляхів як можливі основні причини ХХН та гіпертензії \n\U0001F6A9 Оцінити черевну аорту порожнини для підтвердження аневризматичної дилатації та судинних захворювань \n\U0001F6A9 Перевірити надниркові залози для підтвердження аденоми або феохромоцитоми (для детального дослідження рекомендується КТ або МРТ)  \n Допплерівські дослідження ниркових артерій для скринінгу реноваскулярних захворювань, особливо при наявності асиметричного розміру нирок \n\n\U0000270F КПІ (кісточково-плечовий індекс) \n Обстеження для скринінгу захворювання артерій нижніх кінцівок \n\n\U0000270F Когнітивне функціональне тестування \n Оцінити когнітивну функцію у пацієнтів із симптомами, що свідчать про когнітивні порушення \n\n\U0000270F Візуалізація мозку \n Оцінити наявність ішемічного або геморагічного ушкодження головного мозку, особливо у пацієнтів з анамнезом цереброваскулярних захворювань або зниженням когнітивних функцій", reply_markup =user_no_hd1)

    elif message.text.lower() == 'огуом': 
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 ОГУОМ – Обумовлені Гіпертензією Ураження Органів Мішеней.\n\nБазові тести для скринінгу ОГУОМ: \n\n\U0000270F ЕКГ у 12 відведеннях:\nСкринінг для виявлення ГЛШ та інших можливих аномалій серця, а також документування пульсу та серцевого ритму \n\n\U0000270F Співвідношення альбуміну та креатиніну в сечі: \n Виявити підвищення екскреції альбуміну, що свідчить про можливе захворювання нирок \n\n\U0000270F Креатинін крові та рШКФ \n Виявити можливе захворювання нирок \n\n\U0000270F Фундоскопія \n Виявити гіпертензивну ретинопатію, особливо у пацієнтів з гіпертензією 2-го або 3-го ступеня \n\n\U0000270F Ехокардіографія \n Оцінити структуру і функцію серця, коли ця інформація може вплинути на прийняття рішення про лікування \n\n\U0000270F УЗД сонної артерії \n Визначити наявність бляшки або стенозу в каротидних артеріях, зокрема в пацієнтів з цереброваскулярним захворюванням або судинними захворюваннями. \n Ультразвукове дослідження органів черевної порожнини та допплерографія \n\U0001F6A9 Оцінити розмір та структуру нирки (наприклад, рубцювання) і виключити обструкцію сечовивідних шляхів як можливі основні причини ХХН та гіпертензії \n\U0001F6A9 Оцінити черевну аорту порожнини для підтвердження аневризматичної дилатації та судинних захворювань \n\U0001F6A9 Перевірити надниркові залози для підтвердження аденоми або феохромоцитоми (для детального дослідження рекомендується КТ або МРТ)  \n Допплерівські дослідження ниркових артерій для скринінгу реноваскулярних захворювань, особливо при наявності асиметричного розміру нирок \n\n\U0000270F КПІ (кісточково-плечовий індекс) \n Обстеження для скринінгу захворювання артерій нижніх кінцівок \n\n\U0000270F Когнітивне функціональне тестування \n Оцінити когнітивну функцію у пацієнтів із симптомами, що свідчать про когнітивні порушення \n\n\U0000270F Візуалізація мозку \n Оцінити наявність ішемічного або геморагічного ушкодження головного мозку, особливо у пацієнтів з анамнезом цереброваскулярних захворювань або зниженням когнітивних функцій", reply_markup =user_no_hd1)



        
    elif message.text == '\U0001F55B Амбулаторний моніторинг АТ(АМАТ)':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Переваги')
        user_no_hd1.row('\U0000274E Недоліки')
        user_no_hd1.row('\U0001F4C9 Дипер-статус')
        user_no_hd1.row('\U0001F3E0 Домашній моніторинг АТ(ДМАТ)')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 АМАТ – Амбулаторний моніторинг артеріального тиску – автоматичний моніторинг артеріального тиску протягом 24 годин з інтервалами 15-30 хв.  \n\U00002705Варто пам’ятати, що критерії діагностики артеріальної гіпертензії цим методом  становлять:" + \
                         "\n \U0001F6A9 середньодобовий \U0001F552 130\80 і більше.\n \U0001F6A9 середньоденний \U00002600 135\85 і більше. \n \U0001F6A9 середньонічний \U0001F311 120\ 70 і більше." + \
                         "\nВсі показники еквівалентні при офісному вимірювання (медичним працівником) -140\90. \nСтупінь зниження артеріального тиску вночі формує Дипер-статус .", reply_markup =user_no_hd1)
        
    elif message.text == '\U0001F4C9 Дипер-статус':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F55B Амбулаторний моніторинг АТ(АМАТ)')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\n\U0000270F Дипер-статус може змінюватись щодня. \n \U0000270F Відображає відсоток зниження артеріального тиску у нічний час. \n\U0001F6A9 Dipper (нормальне значення) - 10-20%  \n\U0001F6A9 Non-Dipper (недостатнє зниження) - 0-9% \n\U0001F6A9 Over-Dipper (надмірне зниження) - понад 20-22% \n\U0001F6A9 Night-Peacker (відсутність зниження) - менше 0%", reply_markup =user_no_hd1) 

    elif message.text == '\U00002705 Переваги':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274E Недоліки')
        user_no_hd1.row('\U0001F55B Амбулаторний моніторинг АТ(АМАТ)')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U0001F6A9 Виявлення «гіпертензії білого халату»  і масковану гіпертензію. \n\U0001F6A9 Вимірювання вночі. \n\U0001F6A9 Більш доказове прогностичне значення	в оцінці розвитку ОГУОМ і серцево-судинного ризику. \n\U0001F6A9 Вичерпна інформація з одного сеансу вимірювання.", reply_markup =user_no_hd1)

        
    elif message.text == '\U0000274E Недоліки':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Переваги')
        user_no_hd1.row('\U0001F55B Амбулаторний моніторинг АТ(АМАТ)')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U0001F6A9 Більш дорожчий ніж офісний чи домашній моніторинг АТ. \n\U0001F6A9 Може бути незручним.", reply_markup =user_no_hd1)


    elif message.text == '\U0001F3E0 Домашній моніторинг АТ(ДМАТ)':
         user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
         user_no_hd1.row('\U00002705 Перевaги')
         user_no_hd1.row('\U0000274E Недoліки')
         user_no_hd1.row('\U0001F4C2 Правила виміру АТ')
         user_no_hd1.row('\U0001F55B Амбулаторний моніторинг АТ(АМАТ)')
         user_no_hd1.row('\U00002705 Продовжити')
         bot.send_message(message.from_user.id, "\U00002705  Домашній моніторинг АТ ДМАТ – це середнє значення всіх показників АТ отриманих пацієнтом при самостійному вимірюванні  напівавтоматичним (сертифікованим) тонометром  протягом 6-7 днів (мінімум 3 дні) з дотриманням правил виміру АТ. \n\U00002705  Діагностичний критерій АГ -  135\85 (еквівалент 140\90).", reply_markup =user_no_hd1)

    elif message.text == '\U00002705 Перевaги':
         user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
         user_no_hd1.row('\U0000274E Недoліки')
         user_no_hd1.row('\U0001F3E0 Домашній моніторинг АТ(ДМАТ)')
         user_no_hd1.row('\U00002705 Продовжити')
         bot.send_message(message.from_user.id, "\n\U0001F6A9 Виявлення «гіпертензії білого халату»  і масковану гіпертензію. \n\U0001F6A9 Дешево і широко доступно \n\U0001F6A9 Вимірювання можна проводити вдома \n\U0001F6A9 Залучення пацієнта до вимірювання АТ \n\U0001F6A9 Легко повторюється,  і можна більш тривало застосовувати.", reply_markup =user_no_hd1)

    elif message.text == '\U0000274E Недoліки':
         user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
         user_no_hd1.row('\U00002705 Перевaги')
         user_no_hd1.row('\U0001F3E0 Домашній моніторинг АТ(ДМАТ)')
         user_no_hd1.row('\U00002705 Продовжити')
         bot.send_message(message.from_user.id, "\n\U0001F6A9 Доступний тільки статичний АТ \n\U0001F6A9 Більш вірогідні помилки \n\U0001F6A9 Відсутні нічні виміри АТ ", reply_markup =user_no_hd1)

    elif message.text == '\U0001F4C2 Правила виміру АТ':
         user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
         user_no_hd1.row('\U0001F3E0 Домашній моніторинг АТ(ДМАТ)')
         user_no_hd1.row('\U00002705 Продовжити')
         bot.send_message(message.from_user.id, "\n\U00002705  Не вживати чай, каву, не палити перед виміром АТ. \n\U00002705  Перед вимірюванням потрібно відпочити декілька хвилин \n\U00002705  Потрібно сперитися  на спинку стільця, руку покласти на поверхню, щоб середина манжетки була на рівні серця, ноги мають вільно стояти на підлозі. \n\U00002705  Манжетку можна накладати поверх тонкої сорочки, інший одяг потрібно зняти,  а не закочувати рукав. \n\U00002705  При вимірюванні не рекомендовано говорити, дивитись телевізор, не рекомендовано вимірювати також з переповненим сечовим міхуром.", reply_markup =user_no_hd1)


        


#(Скринінг і діагностика)
    elif message.text == '\U0001F50D Скринінг і діагностика':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U000025B6 Менше 120/80')
        user_no_hd1.row('\U000025B6 120-129/80-84')
        user_no_hd1.row('\U000025B6 130-139/85-89')
        user_no_hd1.row('\U000026D4 Більше 140/90')
        bot.send_photo(chat_id=message.from_user.id, photo=open('16120313.896743.7941.jpg', 'rb'))
        bot.send_message(message.from_user.id, "Який систолічний або діастолічний артеріальний тиск у вашого пацієнта (в мм.рт.ст)?", reply_markup =user_no_hd1)    
    elif message.text == '\U000025B6 Менше 120/80':
        user_no_hd2 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd2.row('\U00002705 Продовжити')
        keyboard = types.InlineKeyboardMarkup()
        keyboard1 = types.InlineKeyboardMarkup()
        callback_button2 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button21 = types.InlineKeyboardButton(text=" С ", callback_data="C")
        keyboard.add(callback_button2)
        keyboard1.add(callback_button21)
        bot.send_message(message.from_user.id, "Чудово \U0001F44D  У пацієнта оптимальний АТ. \n\n \U00002705 Рекомендовано повторювати вимірювання АТ кожні 5 років (починаючи з 18-річного віку). ", reply_markup =user_no_hd2)    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard1)
    elif message.text == '\U000025B6 120-129/80-84':
        user_no_hd2 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd2.row('\U00002705 Продовжити')
        keyboard2 = types.InlineKeyboardMarkup()
        keyboard12 = types.InlineKeyboardMarkup()
        callback_button22 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button212 = types.InlineKeyboardButton(text=" С ", callback_data="C")
        keyboard2.add(callback_button22)
        keyboard12.add(callback_button212)
        bot.send_message(message.from_user.id, "Це нормальний артеріальний тиск. \n\n \U00002705 Рекомендовано повторювати вимірювання АТ кожні 3 роки.", reply_markup =user_no_hd2)    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard2)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard12)
    elif message.text == '\U000025B6 130-139/85-89':
        user_no_hd2 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd2.row('\U0001F55B Амбулаторний моніторинг АТ(АМАТ)')
        user_no_hd2.row('\U0001F3E0 Домашній моніторинг АТ(ДМАТ)')
        user_no_hd2.row('\U0001F3AD Маскована гіпертензія')
        user_no_hd2.row('\U0001F34F Модифікація способу життя')
        user_no_hd2.row('\U00002705 Продовжити')
        keyboard2 = types.InlineKeyboardMarkup()
        keyboard12 = types.InlineKeyboardMarkup()
        callback_button22 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button212 = types.InlineKeyboardButton(text=" С ", callback_data="C")
        keyboard2.add(callback_button22)
        keyboard12.add(callback_button212)
        bot.send_message(message.from_user.id, "У пацієнта високий нормальний  артеріальний тиск. \n \U00002705 Рекомендована модифікація способу життя. \n Потрібно виключити наявність маскованої артеріальної гіпертензії, за допомогою домашнього (ДМАТ), або амбулаторного (добового) моніторингу  (АМАТ) артеріального тиску.", reply_markup =user_no_hd2)
        bot.send_message(message.from_user.id, "Також потрібно розглянути необхідність призначення медикаментозного лікування у пацієнтів з встановленим ДУЖЕ високим серцево-судинним ризиком: \n\U0001F537  Симптомне серцево-судинне захворювання (особливо ІХС)\n \U0001F537  Хронічна хвороба нирок 4 ст. і більше \n \U0001F537  Цукровий діабет з ураженням органів мішеней")
        bot.send_message(message.from_user.id, "\U00002705 При відсутності АГ рекомендовано вимірювання артеріального тиску  щороку.")
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard2)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard12)
    elif message.text == '\U000026D4 Більше 140/90':
        user_no_hd2 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd2.row('\U0001F55B Амбулаторний моніторинг АТ(АМАТ)')
        user_no_hd2.row('\U0001F3E0 Домашній моніторинг АТ(ДМАТ)')
        user_no_hd2.row('\U00002705 Продовжити')
        keyboard2 = types.InlineKeyboardMarkup()
        keyboard12 = types.InlineKeyboardMarkup()
        callback_button22 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button212 = types.InlineKeyboardButton(text=" С ", callback_data="C")
        keyboard2.add(callback_button22)
        keyboard12.add(callback_button212)
        bot.send_message(message.from_user.id, "У випадку першого виявлення даного "  + \
                "рівня артеріального тиску, для підтвердження, або спростування діагнозу гіпертонічної хвороби: \n \U00002705 Рекомендовано повторний візит для " + \
                "офісного вимірювання АТ.", reply_markup =user_no_hd2)    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard2)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard12)
        bot.send_message(message.from_user.id, "\U00002705 Або використання домашнього(ДМАТ),\n чи амбулаторного (добового) (АМАТ) моніторингу АТ.")
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard2)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard12)
        bot.send_message(message.from_user.id, "\U00002705 Гіпертензія 3 ст (САТ більше 180, або ДАТ більше 110)" + \
                "\n не потребує повторних візитів для підтвердження діагнозу.", reply_markup =user_no_hd2) 
#Початок медикаментозного лікування
    elif message.text == '\U0001F6A9 Початок медикаментозного лікування':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U000025B6 130-139/85-89 \U000025C0')
        user_no_hd1.row('\U000025B6 140-159/90-99 \U000025C0')
        user_no_hd1.row('\U000025B6 160-179/100-109 \U000025C0')
        user_no_hd1.row('\U000025B6 Більше 180/110 \U000025C0')
        bot.send_message(message.from_user.id, "Який систолічний і діастолічний артеріальний тиск у вашого пацієнта (в мм.рт.ст)?", reply_markup =user_no_hd1)    

    elif message.text == '\U00002B06  Назад':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U000025B6 130-139/85-89 \U000025C0')
        user_no_hd1.row('\U000025B6 140-159/90-99 \U000025C0')
        user_no_hd1.row('\U000025B6 160-179/100-109 \U000025C0')
        user_no_hd1.row('\U000025B6 Більше 180/110 \U000025C0')
        bot.send_message(message.from_user.id, "Який систолічний і діастолічний артеріальний тиск у вашого пацієнта (в мм.рт.ст)?", reply_markup =user_no_hd1)    



    elif message.text == '\U000025B6 130-139/85-89 \U000025C0':
        user_no_hd23 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd23.row('\U00002705 Продовжити')
        user_no_hd23.row('\U00002B06  Назад')
        bot.send_message(message.from_user.id, "Рекомендоване медикаментозне лікування лише" + \
        "у пацієнтів з встановленим ДУЖЕ високим" + \
        " серцево-судинним ризиком: " + \
        "\n \U0001F538 Симптомне серце-судинне захворювання" + \
        "(особливо ІХС) \n \U0001F538 Хронічна хвороба нирок 4 ст і більше " + \
        "\n \U0001F538 Цукровий діабет з ураженням органів мішеней", reply_markup =user_no_hd23)   
    elif message.text == '\U000025B6 140-159/90-99 \U000025C0':
        user_no_hd6_1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd6_1.row('\U000025B6 до 65 років')
        user_no_hd6_1.row('\U000025B6 65-80 років')
        user_no_hd6_1.row('\U000025B6 більше 80 років')
        user_no_hd6_1.row('\U00002B06  Назад')
        bot.send_message(message.from_user.id, "Який вік пацієнта?", reply_markup =user_no_hd6_1)

    elif message.text == '\U00002B06 Назад':
        user_no_hd6_1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd6_1.row('\U000025B6 до 65 років')
        user_no_hd6_1.row('\U000025B6 65-80 років')
        user_no_hd6_1.row('\U000025B6 більше 80 років')
        user_no_hd6_1.row('\U00002B06  Назад')
        bot.send_message(message.from_user.id, "Який вік пацієнта?", reply_markup =user_no_hd6_1)
        
    elif message.text == '\U000025B6 до 65 років':
        user_no_hd6_1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd6_1.row('\U00002705 Продовжити')
        user_no_hd6_1.row('\U00002B06 Назад')
        bot.send_message(message.from_user.id, "\U00002705 Рекомендована модифікація способу життя." + \
                "\n\n При низькому чи помірному" + \
                "ризику серцево-судинних захворювань" + \
                "(без ХХН, або уражень органів мішеней" + \
                "\nобумовлених гіпертензією)" + \
                "\nмодифікація способу життя протягом" + \
                "3-6 місяців\U0001F31B, а при неефективності:" + \
                "- медикаментозне лікування \U0001F48A.", reply_markup =user_no_hd6_1)               
        bot.send_message(message.from_user.id, "\U00002705 Якщо ризик ССЗ високий, " + \
                "або наявна хвороба нирок, або ураження " + \
                "органів мішеней обумовлених гіпертензією" + \
                "негайне призначення медикаментозного лікування \U0000203C", reply_markup =user_no_hd6_1)
    elif message.text == '\U000025B6 65-80 років':
        user_no_hd6_3 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd6_3.row('\U00002705 Продовжити')
        user_no_hd6_3.row('\U00002B06 Назад')
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        bot.send_message(message.from_user.id, "\U00002705 Рекомендована модифікація способу життя.", reply_markup =user_no_hd6_3)   
        bot.send_message(message.from_user.id, "\U00002705 Призначення медикаментозного лікування рекомендовано за умови, що лікування  добре переноситься", reply_markup =user_no_hd6_3)    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)  
    elif message.text == '\U000025B6 більше 80 років':
        user_no_hd6_3 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd6_3.row('\U00002705 Продовжити')
        user_no_hd6_3.row('\U00002B06 Назад')
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  ІІІ  ", callback_data="ІІІ")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        keyboard4 = types.InlineKeyboardMarkup()
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button4 = types.InlineKeyboardButton(text="  ІІв  ", callback_data="ІІв")
        callback_button41 = types.InlineKeyboardButton(text=" В ", callback_data="В")
        keyboard14.add(callback_button4)
        keyboard4.add(callback_button41)
        bot.send_message(message.from_user.id, "\U0001F4DA Достатня доказова база безпечності початку медикаментозного лікування осіб старше 80 р.з АГ 1 ст. на сьогодні недостатня.", reply_markup =user_no_hd6_3)   
        bot.send_message(message.from_user.id, "\U00002705 Проте НЕ рекомендовано відміняти терапію при досягненні 80 віку, за умови що лікування добре переноситься.", reply_markup =user_no_hd6_3)    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)  
        bot.send_message(message.from_user.id, "\U00002705 Медикаментозне лікування може призначатись і в осіб з старечею астенією, при добрій переносимості.", reply_markup =user_no_hd6_3)    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard14)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard4)  
    elif message.text == '\U000025B6 160-179/100-109 \U000025C0':
        user_no_hd6_1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd6_1.row('\U00002705 Продовжити')
        user_no_hd6_1.row('\U00002B06  Назад')
        bot.send_message(message.from_user.id, "\U00002705 Рекомендована модифікація способу життя." + \
                "\n\n \U00002705 Негайне призначення медикаментозного лікування незалежно від серцево-судинного ризику.", reply_markup =user_no_hd6_1)       
    elif message.text == '\U000025B6 Більше 180/110 \U000025C0':
        user_no_hd6_1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd6_1.row('\U00002705 Продовжити')
        user_no_hd6_1.row('\U00002B06  Назад')
        bot.send_message(message.from_user.id, "\U00002705 Рекомендована модифікація способу життя." + \
                "\n\n \U00002705 Негайне призначення медикаментозного лікування незалежно від серцево-судинного ризику.", reply_markup =user_no_hd6_1)       
#(Схеми лікування)              
    elif message.text == '\U0001F4CA Схеми лікування':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00000031\U000020E3 Основна схема лікування')
        user_no_hd1.row('\U00000032\U000020E3 ГХ+ІХС')
        user_no_hd1.row('\U00000033\U000020E3 ГХ + ХХН')
        user_no_hd1.row('\U00000034\U000020E3 ГХ + СН зі зниженою ФВ')
        user_no_hd1.row('\U00000035\U000020E3 ГХ + ФП')
        bot.send_message(message.from_user.id, "Виберіть потрібну схему лікування:", reply_markup =user_no_hd1)

    elif message.text == '\U00000031\U000020E3 Основна схема лікування':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Крок 1')
        user_no_hd1.row('\U00002705 Крок 2')
        user_no_hd1.row('\U00002705 Крок 3')
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити') 
        keyboard4 = types.InlineKeyboardMarkup()
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button4 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button41 = types.InlineKeyboardButton(text=" В ", callback_data="В")
        keyboard14.add(callback_button4)
        keyboard4.add(callback_button41)
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  ІІІ  ", callback_data="ІІІ")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        bot.send_message(message.from_user.id, "\U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B   \n Схема доцільна для пацієнтів з неускладненою гіпертензією, з ураженням органів мішеней при церебровастулярній патології цукровому дібеті і захворюванні периферійних артерій.", reply_markup =user_no_hd1)  
        bot.send_message(message.from_user.id, "\U00002705 Рекомендовано починати терапію комбінацією двох препаратів в одній таблетці. (за винятком пацієнтів похилого віку з старечою астенією і пацієнтів з АГ 1 ст. і при низькому  ризику ССЗ).")    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard14)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard4)   
        bot.send_message(message.from_user.id, "КРОК 1. \nПодвійна комбінація в 1 таблетці \U0001F48A:" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n             \U00002795 \n" + \
                "БКК або діуретик ", reply_markup =user_no_hd1) 
        bot.send_message(message.from_user.id, "КРОК 2. \nПотрійна комбінація в 1 таблетці \U0001F48A:" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n          \U00002795          " + \
                "\n         БКК" + \
                "\n          \U00002795          " + \
                "\n      Діуретик ", reply_markup =user_no_hd1)    
        bot.send_message(message.from_user.id, "КРОК 3. \nВ двох таблетках \U0001F48A\U0001F48A :" + \
                "\n\nПотрійна комбінація" + \
                "\n                \U00002795          \n" + \
                "Спіронолактон (25-50мг)," + \
                "\nабо інший діуретик, або альфа чи бета блокатор.  ", reply_markup =user_no_hd1)   
        bot.send_message(message.from_user.id, "\U0000270F Примітка:\nіАПФ- інгібітори ангіотензинперетворюючого ферменту." + \
                "\nАРАІІ- антагоністи рецепторів альдостерону ІІ" + \
                "\nБКК- блокатори кальцієвих каналів" + \
                "\nДіуретик- тіазидний, або тіазидоподібний" + \
                "\n\n \U0000270F Бета-блокатори  можна додавати при наявності " + \
                "\nспеціальних показань:" + \
                "\nІХС, ХСН, ФП, після ІМ, або молодим жінкам \nз плануванням вагітності.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Комбінувати іАПФ з АРА ІІ  \nНЕ рекомендується", reply_markup =user_no_hd1)    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)

    elif message.text == '\U000021AA  Назад':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Крок 1')
        user_no_hd1.row('\U00002705 Крок 2')
        user_no_hd1.row('\U00002705 Крок 3')
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити') 
        keyboard4 = types.InlineKeyboardMarkup()
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button4 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button41 = types.InlineKeyboardButton(text=" В ", callback_data="В")
        keyboard14.add(callback_button4)
        keyboard4.add(callback_button41)
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  ІІІ  ", callback_data="ІІІ")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        bot.send_message(message.from_user.id, "\U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B   \n Схема доцільна для пацієнтів з неускладненою гіпертензією, з ураженням органів мішеней при церебровастулярній патології цукровому дібеті і захворюванні периферійних артерій.", reply_markup =user_no_hd1)  
        bot.send_message(message.from_user.id, "\U00002705 Рекомендовано починати терапію комбінацією двох препаратів в одній таблетці. (за винятком пацієнтів похилого віку з старечою астенією і пацієнтів з АГ 1 ст. і при низькому  ризику ССЗ).")    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard14)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard4)   
        bot.send_message(message.from_user.id, "КРОК 1. \nПодвійна комбінація в 1 таблетці \U0001F48A:" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n             \U00002795 \n" + \
                "БКК або діуретик ", reply_markup =user_no_hd1) 
        bot.send_message(message.from_user.id, "КРОК 2. \nПотрійна комбінація в 1 таблетці \U0001F48A:" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n          \U00002795          " + \
                "\n         БКК" + \
                "\n          \U00002795          " + \
                "\n      Діуретик ", reply_markup =user_no_hd1)    
        bot.send_message(message.from_user.id, "КРОК 3. \nВ двох таблетках \U0001F48A\U0001F48A :" + \
                "\n\nПотрійна комбінація" + \
                "\n                \U00002795          \n" + \
                "Спіронолактон (25-50мг)," + \
                "\nабо інший діуретик, або альфа чи бета блокатор.  ", reply_markup =user_no_hd1)   
        bot.send_message(message.from_user.id, "\U0000270F Примітка:\nіАПФ- інгібітори ангіотензинперетворюючого ферменту." + \
                "\nАРАІІ- антагоністи рецепторів альдостерону ІІ" + \
                "\nБКК- блокатори кальцієвих каналів" + \
                "\nДіуретик- тіазидний, або тіазидоподібний" + \
                "\n\n \U0000270F Бета-блокатори  можна додавати при наявності " + \
                "\nспеціальних показань:" + \
                "\nІХС, ХСН, ФП, після ІМ, або молодим жінкам \nз плануванням вагітності.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Комбінувати іАПФ з АРА ІІ  \nНЕ рекомендується", reply_markup =user_no_hd1)    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)

    elif message.text == '\U00002705 Крок 1':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F499 І-АПФ + БКК')
        user_no_hd1.row('\U0001F499 І-АПФ + Діуретики')
        user_no_hd1.row('\U0001F49B АРА ІІ + БКК')
        user_no_hd1.row('\U0001F49B АРА ІІ + Діуретики')
        user_no_hd1.row('\U000021AA  Назад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U000021AA Назад':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F499 І-АПФ + БКК')
        user_no_hd1.row('\U0001F499 І-АПФ + Діуретики')
        user_no_hd1.row('\U0001F49B АРА ІІ + БКК')
        user_no_hd1.row('\U0001F49B АРА ІІ + Діуретики')
        user_no_hd1.row('\U000021AA  Назад') 
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F499 І-АПФ + БКК':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Периндоприл + Амлодипін')
        user_no_hd1.row('Раміприл + Амлодипін')
        user_no_hd1.row('Лізиноприл + Амлодипін')
        user_no_hd1.row('Еналаприл + Лерканідипін')
        user_no_hd1.row('Еналаприл + Нітредипін')
        user_no_hd1.row('Трандолаприл + Верапаміл')
        user_no_hd1.row('\U000021AA Назад') 
        bot.send_message(message.from_user.id, "Виберіть діючі речовини:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F499 І-АПФ + Діуретики':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Раміприл + Гідрохлортіазид')
        user_no_hd1.row('Лізиноприл + Гідрохлортіазид')
        user_no_hd1.row('Каптоприл + Гідрохлортіазид')
        user_no_hd1.row('Еналаприл + Гідрохлортіазид')
        user_no_hd1.row('Квіналаприл + Гідрохлортіазид')
        user_no_hd1.row('Фозинаприл + Гідрохлортіазид')
        user_no_hd1.row('Зофенаприл + Гідрохлортіазид')
        user_no_hd1.row('Периндоприл + Індапамід')
        user_no_hd1.row('Еналаприл + Індапамід')
        user_no_hd1.row('\U000021AA Назад')  
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F49B АРА ІІ + БКК':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Валсартан + Амлодипін')
        user_no_hd1.row('Лозартан + Амлодипін')
        user_no_hd1.row('Ірбесартан + Амлодипін')
        user_no_hd1.row('Кандесартан + Амлодипін')
        user_no_hd1.row('Телмісартан + Амлодипін')
        user_no_hd1.row('Олмесартан + Амлодипін')
        user_no_hd1.row('\U000021AA Назад')  
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)
        
    elif message.text == '\U0001F49B АРА ІІ + Діуретики':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Лозартан + Гідрохлортіазид')
        user_no_hd1.row('Валсартан + Гідрохлортіазид')
        user_no_hd1.row('Ірбесартан + Гідрохлортіазид')
        user_no_hd1.row('Кандесартан + Гідрохлортіазид')
        user_no_hd1.row('Телмісартан + Гідрохлортіазид')
        user_no_hd1.row('Олмесартан + Гідрохлортіазид')
        user_no_hd1.row('\U000021AA Назад')  
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U00002705 Крок 2':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F499 І-АПФ + БКК + Діуретик')
        user_no_hd1.row('\U0001F49B АРА ІІ + БКК + Діуретик')
        user_no_hd1.row('\U000021AA  Назад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U000021AA Нaзад':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F499 І-АПФ + БКК + Діуретик')
        user_no_hd1.row('\U0001F49B АРА ІІ + БКК + Діуретик')
        user_no_hd1.row('\U000021AA  Назад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)
        
    elif message.text == '\U0001F499 І-АПФ + БКК + Діуретик':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Периндоприл + Індапамід + Амлодипін')
        user_no_hd1.row('\U000021AA Нaзад') 
        bot.send_message(message.from_user.id, "Виберіть діючі речовини:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F49B АРА ІІ + БКК + Діуретик':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Валсартан + Гідрохлортіазид + Амлодипін')
        user_no_hd1.row('\U000021AA Нaзад') 
        bot.send_message(message.from_user.id, "Виберіть діючі речовини:", reply_markup =user_no_hd1)


    elif message.text == '\U00002705 Крок 3':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U000021AA  Назад')
        bot.send_message(message.from_user.id, "КРОК 3. \nВ двох таблетках \U0001F48A\U0001F48A :" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n          \U00002795            " + \
                "\n         БКК " + \
                "\n          \U00002795            " + \
                "\n    Діуретик " + \
                "\n          \U00002795            \n" + \
                "Спіронолактон (25-50мг)," + \
                "\nабо інший діуретик, або альфа чи бета блокатор.  ", reply_markup =user_no_hd1)   

    elif message.text == '\U00000032\U000020E3 ГХ+ІХС':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Крoк 1')
        user_no_hd1.row('\U00002705 Крoк 2')
        user_no_hd1.row('\U00002705 Крoк 3') 
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити') 
        keyboard4 = types.InlineKeyboardMarkup()
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button4 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button41 = types.InlineKeyboardButton(text=" В ", callback_data="В")
        keyboard14.add(callback_button4)
        keyboard4.add(callback_button41)
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  ІІІ  ", callback_data="ІІІ")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        bot.send_message(message.from_user.id, "\U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \n Схема доцільна для пацієнтів з гіпертонічною хворобою в поєднанні  з ішемічною хворобою серця.", reply_markup =user_no_hd1)  
        bot.send_message(message.from_user.id, "\U00002705 Рекомендовано починати терапію комбінацією двох препаратів в одній таблетці (за винятком пацієнтів похилого віку з старечою астенією і пацієнтів з АГ 1 ст. і при низькому  ризику ССЗ).")    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard14)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard4)   
        bot.send_message(message.from_user.id, "КРОК 1. \nПодвійна комбінація в 1 таблетці \U0001F48A:\n\n \U0001F449Варіант №1:" + \
                "\n   іАПФ або АРА ІІ" + \
                "\n               \U00002795   " + \
                "\n     ББ або БКК" + \
                "\n\n \U0001F449Варіант 2:" + \
                "\n            БКК" + \
                "\n             \U00002795   " + \
                "\n діуретик або ББ"
                "\n\n \U0001F449Варіант 3:" + \
                "\n              ББ" + \
                "\n             \U00002795   " + \
                "\n       діуретик", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КРОК 2. \nПотрійна комбінація в 1 таблетці \U0001F48A \n(комбінація вищеперерахованих засобів):" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n          \U00002795            " + \
                "\n  ББ або БКК " + \
                "\n          \U00002795            \n" + \
                "   Діуретик ", reply_markup =user_no_hd1)    
        bot.send_message(message.from_user.id, "КРОК 3. \nВ двох таблетках \U0001F48A\U0001F48A:" + \
                "\n\nПотрійна комбінація" + \
                "\n          \U00002795            \n" + \
                "Спіронолактон (25-50мг)," + \
                "\nабо інший діуретик, або альфа чи бета блокатор.  ", reply_markup =user_no_hd1)   
        bot.send_message(message.from_user.id, "\U0000270F Примітка:\nіАПФ- інгібітори ангіотензинперетворюючого ферменту." + \
                "\nАРАІІ- антагоністи рецепторів альдостерону ІІ" + \
                "\nБКК- блокатори кальцієвих каналів" + \
                "\nДіуретик- тіазидний, або тіазидоподібний" + \
                "\nББ-бета-блокатор ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Комбінувати іАПФ з АРА ІІ  \nНЕ рекомендується", reply_markup =user_no_hd1)    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)

    elif message.text == '\U000021AA  Нaзaд':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Крoк 1')
        user_no_hd1.row('\U00002705 Крoк 2')
        user_no_hd1.row('\U00002705 Крoк 3')
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити') 
        keyboard4 = types.InlineKeyboardMarkup()
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button4 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button41 = types.InlineKeyboardButton(text=" В ", callback_data="В")
        keyboard14.add(callback_button4)
        keyboard4.add(callback_button41)
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  ІІІ  ", callback_data="ІІІ")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        bot.send_message(message.from_user.id, "\U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \n Схема доцільна для пацієнтів з гіпертонічною хворобою в поєднанні  з ішемічною хворобою серця.", reply_markup =user_no_hd1)  
        bot.send_message(message.from_user.id, "\U00002705 Рекомендовано починати терапію комбінацією двох препаратів в одній таблетці (за винятком пацієнтів похилого віку з старечою астенією і пацієнтів з АГ 1 ст. і при низькому  ризику ССЗ).")    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard14)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard4)   
        bot.send_message(message.from_user.id, "КРОК 1. \nПодвійна комбінація в 1 таблетці \U0001F48A:\n\n \U0001F449Варіант №1:" + \
                "\n   іАПФ або АРА ІІ" + \
                "\n               \U00002795   " + \
                "\n     ББ або БКК" + \
                "\n\n \U0001F449Варіант 2:" + \
                "\n            БКК" + \
                "\n             \U00002795   " + \
                "\n діуретик або ББ"
                "\n\n \U0001F449Варіант 3:" + \
                "\n              ББ" + \
                "\n             \U00002795   " + \
                "\n       діуретик", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КРОК 2. \nПотрійна комбінація в 1 таблетці \U0001F48A \n(комбінація вищеперерахованих засобів):" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n          \U00002795            " + \
                "\n  ББ або БКК " + \
                "\n          \U00002795            \n" + \
                "   Діуретик ", reply_markup =user_no_hd1)    
        bot.send_message(message.from_user.id, "КРОК 3. \nВ двох таблетках \U0001F48A\U0001F48A:" + \
                "\n\nПотрійна комбінація" + \
                "\n          \U00002795            \n" + \
                "Спіронолактон (25-50мг)," + \
                "\nабо інший діуретик, або альфа чи бета блокатор.  ", reply_markup =user_no_hd1)   
        bot.send_message(message.from_user.id, "\U0000270F Примітка:\nіАПФ- інгібітори ангіотензинперетворюючого ферменту." + \
                "\nАРАІІ- антагоністи рецепторів альдостерону ІІ" + \
                "\nБКК- блокатори кальцієвих каналів" + \
                "\nДіуретик- тіазидний, або тіазидоподібний" + \
                "\nББ-бета-блокатор ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Комбінувати іАПФ з АРА ІІ  \nНЕ рекомендується", reply_markup =user_no_hd1)    
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)

    elif message.text == '\U00002705 Крoк 1':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F499 іАПФ + БКК')
        user_no_hd1.row('\U0001F499 іАПФ + ББ')
        user_no_hd1.row('\U0001F49B AРА ІІ + БКК')
        user_no_hd1.row('\U0001F49B AРА ІІ + ББ')
        user_no_hd1.row('\U0001F499 БКК + діуретик')
        user_no_hd1.row('\U0001F499 БКК + ББ')
        user_no_hd1.row('\U0001F49B ББ + діуретик')
        user_no_hd1.row('\U000021AA  Нaзaд')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U000021AA  Нaзад':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F499 іАПФ + БКК')
        user_no_hd1.row('\U0001F499 іАПФ + ББ')
        user_no_hd1.row('\U0001F49B AРА ІІ + БКК')
        user_no_hd1.row('\U0001F49B AРА ІІ + ББ')
        user_no_hd1.row('\U0001F499 БКК + діуретик')
        user_no_hd1.row('\U0001F499 БКК + ББ')
        user_no_hd1.row('\U0001F49B ББ + діуретик')
        user_no_hd1.row('\U000021AA  Нaзaд')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)
        
    elif message.text == '\U0001F499 іАПФ + БКК':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Периндоприл + Амлодипін')
        user_no_hd1.row('Раміприл + Амлодипін')
        user_no_hd1.row('Лізиноприл + Амлодипін')
        user_no_hd1.row('Еналаприл + Лерканідипін')
        user_no_hd1.row('Еналаприл + Нітредипін')
        user_no_hd1.row('Трандолаприл + Верапаміл')
        user_no_hd1.row('\U000021AA  Нaзад') 
        bot.send_message(message.from_user.id, "Виберіть діючі речовини:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F499 іАПФ + ББ':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Периндоприл + Бісопролол')
        user_no_hd1.row('\U000021AA  Нaзад') 
        bot.send_message(message.from_user.id, "Виберіть діючі речовини:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F49B AРА ІІ + БКК':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Валсартан + Амлодипін')
        user_no_hd1.row('Лозартан + Амлодипін')
        user_no_hd1.row('Ірбесартан + Амлодипін')
        user_no_hd1.row('Кандесартан + Амлодипін')
        user_no_hd1.row('Телмісартан + Амлодипін')
        user_no_hd1.row('Олмесартан + Амлодипін')
        user_no_hd1.row('\U000021AA  Нaзад')  
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F49B AРА ІІ + ББ':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U000021AA  Нaзад')
        bot.send_sticker(message.from_user.id,'CAADAgADHwoAAm4y2AABT5F3OcPvHcYC') 
        bot.send_message(message.from_user.id, "Данна комбінація в одній таблетці відсутня", reply_markup =user_no_hd1)

    elif message.text == '\U0001F499 БКК + діуретик':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Амлодипін + Індапамід')
        user_no_hd1.row('\U000021AA  Нaзад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F499 БКК + ББ':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Бісопролол + Амлодипін')
        user_no_hd1.row('Атенолол + Амлодипін')
        user_no_hd1.row('\U000021AA  Нaзад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F49B ББ + діуретик':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Бісопролол + Гідрохлортіазид')
        user_no_hd1.row('Небівалол + Гідрохлортіазид')
        user_no_hd1.row('Атенолол + Хлорталідон')
        user_no_hd1.row('\U000021AA  Нaзад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U00002705 Крoк 2':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F499  I-AПФ + БКК + Діуретик')
        user_no_hd1.row('\U0001F49B  АРA ІІ + БКК + Діуретик')
        user_no_hd1.row('\U000021AA  Нaзaд')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U000021AA   Назaд':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F499  I-AПФ + БКК + Діуретик')
        user_no_hd1.row('\U0001F49B  АРA ІІ + БКК + Діуретик')
        user_no_hd1.row('\U000021AA  Нaзaд')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)
        
    elif message.text == '\U0001F499  I-AПФ + БКК + Діуретик':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Периндоприл + Індапамід + Амлодипін')
        user_no_hd1.row('\U000021AA   Назaд') 
        bot.send_message(message.from_user.id, "Виберіть діючі речовини:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F49B  АРA ІІ + БКК + Діуретик':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Валсартан + Гідрохлортіазид + Амлодипін')
        user_no_hd1.row('\U000021AA   Назaд') 
        bot.send_message(message.from_user.id, "Виберіть діючі речовини:", reply_markup =user_no_hd1)

    elif message.text == '\U00002705 Крoк 3':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U000021AA  Нaзaд')
        bot.send_message(message.from_user.id, "КРОК 3. \nВ двох таблетках \U0001F48A\U0001F48A:" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n          \U00002795            " + \
                "\n         БКК " + \
                "\n          \U00002795            " + \
                "\n    Діуретик " + \
                "\n          \U00002795            \n" + \
                "Спіронолактон (25-50мг)," + \
                "\nабо інший діуретик, або альфа чи бета блокатор.  ", reply_markup =user_no_hd1)   

    elif message.text == '\U00000033\U000020E3 ГХ + ХХН':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Крoк 1')
        user_no_hd1.row('\U00002705  Крoк 2')
        user_no_hd1.row('\U00002705  Крoк 3')
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити')
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  ІІІ  ", callback_data="ІІІ")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        bot.send_message(message.from_user.id, "\U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \n Схема доцільна для пацієнтів з гіпертонічною хворобою в поєднанні  з хронічною хворобою нирок зі зниженням рівня швидкості клубочком фільтрації менше 60 мл/хв.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КРОК 1. \nПодвійна комбінація в 1 таблетці \U0001F48A:\n \U0001F449Варіант №1:" + \
                "\nіАПФ або АРА ІІ" + \
                "\n             \U00002795   " + \
                "\n           БКК" + \
                "\n\n\U0001F449Варіант 2:" + \
                "\nіАПФ або АРА ІІ" + \
                "\n             \U00002795   " + \
                "\n       діуретик", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КРОК 2. \nПотрійна комбінація в 1 таблетці \U0001F48A\n(комбінація вищеперерахованих засобів):" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n          \U00002795            " + \
                "\n         БКК " + \
                "\n          \U00002795            \n" + \
                "   Діуретик ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КРОК 3. \nВ двох таблетках \U0001F48A\U0001F48A:" + \
                "\n\nПотрійна комбінація" + \
                "\n          \U00002795            \n" + \
                "Спіронолактон (25-50мг)," + \
                "\nабо інший діуретик, або альфа чи бета блокатор.  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U0000270F Примітка:\nіАПФ- інгібітори ангіотензинперетворюючого ферменту." + \
                "\nАРАІІ- антагоністи рецепторів альдостерону ІІ" + \
                "\nБКК- блокатори кальцієвих каналів" + \
                "\nББ-бета-блокатор" + \
                "\nДіуретик – тіазидний, або тіазидоподібний." + \
                "\nЯкщо рШКФ менше 30 мл/хв" + \
                "\nкраще використовувати" + \
                "\n петльовий діуретик." + \
                "\n\n\U0000270F Можливий ризик гіперкаліємії" + \
                "\nпри використанні спіронолактону у пацієнтів " + \
                "\nз рШКФ менше 45 мл/хв., або рівнем калію" + \
                "\nбільше 4,5 ммоль\л.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Комбінувати іАПФ з АРА ІІ  НЕ рекомендується", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)     

    elif message.text == '\U00002B05 Назад':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Крoк 1')
        user_no_hd1.row('\U00002705  Крoк 2')
        user_no_hd1.row('\U00002705  Крoк 3')
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити')
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  ІІІ  ", callback_data="ІІІ")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        bot.send_message(message.from_user.id, "\U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \n Схема доцільна для пацієнтів з гіпертонічною хворобою в поєднанні  з хронічною хворобою нирок зі зниженням рівня швидкості клубочком фільтрації менше 60 мл/хв.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КРОК 1. \nПодвійна комбінація в 1 таблетці \U0001F48A:\n \U0001F449Варіант №1:" + \
                "\nіАПФ або АРА ІІ" + \
                "\n             \U00002795   " + \
                "\n           БКК" + \
                "\n\n\U0001F449Варіант 2:" + \
                "\nіАПФ або АРА ІІ" + \
                "\n             \U00002795   " + \
                "\n       діуретик", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КРОК 2. \nПотрійна комбінація в 1 таблетці \U0001F48A\n(комбінація вищеперерахованих засобів):" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n          \U00002795            " + \
                "\n         БКК " + \
                "\n          \U00002795            \n" + \
                "   Діуретик ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КРОК 3. \nВ двох таблетках \U0001F48A\U0001F48A:" + \
                "\n\nПотрійна комбінація" + \
                "\n          \U00002795            \n" + \
                "Спіронолактон (25-50мг)," + \
                "\nабо інший діуретик, або альфа чи бета блокатор.  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U0000270F Примітка:\nіАПФ- інгібітори ангіотензинперетворюючого ферменту." + \
                "\nАРАІІ- антагоністи рецепторів альдостерону ІІ" + \
                "\nБКК- блокатори кальцієвих каналів" + \
                "\nББ-бета-блокатор" + \
                "\nДіуретик – тіазидний, або тіазидоподібний." + \
                "\nЯкщо рШКФ менше 30 мл/хв" + \
                "\nкраще використовувати" + \
                "\n петльовий діуретик." + \
                "\n\n\U0000270F Можливий ризик гіперкаліємії" + \
                "\nпри використанні спіронолактону у пацієнтів " + \
                "\nз рШКФ менше 45 мл/хв., або рівнем калію" + \
                "\nбільше 4,5 ммоль\л.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Комбінувати іАПФ з АРА ІІ  НЕ рекомендується", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)    

    elif message.text == '\U00002705  Крoк 1':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F538  I-AПФ + БКК')
        user_no_hd1.row('\U0001F538  I-AПФ + Діуретик')
        user_no_hd1.row('\U0001F539  АРA ІІ + БКК')
        user_no_hd1.row('\U0001F539  АРA ІІ + Діуретик')
        user_no_hd1.row('\U00002B05 Назад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U00002B05  Назад':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F538  I-AПФ + БКК')
        user_no_hd1.row('\U0001F538  I-AПФ + Діуретик')
        user_no_hd1.row('\U0001F539  АРA ІІ + БКК')
        user_no_hd1.row('\U0001F539  АРA ІІ + Діуретик')
        user_no_hd1.row('\U00002B05 Назад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F538  I-AПФ + БКК':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Периндоприл + Амлодипін')
        user_no_hd1.row('Раміприл + Амлодипін')
        user_no_hd1.row('Лізиноприл + Амлодипін')
        user_no_hd1.row('Еналаприл + Лерканідипін')
        user_no_hd1.row('Еналаприл + Нітредипін')
        user_no_hd1.row('Трандолаприл + Верапаміл')
        user_no_hd1.row('\U00002B05  Назад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F538  I-AПФ + Діуретик':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Раміприл + Гідрохлортіазид')
        user_no_hd1.row('Лізиноприл + Гідрохлортіазид')
        user_no_hd1.row('Каптоприл + Гідрохлортіазид')
        user_no_hd1.row('Еналаприл + Гідрохлортіазид')
        user_no_hd1.row('Квіналаприл + Гідрохлортіазид')
        user_no_hd1.row('Фозинаприл + Гідрохлортіазид')
        user_no_hd1.row('Зофенаприл + Гідрохлортіазид')
        user_no_hd1.row('Периндоприл + Індапамід')
        user_no_hd1.row('Еналаприл + Індапамід')
        user_no_hd1.row('\U00002B05  Назад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F539  АРA ІІ + БКК':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Валсартан + Амлодипін')
        user_no_hd1.row('Лозартан + Амлодипін')
        user_no_hd1.row('Ірбесартан + Амлодипін')
        user_no_hd1.row('Кандесартан + Амлодипін')
        user_no_hd1.row('Телмісартан + Амлодипін')
        user_no_hd1.row('Олмесартан + Амлодипін')
        user_no_hd1.row('\U00002B05  Назад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F539  АРA ІІ + Діуретик':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Лозартан + Гідрохлортіазид')
        user_no_hd1.row('Валсартан + Гідрохлортіазид')
        user_no_hd1.row('Ірбесартан + Гідрохлортіазид')
        user_no_hd1.row('Кандесартан + Гідрохлортіазид')
        user_no_hd1.row('Телмісартан + Гідрохлортіазид')
        user_no_hd1.row('Олмесартан + Гідрохлортіазид')
        user_no_hd1.row('\U00002B05  Назад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U00002705  Крoк 2':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F538 I-AПФ + БКК + Діуретик')
        user_no_hd1.row('\U0001F539 АРA ІІ + БКК + Діуретик')
        user_no_hd1.row('\U00002B05 Назад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U00002B05  Нaзад':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F538 I-AПФ + БКК + Діуретик')
        user_no_hd1.row('\U0001F539 АРA ІІ + БКК + Діуретик')
        user_no_hd1.row('\U00002B05 Назад')
        bot.send_message(message.from_user.id, "Виберіть потрібну комбінацію:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F538 I-AПФ + БКК + Діуретик':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Периндоприл + Індапамід + Амлодипін')
        user_no_hd1.row('\U00002B05  Нaзад') 
        bot.send_message(message.from_user.id, "Виберіть діючі речовини:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F539 АРA ІІ + БКК + Діуретик':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Валсартан + Гідрохлортіазид + Амлодипін')
        user_no_hd1.row('\U00002B05  Нaзад') 
        bot.send_message(message.from_user.id, "Виберіть діючі речовини:", reply_markup =user_no_hd1)

    elif message.text == '\U00002705  Крoк 3':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002B05 Назад')
        bot.send_message(message.from_user.id, "КРОК 3. \nВ двох таблетках \U0001F48A\U0001F48A:" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n          \U00002795            " + \
                "\n         БКК " + \
                "\n          \U00002795            " + \
                "\n    Діуретик " + \
                "\n          \U00002795            \n" + \
                "Спіронолактон (25-50мг)," + \
                "\nабо інший діуретик, або альфа чи бета блокатор.  ", reply_markup =user_no_hd1)

    elif message.text == '\U00000034\U000020E3 ГХ + СН зі зниженою ФВ':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F48A Антигіпертензивні препарати')
        user_no_hd1.row('\U0001F3AF Цільові рівні АТ')
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити')
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  ІІІ  ", callback_data="ІІІ")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        bot.send_message(message.from_user.id, "\U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \n Дана схема доцільна для пацієнтів з гіпертонічною хворобою в поєднанні  з хронічною серцевою недостатністю зі зниженою фракцією викиду.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КРОК 1:\n" + \
                "\nіАПФ або АРА ІІ" + \
                "\n             \U00002795   " + \
                "\n      Діуретик" + \
                "\n             \U00002795   " + \
                "\n             ББ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КРОК 2:" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n          \U00002795            " + \
                "\n     Діуретик " + \
                "\n          \U00002795            " + \
                "\n          ББ " + \
                "\n          \U00002795            " + \
                "\n         АМР ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U0000270F Примітка:\nіАПФ- інгібітори ангіотензинперетворюючого ферменту." + \
                "\nАРАІІ- антагоністи рецепторів альдостерону ІІ" + \
                "\nБКК- блокатори кальцієвих каналів" + \
                "\nББ-бета-блокатор" + \
                "\nДіуретик- тіазидний, або тіазидоподібний." + \
                "\n(петльовий діуретик альтернатива при набряках)." + \
                "\n АМР- антагоністи мінералокортикоїдних" + \
                "\nрецепторів (спіронолактон, або еплеренон)." + \
                "\n\n\U0000270F Можливий ризик гіперкаліємії" + \
                "\nпри використанні спіронолактону у пацієнтів " + \
                "\nз рШКФ менше 45 мл/хв, або рівнем калію" + \
                "\nбільше 4,5 ммоль\л." + \
                "\n\n\U0000270F Коли антигіпертензивна терапія не потрібна у хворих з СН зі зниженою ФВ" + \
                "лікування призначати відповідно рекомендаціям ЄТК з СН.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Комбінувати іАПФ з АРА ІІ  \nНЕ рекомендується", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)  
    elif message.text == '\U00000035\U000020E3 ГХ + ФП':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F48A Антигіпертензивні препарати')
        user_no_hd1.row('\U0001F3AF Цільові рівні АТ')
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити')
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  ІІІ  ", callback_data="ІІІ")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        bot.send_message(message.from_user.id, "\U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \U0001F53B \nДана схема доцільна для пацієнтів з гіпертонічною хворобою в поєднанні з фібриляцією передсердь.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КРОК 1. \n\U0001F449 Варіант 1:\n" + \
                "\nіАПФ або АРА ІІ" + \
                "\n            \U00002795 " + \
                "\nББ або не ДГП БКК" + \
                "\n\n\U0001F449 2 варіант:" + \
                "\n            ББ" + \
                "\n            \U00002795" + \
                "\n           БКК ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КРОК 2. \n\U0001F449 Варіант 1:" + \
                "\n\nіАПФ або АРА ІІ" + \
                "\n          \U00002795            " + \
                "\n          ББ " + \
                "\n          \U00002795            \n" + \
                "ДГП АКК або діуретик" + \
                "\n\n\U0001F449 Варіант 2:" + \
                "\n\n          ББ" + \
                "\n          \U00002795            \n" + \
                "     ДГП АКК " + \
                "\n          \U00002795            \n" + \
                "     Діуретик" + \
                "\n\n+ додати антикоагулянти" + \
                "\nза шкалою CHA2DS2-VASc", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U0000270F Примітка:\nіАПФ- інгібітори ангіотензинперетворюючого ферменту." + \
                "\nАРАІІ- антагоністи рецепторів альдостерону ІІ" + \
                "\nБКК- блокатори кальцієвих каналів" + \
                "\nне ДГП- недигідропіридинові БКК(верапаміл чи дилтіазем)" + \
                "\nДГП-дигідропіридинові БКК (амлодіпін, лерканідіпін)" + \
                "\nББ-бета-блокатор" + \
                "\nДіуретик- тіазидний, або тіазидоподібний." + \
                "\n(петльовий діуретик альтернатива при набряках)." + \
                "\n\U0000270F Рутинне комбінування ББ і не ДГП БКК не рекомендовано.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Комбінувати іАПФ з АРА ІІ  НЕ рекомендується", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)
        
#(Цільові рівні АТ)
    elif message.text == '\U0001F3AF Цільові рівні АТ':
        user_no_hd6_1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd6_1.row('\U000025B6 18 - 65 років')
        user_no_hd6_1.row('\U000025B6 65-79 років')
        user_no_hd6_1.row('\U000025B6 80 і більше років')
        bot.send_sticker(message.from_user.id,'CAADAgADDQADw9L7DKCYTWj-YqO0Ag') 
        bot.send_message(message.from_user.id, "Вкажіть вік пацієнта?", reply_markup =user_no_hd6_1)
    elif message.text == '\U00002196 Назад':
        user_no_hd6_1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd6_1.row('\U000025B6 18 - 65 років')
        user_no_hd6_1.row('\U000025B6 65-79 років')
        user_no_hd6_1.row('\U000025B6 80 і більше років')
        bot.send_sticker(message.from_user.id,'CAADAgADDQADw9L7DKCYTWj-YqO0Ag') 
        bot.send_message(message.from_user.id, "Вкажіть вік пацієнта?", reply_markup =user_no_hd6_1)

    elif message.text == '\U000025B6 18 - 65 років':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F538АГ')
        user_no_hd1.row('\U0001F538АГ+ЦД')
        user_no_hd1.row('\U0001F538АГ+ХХН')
        user_no_hd1.row('\U0001F538АГ+ІХС')
        user_no_hd1.row('\U0001F538АГ+Інсульт чи ТІА')
        user_no_hd1.row('\U00002196 Назад')
        bot.send_message(message.from_user.id, "Виберіть супутнє захворювання (якщо наявне)?", reply_markup =user_no_hd1)

    elif message.text == '\U00002196  Назад':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F538АГ')
        user_no_hd1.row('\U0001F538АГ+ЦД')
        user_no_hd1.row('\U0001F538АГ+ХХН')
        user_no_hd1.row('\U0001F538АГ+ІХС')
        user_no_hd1.row('\U0001F538АГ+Інсульт чи ТІА')
        user_no_hd1.row('\U00002196 Назад')
        bot.send_message(message.from_user.id, "Виберіть супутнє захворювання (якщо наявне)?", reply_markup =user_no_hd1)

    elif message.text == '\U0001F538АГ':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Назад')
        bot.send_message(message.from_user.id, "При артеріальній гіпертензії:" + \
        "\n\U00002705Систолічний АТ" + \
        "до 130, або нижче, якщо " + \
        "переноситься, але не нижче 120." + \
        "\n\U00002705Діастолічний - 70-79.", reply_markup =user_no_hd1)
    elif message.text == '\U0001F538АГ+ЦД':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Назад')
        bot.send_message(message.from_user.id, "Артеріальна гіпертензія" + \
        "\nз цукровим діабетом:" + \
        "\n\U00002705 Систолічний АТ" + \
        "до 130, або нижче, якщо " + \
        "переноситься, але не нижче 120." + \
        "\n\U00002705 Діастолічний - 70-79 мм.рт.ст.", reply_markup =user_no_hd1)
    elif message.text == '\U0001F538АГ+ХХН':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Назад')
        bot.send_message(message.from_user.id, "Артеріальна гіпертензія" + \
        "\nз хронічною хворобою нирок:" + \
        "\n\U00002705 Систолічний АТ" + \
        " нижче 140, до 130 " + \
        " якщо переноситься." + \
        "\n\U00002705 Діастолічний- 70-79 мм.рт.ст.", reply_markup =user_no_hd1)
    elif message.text == '\U0001F538АГ+ІХС':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Назад')
        bot.send_message(message.from_user.id, "Артеріальна гіпертензія" + \
        "\nз ішемічною хворобою серця:" + \
        "\n\U00002705 Cистолічний АТ" + \
        "до 130, або нижче, якщо " + \
        "переноситься, але " + \
        "не нижче 120." + \
        "\n\U00002705 Діастолічний- 70-79 мм.рт.ст.", reply_markup =user_no_hd1)
    elif message.text == '\U0001F538АГ+Інсульт чи ТІА':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Назад')
        bot.send_message(message.from_user.id, "Цільовий рівень для пацієнтів," + \
        "\nщо перенесли інсульт." + \
        "\n(не стосується пацієнтів з гострим інсультом)" + \
        "\n\U00002705 Систолічний АТ" + \
        "до 130, або нижче, якщо " + \
        "переноситься, але " + \
        "не нижче 120." + \
        "\n\U00002705 Діастолічний- 70-79 мм.рт.ст.", reply_markup =user_no_hd1)
    elif message.text == '\U000025B6 65-79 років':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Назад')
        bot.send_message(message.from_user.id, "\U00002705 Цільовий систолічний АТ" + \
        "130-139  якщо переноситься." + \
        "\n\U00002705 Діастолічний АТ - 70-79." + \
        "\nСтосується також  пацієнтів" + \
        "з супутніми: ЦД, ХХН, ІХС," + \
        "чи перенесеним інсультом" + \
        "в минулому.", reply_markup =user_no_hd1)
    elif message.text == '\U000025B6 80 і більше років':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4CA Схеми лікування')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Назад')
        bot.send_message(message.from_user.id, "\U00002705 Цільовий систолічний АТ" + \
        "130-139  якщо переноситься." + \
        "\n\U00002705 Діастолічний АТ - 70-79." + \
        "\nСтосується також  пацієнтів" + \
        "з супутніми: ЦД, ХХН, ІХС," + \
        "чи перенесеним інсультом" + \
        "в минулому.", reply_markup =user_no_hd1)
#(Модифікація способу життя)

    elif message.text == '\U0001F34F Модифікація способу життя':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F34F Харчування')
        user_no_hd1.row('\U0001F6AC Шкідливі звички')
        user_no_hd1.row('\U0001F3CA Спосіб життя')
        bot.send_message(message.from_user.id, "Вкажіть розділ:", reply_markup =user_no_hd1)

    elif message.text == '\U0001F34F Харчування':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        user_no_hd1.row('\U0001F6AC Шкідливі звички')
        user_no_hd1.row('\U0001F3CA Спосіб життя')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Рекомендовано обмеження \nспоживання (кухонної) солі" + \
                " до < 5 г/день", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)
        bot.send_message(message.from_user.id, "\U00002705 Рекомендовано: \n\U00002B06 збільшити споживання овочів, свіжих фруктів\U0001F34E, риби\U0001F41F, горіхів, ненасичених жирних кислот (маслинова олія), вживання знежирених молочних продуктів; \n\U00002B07 низьке споживання червоного м'яса", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)

    elif message.text == '\U0001F6AC Шкідливі звички':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F34F Харчування')
        user_no_hd1.row('\U0001F3CA Спосіб життя')
        user_no_hd1.row('\U00002705 Продовжити')
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        keyboard4 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        callback_button4 = types.InlineKeyboardButton(text="  B  ", callback_data="В")
        keyboard4.add(callback_button4)
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        bot.send_message(message.from_user.id, "\U00002705 Рекомендовано обмеження  споживання алкоголю: \nдля чоловіків менше 14 одиниць на тиждень, \nдля жінок менше 8 одиниць на тиждень. \n1 одиниця – 250 мл пива\U0001F37A, або 125 мл вина\U0001F377.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)
        bot.send_message(message.from_user.id, "\U00002705 Рекомендована відмова від паління  \U0001F6AD, спостереження і медична підтримка,направлення до програм відмови від паління.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard4)

    elif message.text == '\U0001F3CA Спосіб життя':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F34F Харчування')
        user_no_hd1.row('\U0001F6AC Шкідливі звички')
        user_no_hd1.row('\U00002705 Продовжити')
        keyboard3 = types.InlineKeyboardMarkup()
        keyboard13 = types.InlineKeyboardMarkup()
        callback_button3 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button31 = types.InlineKeyboardButton(text=" A ", callback_data="А")
        keyboard13.add(callback_button3)
        keyboard3.add(callback_button31)
        bot.send_message(message.from_user.id, "\U00002705 Показано контролювати масу, щоб уникнути ожиріння \n(ІМТ > 30 кг/м2 або окружність талії > 102 см у чоловіків та > 88 см у жінок), орієнтуючись на здорові" + \
                         "  значення ІМТ (приблизно 20-25 кг/м2) та окружності талії (< 94 см у чоловіків " + \
                         "  та < 80 см у жінок), щоб знизити рівень АТ та СС-ризик", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)
        bot.send_message(message.from_user.id, "\U00002705 Рекомендуються регулярні  аеробні фізичні навантаження (наприклад, принаймні 30 хв " + \
                         "помірних динамічних вправ  5-7 днів на тиждень)", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard13)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard3)
        
#Гіпертензія при спеціальних станах
        
    elif message.text == '\U00002764 Гіпертензія при спеціальних станах':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F3AD Маскована гіпертензія')
        user_no_hd1.row('\U0001F637 Гіпертензія білого халата')
        user_no_hd1.row('\U0001F575 Псевдорезистентна гіпертензія')
        user_no_hd1.row('\U0001F512 Резистентна гіпертензія')
        user_no_hd1.row('\U00002753 Вторинна гіпертензія')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Виберіть потрібний розділ", reply_markup =user_no_hd1)

    elif message.text == '\U0001F3AD Маскована гіпертензія':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F3E0 Домашній моніторинг АТ(ДМАТ)')
        user_no_hd1.row('\U0001F55B Амбулаторний моніторинг АТ(АМАТ)')
        user_no_hd1.row('\U000025B6 130-139/85-89')
        user_no_hd1.row('\U00002764 Гіпертензія при спеціальних станах')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U0000270F Маскована гіпертензія саме той випадок, коли при офісному вимірюванні артеріального тиску (тобто медичним працівником) рівень тиску відповідає нормі, проте при вимірюванні шляхом домашнього чи добового моніторингу рівень тиску підвищений.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U0000270F Маскована гіпертензія більш поширена  в осіб з високим нормальним АТ (130-139/80-89). ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U0000270F Потрібно провести оцінку серце-судинного ризику. У таких пацієнтів доцільно назначати антигіпертензивні препарати, оскільки такі пацієнти мають високий ризик ССЗ  і часто мають ураження органів мішеней, обумовлених гіпертензією." , reply_markup =user_no_hd1)    

    elif message.text == '\U0001F637 Гіпертензія білого халата':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4A3 ОГУОМ')
        user_no_hd1.row('\U0001F3E0 Домашній моніторинг АТ(ДМАТ)')
        user_no_hd1.row('\U0001F55B Амбулаторний моніторинг АТ(АМАТ)')
        user_no_hd1.row('\U00002764 Гіпертензія при спеціальних станах')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U0000270F Гіпертензія білого халата, це підвищений офісний артеріальний тиск (виміряний медичним працівником) незважаючи на нормальний позаофісний АТ. \n\U0000270F Рекомендується ретельне проведення оцінки серцево-судинного ризику і  вимірювання, як офісного,  так і позаофісного АТ  не рідше ніж кожні 2 роки.  \n\U0000270F Лікування повинно включати  модифікацію способу життя . \n\U0000270F Чи має дана категорія пацієнтів отримувати антигіпертензивні препарати на сьогодні остаточно не вирішено, проте це не є приводом виключати медикаментозне лікування  у хворих високого ризику ССЗ чи з наявністю  ОГУОМ.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F575 Псевдорезистентна гіпертензія':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002764 Гіпертензія при спеціальних станах')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, '\U0000270F Псевдорезистентна гіпертензія стан при якому не досягається цільовий рівень артеріального тиску, у зв’язку з причинами, які можна змінити. \n\U0000270F Псевдорезистентна гіпертензія може бути зумовлена наступними причинами:  \n\U00000031\U000020E3 Погана прихільність до ліків. \n\U00000032\U000020E3 "Феномен білого халату" \n\U00000033\U000020E3 Неправильна методика вимірювання. \n\U00000034\U000020E3 Виражена кальцифікація плечової артерії. \n\U00000035\U000020E3 Неадекватні дози чи комбінація ліків. ', reply_markup =user_no_hd1)
        
    elif message.text == '\U0001F512 Резистентна гіпертензія':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4C4 Причини')
        user_no_hd1.row('\U0001F489 Лікування')
        user_no_hd1.row('\U0001F3E0 Домашній моніторинг АТ(ДМАТ)')
        user_no_hd1.row('\U0001F55B Амбулаторний моніторинг АТ(АМАТ)')
        user_no_hd1.row('\U00002764 Гіпертензія при спеціальних станах')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U0000270F Рекомендується визначити  АГ,  як стійку до лікування  (тобто резистентну гіпертензію), коли: \n\U0001F6A9 Призначене лікування в оптимальних дозах, або найкраще переносимих дозах, яке повинна включати, як правило, інгібітор АПФ або АРА ІІ  із БКК і тіазид/тіазидовий діуретик не знижує клінічні показники САТ і ДАТ до < 140 мм рт.ст. і/або < 90 мм рт.ст. відповідно \n\U0001F6A9 Неадекватний контроль АТ підтверджений АМАТ або ДМАТ \n\U0001F6A9 Після виключення різних причин  псевдорезистентної гіпертензії (особливо поганої прихильності до ліків) і вторинних гіпертензій", reply_markup =user_no_hd1)

    elif message.text == '\U0001F4C4 Причини':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F489 Лікування')
        user_no_hd1.row('\U00002753 Вторинна гіпертензія')
        user_no_hd1.row('\U00002764 Гіпертензія при спеціальних станах')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U0000270F Причини: \n\n\U00000031\U000020E3 Ожиріння, надмірне споживання алкоголю, натрію. \n\n\U00000032\U000020E3 Вживання вазопресорів або натрій затримуючих речовин.  \n\U0001F6A9 Ліки: оральні контрацептиви,  симпатоміметичні засоби, НПЗЗ,  Циклоспорин, Еритропоетин, стероїди,  деякі препарати для лікування раку.  \n\U0001F6A9 Інші засоби: кокаїн, анаболічні стероїди, надмірне споживання локриці, ефедра і хуанг . \n\n\U00000033\U000020E3 Вторинні форми гіпертензії:  \n\U0001F6A9 Часто: первинній альдостеронізм,  атеросклеротична реноваскулярна хвороба,  ХХН, обструктивне апное сну. \n\U0001F6A9 Нечасто: феохромоцитома,  фібромускулярна дисплазія,  коартація аорти, хв. Кушинга, гіперпаратиреоз. ", reply_markup =user_no_hd1)

    elif message.text == '\U0001F489 Лікування':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4C4 Причини')
        user_no_hd1.row('\U0001F48A Антигіпертензивні препарати')
        user_no_hd1.row('\U00002764 Гіпертензія при спеціальних станах')
        user_no_hd1.row('\U00002705 Продовжити')
        keyboard2 = types.InlineKeyboardMarkup()
        keyboard12 = types.InlineKeyboardMarkup()
        callback_button22 = types.InlineKeyboardButton(text="  І  ", callback_data="І")
        callback_button212 = types.InlineKeyboardButton(text=" С ", callback_data="C")
        keyboard2.add(callback_button22)
        keyboard12.add(callback_button212)
        bot.send_message(message.from_user.id, "\U0000270F Рекомендоване наступне  лікування резистентної гіпертензії: \n\U0001F6A9 Посилення заходів щодо способу життя, особливо обмеження натрію \n\U0001F6A9 Додавання до існуючого лікування низьких доз  спіронолактону \n\U0001F6A9 При непереносимості  спіронолактону - подальше доповнення діуретичної  терапії, або еплереноном,  або амілоридом, або  більш високими дозами  тіазиду/тіазидового діуретика  або петльовим діуретином, або додавання бісопрололу чи доксазозину ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "КЛАС:", reply_markup =keyboard2)
        bot.send_message(message.from_user.id, "РІВЕНЬ:", reply_markup =keyboard12)
        bot.send_message(message.from_user.id, "\U0001F4DD Спіронолактон лише для хворих з  рШКФ більше 45 мл/хв, та концентрація калію в плазмі менше 4,5 ммоль/л. \n\U0001F4DD При непереносимості спіронолактону:  еплеренон.", reply_markup =user_no_hd1)

    elif message.text == '\U00002753 Вторинна гіпертензія':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4C3 Причини')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Вторинна гіпертензія- це гіпертензія внаслідок встановленої причини, яка може бути вилікована специфічним для причини втручанням. ", reply_markup =user_no_hd1)

    elif message.text == '\U0001F4C3 Причини':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002764 Гіпертензія при спеціальних станах')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Причини:  \n\U00000031\U000020E3 Первинний альдостеронізм (5-15% серед хворих на АГ) \n\U00000032\U000020E3 Обструктивне апное сну (5-10%) \n\U00000033\U000020E3 Хвороба паренхіми нирок (2-10%) \n\U00000034\U000020E3 Атеросклеротичне реноваскулярне захворювання, або фібромускулярна  дисплазія (1-10%)  \n\U00000035\U000020E3 Феохромоцитома (менше1%)  \n\U00000036\U000020E3 Синдром Кушинга (менше1%) \n\U00000037\U000020E3 Гіпер- та гіпотиреоз (1-2%) \n\U00000038\U000020E3 Гіперпаратиреоз (менше1%) \n\U00000039\U000020E3 Коарктація аорти (менше1%)", reply_markup =user_no_hd1)


#Антигіпертензивні препарати

    elif message.text == '\U0001F48A Антигіпертензивні препарати':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U0001F536 АРА ІІ')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U0001F536 БКК')
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Виберіть групу препаратів", reply_markup =user_no_hd1)

    elif message.text == '\U00002196 Нaзaд':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U0001F536 АРА ІІ')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U0001F536 БКК')
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Виберіть групу препаратів", reply_markup =user_no_hd1)

#ІАПФ

        
    elif message.text == '\U0001F537 ІАПФ':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Периндоприл')
        user_no_hd1.row('\U0001F4D4 Раміприл')
        user_no_hd1.row('\U0001F4D4 Лізиноприл')
        user_no_hd1.row('\U0001F4D4 Каптоприл')
        user_no_hd1.row('\U0001F4D4 Еналаприл')
        user_no_hd1.row('\U0001F4D4 Хінаприл')
        user_no_hd1.row('\U0001F4D4 Фозиноприл')
        user_no_hd1.row('\U0001F4D4 Зофеноприл')
        user_no_hd1.row('\U0001F4D4 Трандолаприл')
        user_no_hd1.row('\U00002196 Нaзaд')
        bot.send_message(message.from_user.id, "Вкажіть діючу речовину", reply_markup =user_no_hd1)

    elif message.text == '\U00002196 Нaзад':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Периндоприл')
        user_no_hd1.row('\U0001F4D4 Раміприл')
        user_no_hd1.row('\U0001F4D4 Лізиноприл')
        user_no_hd1.row('\U0001F4D4 Каптоприл')
        user_no_hd1.row('\U0001F4D4 Еналаприл')
        user_no_hd1.row('\U0001F4D4 Хінаприл')
        user_no_hd1.row('\U0001F4D4 Фозиноприл')
        user_no_hd1.row('\U0001F4D4 Зофеноприл')
        user_no_hd1.row('\U0001F4D4 Трандолаприл')
        user_no_hd1.row('\U00002196 Нaзaд')
        bot.send_message(message.from_user.id, "Вкажіть діючу речовину", reply_markup =user_no_hd1)

    elif message.text == '\U0001F4D4 Периндоприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Показання')
        user_no_hd1.row('\U0000274C Протипокази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати периндоприла')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати периндоприла')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Нaзад')
        bot.send_message(message.from_user.id, "Перендоприл \n\U0001F4CB Спосіб застосування: (Інструкція - Престаріум) \n\U0001F6A9 Рекомендовану дозу приймати щодня 1 раз на добу вранці перед вживанням їжі. \n\U0001F6A9 Рекомендована початкова доза становить 4 мг один раз на добу, через місяць лікування дозу можна збільшити до 8 мг один раз на добу. \n\U0001F6A9 Пацієнтам, які перебувають на гемодіалізі, слід застосовувати периндоприл після проведення гемодіалізу. \n\U0001F6A9 Пацієнти з печінковою недостатністю не потребують підбору дози препарату. \n\U0001F6A9 Таблетки 4 мг і 5 мг підлягають поділу. Таблетки в дозуванні 2 мг 2,5 мг 8 мг 10 мг не підлягають поділу.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705Препарати з  дозуванням  \U00000034\U000020E3  мг і \U00000035\U000020E3  мг, або  \U00000038\U000020E3  і \U00000031\U000020E3 \U00000030\U000020E3 мг між собою еквівалентні, тому що містять різні похідні периндоприлу. \n(периндоприл тертбутиламіну  і  периндоприл аргініну відповідно) ", reply_markup =user_no_hd1)
        
    elif message.text == '\U00002705 Показання':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C Протипокази')
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Покази до застосування інгібіторів АПФ: \n\U00002705 Артеріальна гіпертензія \n\U00002705 Хронічна серцева недостатність \n\U00002705 Стабільна ІХС (профілактика серцево-судинних ускладнень)", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C Протипокази':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Показання')
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипокази до застосування інгібіторів АПФ: \n\U0000274C Вагітність і лактація \n\U0000274C Ангіоневротичний набряк в анамнезі на ІАПФ \n\U0000274C Двохсторонній стеноз нирок (або стеноз артерії єдиної нирки) \n\U0000274C Гіперкаліємія", reply_markup =user_no_hd1)
        


    elif message.text == '\U0001F48A Монокомпонентні препарати периндоприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Престаріум', url='https://medhub.info/38ce75bd')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="2 мг", callback_data="2 мг периндоприл")
        callback_button2 = types.InlineKeyboardButton(text="2,5 мг ", callback_data="2,5 мг периндоприл")
        callback_button3 = types.InlineKeyboardButton(text="4 мг", callback_data="4 мг периндоприл")
        callback_button4 = types.InlineKeyboardButton(text="5 мг ", callback_data="5 мг периндоприл")
        callback_button5 = types.InlineKeyboardButton(text="8 мг", callback_data="8 мг периндоприл")
        callback_button6 = types.InlineKeyboardButton(text="10 мг ", callback_data="10 мг периндоприл")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6)
        user_no_hd1.row('\U0001F4D4 Периндоприл')
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною: периндоприл.\n\U000025B6ПРЕСТАРІУМ \nІрландія + Франція \n\U000025B6 ПЕРИНДОПРИЛ САНДОЗ \nНімеччина + Словенія \n\U000025B6ПЕРИНДОПРИЛ КРКА  \nСловенія \n\U000025B6ПРЕНЕСА  \nСловенія \n\U000025B6ПРОМЕПРИЛ \nСловенія + Чеська республіка \n\U000025B6ПЕРИНДОПРИЛ-РІХТЕР  \nПольща + Угорщина \n\U000025B6ПЕРИНДОПРИЛ-ТЕВА \nУгорщина \n\U000025B6ПЕРІНДОПРЕС \nУкраїна \n\U000025B6 ЕРУПНІЛ \nІндія \n\U000025B6 ХІТЕН  \nІндія \n\U000025B6ПЕРИСТАР  \nІндія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
       

    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати периндоприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Периндоприл + Індапамід')
        user_no_hd1.row('Периндоприл + Амлодипін')
        user_no_hd1.row('Периндоприл + Бісопролол')
        user_no_hd1.row('Периндоприл + Індапамід + Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: периндоприл.", reply_markup =user_no_hd1)

    elif message.text == 'Периндоприл + Індапамід':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="2 мг\U000026A1 0,625 мг", callback_data="2 мг Периндоприл + Індапамід")
        callback_button2 = types.InlineKeyboardButton(text="2,5 мг\U000026A1 0,625 мг", callback_data="2,5 мг Периндоприл + Індапамід")
        callback_button3 = types.InlineKeyboardButton(text="4 мг\U000026A1 1,25 мг", callback_data="4 мг Периндоприл + Індапамід")
        callback_button4 = types.InlineKeyboardButton(text="5 мг\U000026A1 1,25 мг", callback_data="5 мг Периндоприл + Індапамід")
        callback_button5 = types.InlineKeyboardButton(text="8 мг\U000026A1 2,5 мг", callback_data="8 мг Периндоприл + Індапамід")
        callback_button6 = types.InlineKeyboardButton(text="10 мг\U000026A1 2,5 мг", callback_data="10 мг Периндоприл + Індапамід")
        keyboard14.add(callback_button1, callback_button2)
        keyboard14.add(callback_button3, callback_button4)
        keyboard14.add(callback_button5, callback_button6)
        user_no_hd1.row('\U0001F4D4 Периндоприл')
        user_no_hd1.row('\U0001F4D4 Індапамід')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію периндоприла з індапамідом містять препарати: \n \U000025B6 ЕРУПНІЛ ПЛЮС    \nІндія \n \U000025B6 ІН-АЛІТЕР  \nУкраїна \n \U000025B6 КО-ПРЕНЕСА  \n Словенія \n \U000025B6 НОЛІПРЕЛ \nІрландія + Франція \n \U000025B6 ПЕРИНДОПРИЛ/ІНДАПАМІД КРКА  \nСловенія \n \U000025B6 ПЕРИНДОПРИЛ/ІНДАПАМІД ТЕВА  \nУгорщина \n \U000025B6 ПРЕСТАРІУМ АРГІНІН КОМБІ   \nІрландія + Франція \n \U000025B6 ПРИЛАМІД  \nСловенія", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)
        
    elif message.text == 'Периндоприл + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="3,5 мг\U000026A1 2,5 мг", callback_data="3,5 мг Периндоприл + 2,5Амлодипін")
        callback_button2 = types.InlineKeyboardButton(text="4 мг\U000026A1 5 мг", callback_data="4 мг Периндоприл + 5Амлодипін")
        callback_button3 = types.InlineKeyboardButton(text="4 мг\U000026A1 10 мг", callback_data="4 мг Периндоприл + 10Амлодипін")
        callback_button4 = types.InlineKeyboardButton(text="5 мг\U000026A1 5 мг", callback_data="5 мг Периндоприл + 5Амлодипін")
        callback_button5 = types.InlineKeyboardButton(text="5 мг\U000026A1 10 мг", callback_data="5 мг Периндоприл + 10Амлодипін")
        callback_button6 = types.InlineKeyboardButton(text="7 мг\U000026A1 5 мг", callback_data="7 мг Периндоприл + 5Амлодипін")
        callback_button7 = types.InlineKeyboardButton(text="8 мг\U000026A1 5 мг", callback_data="8 мг Периндоприл + 5Амлодипін")
        callback_button8 = types.InlineKeyboardButton(text="8 мг\U000026A1 10 мг", callback_data="8 мг Периндоприл + 10Амлодипін")
        callback_button9 = types.InlineKeyboardButton(text="10 мг\U000026A1 5 мг", callback_data="10 мг Периндоприл + 5Амлодипін")
        callback_button10 = types.InlineKeyboardButton(text="10 мг\U000026A1 10 мг ", callback_data="10 мг Периндоприл + 10Амлодипін")
        callback_button11 = types.InlineKeyboardButton(text="14 мг\U000026A1 10 мг", callback_data="14 мг Периндоприл + 10Амлодипін")
        keyboard14.add(callback_button1, callback_button2)
        keyboard14.add(callback_button3, callback_button4)
        keyboard14.add(callback_button5, callback_button6)
        keyboard14.add(callback_button7, callback_button8)
        keyboard14.add(callback_button9, callback_button10)
        keyboard14.add(callback_button11)
        user_no_hd1.row('\U0001F4D4 Периндоприл')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію периндоприла з амлодипіном містять препарати:   \n\U000025B6 АМ-АЛІТЕР  \n Україна \n\U000025B6 АМЛЕCСА   \n Словенія \n\U000025B6 АМЛОДИПІН-ПЕРИНДОПРИЛ-РІХТЕР  \n Польща \n\U000025B6 БІ-ПРЕСТАРІУМ  \n Ірландія + Польща + Франція \n\U000025B6 БІ-ПРЕСТАРІУМ N   \n  Ірландія \n\U000025B6 ВІАКОРАМ 14МГ/10МГ  \n  Ірландія \n\U000025B6 ПЕРИНДОПРИЛ 4/АМЛОДИПІН 10 КРКА  \n Словенія \n\U000025B6 ПЕРИНДОПРИЛ/АМЛОДИПІН-ТЕВА  \n Угорщина ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)
        
    elif message.text == 'Периндоприл + Бісопролол':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="5 мг\U000026A1 5 мг", callback_data=" 5Периндоприл + 5Бісопролол")
        callback_button2 = types.InlineKeyboardButton(text="5 мг\U000026A1 10 мг", callback_data=" 5Периндоприл + 10Бісопролол ")
        callback_button3 = types.InlineKeyboardButton(text="10 мг\U000026A1 5 мг", callback_data=" 10Периндоприл + 5Бісопролол")
        callback_button4 = types.InlineKeyboardButton(text="10 мг\U000026A1 10 мг", callback_data="10 Периндоприл + 10Бісопролол")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F4D4 Периндоприл')
        user_no_hd1.row('\U0001F4D4 Бісопролол')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію периндоприла з бісопрололом містять препарати:  \n\U000025B6 КОСІРЕЛЬ \nІрландія + Франція \n\U000025B6 ПРЕСТИЛОЛ \nІрландія + Франція ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)
    

    elif message.text == 'Периндоприл + Індапамід + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625\U000026A1 5 ", callback_data="2 мг\0,625 мг\5 мгПериндоприл ")
        callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625\U000026A1 5 мг", callback_data="2,5 мг\0,625 мг\5 мг Периндоприл ")
        callback_button3 = types.InlineKeyboardButton(text="4 \U000026A1 1,25 \U000026A1 5 мг", callback_data="4 мг\1,25 мг\5 мг Периндоприл ")
        callback_button4 = types.InlineKeyboardButton(text="4\U000026A1 1,25\U000026A1 10 мг", callback_data="4 мг\1,25 мг\10 мг Периндоприл ")
        callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 1,25\U000026A1 10 мг", callback_data="5 мг\1,25 мг\10 мг Периндоприл ")
        callback_button6 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 5 мг", callback_data="8 мг\2,5 мг\5 мг Периндоприл ")
        callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 10 мг", callback_data="8 мг\2,5 мг\10 мг Периндоприл ")
        callback_button8 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 5 мг", callback_data="10 мг\2,5 мг\5 мг Периндоприл ")
        callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 10 мг", callback_data="10 мг\2,5 мг\10 мг Периндоприл ")
        keyboard14.add(callback_button1, callback_button2)    
        keyboard14.add(callback_button3, callback_button4)
        keyboard14.add(callback_button5, callback_button6)
        keyboard14.add(callback_button7, callback_button8)
        keyboard14.add(callback_button9)
        user_no_hd1.row('\U0001F4D4 Периндоприл')
        user_no_hd1.row('\U0001F4D4 Індапамід')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Потійну комбінацію периндоприла з індапамідом і амлодипіном містять препарати:  \n\U000025B6 КО-АМЛЕССА  \nНімеччина + Польща + Словенія \n\U000025B6 ТРИПЛІКСАМ  \nІрландія + Франція ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)
#Раміприл

    elif message.text == '\U0001F4D4 Раміприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Показання')
        user_no_hd1.row('\U0000274C Протипокази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати раміприла')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати раміприла')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Нaзад')
        bot.send_message(message.from_user.id, "Раміприл \n\U0001F4CB Спосіб застосування: (Інструкція – Рамі-Сандоз) \n\U0001F6A9 Препарат можна приймати до, під час та після їди, оскільки вживання їжі не впливає на біодоступність препарату. \n\U0001F6A9 Таблетки по 2,5 мг, 5 мг та 10 мг призначені для розподілу навпіл, але не можна розжовувати або подрібнювати. ", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати раміприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Тритаце', url='https://medhub.info/bff1f32a')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="1,25 мг", callback_data="1,25раміприл")
        callback_button2 = types.InlineKeyboardButton(text="2,5 мг ", callback_data="2,5раміприл")
        callback_button3 = types.InlineKeyboardButton(text="5 мг", callback_data="5раміприл")
        callback_button4 = types.InlineKeyboardButton(text="10 мг ", callback_data="10раміприл")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F4D4 Раміприл')
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною: раміприл. \n\U000025B6  АМПРИЛ  \n  Словенія \n\U000025B6  АНГІРАМ  \n  Індія \n\U000025B6  БРЮМІПРИЛ  \n  Бельгія + Португалія \n\U000025B6  КАРДИПРИЛ   \n  Індія \n\U000025B6 ПОЛАПРИЛ  \n Ісландія + Мальта + Польща \n\U000025B6 РАМАГ  \n  Болгарія + Ісландія + Мальта \n\U000025B6 РАМІ САНДОЗ  \n  Польща \n\U000025B6 РАМІЗЕС  \n  Україна \n\U000025B6 РАМІМЕД  \n  Мальта \n\U000025B6 РАМІПРИЛ АЙКОР  \n  Мальта \n\U000025B6 РАМІПРИЛ-ТЕВА  \n  Німеччина \n\U000025B6 РАМКОР  \n  Індія \n\U000025B6 ТОПРИЛ  \n  Індія \n\U000025B6 ТРИТАЦЕ  \n  Італія \n\U000025B6 ХАРТИЛ  \n  Мальта + Угорщина ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати раміприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Раміприл + Гідрохлортіазид')
        user_no_hd1.row('Раміприл + Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: раміприл.", reply_markup =user_no_hd1)


#Раміприл з гідрохлортіазидом

    elif message.text == 'Раміприл + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="2,5 \U000026A1 12,5", callback_data="2,5Раміприл+ 12,5Гідрохлортіазид")
        callback_button2 = types.InlineKeyboardButton(text="5 \U000026A1 12,5", callback_data="5Раміприл+ 12,5Гідрохлортіазид")
        callback_button3 = types.InlineKeyboardButton(text="5 \U000026A1 25", callback_data="5Раміприл+ 25Гідрохлортіазид")
        callback_button4 = types.InlineKeyboardButton(text="10 \U000026A1 12,5", callback_data="10Раміприл+ 12,5Гідрохлортіазид")
        callback_button5 = types.InlineKeyboardButton(text="10 \U000026A1 25", callback_data="10Раміприл+ 25Гідрохлортіазид")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5)
        user_no_hd1.row('\U0001F4D4 Раміприл')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію раміприла з гідрохлоротіазидом містять препарати: \n\U000025B6 АМПРИЛ HD  \n  Словенія \n\U000025B6  ПРЕВЕНКОР ПЛЮС  \n  Канада \n\U000025B6  РАМАГ Н  \n  Ісландія + Мальта \n\U000025B6 РАМАЗІД Н \n  Мальта \n\U000025B6  РАМІ САНДОЗ КОМПОЗИТУМ  \n Німеччина + Польща \n\U000025B6  РАМІЗЕС КОМ  \n Україна \n\U000025B6  РАМІМЕД КОМБІ  \n Мальта \n\U000025B6  ТРИТАЦЕ ПЛЮС \n Італія \n\U000025B6  ХАРТИЛ-Н  \n  Німеччина + Угорщина", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

#Раміприл з амлодипіном
        
    elif message.text == 'Раміприл + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="5 мг \U000026A1 5 мг", callback_data="5Раміприл+ 5Амлодипін")
        callback_button2 = types.InlineKeyboardButton(text="5 мг \U000026A1 10 мг", callback_data="5Раміприл + 10Амлодипін")
        callback_button3 = types.InlineKeyboardButton(text="10 мг \U000026A1 5 мг", callback_data="10Раміприл + 5Амлодипін")
        callback_button4 = types.InlineKeyboardButton(text="10 мг \U000026A1 10 мг", callback_data="10Раміприл + 10Амлодипін")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F4D4 Раміприл')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію раміприла з амлодипіном містять препарати:\U00002705 Комбінацію раміприла з амлодипіном містять препарати: \n\U000025B6 БІ-РАМАГ  \n  Польща \n\U000025B6 СУМІЛАР  \n Польща + Словенія \n\U000025B6 ТРИТАЦЕ-А \n Польща ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

#Лізиноприл

    elif message.text == '\U0001F4D4 Лізиноприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Показання')
        user_no_hd1.row('\U0000274C Протипокази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати лізиноприла')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати лізиноприла')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Нaзад')
        bot.send_message(message.from_user.id, "\n\U0001F4CB Спосіб застосування: \n\U0001F6A9 Приймати 1 раз на добу, в один і той же час, незалежно від прийому їжі.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати лізиноприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Лізиноприл', url='https://medhub.info/424de09e')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5лізиноприл")
        callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5лізиноприл")
        callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10лізиноприл")
        callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20лізиноприл")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F4D4 Лізиноприл')
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною: лізиноприл: \n\U000025B6  АУРОЛАЙЗА  \n  Індія \n\U000025B6  ВІТОПРИЛ  \n  В'єтнам + Німеччина \n\U000025B6  ДАПРИЛ  \n  Кіпр \n\U000025B6  ДИРОТОН  \n  Угорщина \n\U000025B6  ІРУМЕД  \n  Хорватія \n\U000025B6  ЛІЗИ САНДОЗ  \n  Німеччина + Словенія \n\U000025B6  ЛІЗИНОПРИЛ  \n  Україна \n\U000025B6  ЛІЗИНОПРИЛ КРКА  \n  Словенія + Хорватія \n\U000025B6  ЛІЗИНОПРИЛ ЛЮПІН  \n  Індія \n\U000025B6  ЛІЗИНОПРИЛ-АСТРАФАРМ  \n  Україна \n\U000025B6  ЛІЗИНОПРИЛ-ТЕВА  \n  Німеччина + Угорщина \n\U000025B6  ЛІНОТОР  \n  Йорданія \n\U000025B6  ЛІПРИЛ  \n  Україна \n\U000025B6  ЛОПРИЛ БОСНАЛЕК  \n Боснія і Герцоговина \n\U000025B6  СКОПРИЛ  \n  Македонія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)




    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати лізиноприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Лізиноприл + Гідрохлортіазид')
        user_no_hd1.row('Лізиноприл + Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: лізиноприл.", reply_markup =user_no_hd1)
#Лізиноприл з гідрохлортіазидом

    elif message.text == 'Лізиноприл + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="10 мг \U000026A1 12,5 мг", callback_data="10Лізиноприл+ 12,5Гідрохлортіазид")
        callback_button2 = types.InlineKeyboardButton(text="20 мг \U000026A1 12,5 мг", callback_data="20Лізиноприл+ 12,5Гідрохлортіазид")
        callback_button3 = types.InlineKeyboardButton(text="20 мг \U000026A1 25 мг", callback_data="20Лізиноприл+ 25Гідрохлортіазид")
        keyboard14.add(callback_button1)
        keyboard14.add(callback_button2)
        keyboard14.add(callback_button3)
        user_no_hd1.row('\U0001F4D4 Лізиноприл')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію лізиноприла з гідрохлоротіазидом містять препарати: \n\U000025B6 ІРУЗИД  \n  Хорватія \n\U000025B6 КО-ДИРОТОН  \n   Польща + Угорщина \n\U000025B6 ЛІЗИНОПРАЗИД  \n  Україна \n\U000025B6 ЛІЗИНОПРИЛ  НЛ КРКА  таблетки  Словенія + Хорватія \n\U000025B6 ЛІЗОРЕТИК \n Індія \n\U000025B6 ЛІЗОТІАЗИД-ТЕВА  \n  Угорщина \n\U000025B6 ЛІПРАЗИД \n Україна \n\U000025B6 ЛОПРИЛ БОСНАЛЕК Н \n Боснія і Герцоговина \n\U000025B6 СКОПРИЛ ПЛЮС  \n  Македонія", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)
#Лізиноприл з амлодипіном
        
    elif message.text == 'Лізиноприл + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="5 \U000026A1 5", callback_data="5Лізиноприл+ 5Амлодипіна")
        callback_button2 = types.InlineKeyboardButton(text="10 \U000026A1 5", callback_data="10Лізиноприл+ 5Амлодипіна")
        callback_button3 = types.InlineKeyboardButton(text="20 \U000026A1 5", callback_data="20Лізиноприл+ 5Амлодипіна")
        callback_button4 = types.InlineKeyboardButton(text="20 \U000026A1 10", callback_data="20Лізиноприл+ 10Амлодипіна")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F4D4 Лізиноприл')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію лізиноприла з амлодипіном містять препарати: \n\U000025B6 АМАПІН-Л  \n  Індія \n\U000025B6 АМЛІПІН  \n Франція \n\U000025B6 ЕКВАТОР  \n  Угорщина \n\U000025B6 КОМБІПРИЛ-КВ  \n  Україна   ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)
#Каптоприл
        
    elif message.text == '\U0001F4D4 Каптоприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Показання')
        user_no_hd1.row('\U0000274C Протипокази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати каптоприла')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати каптоприла')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Нaзад')
        bot.send_message(message.from_user.id, "Каптоприл \n\U0001F4CB Спосіб застосування: \n\U0001F6A9 Каптоприл приймати внутрішньо до, під час або після прийому їжі. \n\U0001F6A9 Слід приймати препарат регулярно, в один і той же час кожного дня. \n\U0001F6A9 Не слід приймати 2 дози каптоприлу одночасно.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати каптоприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Каптоприл', url='https://medhub.info/7d76f434')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="12,5 мг", callback_data="Каптоприл")
        callback_button2 = types.InlineKeyboardButton(text="25 мг ", callback_data="Каптоприл")
        callback_button3 = types.InlineKeyboardButton(text="50 мг", callback_data="Каптоприл")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F4D4 Каптоприл')
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною: каптоприл: \n\U000025B6  КАПТОПРИЛ  \n  Словенія + Україна ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування каптоприла: \n\U00002764 12,5 мг \n\U00002764 25 мг \n\U00002764 50 мг", reply_markup =user_no_hd1)


    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати каптоприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Каптоприл + Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: каптоприл.", reply_markup =user_no_hd1)

    elif message.text == 'Каптоприл + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="50 мг \U000026A1 12,5 мг", callback_data="50Каптоприл+ 12,5Гідрохлортіазид")
        callback_button2 = types.InlineKeyboardButton(text="50 мг \U000026A1 25 мг", callback_data="50Каптоприл+ 25Гідрохлортіазид")
        keyboard14.add(callback_button1, callback_button2)
        user_no_hd1.row('\U0001F4D4 Каптоприл')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію каптоприла з гідрохлортіазидом містять препарати: \n\U000025B6 КАПОТІАЗИД  \n Україна \n\U000025B6 КАПТОПРЕС-ДАРНИЦЯ  \n Україна \n\U000025B6 НОРМОПРЕС  \n  Україна", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)
#Еналаприл

    elif message.text == '\U0001F4D4 Еналаприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Показання')
        user_no_hd1.row('\U0000274C Протипокази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати еналаприла')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати еналаприла')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Нaзад')
        bot.send_message(message.from_user.id, "\n\U0001F4CB Спосіб застосування: (Інструкція – Еналаприл-Дарниця) \n\U0001F6A9 Таблетки приймати цілими, запиваючи невеликою кількістю води, незалежно від прийому їжі. \n\U0001F6A9 Приймати в один і той самий час кожного дня та не перевищувати призначену дозу. \n\U0001F6A9 Таблетку по 10 мг можна ділити.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати еналаприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Бердіприл', url='https://medhub.info/1634b24e')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5Еналаприл")
        callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5Еналаприл")
        callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10Еналаприл")
        callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20Еналаприл")
        callback_button5 = types.InlineKeyboardButton(text="Розчин", callback_data="РозчинЕналаприл")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5)
        user_no_hd1.row('\U0001F4D4 Еналаприл')
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною еналаприл: \n\U000025B6 БЕРЛІПРИЛ \n  Німеччина \n\U000025B6 ЕНА САНДОЗ  \n  Німеччина + Туреччина \n\U000025B6 ЕНАЛАПРИЛ  \n Україна \n\U000025B6 ЕНАЛАПРИЛ КРКА  \n  Словенія \n\U000025B6 ЕНАЛАПРИЛ-АСТРАФАРМ  \n  Україна \n\U000025B6 ЕНАЛАПРИЛ-ДAРНИЦЯ  \n  Україна \n\U000025B6 ЕНАЛАПРИЛ-ЗДОРОВ'Я  \n  Україна \n\U000025B6 ЕНАЛАПРИЛ-ТЕВА  \n  Польща \n\U000025B6 ЕНАЛОЗИД МОНО  \n  Україна \n\U000025B6 ЕНАМ  \n  Індія \n\U000025B6 ЕНАП  \n  Словенія \n\U000025B6 РЕНІТЕК  \n  Велика Британія + Нідерланди", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати еналаприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Еналаприл + Гідрохлортіазид')
        user_no_hd1.row('Еналаприл + Індапамід')
        user_no_hd1.row('Еналаприл + Лерканідипін')
        user_no_hd1.row('Еналаприл + Нітредипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: еналаприл.", reply_markup =user_no_hd1)

    elif message.text == 'Еналаприл + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="5 \U000026A1 12,5", callback_data="5Еналаприл+ 12,5Гідрохлортіазид")
        callback_button2 = types.InlineKeyboardButton(text="10 \U000026A1 12,5", callback_data="10Еналаприл+ 12,5Гідрохлортіазид")
        callback_button3 = types.InlineKeyboardButton(text="10 \U000026A1 25", callback_data="10Еналаприл+ 25Гідрохлортіазид")
        callback_button4 = types.InlineKeyboardButton(text="20 \U000026A1 12,5", callback_data="20Еналаприл+ 12,5Гідрохлортіазид")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F4D4 Еналаприл')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію еналаприла  з гідрохлортіазидом містять препарати: \n\U000025B6 БЕРЛІПРИЛ ПЛЮС \n Німеччина \n\U000025B6 ЕНАЛАПРИЛ /ГІДРОХЛОРОТІАЗИД  КРКА  \n  Словенія \n\U000025B6 ЕНАЛАПРИЛ Н-ТЕВА  \n  Угорщина \n\U000025B6 ЕНАЛАПРИЛ Н-ФАРМЕКС  \n  Україна \n\U000025B6 ЕНАЛАПРИЛ-Н-ЗДОРОВ'Я  \n  Україна \n\U000025B6 ЕНАЛОЗИД  \n   Україна \n\U000025B6 ЕНАП    \n  Словенія \n\U000025B6 ЕНАПРІЛ-Н  \n  Індія \n\U000025B6 КО-РЕНІТЕК  \n  Велика Британія + Нідерланди", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == 'Еналаприл + Індапамід':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="10 \U000026A1 2,5", callback_data="10Еналаприл+ Індапамід")
        callback_button2 = types.InlineKeyboardButton(text="20 \U000026A1 2,5", callback_data="20Еналаприл+ Індапамід")
        keyboard14.add(callback_button1, callback_button2)
        user_no_hd1.row('\U0001F4D4 Еналаприл')
        user_no_hd1.row('\U0001F4D4 Індапамід')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію еналаприла  з індапамідом містять препарати:  \n\U000025B6 ЕНЗИКС  \n Сербія   ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == 'Еналаприл + Лерканідипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="10 \U000026A1 10", callback_data="10Еналаприл+ 10Лерканідипін")
        callback_button2 = types.InlineKeyboardButton(text="20 \U000026A1 10", callback_data="20Еналаприл+ 10Лерканідипін")
        callback_button3 = types.InlineKeyboardButton(text="20 \U000026A1 20", callback_data="200Еналаприл+ 20Лерканідипін")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F4D4 Еналаприл')
        user_no_hd1.row('\U0001F4D4 Лерканідипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію еналаприла  з лерканідипіном містять препарати:  \n\U000025B6 ЕНАП Л КОМБІ  \n Словенія \n\U000025B6КОРІПРЕН \n Італія", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == 'Еналаприл + Нітредипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Еналаприл')
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, " \U00002705 Комбінацію еналаприла  з нітредипіном містять препарати:  \n\U000025B6 ЕНЕАС  \n  Іспанія     ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Комбінація еналаприла з нітредипіном (ЕНЕАС)  має таке дозування:   \n\U00002764 10 мг еналаприла і  20 мг нітредипіна ", reply_markup =user_no_hd1)
#Хіналаприл

    elif message.text == '\U0001F4D4 Хінаприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Показання')
        user_no_hd1.row('\U0000274C Протипокази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати хіналаприла')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати хіналаприла')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Нaзад')
        bot.send_message(message.from_user.id, "\n\U0001F4CB Спосіб застосування: (Інструкція – Аккупро) \n\U0001F6A9 Препарат Аккупро® можна застосовувати незалежно від прийому їжі; \n\U0001F6A9 Зазвичай початкова доза становить 10 мг квінаприлу на добу. Якщо ця доза не призводить до нормалізації тиску, доза може бути збільшена до 20 мг на добу. Цю дозу можна прийняти як одноразову або розділити на 2 прийоми (вранці та ввечері). \n\U0001F6A9 Збільшувати дозу протягом 3 тижнів небажано. \n\U0001F6A9 Зазвичай підтримуюча доза становить 10 мг квінаприлу на день, максимальна доза не повинна перевищувати 20 мг квінаприлу двічі на день (40 мг).", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати хіналаприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Аккупро', url='https://medhub.info/1fbc95e4')
        markup.add(btn_my_site)
        user_no_hd1.row('\U0001F4D4 Хінаприл')
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною хіналаприл: \n\U000025B6 АККУПРО  \n Німеччина", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Хіналаприл (квіналаприл) доступний в таких дозуваннях: :   \n\U00002764 5 мг,    \n\U00002764 10 мг,    \n\U00002764 20 мг,    \n\U00002764 40 мг.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати хіналаприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Квіналаприл + Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: хіналаприл (квіналаприл)", reply_markup =user_no_hd1)

        
    elif message.text == 'Квіналаприл + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Хінаприл')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію хіналаприла  з гідрохлортіазидом містять препарати:  \n\U000025B6 АККУЗИД \n Німеччина  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Комбінація хіналаприла і гідрохлортіазида (АККУЗИД)  має такі дозування:  \n\U00002764 10 мг  \n\U00002764 20 мг  ", reply_markup =user_no_hd1)
#Фозиноприл

    elif message.text == '\U0001F4D4 Фозиноприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Показання')
        user_no_hd1.row('\U0000274C Протипокази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати фозинаприл')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати фозинаприл')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Нaзад')
        bot.send_message(message.from_user.id, "\n\U0001F4CB Спосіб застосування: (Інструкція – Фозикард) \n\U0001F6A9 Початкова доза становить 10 мг на добу. \n\U0001F6A9 Звичайна підтримуюча доза – 20 мг на добу. \n\U0001F6A9 Звичайний діапазон дози становить від 10 до 40 мг на добу. \n\U0001F6A9 Можливе коригування дози через 4 тижні залежно від ефекту. \n\U0001F6A9 Дози, що перевищують 40 мг на добу, не призводять до додаткового зниження артеріального тиску. ", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати фозинаприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Фозикард', url='https://tabletki.ua/uk/Фозикард/')
        markup.add(btn_my_site)
        user_no_hd1.row('\U0001F4D4 Фозиноприл')
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною фозиноприл: \n\U000025B6 ФОЗИКАРД  \n Болгарія + Ісландія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Фозиноприл (фозикард) доступний в таких дозуваннях: :   \n\U00002764 5 мг,    \n\U00002764 10 мг,    \n\U00002764 20 мг.  ", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати фозинаприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Фозинаприл + Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: фозинаприл", reply_markup =user_no_hd1)

    elif message.text == 'Фозинаприл + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Фозиноприл')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію фозиналаприла  з гідрохлортіазидом містять препарати:  \n\U000025B6 ФОЗИКАРД Н  \n  Болгарія + Ісландія  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, " Комбінація фозинаприла і гідрохлортіазида (ФОЗИКАРД Н)  має такі дозування:  \n\U00002764 20 мг  фозинаприла і 12,5 мг гідрохлортіазида  ", reply_markup =user_no_hd1)


#Зофенаприл

    elif message.text == '\U0001F4D4 Зофеноприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Показання')
        user_no_hd1.row('\U0000274C Протипокази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати зофенаприл')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати зофенаприл')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Нaзад')
        bot.send_message(message.from_user.id, "Зофенаприл \n\U0001F4CB Спосіб застосування: (Інструкція – Зокардіс) \n\U0001F6A9 Препарат можна застосовувати незалежно від прийому їжі. \n\U0001F6A9 Лікування розпочинати з дози 15 мг  1 раз на добу та підвищувати дозу до оптимального артеріального тиску. \n\U0001F6A9 Зазвичай ефективна доза становить 30 мг на добу. \n\U0001F6A9 Максимальна доза становить 60 мг на добу, яку можна прийняти за 1 раз або розділити на 2 прийоми.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати зофенаприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Зокардіс', url='https://medhub.info/3a92e6cb')
        markup.add(btn_my_site)
        user_no_hd1.row('\U0001F4D4 Зофеноприл')
        user_no_hd1.row('\U0001F537 ІАПФ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною зофенаприл: \n\U000025B6 ЗОКАРДІС \n  Італія + Німеччина", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Зофенаприл (зокардіс) доступний в таких дозуваннях: :   \n\U00002764 7,5 мг    \n\U00002764 30 мг ", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати зофенаприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Зофенаприл + Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: зофенаприл", reply_markup =user_no_hd1)

    elif message.text == 'Зофенаприл + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Зофеноприл')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію зофеналаприла  з гідрохлортіазидом містять препарати:  \n\U000025B6 ЗОКАРДІС ПЛЮС  \n Італія + Німеччина", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Комбінація зофенаприла і гідрохлортіазида (ЗОКАРДІС ПЛЮС)  має такі дозування:  \n\U00002764 30 мг  зофенаприла і 12,5 мг гідрохлортіазида  ", reply_markup =user_no_hd1)


# Трандолаприл
        
    elif message.text == '\U0001F4D4 Трандолаприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Показання')
        user_no_hd1.row('\U0000274C Протипокази')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати трандолаприл')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Нaзад')
        bot.send_message(message.from_user.id, "Трандолаприл \n\U0001F4CB Спосіб застосування:  \n\U0001F6A9 Дорослим застосовувати 1 таблетку 1 раз на добу, вранці, незалежно від прийому їжі. \n\U0001F6A9 Таблетку слід ковтати цілою, не розжовуючи та запиваючи водою.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати трандолаприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Трандолаприл + Верапаміл')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: трандолаприл", reply_markup =user_no_hd1)

    elif message.text == 'Трандолаприл + Верапаміл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Трандолаприл')
        user_no_hd1.row('\U0001F4D4 Верапаміл')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію трандолаприла  з  верапамілом містять препарати:  \n\U000025B6 ТАРКА  \n  Німеччина", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, " Комбінація трандолаприла і верапаміла (ТАРКА)  має такі дозування:   \n\U00002764  трандолаприлу 2 мг та верапамілу 180 мг  \n\U00002764  трандолаприлу 4 мг та верапамілу  240 мг ", reply_markup =user_no_hd1)


#АРА ІІ
 
    elif message.text == '\U0001F536 АРА ІІ':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Лозартан')
        user_no_hd1.row('\U0001F4D4 Епросартан')
        user_no_hd1.row('\U0001F4D4 Валсартан')
        user_no_hd1.row('\U0001F4D4 Ірбесартан')
        user_no_hd1.row('\U0001F4D4 Кандесартан')
        user_no_hd1.row('\U0001F4D4 Телмісартан')
        user_no_hd1.row('\U0001F4D4 Олмесартан')
        user_no_hd1.row('\U0001F4D4 Азилсартан')
        user_no_hd1.row('\U00002196 Нaзaд')
        bot.send_message(message.from_user.id, "Вкажіть діючу речовину", reply_markup =user_no_hd1)

    elif message.text == '\U00002196 Назaд':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Лозартан')
        user_no_hd1.row('\U0001F4D4 Епросартан')
        user_no_hd1.row('\U0001F4D4 Валсартан')
        user_no_hd1.row('\U0001F4D4 Ірбесартан')
        user_no_hd1.row('\U0001F4D4 Кандесартан')
        user_no_hd1.row('\U0001F4D4 Телмісартан')
        user_no_hd1.row('\U0001F4D4 Олмесартан')
        user_no_hd1.row('\U0001F4D4 Азилсартан')
        user_no_hd1.row('\U00002196 Нaзaд')
        bot.send_message(message.from_user.id, "Вкажіть діючу речовину", reply_markup =user_no_hd1)


    elif message.text == '\U0001F4D4 Лозартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Покaзaння')
        user_no_hd1.row('\U0000274C Прoтипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати лозартан')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати лозартан')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Назaд')
        bot.send_message(message.from_user.id, "Лозартан \n\U0001F4CB Спосіб застосування: (Інструкція – Лоріста) \n\U0001F6A9 Зазвичай початкова і підтримуюча доза для більшості пацієнтів становить 50 мг препарату 1 раз на добу. \n\U0001F6A9 Максимальний антигіпертензивний ефект досягається на 3-6 тиждень від початку лікування. \n\U0001F6A9 Для деяких пацієнтів може виявитися сприятливішим підвищення дози препарату до 100 мг 1 раз на добу (вранці).\n\U0001F6A9 Застосування препарату не залежить від прийому їжі.", reply_markup =user_no_hd1)
    elif message.text == '\U00002705 Покaзaння':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C Прoтипoкази')
        user_no_hd1.row('\U0001F536 АРА ІІ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Покази до застосування антагоністів рецепторів ангіотензину ІІ: \n\U00002705 Артеріальна гіпертензія \n\U00002705 Профілактика серцево-судинних ускладнень у пацієнтів з : \n\U0001F6A9 ішемічною хворобою серця, \n\U0001F6A9 інсультом або захворювання периферичних артерій в анамнезі, \n\U0001F6A9 цукровим діабетом ІІ типу з діагностованним ураженням органів-мішеней.", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C Прoтипoкази':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Покaзaння')
        user_no_hd1.row('\U0001F536 АРА ІІ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипокази до застосування антагоністів рецепторів ангіотензину ІІ:\n\U0000274C Вагітність і лактація, або планування вагітності \n\U0000274C Двохсторонній стеноз нирок (або стеноз артерії єдиної нирки) \n\U0000274C Гіперкаліємія ", reply_markup =user_no_hd1)
         
    elif message.text == '\U0001F48A Монокомпонентні препарати лозартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Лоріста', url='https://medhub.info/ef04202e')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="12,5 мг", callback_data="12,5лозартан")
        callback_button2 = types.InlineKeyboardButton(text="25 мг ", callback_data="25лозартан")
        callback_button3 = types.InlineKeyboardButton(text="50 мг", callback_data="50лозартан")
        callback_button4 = types.InlineKeyboardButton(text="100 мг ", callback_data="100лозартан")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F4D4 Лозартан')
        user_no_hd1.row('\U0001F536 АРА ІІ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною лозартан:\n\U000025B6  АНГІЗАР  \n Індія \n\U000025B6  ВАЗОТЕНЗ  \n Болгарія + Індія \n\U000025B6  КЛОСАРТ  \n Україна \n\U000025B6  ЛОЗАП  \n Словенія \n\U000025B6  ЛОЗАРТАН КРКА  \n Китай + Словенія \n\U000025B6  ЛОЗАРТАН-ТЕВА  \n Угорщина \n\U000025B6  ЛОРІСТА  \n Німеччина + Словенія \n\U000025B6  ЛОТАР  \n  Македонія \n\U000025B6  ПРЕСАРТАН \n Індія \n\U000025B6  СЕНТОР  \n Польща + Угорщина \n\U000025B6  ТРОСАН  \n Індія", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати лозартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Лозартан + Гідрохлортіазид')
        user_no_hd1.row('Лозартан + Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: лозартан", reply_markup =user_no_hd1)

    elif message.text == 'Лозартан + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="50 \U000026A1 12,5", callback_data="50Лозартан + 12,5Гідрохлортіазид")
        callback_button2 = types.InlineKeyboardButton(text="100 \U000026A1 12,5", callback_data="100Лозартан + 12,5Гідрохлортіазид")
        callback_button3 = types.InlineKeyboardButton(text="100 \U000026A1 25", callback_data="100Лозартан + 25Гідрохлортіазид")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F4D4 Лозартан')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію лозартана з гідрохлортіазидом містять препарати:\n\U000025B6  АНГІЗАР ПЛЮС  \n Індія \n\U000025B6  ВАЗОТЕНЗ Н  \n Ісландія + Мальта \n\U000025B6  КО-СЕНТОР  \n Польща + Угорщина \n\U000025B6  ЛОЗАП 100 ПЛЮС  \n Польща \n\U000025B6  ЛОЗАП ПЛЮС  \n Чеська республіка \n\U000025B6  ЛОЗАРТАН /ГІДРОХЛОРОТІАЗИД  КРКА  \n Словенія \n\U000025B6  ЛОЗАРТАН ПЛЮС-ТЕВА  \n Угорщина \n\U000025B6  ЛОРІСТА Н  \n Словенія \n\U000025B6  ПРЕСАРТАН Н-50  \n Індія \n\U000025B6  САРТОКАД-Н  \n Індія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == 'Лозартан + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="50 \U000026A1 5", callback_data="50Лозартан + 5Амлодипін")
        callback_button2 = types.InlineKeyboardButton(text="50 \U000026A1 10", callback_data="50Лозартан + 10Амлодипін")
        callback_button3 = types.InlineKeyboardButton(text="100 \U000026A1 5", callback_data="100Лозартан + 5Амлодипін")
        callback_button4 = types.InlineKeyboardButton(text="100 \U000026A1 10", callback_data="100Лозартан + 10Амлодипін")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F4D4 Лозартан')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію лозартана з амлодипіном містять препарати: \n\U000025B6  АМОСАРТАН  \n  Південна Корея \n\U000025B6  ЛОРТЕНЗА  \n  Німеччина + Словенія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)
        
    elif message.text == '\U0001F4D4 Епросартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Теветен', url='https://tabletki.ua/uk/Теветен/')
        markup.add(btn_my_site)
        user_no_hd1.row('\U00002705 Покaзaння')
        user_no_hd1.row('\U0000274C Прoтипoкази')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Назaд')
        bot.send_message(message.from_user.id, "Епросартан \n\U0001F4CB Спосіб застосування: (Інструкція – Теветен) \n\U0001F6A9 Рекомендована доза для дорослих становить 600 мг епросартану 1 раз на день (вранці). \n\U0001F6A9 У більшості хворих максимальне зниження артеріального тиску досягається через 2-3 тижні лікування.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною епросартан:\n\U000025B6  ТЕВЕТЕН  \n  Німеччина + Франція", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Теветен має дозування: \n\U00002764 600 мг", reply_markup =user_no_hd1)

    elif message.text == '\U0001F4D4 Валсартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Покaзaння')
        user_no_hd1.row('\U0000274C Прoтипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати валсартан')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати валсартан')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Назaд')
        bot.send_message(message.from_user.id, "Валсартан \n\U0001F4CB Спосіб застосування: (Інструкція – Діован) \n\U0001F6A9 Препарат можна застосовувати незалежно від прийому їжі, таблетки слід запивати водою. \n\U0001F6A9 Рекомендована початкова доза валсартану становить 80 мг 1 раз на добу. \n\U0001F6A9 Антигіпертензивний ефект досягається протягом 2 тижнів, а максимальний ефект – протягом 4 тижнів. \n\U0001F6A9 Деяким пацієнтам із неадекватно контрольованим артеріальним тиском дозу можна підвищити до 160 мг та до максимальної – 320 мг.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати валсартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Діован', url='https://medhub.info/e1172691')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40валсартан")
        callback_button2 = types.InlineKeyboardButton(text="80 мг ", callback_data="80валсартан")
        callback_button3 = types.InlineKeyboardButton(text="160 мг", callback_data="160валсартан")
        callback_button4 = types.InlineKeyboardButton(text="320 мг ", callback_data="320валсартан")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F536 АРА ІІ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною: валсартан.\n\U000025B6  ВАЗАР  \n Болгарія + Мальта \n\U000025B6  ВАЛЕЗА  \n  Індія + Македонія \n\U000025B6  ВАЛМІСАР 160  \n Індія \n\U000025B6  ВАЛСАР  \n Індія \n\U000025B6  ВАЛСАРТАН  \n Індія \n\U000025B6  ВАЛСАРТАН КРКА  \n Словенія \n\U000025B6  ВАЛСАРТАН САНДОЗ  \n Іспанія + Словенія \n\U000025B6  ВАЛСАРТАН-РІХТЕР  \n Польща + Угорщина \n\U000025B6  ВАЛЬСАКОР  \n Словенія \n\U000025B6  ВАНАТЕКС  \n Польща \n\U000025B6  ДІОВАН  \n  Іспанія + Швейцарія \n\U000025B6  ДІОКОР СОЛО   \n Україна \n\U000025B6  ДІОСТАР  \n  Йорданія \n\U000025B6  КАРДОПАН-САНОВЕЛЬ  \n Туреччина \n\U000025B6  САКОРД  \n Болгарія \n\U000025B6  САРТОКАД-В  \n Індія  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати валсартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Валсартан + Гідрохлортіазид')
        user_no_hd1.row('Валсартан + Амлодипін')
        user_no_hd1.row('Валсартан + Гідрохлортіазид + Амлодипін')
        user_no_hd1.row('Валсартан + Саркубітрил')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: валсартан", reply_markup =user_no_hd1)

    elif message.text == 'Валсартан + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="80 \U000026A1 12,5", callback_data="80Валсартан + Гідрохлортіазид")
        callback_button2 = types.InlineKeyboardButton(text="160 \U000026A1 12,5", callback_data="160Валсартан + Гідрохлортіазид")
        callback_button3 = types.InlineKeyboardButton(text="160 \U000026A1 25", callback_data="160Валсартан + 25Гідрохлортіазид")
        callback_button4 = types.InlineKeyboardButton(text="320 \U000026A1 12,5", callback_data="320Валсартан + Гідрохлортіазид")
        callback_button5 = types.InlineKeyboardButton(text="320 \U000026A1 25", callback_data="320Валсартан + 25Гідрохлортіазид")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5)
        user_no_hd1.row('\U0001F4D4 Валсартан')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію валсартана з гідрохлоротіазидом містять препарати:\n\U000025B6  ВАЗАР Н  \n Болгарія + Мальта \n\U000025B6  ВАЛМІСАР H  \n Індія \n\U000025B6  ВАЛСАР-Н  \n Індія \n\U000025B6  ВАЛСАРТАН /ГІДРОХЛОРОТІАЗИД  КРКА  \n Словенія \n\U000025B6  ВАЛСАРТАН САНДОЗ КОМПОЗИТУМ  \n Італія + Словенія \n\U000025B6  ВАЛЬСАКОР H   \n Словенія \n\U000025B6  ВАНАТЕКС КОМБІ  \n Польща \n\U000025B6  ДІОКОР   \n Україна \n\U000025B6  КО-ДІОВАН  \n Італія + Швейцарія \n\U000025B6  КОРСАР Н  \n Україна \n\U000025B6  САКОРД Н  \n Болгарія \n\U000025B6  ТІАРА ДУО  \n Україна  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

        
    elif message.text == 'Валсартан + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="80 \U000026A1 5", callback_data="80Валсартан + Амлодипін")
        callback_button2 = types.InlineKeyboardButton(text="160 \U000026A1 5", callback_data="160Валсартан + Амлодипін")
        callback_button3 = types.InlineKeyboardButton(text="160 \U000026A1 10", callback_data="160Валсартан + 10Амлодипін")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F4D4 Валсартан')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію валсартана з амлодипіном містять препарати: \n\U000025B6  АМЛОСАРТАН  \n Україна \n\U000025B6  БІ-САКОРД  \n  Болгарія + Мальта \n\U000025B6  ВАЗАР А  \n  Болгарія + Хорватія \n\U000025B6  ВАЛЄМБІК \n Індія \n\U000025B6  ВАЛОДІП  \n Росія + Словенія \n\U000025B6  ВАЛСАР-АМ  \n Індія \n\U000025B6  ДІФОРС  \n Україна \n\U000025B6  ЕКСФОРЖ  \n Іспанія + Швейцарія \n\U000025B6  КОМБІСАРТ  \n Україна", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)


    elif message.text == 'Валсартан + Гідрохлортіазид + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="160 \U000026A1 12,5 \U000026A1 5", callback_data="160Валсартан + 12,5Гідрохлортіазид +А")
        callback_button2 = types.InlineKeyboardButton(text="160 \U000026A1 12,5 \U000026A1 10", callback_data="160Валсартан + 12,5Гідрохлортіазид +10А")
        callback_button3 = types.InlineKeyboardButton(text="160 \U000026A1 25 \U000026A1 5 ", callback_data="160Валсартан + 25Гідрохлортіазид + А")
        callback_button4 = types.InlineKeyboardButton(text="320 \U000026A1 25 \U000026A1 10", callback_data="320Валсартан + 25Гідрохлортіазид + 10А")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F4D4 Валсартан')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію валсартана з гідрохлоротіазидом і амлодипіном містять препарати:\n\U000025B6  ЕКСФОРЖ Н  \n Іспанія + Швейцарія \n\U000025B6  КОМБІСАРТ Н  \n Україна \n\U000025B6  ТІАРА ТРІО  \n Україна ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)
    elif message.text == 'Валсартан + Саркубітрил':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Валсартан')
        user_no_hd1.row('\U0001F536 АРА ІІ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію валсартана з саркубітрилом містять препарати: \n\U000025B6  ЮПЕРІО  \n  Італія + Сінгапур + Швейцарія  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Юперіо доступний в дозуванні:\n\U00002764 50 мг \n\U00002764 100 мг \n\U00002764 200 мг" , reply_markup =user_no_hd1)
        
    elif message.text == '\U0001F4D4 Ірбесартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Покaзaння')
        user_no_hd1.row('\U0000274C Прoтипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати ірбесартан')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати ірбесартан')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Назaд')
        bot.send_message(message.from_user.id, "Ірбесартан \n\U0001F4CB Спосіб застосування: (Інструкція – Апровель) \n\U0001F6A9 Звичайна рекомендована початкова і підтримуюча доза становить 150 мг один раз на добу незалежно від прийому їжі. \n\U0001F6A9 Однак слід зважити доцільність початку лікування із застосуванням дози 75 мг, пацієнтам, які знаходяться на гемодіалізі, а також літнім особам віком понад 75 років.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати ірбесартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Аровель', url='https://medhub.info/2b0f77b9')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="75 мг", callback_data="75ірбесартан")
        callback_button2 = types.InlineKeyboardButton(text="150 мг ", callback_data="150ірбесартан")
        callback_button3 = types.InlineKeyboardButton(text="300 мг", callback_data="300ірбесартан")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F4D4 Ірбесартан')
        user_no_hd1.row('\U0001F536 АРА ІІ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною: ірбесартан. \n\U000025B6  АПРОВЕЛЬ  \n  Франція \n\U000025B6  ІРБЕССО  \n  Греція \n\U000025B6  ІРБЕТАН  \n    Україна \n\U000025B6  ІСТАР  \n  Індія \n\U000025B6  КОНВЕРІУМ  \n    Кіпр \n\U000025B6  РОТАЗАР  \n  Туреччина \n\U000025B6  ФІРМАСТА  \n    Словенія", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати ірбесартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Ірбесартан + Гідрохлортіазид')
        user_no_hd1.row('Ірбесартан + Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: ірбесартан", reply_markup =user_no_hd1)

    elif message.text == 'Ірбесартан + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="150 \U000026A1 12,5", callback_data="150Ірбесартан + Гідрохлортіазид")
        callback_button2 = types.InlineKeyboardButton(text="300 \U000026A1 12,5", callback_data="300Ірбесартан + Гідрохлортіазид")
        callback_button3 = types.InlineKeyboardButton(text="300 \U000026A1 25", callback_data="300Ірбесартан + 25Гідрохлортіазид")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F4D4 Ірбесартан')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію ірбесартана з гідрохлортіазидом містять препарати:\n\U000025B6  ІРБАТАЛ-Н   \n  Індія \n\U000025B6  ІРБЕТАН-Н  \n  Україна \n\U000025B6  ІСТАР H  \n  Індія \n\U000025B6  КО-ІРБЕСАН  \n  Туреччина \n\U000025B6  КО-ІРБЕССО  \n  Греція \n\U000025B6  ФІРМАСТА Н  \n  Греція + Німеччина + Словенія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

        
    elif message.text == 'Ірбесартан + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Ірбесартан')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію ірбесартана з амлодипіном містить препарат: \n\U000025B6  АПРОВАСК  \n  Мексика ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Апроваск має наступні дозування: \n\U00002764 150 мг \U000026A1 5 мг \n\U00002764 150 мг \U000026A1 10 мг \n\U00002764 300 мг \U000026A1 5 мг ", reply_markup =user_no_hd1)
#кандесартан
    elif message.text == '\U0001F4D4 Кандесартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Покaзaння')
        user_no_hd1.row('\U0000274C Прoтипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати кандесартану')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати кандесартану')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Назaд')
        bot.send_message(message.from_user.id, "Кандесартан \n\U0001F4CB Спосіб застосування: (Інструкція – Атаканд) \n\U0001F6A9 Рекомендована початкова доза і звичайна підтримуюча доза препарату становить 8 мг 1 раз на добу. \n\U0001F6A9 У більшості випадків антигіпертензивний ефект досягається протягом 4 тижнів. \n\U0001F6A9 У деяких пацієнтів із недостатнім контролем артеріального тиску дозу можна збільшити до 16 мг 1 раз на добу і максимум до 32 мг 1 раз на добу.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати кандесартану':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Атаканд', url='https://medhub.info/c26c08da')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="4 мг", callback_data="4кандесартан")
        callback_button2 = types.InlineKeyboardButton(text="8 мг ", callback_data="8кандесартан")
        callback_button3 = types.InlineKeyboardButton(text="16 мг", callback_data="16кандесартан")
        callback_button4 = types.InlineKeyboardButton(text="32 мг ", callback_data="32кандесартан")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F4D4 Кандесартан')
        user_no_hd1.row('\U0001F536 АРА ІІ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, " \U00002705 Препарати з діючою речовиною: кандесартан. \n\U000025B6  АЙРА-САНОВЕЛЬ  \n Туреччина \n\U000025B6  АТАКАНД  \n Німеччина + Швеція \n\U000025B6  КАНДЕКОР  \n  Словенія \n\U000025B6  КАНДЕСАР  \n  Індія \n\U000025B6  КАНТАБ  \n Туреччина \n\U000025B6  КАРЗАП  \n  Мальта + Франція + Чеська республіка \n\U000025B6  КАСАРК  \n  Україна  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати кандесартану':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Кандесартан + Гідрохлортіазид')
        user_no_hd1.row('Кандесартан + Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: кандесартан", reply_markup =user_no_hd1)

    elif message.text == 'Кандесартан + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="8 \U000026A1 12,5", callback_data="8Кандесартан + Гідрохлортіазид")
        callback_button2 = types.InlineKeyboardButton(text="16 \U000026A1 12,5", callback_data="16Кандесартан + Гідрохлортіазид")
        callback_button3 = types.InlineKeyboardButton(text="32 \U000026A1 12,5", callback_data="32Кандесартан + Гідрохлортіазид")
        callback_button4 = types.InlineKeyboardButton(text="32 \U000026A1 25", callback_data="32Кандесартан + 25Гідрохлортіазид")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F4D4 Кандесартан')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію кандесартану з гідрохлоротіазидом містять препарати: \n\U000025B6  АТАКАНД ПЛЮС  \n  Німеччина + Швеція \n\U000025B6  КАНДЕКОР H 16  \n    Словенія \n\U000025B6  КАНТАБ ПЛЮС  \n  Туреччина \n\U000025B6  ХІЗАРТ-H  \n  Індія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

        
    elif message.text == 'Кандесартан + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="8 \U000026A1 5", callback_data="8Кандесартан + 5Амлодипіна")
        callback_button2 = types.InlineKeyboardButton(text="16 \U000026A1 5", callback_data="Кандесартан + 5Амлодипіна")
        callback_button3 = types.InlineKeyboardButton(text="16 \U000026A1 10", callback_data="Кандесартан + 10Амлодипіна")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F4D4 Кандесартан')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію кандесартана з амлодипіном містять препарати: \n\U000025B6  КАРЗАП-А  \n  Чеська республіка \n\U000025B6  САРТАПІН  \n  Німеччина + Польща ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)
        

    elif message.text == '\U0001F4D4 Телмісартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Покaзaння')
        user_no_hd1.row('\U0000274C Прoтипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати телмісартана')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати телмісартана')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Назaд')
        bot.send_message(message.from_user.id, "Телмісартан \n\U0001F4CB Спосіб застосування: (Інструкція – Мікардіс) \n\U0001F6A9 Звичайна ефективна доза телмісартану становить 40 мг на добу. \n\U0001F6A9 Деяким пацієнтам може бути достатня добова доза телмісартану 20 мг. \n\U0001F6A9 У разі якщо артеріальний тиск не знижується до бажаного значення, дозу телміcартану можна підвищити до 80 мг 1 раз на добу.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати телмісартана':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Хіпотел', url='https://tabletki.ua/uk/Хипотел/')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="20 мг", callback_data="20телмісартан")
        callback_button2 = types.InlineKeyboardButton(text="40 мг ", callback_data="40телмісартан")
        callback_button3 = types.InlineKeyboardButton(text="80 мг", callback_data="80телмісартан")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F4D4 Телмісартан')
        user_no_hd1.row('\U0001F536 АРА ІІ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною: телмісартан: \n\U000025B6  МІКАРДИС  \n Греція + Німеччина \n\U000025B6  ТЕЛМІЛАКС  \n  Іспанія \n\U000025B6  ТЕЛМІНОРМ-80  \n  Індія \n\U000025B6  ТЕЛМІСАРТАН-ТЕВА  \n  Індія + Угорщина \n\U000025B6  ТЕЛМІСТА  \n Польща + Словенія \n\U000025B6  ТЕЛНОР  \n  Індія \n\U000025B6  ТЕЛПРЕС  \n  Іспанія \n\U000025B6  ТЕЛСАРТАН  \n Індія \n\U000025B6  ТСАРТ  \n Індія \n\U000025B6  ХІПОТЕЛ  \n Україна ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати телмісартана':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Телмісартан + Гідрохлортіазид')
        user_no_hd1.row('Телмісартан + Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: телмісартан", reply_markup =user_no_hd1)
        
    elif message.text == 'Телмісартан + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="40 \U000026A1 12,5", callback_data="40Телмісартан + Гідрохлортіазид")
        callback_button2 = types.InlineKeyboardButton(text="80 \U000026A1 12,5", callback_data="80Телмісартан + Гідрохлортіазид")
        callback_button3 = types.InlineKeyboardButton(text="80 \U000026A1 25", callback_data="80Телмісартан + 25Гідрохлортіазид")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F4D4 Телмісартан')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію телмісартана з гідрохлоротіазидом містять препарати: \n\U000025B6  ІЗІКАРД Н  \n Індія \n\U000025B6  МІКАРДИСПЛЮС  \n Греція + Німеччина \n\U000025B6  ТЕЛМІЛАКС ПЛЮС  \n  Іспанія \n\U000025B6  ТЕЛПРЕС ПЛЮС  \n  Іспанія \n\U000025B6  ТЕЛСАРТАН-Н  \n Індія \n\U000025B6  ТЕЛСІ Н  \n Індія  \n\U000025B6  ТЕЛЬМІСТА H 40  \n  Словенія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

        
    elif message.text == 'Телмісартан + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="40 \U000026A1 5", callback_data="40Телмісартан+ 5Амлодипіна")
        callback_button2 = types.InlineKeyboardButton(text="40 \U000026A1 10", callback_data="40Телмісартан+ 10Амлодипіна")
        callback_button3 = types.InlineKeyboardButton(text="80 \U000026A1 5", callback_data="80Телмісартан+ 5Амлодипіна")
        callback_button4 = types.InlineKeyboardButton(text="80 \U000026A1 10", callback_data="80Телмісартан+ 10Амлодипіна")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F4D4 Телмісартан')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію телмісартан з амлодипіном містять препарати:\n\U000025B6  ІЗІКАРД A  \n Індія \n\U000025B6  ТЕЛДІПІН  \n Словенія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

#Олмесартан

    elif message.text == '\U0001F4D4 Олмесартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Покaзaння')
        user_no_hd1.row('\U0000274C Прoтипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати олмесартан')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати олмесартан')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Назaд')
        bot.send_message(message.from_user.id, "Олмесартан \n\U0001F4CB Спосіб застосування: (Інструкція – Кардосал) \n\U0001F6A9 Початкова добова доза олмесартану медоксомілу становить 10 мг 1 раз на добу.  Якщо зменшення артеріального тиску недостатнє, то дозу слід збільшити до 20 мг 1 раз на добу. Якщо є необхідність, дозу препарату можна збільшити до 40 мг 1 раз на добу (максимальна добова доза). \n\U0001F6A9 Антигіпертензивний ефект олмесартану медоксомілу спостерігається, як правило, протягом  2 тижнів після початку лікування, а максимальний ефект спостерігається через 8 тижнів після початку терапії. Це слід мати на увазі при розгляді зміни режиму дозування для будь-якого пацієнта. \n\U0001F6A9 З метою дотримання режиму дозування препарат рекомендується застосовувати приблизно в один і той самий час кожен день, з або без їжі, наприклад, під час сніданку. Таблетки слід запивати достатньою кількістю рідини (наприклад, 1 склянкою води). Таблетку не слід розжовувати.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати олмесартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Кардосал', url='https://medhub.info/6bfec020')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="10 мг", callback_data="10олмесартан")
        callback_button2 = types.InlineKeyboardButton(text="20 мг ", callback_data="20олмесартан")
        callback_button3 = types.InlineKeyboardButton(text="40 мг", callback_data="40олмесартан")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F4D4 Олмесартан')
        user_no_hd1.row('\U0001F536 АРА ІІ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною: олмесартан. \n\U000025B6  КАРДОСАЛ  \n  Німеччина \n\U000025B6  ОЛЕМБІК  \n  Індія \n\U000025B6  ОЛІМЕСТРА  \n  Словенія \n\U000025B6  ОЛМЕСАР  \n  Індія  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати олмесартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Олмесартан + Гідрохлортіазид')
        user_no_hd1.row('Олмесартан + Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: олмесартан", reply_markup =user_no_hd1)


    elif message.text == 'Олмесартан + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="20 \U000026A1 12,5", callback_data="20Олмесартан + Гідрохлортіазид")
        callback_button2 = types.InlineKeyboardButton(text="20 \U000026A1 25", callback_data="20Олмесартан + 25Гідрохлортіазид")
        callback_button3 = types.InlineKeyboardButton(text="40 \U000026A1 12,5", callback_data="40Олмесартан + Гідрохлортіазид")
        callback_button4 = types.InlineKeyboardButton(text="40 \U000026A1 25", callback_data="40Олмесартан + 25Гідрохлортіазид")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F4D4 Олмесартан')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію олмесартана з гідрохлоротіазидом містять препарати: \n\U000025B6  КАРДОСАЛ ПЛЮС \n Німеччина \n\U000025B6  ОЛЕМБІК-Н \n Індія \n\U000025B6  ОЛІМЕСТРА H \n  Німеччина + Словенія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

        
    elif message.text == 'Олмесартан + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Олмесартан')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію олмесартана з амлодипіном містить: \n\U000025B6  АТТЕНТО \n Німеччина   ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Аттенто має дозування \n\U00002764 20 мг \U000026A1 5 мг \n\U00002764 40 мг \U000026A1 5 мг \n\U00002764 40 мг \U000026A1 10 мг", reply_markup =user_no_hd1)

#Азилсартан
        
    elif message.text == '\U0001F4D4 Азилсартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Покaзaння')
        user_no_hd1.row('\U0000274C Прoтипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати азилсартан')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати азилсартан')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196 Назaд')
        bot.send_message(message.from_user.id, "Азилсартан \n\U0001F4CB Спосіб застосування: (Інструкція – Едарбі) \n\U0001F6A9 Рекомендована початкова доза становить 40 мг 1 раз на добу. \n\U0001F6A9 Для пацієнтів, у яких ця доза адекватно не контролює артеріальний тиск, дозу можна збільшити до максимальної рекомендованої дози 80 мг 1 раз на добу. \n\U0001F6A9 Стійкий антигіпертензивний ефект досягається протягом 2 тижнів лікування. \n\U0001F6A9 Максимальний ефект досягається через 4 тижні терапії препаратом.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати азилсартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Едарбі', url='https://medhub.info/236bfc89')
        markup.add(btn_my_site)
        user_no_hd1.row('\U0001F4D4 Азилсартан')
        user_no_hd1.row('\U0001F536 АРА ІІ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарат з діючою речовиною: азилсартан. \n\U000025B6  ЕДАРБІ  \n  Ірландія + Японія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Препарта Едарбі має такі дозування: \n\U00002764 20 мг \n\U00002764 40 мг \n\U00002764 80 мг ", reply_markup =user_no_hd1)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати азилсартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Азилсартан + Хлорталідон')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: азилсартан", reply_markup =user_no_hd1)

    elif message.text == 'Азилсартан + Хлорталідон':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Азилсартан')
        user_no_hd1.row('\U0001F4D4 Хлорталідон')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію азилсартан з хлорталідоном містить препарат: \n\U000025B6  ЕДАРБІКЛОР  \n  США + Японія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Едарбіклор має наступні дозування: \n\U00002764 40 мг \U000026A1 12,5 мг \n\U00002764 40 мг \U000026A1 25 мг ", reply_markup =user_no_hd1)

#Діуретики

    elif message.text == '\U0001F537 Діуретики':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="\U00002764 Тіазидні і тіазидоподібні", callback_data="Тіазидні")
        callback_button2 = types.InlineKeyboardButton(text="\U0001F49B Петльові", callback_data="Петльові")
        callback_button3 = types.InlineKeyboardButton(text="\U0001F49A Калійзберігаючі", callback_data="Калійзберігаючі")
        keyboard14.add(callback_button1)
        keyboard14.add(callback_button2)
        keyboard14.add(callback_button3)   
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U0001F4D4 Хлорталідон')
        user_no_hd1.row('\U0001F4D4 Індапамід')
        user_no_hd1.row('\U0001F4D4 Фуросемід')
        user_no_hd1.row('\U0001F4D4 Торасемід')
        user_no_hd1.row('\U0001F4D4 Спіронолактон')
        user_no_hd1.row('\U0001F4D4 Еплеренон')
        user_no_hd1.row('\U00002196 Нaзaд')
        bot.send_message(message.from_user.id, "Класифікація діуретиків:", reply_markup =keyboard14)
        bot.send_message(message.from_user.id, "Вкажіть діючу речовину", reply_markup =user_no_hd1)

    elif message.text == '\U00002196  Нaзад':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="\U00002764 Тіазидні і тіазидоподібні", callback_data="Тіазидні")
        callback_button2 = types.InlineKeyboardButton(text="\U0001F49B Петльові", callback_data="Петльові")
        callback_button3 = types.InlineKeyboardButton(text="\U0001F49A Калійзберігаючі", callback_data="Калійзберігаючі")
        keyboard14.add(callback_button1)
        keyboard14.add(callback_button2)
        keyboard14.add(callback_button3)   
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U0001F4D4 Хлорталідон')
        user_no_hd1.row('\U0001F4D4 Індапамід')
        user_no_hd1.row('\U0001F4D4 Фуросемід')
        user_no_hd1.row('\U0001F4D4 Торасемід')
        user_no_hd1.row('\U0001F4D4 Спіронолактон')
        user_no_hd1.row('\U0001F4D4 Еплеренон')
        user_no_hd1.row('\U00002196 Нaзaд')
        bot.send_message(message.from_user.id, "Класифікація діуретиків:", reply_markup =keyboard14)
        bot.send_message(message.from_user.id, "Вкажіть діючу речовину", reply_markup =user_no_hd1)


#Гідрохлортіазид
        
    elif message.text == '\U0001F4D4 Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705   Показання')
        user_no_hd1.row('\U0000274C   Протипокази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати гідрохлортіазида')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати гідрохлортіазида')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзад')
        bot.send_message(message.from_user.id, "Гідрохлортіазид \n\U0001F4CB Спосіб застосування: (Інструкція – Гідрохлортіазид) \n\U0001F6A9 Таблетки слід приймати після їжі. В окремих випадках ефективне застосування у початковій дозі 12,5  мг. При необхідності дозу підвищувати, але максимальна добова доза не має перевищувати 100 мг на добу. \n\U0001F6A9 Гіпотензивна дія гідрохлортіазиду проявляється протягом 3-4 днів, однак для досягнення оптимального ефекту може знадобитися до 3-4 тижнів. \n\U0001F6A9 У зв'язку зі збільшенням виведення калію та магнію під час лікування може бути необхідним проведення замісної терапії калієм (К+ < 3,0 ммоль/л) та магнієм.", reply_markup =user_no_hd1)

    elif message.text == '\U00002705   Показання':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C   Протипокази')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Показання для призначення гідрохлортіазиду: \n\U00002705 Набряковий синдром різного ґенезу \n\U00002705 Артеріальна гіпертензія  \n\U00002705 Симптоматичне лікування нейрогенного нецукрового діабету  \n\U00002705 Субкомпенсовані  форми  глаукоми; \n\U00002705 Профілактика утворення кальцієвих ниркових конкрементів.", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C   Протипокази':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705   Показання')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипоказання  для призначення гідрохлортіазиду: \n\U0000274C Підвищена чутливість до гідрохлортіазиду, інших сульфонамідів або до будь-якого компонента препарату \n\U0000274C Тяжка ниркова недостатність (кліренс креатиніну нижче 30 мл/хв) \n\U0000274C Механічна непрохідність сечовивідних шляхів \n\U0000274C Тяжка печінкова недостатність, печінкова енцефалопатія \n\U0000274C  Анурія \n\U0000274C  Подагра (тяжкі форми) \n\U0000274C  Гіповолемія \n\U0000274C  Декомпенсований цукровий діабет \n\U0000274C  Порушення водно-сольового обміну (гіпокаліємія, гіперкальціємія, гіпонатріємія)", reply_markup =user_no_hd1)
        
    elif message.text == '\U0001F48A Монокомпонентні препарати гідрохлортіазида':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Гідрохлортіазид', url='https://medhub.info/477a1fcc')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="25 мг", callback_data="25гідрохлортіазид")
        callback_button2 = types.InlineKeyboardButton(text="100 мг ", callback_data="100гідрохлортіазид")
        keyboard14.add(callback_button1, callback_button2)
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною гідрохлортіазид: \n\U000025B6  ГІДРОХЛОРТІАЗИД  \n Україна \n\U000025B6  ГІПОТІАЗИД  \n  Угорщина  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати гідрохлортіазида':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Гідрохлортіазид + Спіронолактон')
        user_no_hd1.row('Гідрохлортіазид + Тріамтерен')
        user_no_hd1.row('Раміприл + Гідрохлортіазид')
        user_no_hd1.row('Лізиноприл + Гідрохлортіазид')
        user_no_hd1.row('Каптоприл + Гідрохлортіазид')
        user_no_hd1.row('Еналаприл + Гідрохлортіазид')
        user_no_hd1.row('Квіналаприл + Гідрохлортіазид')
        user_no_hd1.row('Фозинаприл + Гідрохлортіазид')
        user_no_hd1.row('Зофенаприл + Гідрохлортіазид')
        user_no_hd1.row('Лозартан + Гідрохлортіазид')
        user_no_hd1.row('Валсартан + Гідрохлортіазид')
        user_no_hd1.row('Ірбесартан + Гідрохлортіазид')
        user_no_hd1.row('Кандесартан + Гідрохлортіазид')
        user_no_hd1.row('Телмісартан + Гідрохлортіазид')
        user_no_hd1.row('Олмесартан + Гідрохлортіазид')
        user_no_hd1.row('Бісопролол + Гідрохлортіазид')
        user_no_hd1.row('Небівалол + Гідрохлортіазид')
        user_no_hd1.row('Валсартан + Гідрохлортіазид + Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: гідрохлортіазид", reply_markup =user_no_hd1)

    elif message.text == 'Гідрохлортіазид + Спіронолактон':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U0001F4D4 Спіронолактон')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію гідрохлортіазида з спіронолактоном містить:\n\U000025B6  СПІНОЛ-Н  \n  Туреччина ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Препарати мають такі дозування: \n\U00002764 25 мг \U000026A1   25 мг \n\U00002764 50 мг \U000026A1 50 мг ", reply_markup =user_no_hd1)

    elif message.text == 'Гідрохлортіазид + Тріамтерен':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію гідрохлортіазида з тріамтереном містить: \n\U000025B6  ТРИАМПУР КОМПОЗИТУМ  \n  Хорватія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Препарат має дозування гідрохлортіазида і тріамтерена відповідно: \n\U00002764 12,5 мг \U000026A1 250 мг ", reply_markup =user_no_hd1)
#Хлорталідон
        
    elif message.text == '\U0001F4D4 Хлорталідон':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Показaння')
        user_no_hd1.row('\U0000274C Протипокaзи')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати хлорталідона')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати хлорталідона')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзад')
        bot.send_message(message.from_user.id, "Хлорталідон \n\U0001F4CB Спосіб застосування: (Інструкція – Дихлор) \n\U0001F6A9 Для лікування гіпертензії рекомендована початкова доза хлорталідону для дорослих 25 мг щодня. Цього достатньо, щоб викликати максимальний гіпотензивний ефект у більшості хворих. \n\U0001F6A9 Якщо зниження артеріального тиску не відбувається при дозі 25 мг/добу, її можна збільшити до 50 мг/день. \n\U0001F6A9 Якщо застосовують додаткову антигіпертензивну терапію, підвищення дози препарату понад 50 мг збільшує метаболічні ускладнення і рідко має терапевтичний ефект.", reply_markup =user_no_hd1)

    elif message.text == '\U00002705 Показaння':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C Протипокaзи')
        user_no_hd1.row('\U0001F4D4 Хлорталідон')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Показання для призначення хлорталідону:\n\U00002705 Лікування артеріальної гіпертензії \n\U00002705 Лікування хронічної серцевої недостатності (ФК  II або III NYHA) \n\U00002705 Лікування набряків. ", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C Протипокaзи':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Показaння')
        user_no_hd1.row('\U0001F4D4 Хлорталідон')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипоказання  для призначення хлорталідону:\n\U0000274C Гіперчутливість до хлорталідону або інших лікарських засобів, отриманих із сульфаніламідів \n\U0000274C Анурія  \n\U0000274C Тяжка печінкова або ниркова недостатність (кліренс креатиніну <30 мл/хв)  \n\U0000274C Рефрактерна гіпокаліємія, гіперкальціємія та гіпонатріємія  \n\U0000274C Симптоматична гіперурикемія (подагра або сечокислі камені в анамнезі) \n\U0000274C Гіпертензія під час вагітності \n\U0000274C Нелікована хвороба Аддісона  \n\U0000274C Супутня терапія літієм \n\U0000274C Дитячий вік \n\U0000274C Вагітність, період годування груддю  \n\U0000274C Інтоксикація препаратами серцевих глікозидів ", reply_markup =user_no_hd1)
        

    elif message.text == '\U0001F48A Монокомпонентні препарати хлорталідона':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Дихлор', url='https://medhub.info/16781374')
        markup.add(btn_my_site)
        user_no_hd1.row('\U0001F4D4 Хлорталідон')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарат з діючою речовиною хлорталідон: \n\U000025B6  ДИХЛОР  \n  Індія  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дихлор має наступні дозування:\n\U00002764 25 мг \n\U00002764 50 мг ", reply_markup =user_no_hd1)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати хлорталідона':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Азилсартан + Хлорталідон')
        user_no_hd1.row('Атенолол + Хлорталідон')
        user_no_hd1.row('Атенолол + Ніфедипін + Хлорталідон')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: хлорталідон", reply_markup =user_no_hd1)
#Індапамід      
        
    elif message.text == '\U0001F4D4 Індапамід':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Показaння')
        user_no_hd1.row('\U0000274C  Протипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати індапаміда')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати індапаміда')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзад')
        bot.send_message(message.from_user.id, "Індапамід \n\U0001F4CB Спосіб застосування: (Інструкція – Арифон) \n\U0001F6A9 Дозування - 1 таблетка на добу, бажано вранці. Таблетку слід  ковтати цілою, не розжовуючи, запиваючи водою. \n\U0001F6A9 Застосування більш високих доз препарату (2,5 мг) не призводить до збільшення антигіпертензивного ефекту, але діуретичний ефект зростає.", reply_markup =user_no_hd1)

    elif message.text == '\U00002705  Показaння':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C  Протипoкази')
        user_no_hd1.row('\U0001F4D4 Індапамід')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Показання для призначення індапаміду: \n\U00002705 Есенціальна гіпертензія у дорослих.", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C  Протипoкази':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Показaння')
        user_no_hd1.row('\U0001F4D4 Індапамід')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипоказання  для призначення індапаміду: \n\U0000274C Підвищена чутливість до діючої речовини, інших сульфонамідів \n\U0000274C Тяжка ниркова недостатнiсть \n\U0000274C Печінкова енцефалопатія або тяжке порушення функції печiнки; \n\U0000274C Гіпокаліємія. ", reply_markup =user_no_hd1)
        

    elif message.text == '\U0001F48A Монокомпонентні препарати індапаміда':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Арифон', url='https://medhub.info/2fb1f9c8')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="1,25 мг", callback_data="125індапамід")
        callback_button2 = types.InlineKeyboardButton(text="1,5 мг ", callback_data="15індапамід")
        callback_button3 = types.InlineKeyboardButton(text="2,5 мг", callback_data="25індапамід")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною індапамід:  \n\U000025B6  АРИФОН  \n Франція \n\U000025B6  АРИФОН РЕТАРД  \n Ірландія + Польща + Франція \n\U000025B6  ВАЗОПАМІД  \n Румунія \n\U000025B6  ІНДАБРЮ  \n Бельгія + Португалія \n\U000025B6  ІНДАП  \n Чеська республіка \n\U000025B6  ІНДАПАМІД  \n Сербія \n\U000025B6  ІНДАПАМІД-АСТРАФАРМ  \n Україна \n\U000025B6  ІНДАПАМІД-ТЕВА \n Німеччина \n\U000025B6  ІНДАПЕН  \n Польща \n\U000025B6  ІНДОПРЕС  \n Україна \n\U000025B6  ІПАМІД  \n Україна \n\U000025B6  РАВЕЛ \n  Словенія \n\U000025B6  СОФТЕНЗИФ  \n Болгарія \n\U000025B6  ХЕМОПАМІД РЕТАРД  \n Сербія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати індапаміда':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Периндоприл + Індапамід')
        user_no_hd1.row('Еналаприл + Індапамід')
        user_no_hd1.row('Амлодипін + Індапамід')
        user_no_hd1.row('Периндоприл + Індапамід + Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: індапамід", reply_markup =user_no_hd1)

#Фуросемід
        
    elif message.text == '\U0001F4D4 Фуросемід':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Покaзaння')
        user_no_hd1.row('\U0000274C  Прoтипокази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати фуросеміда')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати фуросеміда')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзад')
        bot.send_message(message.from_user.id, "Фуросемід \n\U0001F4CB Спосіб застосування: (Таблетки) \n\U0001F6A9 Фуросемід приймати внутрішньо зазвичай під час їди або натщесерце. \n\U0001F6A9 Режим дозування встановлює лікар індивідуально відповідно до терапевтичної відповіді пацієнта, застосовуючи мінімальну ефективну дозу. Можна застосовувати 1 раз на добу або через день. \n\U0001F6A9 Рекомендована початкова однократна доза для дорослих становить 40 мг.. При легких випадках доза 40 мг через день може бути достатньою. У випадках резистентних набряків звичайна добова доза становить 80 мг і більше, один або два рази на добу, або застосовується при необхідності. При важких станах, спричинених набряками, може бути необхідне поступове збільшення дози до 600 мг на добу. \n\U0001F6A9 Максимальна добова доза фуросеміду не повинна перевищувати 1500 мг. \n\U0001F4CB Спосіб застосування: (Розчин) \n\U0001F6A9 Фуросемід призначають внутрішньовенно лише у тому випадку, коли прийом внутрішньо є недоцільним або неефективним (наприклад при порушенні всмоктування у кишечнику) або у разі необхідності швидкого ефекту. У разі застосування внутрішньовенної терапії рекомендується якомога швидший перехід до терапії лікарським засобом для перорального застосування. \n\U0001F6A9 У тих випадках, коли безперервна інфузія фуросеміду є недоцільною для подальшого лікування після введення однієї або кількох болюсних доз, віддається перевага подальшій схемі лікування з призначенням низьких доз, що вводяться через короткі часові інтервали (приблизно 4 години), порівняно з більшими болюсними дозами, що вводяться через більші проміжки часу.", reply_markup =user_no_hd1)
    elif message.text == '\U00002705  Покaзaння':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C  Прoтипокази')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Показання для призначення петльових діуретиків: \n\U00002705 Набряки при хронічній застійній серцевій недостатності \n\U00002705 Набряки при гострій застійній серцевій недостатності. \n\U00002705 Набряки при хронічній нирковій недостатності. \n\U00002705 Гостра ниркова недостатність, у тому числі  у вагітних або під час пологів. \n\U00002705 Набряки при захворюваннях печінки \n\U00002705 Гіпертензивний криз . \n\U00002705 Підтримка форсованого діурезу.", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C  Прoтипокази':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Покaзaння')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипоказання  для призначення петльових діуретиків: \n\U0000274C Гіперчутливість до фуросеміду або до інших компонентів, що входять до складу препарату. \n\U0000274C У пацієнтів з алергією на сульфонаміди (наприклад на сульфонамідні антибіотики або сульфонілсечовину) може виявитися перехресна чутливість до фуросеміду. \n\U0000274C Гіповолемія або зневоднення організму. \n\U0000274C Ниркова недостатність у вигляді анурії, якщо не спостерігається терапевтична відповідь на фуросемід. \n\U0000274C Ниркова недостатність внаслідок отруєння нефротоксичними або гепатотоксичними препаратами. \n\U0000274C Тяжка гіпокаліємія. \n\U0000274C Тяжка гіпонатріємія. \n\U0000274C Прекоматозний або коматозний стани, що асоціюються з печінковою енцефалопатією. ", reply_markup =user_no_hd1)
        

    elif message.text == '\U0001F48A Монокомпонентні препарати фуросеміда':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Фуросемід', url='https://medhub.info/cbcd706c')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40фуросемід")
        callback_button2 = types.InlineKeyboardButton(text="Розчин", callback_data="Розчин фуросемід")
        keyboard14.add(callback_button1, callback_button2)
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною фуросемід:\n\U000025B6  ЛАЗИКС  \n Індія \n\U000025B6  ЛАЗИКС НЕО  \n Румунія \n\U000025B6  ФУРОСЕМІД  \n Україна \n\U000025B6  ФУРОСЕМІД СОФАРМА  \n Болгарія + Україна \n\U000025B6  ФУРОСЕМІД-ДАРНИЦЯ  \n Україна  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати фуросеміда':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Фуросемід + Спіронолактон')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: фуросемід", reply_markup =user_no_hd1)

    elif message.text == 'Фуросемід + Спіронолактон':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Фуросемід')
        user_no_hd1.row('\U0001F4D4 Спіронолактон')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію фуросеміда з спіронолактоном містить препарат:\n\U000025B6  ФУРОСТІМ  \n  Румунія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Фуростім має дозування фуросеміду і споронолактону відповідно: \n\U00002764 20 мг  \U000026A1 50мг ", reply_markup =user_no_hd1)
#Торасемід
        

    elif message.text == '\U0001F4D4 Торасемід':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Трифас', url='https://medhub.info/94f7bf53')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5торасемід")
        callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5торасемід")
        callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10торасемід")
        callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20торасемід")
        callback_button5 = types.InlineKeyboardButton(text="50 мг", callback_data="50торасемід")
        callback_button6 = types.InlineKeyboardButton(text="100 мг ", callback_data="100торасемід")
        callback_button7 = types.InlineKeyboardButton(text="200 мг", callback_data="200торасемід")
        callback_button8 = types.InlineKeyboardButton(text="2 мл 0,5%", callback_data="2млторасемід")
        callback_button9 = types.InlineKeyboardButton(text="4 мл 0,5%", callback_data="4млторасемід")
        callback_button10 = types.InlineKeyboardButton(text="20 мл 1%", callback_data="20млторасемід")
        keyboard14.add(callback_button1, callback_button2)
        keyboard14.add(callback_button3, callback_button4)
        keyboard14.add(callback_button5, callback_button6)
        keyboard14.add(callback_button7, callback_button8)
        keyboard14.add(callback_button9, callback_button10)
        user_no_hd1.row('\U00002705  Покaзaння')
        user_no_hd1.row('\U0000274C  Прoтипокази')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзад')
        bot.send_message(message.from_user.id, "Торасемід \n\U0001F4CB Спосіб застосування: (Брітомар) \n\U0001F6A9 Загальна початкова доза становить 5 мг 1 раз на добу. \n\U0001F6A9 Якщо такий режим дозування не забезпечує необхідного зниження артеріального тиску через 4-6 тижнів, дозування необхідно збільшити до 10 мг 1 раз на добу. \n\U0001F6A9 Таблетки слід приймати, не розжовуючи та не подрібнюючи, незалежно від прийому їжі та від часу доби, запиваючи невеликою кількістю рідини.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною торасемід: \n\U000025B6 БРІТОМАР  \n Іспанія \n\U000025B6 ТОР-ЛУП  \n Індія \n\U000025B6 ТОРАДІВ  \n Україна \n\U000025B6 ТОРАРЕН  \n Україна \n\U000025B6 ТОРАСЕМІД САНДОЗ  \n  Німеччина + Польща \n\U000025B6 ТОРАСЕМІД-ДАРНИЦЯ  \n Україна \n\U000025B6 ТОРАСЕМІД-ТЕВА  \n Хорватія \n\U000025B6 ТОРІКАРД  \n Індія \n\U000025B6 ТОРСИД  \n Україна \n\U000025B6 ТРИГРИМ  \n Польща \n\U000025B6 ТРИФАС  \n Німеччина \n\U000025B6 ТРИФАС АМПУЛИ  \n Італія \n\U000025B6 ТРИФАС СOR  \n Німеччина ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)


#Спіронолактон

    elif message.text == '\U0001F4D4 Спіронолактон':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Пoкaзання')
        user_no_hd1.row('\U0000274C  Прoтипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати спіронолакторна')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати спіронолакторна')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзад')
        bot.send_message(message.from_user.id, "Спіронолактон \n\U0001F4CB Спосіб застосування: (Спіронолактон-Сандоз) \n\U0001F6A9 Початкова добова доза, що призначається за 1 або 2 прийоми, становить 50-100 мг, її слід приймати у комбінації з іншими антигіпертензивними препаратами. \n\U0001F6A9 Терапію продовжують протягом щонайменше двох тижнів, оскільки до кінця цього періоду досягається максимальний антигіпертензивний ефект. Потім величину дози слід корегувати індивідуально, залежно від досягнутого ефекту.", reply_markup =user_no_hd1)

    elif message.text == '\U00002705  Пoкaзання':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C  Прoтипoкази')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Показання для призначення калійзберігаючих діуретиків: \n\U00002705 Застійна серцева недостатність у пацієнтів, які не відповідають на лікування іншими діуретинами, або у разі необхідності потенціювання їх ефектів.  \n\U00002705 Есенціальна артеріальна гіпертензія, головним чином у разі гіпокаліємії (зазвичай у комбінації з іншими антигіпертензивними препаратами). \n\U00002705 Цироз печінки, що супроводжується набряками та/або асцитом. \n\U00002705 Первинний гіперальдостеронізм. \n\U00002705 Набряки, зумовлені нефротичним синдромом. \n\U00002705 Гіпокаліємія, у разі неможливості отримання іншої терапії. ", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C  Прoтипoкази':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Пoкaзання')
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипоказання  для призначення калійзберігаючих діуретиків: \n\U0000274C Гіперчутливість  до діючої речовини або будь-яких інших допоміжних речовин. \n\U0000274C  Застосовування в комбінації з мітотаном, оскільки він може блокувати дію мітотану.  \n\U0000274C Анурія, гостра ниркова недостатність, виражене порушення азотовидільної функції нирок (швидкість клубочкової фільтрації <10 мл/хв). \n\U0000274C Тяжка ниркова недостатність, що супроводжується олігурією або анурією (кліренс креатиніну нижче 30 мл/хв на 1,73 м2 поверхні тіла і/або креатинін сироватки крові вище 1,8 мг/дл). \n\U0000274C Гіперкаліємія (показники рівня калію в крові > 5,0 ммоль/л) \n\U0000274C Гіпонатріємія. \n\U0000274C Хвороба Аддісона. \n\U0000274C Гіповолемія або зневоднення. \n\U0000274C Одночасне застосування еплеренону або інших калійзберігаючих діуретинів \n\U0000274C Вагітність та годування груддю \n\U0000274C Інгібітори АПФ або блокатори рецепторів AT1 у комбінації ", reply_markup =user_no_hd1)
        

    elif message.text == '\U0001F48A Монокомпонентні препарати спіронолакторна':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Спіронолактон', url='https://medhub.info/b5c96e07')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="25 мг", callback_data="25спіронолакторн")
        callback_button2 = types.InlineKeyboardButton(text="50 мг ", callback_data="50спіронолакторн")
        callback_button3 = types.InlineKeyboardButton(text="100 мг", callback_data="100спіронолакторн")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною  спіронолактон:\n\U000025B6 ВЕРОШПІРОН  \n  Польща + Угорщина \n\U000025B6 СПІЛАКТОН  \n Туреччина \n\U000025B6 СПІРОНОЛАКТОН САНДОЗ  \n Німеччина \n\U000025B6 СПІРОНОЛАКТОН-ДАРНИЦЯ  \n Україна  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати спіронолакторна':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Фуросемід + Спіронолактон')
        user_no_hd1.row('Гідрохлортіазид + Спіронолактон')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: спіронолактон", reply_markup =user_no_hd1)

#Еплеренон
        

    elif message.text == '\U0001F4D4 Еплеренон':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Інспра', url='https://medhub.info/14062473')
        markup.add(btn_my_site)
        user_no_hd1.row('\U00002705  Пoкaзання')
        user_no_hd1.row('\U0000274C  Прoтипoкази')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзад')
        bot.send_message(message.from_user.id, "Еплеренон \n\U0001F4CB Спосіб застосування: (Інспра) \n\U0001F6A9 Для індивідуального підбору дозування препарат існує у дозах 25 мг та 50 мг. \n\U0001F6A9 Максимальна добова доза препарату становить 50 мг на добу. \n\U0001F6A9 Еплеренон можна застосовувати як з їжею, так і незалежно від прийому їжі.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною еплеренон:\n\U000025B6 ДЕКРИЗ  \n Польща \n\U000025B6 ЕПЛЕПРЕС  \n Україна \n\U000025B6 ЕПЛЕРЕНОН СТАДА  \n Іспанія + Німеччина \n\U000025B6 ЕПЛЕТОР  \n Іспанія + Україна \n\U000025B6 ЕПНОН   \n Індія \n\U000025B6 ІНСПРА  \n США + Франція \n\U000025B6 РЕНІАЛЬ  \n Україна  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Всі препарати мають дозування: \n\U00002764 25 мг  \n\U00002764 50 мг ", reply_markup =user_no_hd1)


#АК

        
    elif message.text == '\U0001F536 БКК':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="\U00002764 Дигідропіридинові", callback_data="БКК судини")
        callback_button2 = types.InlineKeyboardButton(text="\U0001F49B Не дигідропіридинові", callback_data="БКК серце")
        keyboard14.add(callback_button1)
        keyboard14.add(callback_button2)     
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U0001F4D4 Лацидипін')
        user_no_hd1.row('\U0001F4D4 Лерканідипін')
        user_no_hd1.row('\U0001F4D4 Верапаміл')
        user_no_hd1.row('\U0001F4D4 Дилтіазем')
        user_no_hd1.row('\U00002196 Нaзaд')
        bot.send_message(message.from_user.id, "Класи блокаторів кальцієвих каналів:", reply_markup =keyboard14)
        bot.send_message(message.from_user.id, "Вкажіть діючу речовину", reply_markup =user_no_hd1)
        
    elif message.text == '\U00002196  Назaд':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="\U00002764 Дигідропіридинові", callback_data="БКК судини")
        callback_button2 = types.InlineKeyboardButton(text="\U0001F49B Не дигідропіридинові", callback_data="БКК серце")
        keyboard14.add(callback_button1)
        keyboard14.add(callback_button2)     
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U0001F4D4 Лацидипін')
        user_no_hd1.row('\U0001F4D4 Лерканідипін')
        user_no_hd1.row('\U0001F4D4 Верапаміл')
        user_no_hd1.row('\U0001F4D4 Дилтіазем')
        user_no_hd1.row('\U00002196 Нaзaд')
        bot.send_message(message.from_user.id, "Класи блокаторів кальцієвих каналів:", reply_markup =keyboard14)
        bot.send_message(message.from_user.id, "Вкажіть діючу речовину", reply_markup =user_no_hd1)
        

        
    elif message.text == '\U0001F4D4 Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Показання')
        user_no_hd1.row('\U0000274C  Протипокази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати амлодипіна')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати амлодипіна')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Назaд')
        bot.send_message(message.from_user.id, "Амлодипін \n\U0001F4CB Спосіб застосування: (Амлодипін) \n\U0001F6A9 Для лікування артеріальної гіпертензії та стенокардії звичайна початкова доза препарату становить 5 мг 1 раз на добу. \n\U0001F6A9 Залежно від реакції пацієнта на терапію дозу можна збільшити до максимальної дози, що становить 10 мг на 1 раз на добу.", reply_markup =user_no_hd1)

    elif message.text == '\U00002705  Показання':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C  Протипокази')
        user_no_hd1.row('\U0001F536 БКК')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Покази для призначення дигідропіридинових блокаторів кальцієвих каналів: \n\U00002705 Артеріальна гіпертензія \n\U00002705 Хронічна стабільна стенокардія \n\U00002705 Вазоспастична стенокардія (стенокардія Принцметала) ", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C  Протипокази':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Показання')
        user_no_hd1.row('\U0001F536 БКК')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипокази до дигідропіридинових блокаторів кальцієвих каналів: \n\U0000274C Артеріальна гіпотензія тяжкого ступеня \n\U0000274C Шок (включаючи кардіогенний шок) \n\U0000274C Обструкція вивідного тракту лівого шлуночка (наприклад стеноз аорти тяжкого ступеня) \n\U0000274C Гемодинамічно нестабільна серцева недостатність після гострого інфаркту міокарда \n\U0000274C Відносними протипоказами є попередній набряк гомілок, тахікардія, і СН зі зниженою ФВ (ІІІ-ІV ФК) ", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати амлодипіна':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Норваск', url='https://medhub.info/455d505b')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5амлодипін")
        callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5амлодипін")
        callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10амлодипін")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F536 БКК')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною амлодипін:\n\U000025B6 АГЕН  \n Чеська республіка \n\U000025B6 АЗОМЕКС  \n Індія \n\U000025B6 АЛАДИН  \n  Україна \n\U000025B6 АМЛОВАС  \n Індія \n\U000025B6 АМЛОГЕН   \n Індія \n\U000025B6 АМЛОДИЛ БОСНАЛЕК  \n Боснія і Герцоговина \n\U000025B6 АМЛОДИПІН  \n Україна \n\U000025B6 АМЛОДИПІН КРКА  \n  Словенія \n\U000025B6 АМЛОДИПІН САНДОЗ  \n Словенія + Туреччина \n\U000025B6 АМЛОДИПІН-АСТРАФАРМ  \n  Україна \n\U000025B6 АМЛОДИПІН-ДАРНИЦЯ  \n Україна \n\U000025B6 АМЛОДИПІН-ЗДОРОВ'Я  \n Україна \n\U000025B6 АМЛОДИПІН-КВ  \n Україна \n\U000025B6 АМЛОДИПІН-ТЕВА  \n Угорщина \n\U000025B6 АМЛОДИПІН-ФАРМАК  \n Україна \n\U000025B6 АМЛОДИПІН-ФІТОФАРМ  \n Україна \n\U000025B6 АМЛОЦИМ   \n Індія + Швейцарія \n\U000025B6 ВАЗОТАЛ  \n Боснія і Герцоговина + Сербія \n\U000025B6 ЕМЛОДИН  \n Угорщина \n\U000025B6 ЕСЛО   \n Індія \n\U000025B6 НОРВАСК  \n Німеччина \n\U000025B6 НОРМОДИПІН  \n Угорщина \n\U000025B6 СЕМЛОПІН  \n Україна \n\U000025B6 СТАМЛО  \n Індія  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати амлодипіна':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Амлодипін + Індапамід')
        user_no_hd1.row('Периндоприл + Амлодипін')
        user_no_hd1.row('Раміприл + Амлодипін')
        user_no_hd1.row('Лізиноприл + Амлодипін')
        user_no_hd1.row('Валсартан + Амлодипін')
        user_no_hd1.row('Лозартан + Амлодипін')
        user_no_hd1.row('Ірбесартан + Амлодипін')
        user_no_hd1.row('Кандесартан + Амлодипін')
        user_no_hd1.row('Телмісартан + Амлодипін')
        user_no_hd1.row('Олмесартан + Амлодипін')
        user_no_hd1.row('Бісопролол + Амлодипін')
        user_no_hd1.row('Атенолол + Амлодипін')
        user_no_hd1.row('Периндоприл + Індапамід + Амлодипін')
        user_no_hd1.row('Валсартан + Гідрохлортіазид + Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: амлодипін", reply_markup =user_no_hd1)

    elif message.text == 'Амлодипін + Індапамід':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U0001F4D4 Індапамід')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію амлодипіна з індапамідом містять препарати:\n\U000025B6 АРИФАМ \n Ірландія + Франція ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування Арифам:  \n\U00002764 5 мг \U000026A1 1,5 мг  \n\U00002764 10 мг \U000026A1 1,5 мг", reply_markup =user_no_hd1)


    elif message.text == '\U0001F4D4 Лацидипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Лаципіл', url='https://tabletki.ua/uk/Лаципил/')
        markup.add(btn_my_site)
        user_no_hd1.row('\U00002705  Показання')
        user_no_hd1.row('\U0000274C  Протипокази')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Назaд')
        bot.send_message(message.from_user.id, "Лацидипін \n\U0001F4CB Спосіб застосування: (Лаципіл) \n\U0001F6A9 Початкова доза для дорослих – 2 мг 1 раз на добу, яка приймається кожного дня, в один і той самий час, бажано вранці. \n\U0001F6A9Дозу можна збільшити до 4 мг на добу, при необхідності – до 6 мг після закінчення часу необхідного для досягнення повного фармакологічного ефекту. Зазвичай у терапевтичній практиці цей період становить 3-4 тижні, якщо тільки стан пацієнта не вимагатиме швидшого збільшення дози. \n\U0001F6A9 Хворим літнього віку, а також хворим із легкою або помірною печінковою або нирковою недостатністю змінювати дозу не потрібно. Даних для рекомендацій щодо застосування препарату для лікування хворих із тяжкою печінковою недостатністю недостатньо.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною лацидипін: \n\U000025B6 ЛАЦИПІЛ  \n Польща ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування Лаципілу \n\U00002764  4 мг ", reply_markup =user_no_hd1)

    elif message.text == '\U0001F4D4 Лерканідипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Показання')
        user_no_hd1.row('\U0000274C  Протипокази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати лерканідипін')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати лерканідипін')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Назaд')
        bot.send_message(message.from_user.id, "Лерканідипін \n\U0001F4CB Спосіб застосування: (Леркамен) \n\U0001F6A9 Лікарський засіб слід застосовувати переважно вранці, принаймні за 15 хвилин до сніданку. \n\U0001F6A9 Таблетки Леркаменуâ 10 приймати перорально, 1 раз на добу, принаймні за 15 хвилин до їди. Цей лікарський засіб не слід приймати з соком грейпфрута. \n\U0001F6A9 Рекомендована доза становить 10 мг, але її можна підвищити до 20 мг, залежно від індивідуальної чутливості пацієнта. \n\U0001F6A9 Підбір дози має бути поступовим, оскільки максимальна антигіпертензивна дія може проявитися через 2 тижні після початку лікування.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати лерканідипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btnmsit= types.InlineKeyboardButton(text='\U0001F48A Леркамен', url='https://medhub.info/8eafd0fe')
        markup.add(btnmsit)
        user_no_hd1.row('\U0001F536 БКК')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною лерканідипін:\n\U000025B6 АЛВОТЕНС  \n Індія + Румунія \n\U000025B6 ЗАНІДІП  \n Італія \n\U000025B6 ЛЕРКАМЕН  \n Німеччина \n\U000025B6 ЛЕРКАНІДИПІН-ТЕВА  \n Болгарія + Ізраїль \n\U000025B6 ЛЕРКАНОСТ  \n Болгарія  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Всі препарати мають дозування: \n\U00002764  10 мг \n\U00002764  20 мг", reply_markup =user_no_hd1)


    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати лерканідипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Еналаприл + Лерканідипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: лерканідипін", reply_markup =user_no_hd1)

    elif message.text == '\U0001F4D4 Верапаміл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705   Покази')
        user_no_hd1.row('\U0000274C    Протипоказання')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати верапаміла')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати верапаміла')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Назaд')
        bot.send_message(message.from_user.id, "Верапаміл \n\U0001F4CB Спосіб застосування: (Інструкція – Ізоптин) \n\U0001F6A9 Рекомендована добова доза становить 120–360 мг, розділених на 3 прийоми. \n\U0001F6A9 Препарат слід приймати не розсмоктуючи та не розжовуючи, з достатньою кількістю рідини (наприклад 1 склянка води, в жодному випадку не грейпфрутовий сік), краще за все під час або одразу після їжі.", reply_markup =user_no_hd1)

    elif message.text == '\U00002705   Покази':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C    Протипоказання')
        user_no_hd1.row('\U0001F536 БКК')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Покази для застосування верапамілу: \n\U00002705 Ішемічна хвороба серця \n\U00002705 Аритмії: (за винятком синдрому Вольфа – Паркінсона – Уайта (WPW)) \n\U00002705 Артеріальна гіпертензія", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C    Протипоказання':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705   Покази')
        user_no_hd1.row('\U0001F536 БКК')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипокази до верапамілу: \n\U0000274C СА, або АВ блокада \n\U0000274C Фібриляція/тріпотіння передсердь при наявності додаткових провідних шляхів (WPW-синдром та LGL-синдром (синдром Лауна-Ґанонґа-Левіна)) \n\U0000274C Виражена дисфункція ЛШ (ФВ<40%) \n\U0000274C Брадикардія  \n\U0000274C Відносним протипоказом є супутні запори  ", reply_markup =user_no_hd1)


        

    elif message.text == '\U0001F48A Монокомпонентні препарати верапаміла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Ізоптин', url='https://medhub.info/327d6c18')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40верапаміл")
        callback_button2 = types.InlineKeyboardButton(text="80 мг ", callback_data="80верапаміл")
        callback_button3 = types.InlineKeyboardButton(text="180 мг", callback_data="180верапаміл")
        callback_button4 = types.InlineKeyboardButton(text="240 мг ", callback_data="240верапаміл")
        callback_button5 = types.InlineKeyboardButton(text="Розчин", callback_data="розчинверапаміл")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5)
        user_no_hd1.row('\U0001F536 БКК')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною верапаміл:\n\U000025B6 ВЕРАПАМІЛ-ДАРНИЦЯ  \n Україна \n\U000025B6 ВЕРАПАМІЛУ ГІДРОХЛОРИД  \n Україна \n\U000025B6 ВЕРАТАРД  \n Україна \n\U000025B6 ІЗОПТИН  \n Греція + Німеччина \n\U000025B6 ІЗОПТИН SR  \n Німеччина \n\U000025B6 ЛЕКОПТИН  \n Словенія  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати верапаміла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Трандолаприл + Верапаміл')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: верапаміл", reply_markup =user_no_hd1)

    elif message.text == '\U0001F4D4 Дилтіазем':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Дилтіазем', url='https://medhub.info/0ea35db8')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="60 мг", callback_data="60Дилтіазем")
        callback_button2 = types.InlineKeyboardButton(text="90 мг ", callback_data="90Дилтіазем")
        callback_button3 = types.InlineKeyboardButton(text="120 мг", callback_data="120Дилтіазем")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U00002705    Показання')
        user_no_hd1.row('\U0000274C    Протипокази')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Назaд')
        bot.send_message(message.from_user.id, "Дилтіазем \n\U0001F4CB Спосіб застосування: (Інструкція – Дилтіазем) \n\U0001F6A9 Препарат слід приймати з їжею або натщесерце. Таблетку слід ковтати цілою, запиваючи достатньою кількістю води. \n\U0001F6A9 Середня добова доза для дорослих - 180-240 мг. Максимальна добова доза – 480 мг. \n\U0001F6A9 Зазвичай початкова доза становить 60 мг 3-4 рази на добу. Доза може бути збільшена відповідно до терапевтичного ефекту до 120 мг 3 рази на добу. \n\U0001F6A9 Для пацієнтів літнього віку або пацієнтів з порушеною функцією печінки рекомендується розпочинати лікування з нижчої дози - 30 мг 3-4 рази на добу.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною дилтіазем: \n\U000025B6 АЛДІЗЕМ  \n Македонія \n\U000025B6 ДИЛТІАЗЕМ  \n Україна \n\U000025B6 ДІАКОРДИН  \n Чеська республіка ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == '\U00002705    Показання':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C    Протипокази')
        user_no_hd1.row('\U0001F536 БКК')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Покази для застосування дилтіазему: \n\U00002705 Стабільна стенокардія напруження \n\U00002705 Вазоспастична стенокардія  \n\U00002705 Артеріальна гіпертензія ", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C    Протипокази':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705    Показання')
        user_no_hd1.row('\U0001F536 БКК')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипокази до дилтіазему: \n\U0000274C СА, або АВ блокада \n\U0000274C Фібриляція/тріпотіння передсердь при наявності додаткових провідних шляхів (WPW-синдром та LGL-синдром (синдром Лауна-Ґанонґа-Левіна)) \n\U0000274C Виражена дисфункція ЛШ (ФВ<40%) \n\U0000274C Брадикардія  \n\U0000274C Відносним протипоказом є супутні запори  ", reply_markup =user_no_hd1)

#ББ
    elif message.text == '\U0001F537 ББ':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="\U00002764 Селективні", callback_data="Селективні")
        callback_button2 = types.InlineKeyboardButton(text="\U0001F49B Не селективні", callback_data="Не селективні")
        callback_button3 = types.InlineKeyboardButton(text="\U0001F49A Альфа і Бета-блокатори", callback_data="А і В блокатори")
        keyboard14.add(callback_button1)
        keyboard14.add(callback_button2)
        keyboard14.add(callback_button3)      
        user_no_hd1.row('\U0001F4D4 Небівалол')
        user_no_hd1.row('\U0001F4D4 Бетаксолол')
        user_no_hd1.row('\U0001F4D4 Бісопролол')
        user_no_hd1.row('\U0001F4D4 Есмолол')
        user_no_hd1.row('\U0001F4D4 Метопролол')
        user_no_hd1.row('\U0001F4D4 Атенолол')
        user_no_hd1.row('\U0001F4D4 Карведілол')
        user_no_hd1.row('\U0001F4D4 Пропранолол')
        user_no_hd1.row('\U0001F4D4 Соталол')
        user_no_hd1.row('\U00002196 Нaзaд')
        bot.send_message(message.from_user.id, "Класи бета-блокаторів:", reply_markup =keyboard14)
        bot.send_message(message.from_user.id, "Вкажіть діючу речовину.", reply_markup =user_no_hd1)
        

    elif message.text == '\U00002196  Нaзaд':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="\U00002764 Селективні", callback_data="Селективні")
        callback_button2 = types.InlineKeyboardButton(text="\U0001F49B Не селективні", callback_data="Не селективні")
        callback_button3 = types.InlineKeyboardButton(text="\U0001F49A Альфа і Бета-блокатори", callback_data="А і В блокатори")
        keyboard14.add(callback_button1)
        keyboard14.add(callback_button2)
        keyboard14.add(callback_button3)      
        user_no_hd1.row('\U0001F4D4 Небівалол')
        user_no_hd1.row('\U0001F4D4 Бетаксолол')
        user_no_hd1.row('\U0001F4D4 Бісопролол')
        user_no_hd1.row('\U0001F4D4 Есмолол')
        user_no_hd1.row('\U0001F4D4 Метопролол')
        user_no_hd1.row('\U0001F4D4 Атенолол')
        user_no_hd1.row('\U0001F4D4 Карведілол')
        user_no_hd1.row('\U0001F4D4 Пропранолол')
        user_no_hd1.row('\U0001F4D4 Соталол')
        user_no_hd1.row('\U00002196 Нaзaд')
        bot.send_message(message.from_user.id, "Вкажіть діючу речовину.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Класи бета-блокаторів", reply_markup =keyboard14)

    elif message.text == '\U0001F4D4 Пропранолол':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Пoкaзaння')
        user_no_hd1.row('\U0000274C  Прoтипoкaзи')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзaд')
        bot.send_message(message.from_user.id, "Пропранолол \n\U0001F4CB Спосіб застосування: (Інструкція – Анаприлін) \n\U0001F6A9 Призначати внутрішньо за 10-30 хвилин до їди, запиваючи достатньою кількістю рідини. \n\U0001F6A9 Початкова доза становить 80 мг 2 рази на добу. При необхідності дозу поступово підвищувати кожен тиждень залежно від реакції хворого на лікування.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною пропранолол:  \n\U000025B6 АНАПРИЛІН-ЗДОРОВ'Я  \n Україна", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування: \n\U00002764  10 мг \n\U00002764  40 мг", reply_markup =user_no_hd1)

    elif message.text == '\U00002705  Пoкaзaння':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C  Прoтипoкaзи')
        user_no_hd1.row('\U0001F4D4 Пропранолол')
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Показання для призначення пропранололу: \n\U00002705 Контроль есенціальної та ниркової гіпертензії \n\U00002705 Стенокардія \n\U00002705 Довготривала профілактична терапія після перенесеного інфаркту міокарда \n\U00002705 Контроль більшості форм аритмій серця", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C  Прoтипoкaзи':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705  Пoкaзaння')
        user_no_hd1.row('\U0001F4D4 Пропранолол')
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипоказання  для призначення пропранололу:\n\U0000274C Підвищена чутливість до будь-яких компонентів препарату \n\U0000274C Кардіогенний шок \n\U0000274C Атріовентрикулярна блокада II і III ступеня, синоатріальна блокада, синдром слабкості синусового вузла \n\U0000274C Синусова брадикардія (частота серцевих скорочень менше 50 уд/хв), стенокардія Принцметала \n\U0000274C Артеріальна гіпотензія, неконтрольована серцева недостатність \n\U0000274C Бронхіальна астма або бронхоспазм в анамнезі \n\U0000274C Тяжкі порушення периферичного кровообігу \n\U0000274C Метаболічний ацидоз (у т. ч. діабетичний ацидоз) \n\U0000274C Після тривалого голодування  \n\U0000274C Нелікована феохромоцитома \n\U0000274C Цукровий діабет \n\U0000274C Хронічні захворювання печінки ", reply_markup =user_no_hd1)
        
    elif message.text == '\U0001F4D4 Соталол': 
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Соталол', url='https://medhub.info/c751dc86')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40соталол")
        callback_button2 = types.InlineKeyboardButton(text="80 мг ", callback_data="80соталол")
        callback_button3 = types.InlineKeyboardButton(text="160 мг", callback_data="160соталол")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U00002705   Покaзaння')
        user_no_hd1.row('\U0000274C   Прoтипoкази')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзaд')
        bot.send_message(message.from_user.id, "Соталол \n\U0001F4CB Спосіб застосування: (Інструкція – Соталол-Сандоз) \n\U0001F6A9 Таблетки слід приймати не розжовуючи, запиваючи достатньою кількістю рідини (наприклад,  1 склянка води), до їжі. \n\U0001F6A9 Препарат не слід приймати під час їди, оскільки при цьому всмоктування соталолу гідрохлориду з травного тракту може зменшитися (зокрема це стосується молока і молочних продуктів).", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною соталол: \n\U000025B6 СОРИТМІК  \n Україна \n\U000025B6 СОТАЛОЛ САНДОЗ  \n Німеччина + Польща", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == '\U00002705   Покaзaння':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C   Прoтипoкази')
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U0001F4D4 Соталол')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Показання для призначення соталолу: \n\U00002705 Шлуночкові аритмії: \n профілактика рецидивів шлуночкової тахіаритмії, що загрожує життю;  \n лікування симптоматичної нестійкої шлуночкової тахіаритмії. \n\U00002705 Суправетрикулярні аритмії:  профілактика пароксизмальної передсердної тахікардії, пароксизмальної фібриляції передсердь, пароксизмальної атріовентрикулярної (AV) вузлової реципрокної тахікардії, пароксизмальної AV-реципрокної тахікардії при наявності додаткових провідних шляхів, пароксизмальної суправентрикулярної тахікардії після операції; \n\U00002705 підтримка нормального синусового ритму після конверсії фібриляції або мерехтіння передсердь. ", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C   Прoтипoкази':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705   Покaзaння')
        user_no_hd1.row('\U0001F4D4 Соталол')
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипоказання  для призначення соталолу: \n\U0000274C Підвищена чутливість до соталолу, сульфаніламідів або до інших компонентів препарату; \n\U0000274C Серцева недостатність IV ступеня за NYHA; гостра та хронічна серцева недостатність  ІІ-ІІІ ступеня (у стадії декомпенсації); \n\U0000274C Гострий інфаркт міокарда; \n\U0000274C Синдром слабкості синусового вузла, включаючи синоатріальну блокаду, якщо у пацієнта немає функціонуючого кардіостимулятора; тяжка дисфункція синусового вузла; \n\U0000274C AV-блокада ІІ-ІІІ ступеня (якщо у пацієнта немає функціонуючого кардіостимулятора); \n\U0000274C Вроджений або набутий синдром подовженого QT інтервалу або прийом препаратів, що сприяють подовженню QT інтервалу; \n\U0000274C Шлуночкова тахікардія типу torsade de pointes або прийом препаратів, що сприяють розвитку цього захворювання; \n\U0000274C Симптоматична синусова брадикардія (≤ 45-50 уд/хв); \n\U0000274C Неконтрольована застійна серцева недостатність, включаючи серцеву недостатність правого шлуночка після легеневої гіпертензії; \n\U0000274C Кардіогенний шок; \n\U0000274C Анестезія препаратами, що спричиняють депресію міокарда; \n\U0000274C Гіпокаліємія;  гіпомагніємія;  \n\U0000274C Нелікована феохромоцитома; \n\U0000274C Артеріальна  гіпотензія (за винятком такої, що виникає унаслідок аритмії);  \n\U0000274C Синдром Рейно та тяжкі порушення периферичного кровообігу; \n\U0000274C Бронхіальна астма та хронічні обструктивні захворювання легень; \n\U0000274C Метаболічний ацидоз; \n\U0000274C Ниркова недостатність (кліренс креатиніну < 10 мл/хв). ", reply_markup =user_no_hd1)
      

    elif message.text == '\U0001F4D4 Метопролол':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705   Пoкaзaння')
        user_no_hd1.row('\U0000274C   Протипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати метопрололу')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати метопрололу')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзaд')
        bot.send_message(message.from_user.id, "Метопролол \n\U0001F4CB Спосіб застосування: (Інструкція – Беталок) \n\U0001F6A9 Парентеральне введення препарату слід проводити під наглядом спеціально підготовленого персоналу у місцях, де можна проводити вимірювання артеріального тиску, зробити ЕКГ та проводити реанімаційні заходи.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати метопрололу':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Беталок', url='https://medhub.info/9eb42818')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="25 мг", callback_data="25метопролол")
        callback_button2 = types.InlineKeyboardButton(text="50 мг ", callback_data="50метопролол")
        callback_button3 = types.InlineKeyboardButton(text="100 мг", callback_data="100метопролол")
        callback_button4 = types.InlineKeyboardButton(text="Розчин", callback_data="Розчинметопролол")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною метопролол: \n\U000025B6 БЕТАЛОК  \n Франція \n\U000025B6 БЕТАЛОК ЗОК  \n  Швеція \n\U000025B6 ЕГІЛОК  \n Угорщина \n\U000025B6 КАРДОЛАКС  \n Туреччина \n\U000025B6 КОРВІТОЛ \n Німеччина \n\U000025B6 МЕТОПРОЛОЛ  \n Україна \n\U000025B6 МЕТОПРОЛОЛУ ТАРТРАТ  \n  Україна ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати метопрололу':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Метопролол + Івабрадін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: метопролол", reply_markup =user_no_hd1)

    elif message.text == 'Метопролол + Івабрадін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Метопролол')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію метопролола з івабрадіном містить:\n\U000025B6 ІМПЛИКОР \n  Франція ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування імплікору: \n\U000025B6 50мг метопрололу\ 5 мг івабрадину", reply_markup =user_no_hd1)

    elif message.text == '\U0001F4D4 Атенолол':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705   Пoкaзaння')
        user_no_hd1.row('\U0000274C   Протипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати атенолола')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати атенолола')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзaд')
        bot.send_message(message.from_user.id, "Атенолол \n\U0001F4CB Спосіб застосування: (Інструкція – Атенолол) \n\U0001F6A9 Лікування, як правило, розпочинають із застосування 100 мг препарату 1 раз на добу. Деяким пацієнтам достатньо 50 мг на добу. Ефект спостерігається через 2 тижні. У разі неефективності застосовують атенолол разом із діуретиками. \n\U0001F6A9 Максимальна добова доза – 200 мг. \n\U0001F6A9 Дози для хворих зі значним порушенням функції нирок залежать від рівня кліренсу креатиніну (КК): при КК 10–30 мл/хв дози знижують у 2 рази (по 50 мг на добу або через день), а при КК менше 10 мл/хв дози знижують у 4 рази порівняно зі звичайними. \n\U0001F6A9 Хворим, які перебувають на гемодіалізі, слід застосовувати 50 мг препарату після кожного діалізу. Це необхідно робити в умовах стаціонару, оскільки може відбутися помітне зниження артеріального тиску.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати атенолола':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Атенолол', url='https://tabletki.ua/uk/Атенолол-астрафарм/10079/')
        markup.add(btn_my_site)
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною атенолол: \n\U000025B6 АТЕНОЛОЛ  \n Україна \n\U000025B6 ТЕНОЛОЛ  \n Індія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування: \n\U00002764  50 мг  \n\U00002764 100 мг ", reply_markup =user_no_hd1)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати атенолола':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Атенолол + Хлорталідон')
        user_no_hd1.row('Атенолол + Амлодипін')
        user_no_hd1.row('Атенолол + Ніфедипін + Хлорталідон')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: атенолол", reply_markup =user_no_hd1)

    elif message.text == 'Атенолол + Хлорталідон':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Атенолол')
        user_no_hd1.row('\U0001F4D4 Хлорталідон')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію атенолола з хлорталідоном містять препарати: \n\U000025B6 АТЕНОЛ-Н  \n Індія \n\U000025B6 ДИНОРИК-ДАРНИЦЯ  \n Україна \n\U000025B6 ТЕНОРІК  \n Індія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Всі препарати мають дозування:\n\U00002764 100 мг атенололу і 25 мг хлорталідону ", reply_markup =user_no_hd1)

    elif message.text == 'Атенолол + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Атенолол')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію атенолола з амлодипіном містить: \n\U000025B6 ТЕНОЧЕК  \n  Індія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування: \n\U00002764 50 мг атенолола і 5 мг амлодипіна ", reply_markup =user_no_hd1)


    elif message.text == 'Атенолол + Ніфедипін + Хлорталідон':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Атенолол')
        user_no_hd1.row('\U0001F4D4 Хлорталідон')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Потрійну комбінацію атенолола з ніфедипіном і хлорталідоном містить:\n\U000025B6 ТОНОРМА  \n  Україна ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування тонорми: \n\U00002764  100 мг атенолола + 10 мг ніфедипіна + 25 мг хлорталідона ", reply_markup =user_no_hd1)

    elif message.text == '\U0001F4D4 Бетаксолол':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Локрен', url='https://medhub.info/c6cfa4f8')
        markup.add(btn_my_site)
        callback_button1 = types.InlineKeyboardButton(text="10 мг", callback_data="10бетаксолол")
        callback_button2 = types.InlineKeyboardButton(text="20 мг", callback_data="20бетаксолол")
        keyboard14.add(callback_button1, callback_button2)
        user_no_hd1.row('\U00002705   Пoкaзaння')
        user_no_hd1.row('\U0000274C   Протипoкази')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзaд')
        bot.send_message(message.from_user.id, "Бетаксолол \n\U0001F4CB Спосіб застосування: (Інструкція – Локрен) \n\U0001F6A9 Звичайна доза при артеріальній гіпертензії та для профілактики нападів  стенокардії напруження – 1 таблетка по 20 мг на добу.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Препарати з діючою речовиною бетаксолол:\n\U000025B6 БЕТАК  \n Кіпр \n\U000025B6 БЕТАКОР  \n Україна \n\U000025B6 ЛОКРЕН  \n Франція  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == '\U0001F4D4 Бісопролол':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705   Пoкaзaння')
        user_no_hd1.row('\U0000274C   Протипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати бісопрололу')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати бісопрололу')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзaд')
        bot.send_message(message.from_user.id, "Бісопролол \n\U0001F4CB Спосіб застосування: (Інструкція – Конкор) \n\U0001F6A9 Таблетки препарату слід ковтати не розжовуючи, вранці натще, під час або після сніданку, запиваючи невеликою кількістю рідини. \n\U0001F6A9Лікування слід розпочинати поступово з низьких доз із подальшим підвищенням дози. Рекомендована доза становить 5 мг на добу. \n\U0001F6A9За необхідності добову дозу можна підвищити до 10 мг (1 таблетка препарату Конкор по 10 мг) на добу. Подальше збільшення дози виправдане лише у виняткових випадках. \n\U0001F6A9 Максимальна рекомендована доза становить 20 мг на добу. \n\U0001F6A9Коригування дози встановлюється лікарем індивідуально, залежно від частоти пульсу та терапевтичної користі.", reply_markup =user_no_hd1)

    elif message.text == '\U00002705   Пoкaзaння':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C   Протипoкази')
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Показання для призначення селективних бета-блокаторів: \n\U00002705 Артеріальна гіпертензія \n\U00002705 Ішемічна хвороба серця (ІХС) (стенокардія) \n\U00002705 Хронічна серцева недостатність (ХСН) із систолічною дисфункцією лівого шлуночка   ", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C   Протипoкази':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705   Пoкaзaння')
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипоказання  для призначення селективних бета-блокаторів: \n\U0000274C Підвищена чутливість до бісопрололу або до інших компонентів препарату \n\U0000274C гостра серцева недостатність або серцева недостатність у стані декомпенсації  \n\U0000274C кардіогенний шок \n\U0000274C атріовентрикулярна блокада II і III ступеня (за винятком такої у пацієнтів зі штучним водієм ритму) \n\U0000274C синдром слабкості синусового вузла \n\U0000274C виражена синоатріальна блокада \n\U0000274C симптоматична брадикардія (частота серцевих скорочень менше 60 уд/хв) \n\U0000274C симптоматична артеріальна гіпотензія (систолічний артеріальний тиск нижче 100 мм рт. ст.) \n\U0000274C тяжкі хронічні обструктивні захворювання легень \n\U0000274C тяжка форма бронхіальної астми \n\U0000274C пізні стадії порушення периферичного кровообігу, хвороба Рейно \n\U0000274C феохромоцитома, що не лікувалася \n\U0000274C метаболічний ацидоз \n\U0000274C одночасне застосування з флоктафеніном і сультопридом. ", reply_markup =user_no_hd1)       

    elif message.text == '\U0001F48A Монокомпонентні препарати бісопрололу':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Конкор', url='https://medhub.info/8d048cc9')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5бісопролол")
        callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5бісопролол")
        callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10бісопролол")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною бісопролол: \n\U000025B6 БІКАРД  \n Іспанія \n\U000025B6 БІПРОЛОЛ  \n Україна \n\U000025B6 БІСОПРОЛ  \n Україна \n\U000025B6 БІСОПРОЛОЛ АУРОБІНДО  \n Індія \n\U000025B6 БІСОПРОЛОЛ КРКА  \n Німеччина + Словенія \n\U000025B6 БІСОПРОЛОЛ САНДОЗ  \n Німеччина \n\U000025B6 БІСОПРОЛОЛ-АСТРАФАРМ  \n Україна \n\U000025B6 БІСОПРОЛОЛ-КВ  \n Україна \n\U000025B6 БІСОПРОЛОЛ-ТЕВА  \n Німеччина + Угорщина \n\U000025B6 БІСОСТАД  \n В'єтнам + Німеччина \n\U000025B6 ДОРЕЗ  \n Македонія \n\U000025B6 ЄВРОБІСОПРОЛОЛ \n  Україна \n\U000025B6 КОНКОР  \n Німеччина \n\U000025B6 КОРОНАЛ  \n Словакія ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати бісопрололу':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Бісопролол + Гідрохлортіазид')
        user_no_hd1.row('Бісопролол + Амлодипін')
        user_no_hd1.row('Периндоприл + Бісопролол')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: бісопролол", reply_markup =user_no_hd1)

    elif message.text == 'Бісопролол + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Бісопролол')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію бісопрола з гідрохлоротіазидом містить:\n\U000025B6 КОМБІСО  \n Чеська республіка ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Наявні дозування:\n\U00002764  5 або 10 мг бісопролола з 6,25 мг гідрохлортіазида ", reply_markup =user_no_hd1)
    elif message.text == 'Бісопролол + Амлодипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Бісопролол')
        user_no_hd1.row('\U0001F4D4 Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію бісопрола з амлодипіном містять препарати: \n\U000025B6 АЛОТЕНДИН  \n Угорщина \n\U000025B6 СОБІКОМБІ  \n  Німеччина + Словенія", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Препарати мають дозування: \n\U00002764  5 мг \U000026A1 5 \n\U00002764  5 мг \U000026A1 10 мг \n\U00002764  10 мг \U000026A1 5 мг \n\U00002764  10 мг \U000026A1 10 мг ", reply_markup =user_no_hd1)
                
    elif message.text == '\U0001F4D4 Есмолол':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Біблок', url='https://medhub.info/56393d10')
        markup.add(btn_my_site)
        user_no_hd1.row('\U00002705   Пoкaзaння')
        user_no_hd1.row('\U0000274C   Протипoкази')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзaд')
        bot.send_message(message.from_user.id, "Есмолол \n\U0001F4CB Спосіб застосування: (Інструкція – Біблок) \n\U0001F6A9 Ефективна доза  для лікування надшлуночкової тахіаритмії становить від 50 до 200 мкг/кг/хв, хоча застосовувались і дози до 300 мкг/кг/хв. Для деяких пацієнтів достатньо було дози 25 мкг/кг/хв. \n\U0001F6A9 При надшлуночковій тахіаритмії дозу можна підібрати індивідуально шляхом титрування, при якому кожен наступний крок складається із навантажувальної дози та наступного введення підтримувальної дози.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Препарати з діючою речовиною есмолол:\n\U000025B6 БІБЛОК  \n  Україна ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування біблоку: \n\U00002764 Розчин 10 мл 1% (амп)", reply_markup = user_no_hd1)

    elif message.text == '\U0001F4D4 Небівалол':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705   Пoкaзaння')
        user_no_hd1.row('\U0000274C   Протипoкази')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати небівалола')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати небівалола')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзaд')
        bot.send_message(message.from_user.id, "Небівалол \n\U0001F4CB Спосіб застосування: (Інструкція – Небілет) \n\U0001F6A9 Доза становить 1 таблетку (5 мг небівололу) на добу; бажано застосовувати її завжди в один і той самий час доби. \n\U0001F6A9 Гіпотензивний ефект стає явним через 1–2 тижні лікування, але іноді оптимальна дія спостерігається лише через 4 тижні. \n\U0001F6A9 Таблетки можна застосовувати разом з їжею.", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати небівалола':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Небілет', url='https://medhub.info/f687a329')
        markup.add(btn_my_site)
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною небівалол:\n\U000025B6 НЕБІАР  \n Україна \n\U000025B6 НЕБІВАЛ  \n Україна \n\U000025B6 НЕБІВОЛОЛ ОРІОН  \n Греція + Фінляндія \n\U000025B6 НЕБІВОЛОЛ САНДОЗ  \n Німеччина + Туреччина \n\U000025B6 НЕБІВОЛОЛ СТАДА  \n Німеччина \n\U000025B6 НЕБІВОЛОЛ-ДАРНИЦЯ  \n Україна \n\U000025B6 НЕБІВОЛОЛ-ТЕВА  \n Болгарія + Ісландія + Мальта \n\U000025B6 НЕБІКАРД  \n Індія \n\U000025B6 НЕБІЛЕТ  \n Німеччина \n\U000025B6 НЕБІТЕНЗ  \n Мальта \n\U000025B6 НЕБІТРЕНД-ТЕВА  \n Угорщина \n\U000025B6 НЕБІТРИКС  \n Індія  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Всі препарати мають дозування: \n\U00002764  5 мг  ", reply_markup =user_no_hd1)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновані препарати небівалола':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Небівалол + Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: небівалол", reply_markup =user_no_hd1)

    elif message.text == 'Небівалол + Гідрохлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0001F4D4 Небівалол')
        user_no_hd1.row('\U0001F4D4 Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію небівалола з гідрохлоротіазидом містить: \n\U000025B6 НЕБІАР ПЛЮС  \n Індія + Україна \n\U000025B6 НЕБІЛЕТ ПЛЮС \n Німеччина ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:\n\U00002764  5 мг небівалола і 12,5 мг гідрохлортіазида ", reply_markup =user_no_hd1)

    elif message.text == '\U0001F4D4 Карведілол':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Кардіостад', url='https://medhub.info/58c73e94')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="3,125 мг", callback_data="3,125карведілол")
        callback_button2 = types.InlineKeyboardButton(text="6,25 мг", callback_data="6,25карведілол")
        callback_button3 = types.InlineKeyboardButton(text="12,5 мг", callback_data="12,5карведілол")
        callback_button4 = types.InlineKeyboardButton(text="25 мг", callback_data="25карведілол")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U00002705   Пoкaзання')
        user_no_hd1.row('\U0000274C    Протипoкази')
        user_no_hd1.row('\U00002705 Продовжити')
        user_no_hd1.row('\U00002196  Нaзaд')
        bot.send_message(message.from_user.id, "Карведілол \n\U0001F4CB Спосіб застосування: (Інструкція – Кардіостад) \n\U0001F6A9 Максимальна разова доза не повинна перевищувати 25 мг, рекомендована максимальна добова доза – 50 мг. \n\U0001F6A9 Рекомендована початкова доза у перші 2 дні лікування становить 12,5 мг 1 раз на добу. Потім лікування продовжувати у дозі 25 мг двічі на добу. Надалі, у разі необхідності, дозу поступово можна збільшувати з інтервалом у 2 тижні. \n\U0001F6A9 Рекомендована максимальна добова доза – 100 мг, яку слід розподілити на два прийоми.\n\U0001F6A9 Препарат приймати перорально, незалежно від вживання їжі, запиваючи достатньою кількістю рідини. Проте пацієнтам із серцевою недостатністю рекомендується приймати карведилол під час вживання їжі, щоб подовжити абсорбцію та зменшити ризик ортостатичної гіпотензії.", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Препарати з діючою речовиною карведілол:\n\U000025B6 КАРВЕДИЛОЛ АУРОБІНДО  \n Індія \n\U000025B6 КАРВЕДИЛОЛ САНДОЗ  \n  Німеччина \n\U000025B6 КАРВЕДИЛОЛ-КВ  \n Україна \n\U000025B6 КАРВИДЕКС  \n Індія \n\U000025B6 КАРВІУМ  \n Румунія \n\U000025B6 КАРДІОСТАД  \n Німеччина + Сербія \n\U000025B6 КОРВАЗАН  \n Україна \n\U000025B6 КОРІОЛ  \n Словенія \n\U000025B6 ТАЛЛІТОН  \n Угорщина ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

    elif message.text == '\U00002705   Пoкaзання':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U0000274C    Протипoкази')
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Показання для призначення карведілолу: \n\U00002705 Есенціальна гіпертензія \n\U00002705 Хронічна стабільна стенокардія \n\U00002705 Хронічна серцева недостатність (додаткове лікування)  ", reply_markup =user_no_hd1)

    elif message.text == '\U0000274C    Протипoкази':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705   Пoкaзання')
        user_no_hd1.row('\U0001F537 ББ')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Протипоказання  для призначення карведіололу: \n\U0000274C Підвищена чутливість до діючої речовини або до будь-якої  з допоміжних речовин препарату \n\U0000274C Декомпенсована серцева недостатність \n\U0000274C Серцева недостатність IV класу за класифікацією NYHA, яка вимагає внутрішньовенного введення інотропних засобів \n\U0000274C Атріовентрикулярна блокада ІІ та ІІІ ступеня (крім випадків, коли встановлений постійний кардіостимулятор) \n\U0000274C Супутнє внутрішньовенне введення верапамілу, дилтіазему або інших антиаритмічних засобів (особливо антиаритмічних засобів класу I) \n\U0000274C Виражена брадикардія (ЧСС <50 уд/хв) \n\U0000274C Виражена артеріальна гіпотензія (систолічний тиск нижче 85 мм рт.ст.) \n\U0000274C Кардіогенний шок \n\U0000274C Синдром слабкості синусного вузла (у тому числі синоатріальна блокада) \n\U0000274C Декомпенсована серцева недостатність, яка потребує внутрішньовенного введення позитивних інотропних засобів та/або сечогінних засобів \n\U0000274C Легеневе серце, легенева гіпертензія \n\U0000274C  Бронхіальна астма або обструктивні захворювання дихальних шляхів, що супроводжуються бронхоспазмом \n\U0000274C Феохромоцитома (за винятком випадків, коли вона належним чином контролюється при застосуванні альфа-блокаторів) \n\U0000274C Стенокардія Принцметала \n\U0000274C Виражені порушення функції печінки \n\U0000274C Супутнє застосування інгібіторів МАО (за винятком інгібіторів МАО-В) \n\U0000274C Непереносимість галактози, недостатність лактази Лаппа або глюкозо-галактозна мальабсорбція \n\U0000274C Метаболічний ацидоз  ", reply_markup =user_no_hd1)
           
#черновик
    
    elif message.text == '\U0001F4D4 Лозартан':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('\U00002705 Покaзaння')
        user_no_hd1.row('\U0000274C Прoтипoкази')
        user_no_hd1.row('\U00002757 Пoбічні дії')
        user_no_hd1.row('\U0001F48A Монокомпонентні препарати лозартан')
        user_no_hd1.row('\U0001F48A+\U0001F48A Комбіновані препарати лозартан')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Периндоприл. Спосіб застосування:", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Лозартан", reply_markup =user_no_hd1)

    elif message.text == '\U0001F48A Монокомпонентні препарати лізиноприла':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        markup = types.InlineKeyboardMarkup()
        btn_my_site= types.InlineKeyboardButton(text='\U0001F48A Лізиноприл', url='https://medhub.info/lizinopril-tabletki-instrukciia-cina/016e5f15')
        markup.add(btn_my_site)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5лізиноприл")
        callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5лізиноприл")
        callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10лізиноприл")
        callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20лізиноприл")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('\U0001F537 Діуретики')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Препарати з діючою речовиною: лізиноприл:  ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "\U00002705 Інструкція:", reply_markup =markup)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)



    elif message.text == '\U0001F48A+\U0001F48A Комбіновіані препарати зофенаприл':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        user_no_hd1.row('Зофенаприл + Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "Комбіновані препарати з діючою речовиною: зофенаприл", reply_markup =user_no_hd1)


    elif message.text == 'Лізиноприл + Гідроіхлортіазид':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="10 \U000026A1 12,5", callback_data="1")
        callback_button2 = types.InlineKeyboardButton(text="20 \U000026A1 12,5", callback_data="2")
        callback_button3 = types.InlineKeyboardButton(text="20 \U000026A1 25", callback_data="3")
        keyboard14.add(callback_button1, callback_button2, callback_button3)
        user_no_hd1.row('Лізиноприл + Амлодипін')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію лізиноприла з гідрохлоротіазидом містять препарати: ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування:", reply_markup =keyboard14)

        
    elif message.text == 'Лізиноприл + Амлодіипін':
        user_no_hd1 = telebot.types.ReplyKeyboardMarkup(True, True)
        keyboard14 = types.InlineKeyboardMarkup()
        callback_button1 = types.InlineKeyboardButton(text="5 \U000026A1 5", callback_data="5Лізиноприл+ 5Амлодипіна")
        callback_button2 = types.InlineKeyboardButton(text="10 \U000026A1 5", callback_data="10Лізиноприл+ 5Амлодипіна")
        callback_button3 = types.InlineKeyboardButton(text="20 \U000026A1 5", callback_data="20Лізиноприл+ 5Амлодипіна")
        callback_button4 = types.InlineKeyboardButton(text="20 \U000026A1 10", callback_data="20Лізиноприл+ 10Амлодипіна")
        keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
        user_no_hd1.row('Лізиноприл + Гідрохлортіазид')
        user_no_hd1.row('\U00002705 Продовжити')
        bot.send_message(message.from_user.id, "\U00002705 Комбінацію лізиноприла з амлодипіном містять препарати: а   ", reply_markup =user_no_hd1)
        bot.send_message(message.from_user.id, "Дозування препаратів:\n\U00002764  5 мг \U000026A1 5 \n\U00002764  5 мг \U000026A1 10 мг \n\U00002764  10 мг \U000026A1 5 мг \n\U00002764  10 мг \U000026A1 10 мг ", reply_markup =keyboard14)




        
        
# Обробка кнопок
@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    if call.message:
        if call.data == "І":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\U0001F49A Клас доказів І  -докази, або загальна згода, що таке лікування чи процедура мають сприятливий вплив, корисні, ефективні. (рекомендовано, показано)")
        elif call.data == "ІІа":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\U0001F49B Клас доказів ІІа - значення доказів, або думок на стороні ефективності (повинно бути розглянуто)")
        elif call.data == "ІІв":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\U0001F49B Клас доказів ІІв - ефективність менш добре встановлена доказами чи думками (може бути роглянуто)")
        elif call.data == "ІІІ":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\U00002764 Клас доказів ІІІ - докази, або загальна згода на те, що лікування (процедура)  не є корисними чи ефективними, а в деяких випадках можуть бути шкідливими (не рекомендується)")
        elif call.data == "А":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\U0001F4D7 Рівень доказів - A - дані отримані з декількох рандомінізованих клінічних досліджень, або мета аналізів.")
        elif call.data == "В":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\U0001F4D9 Рівень доказів - B – дані отримані з одного рандомінізованого  клінічного дослідження, або великих нерандомінізованих досліджень.")
        elif call.data == "C":
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\U0001F4D5 Рівень доказів - C – консенсус, або думка експертів, або дані маленьких рандомінізованих досліджень, ретроспективних досліджень, регістрів.")
#периндоприл
        elif call.data == "2 мг периндоприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="2,5 мг ", callback_data="2,5 мг периндоприл")
            callback_button3 = types.InlineKeyboardButton(text="4 мг", callback_data="4 мг периндоприл")
            callback_button4 = types.InlineKeyboardButton(text="5 мг ", callback_data="5 мг периндоприл")
            callback_button5 = types.InlineKeyboardButton(text="8 мг", callback_data="8 мг периндоприл")
            callback_button6 = types.InlineKeyboardButton(text="10 мг ", callback_data="10 мг периндоприл")
            keyboard14.add(callback_button2, callback_button3, callback_button4, callback_button5, callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Периндоприл в дозуванні 2 мг міститься в таких препаратах: \n\U00002764 ЕРУПНІЛ, \n\U00002764 ПЕРИНДОПРИЛ САНДОЗ", reply_markup =keyboard14)


        elif call.data == "2,5 мг периндоприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2 мг", callback_data="2 мг периндоприл")
            callback_button3 = types.InlineKeyboardButton(text="4 мг", callback_data="4 мг периндоприл")
            callback_button4 = types.InlineKeyboardButton(text="5 мг ", callback_data="5 мг периндоприл")
            callback_button5 = types.InlineKeyboardButton(text="8 мг", callback_data="8 мг периндоприл")
            callback_button6 = types.InlineKeyboardButton(text="10 мг ", callback_data="10 мг периндоприл")
            keyboard14.add(callback_button1, callback_button3, callback_button4, callback_button5, callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Периндоприл в дозуванні 2,5 мг міститься в таких препаратах: \n\U00002764 ПРЕСТАРІУМ , \n\U00002764 ПЕРИНДОПРИЛ-ТЕВА  ", reply_markup =keyboard14)
        elif call.data == "4 мг периндоприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2 мг", callback_data="2 мг периндоприл")
            callback_button2 = types.InlineKeyboardButton(text="2,5 мг ", callback_data="2,5 мг периндоприл")
            callback_button4 = types.InlineKeyboardButton(text="5 мг ", callback_data="5 мг периндоприл")
            callback_button5 = types.InlineKeyboardButton(text="8 мг", callback_data="8 мг периндоприл")
            callback_button6 = types.InlineKeyboardButton(text="10 мг ", callback_data="10 мг периндоприл")
            keyboard14.add(callback_button1, callback_button2, callback_button4, callback_button5, callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Периндоприл в дозуванні 4 мг міститься в таких препаратах:\n\U00002764 ПРЕСТАРІУМ , \n\U00002764 ЕРУПНІЛ, \n\U00002764 ПЕРИНДОПРИЛ КРКА, \n\U00002764 ПЕРИНДОПРИЛ САНДОЗ , \n\U00002764 ПЕРИНДОПРИЛ-РІХТЕР , \n\U00002764 ПЕРИСТАР, \n\U00002764 ПЕРІНДОПРЕС, \n\U00002764 ПРЕНЕСА, \n\U00002764 ПРЕНЕСА ОРО ТАБ, \n\U00002764 ПРОМЕПРИЛ, \n\U00002764 ХІТЕН ", reply_markup =keyboard14)     
        elif call.data == "5 мг периндоприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2 мг", callback_data="2 мг периндоприл")
            callback_button2 = types.InlineKeyboardButton(text="2,5 мг ", callback_data="2,5 мг периндоприл")
            callback_button3 = types.InlineKeyboardButton(text="4 мг", callback_data="4 мг периндоприл")
            callback_button5 = types.InlineKeyboardButton(text="8 мг", callback_data="8 мг периндоприл")
            callback_button6 = types.InlineKeyboardButton(text="10 мг ", callback_data="10 мг периндоприл")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button5, callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Периндоприл в дозуванні 5 мг міститься в таких препаратах: \n\U00002764 ПРЕСТАРІУМ , \n\U00002764 ПЕРИНДОПРИЛ-ТЕВА   ", reply_markup =keyboard14)
        elif call.data == "8 мг периндоприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2 мг", callback_data="2 мг периндоприл")
            callback_button2 = types.InlineKeyboardButton(text="2,5 мг ", callback_data="2,5 мг периндоприл")
            callback_button3 = types.InlineKeyboardButton(text="4 мг", callback_data="4 мг периндоприл")
            callback_button4 = types.InlineKeyboardButton(text="5 мг ", callback_data="5 мг периндоприл")
            callback_button6 = types.InlineKeyboardButton(text="10 мг ", callback_data="10 мг периндоприл")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Периндоприл в дозуванні 8 мг міститься в таких препаратах: \n\U00002764 ПРЕСТАРІУМ , \n\U00002764 ЕРУПНІЛ, \n\U00002764 ПЕРИНДОПРИЛ КРКА, \n\U00002764 ПЕРИНДОПРИЛ САНДОЗ, \n\U00002764 ПЕРИНДОПРИЛ-РІХТЕР, \n\U00002764 ПЕРИСТАР, \n\U00002764 ПЕРІНДОПРЕС, \n\U00002764 ПРЕНЕСА, \n\U00002764 ПРЕНЕСА ОРО ТАБ, \n\U00002764 ПРОМЕПРИЛ, \n\U00002764 ХІТЕН" , reply_markup =keyboard14)
        elif call.data == "10 мг периндоприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2 мг", callback_data="2 мг периндоприл")
            callback_button2 = types.InlineKeyboardButton(text="2,5 мг ", callback_data="2,5 мг периндоприл")
            callback_button3 = types.InlineKeyboardButton(text="4 мг", callback_data="4 мг периндоприл")
            callback_button4 = types.InlineKeyboardButton(text="5 мг ", callback_data="5 мг периндоприл")
            callback_button5 = types.InlineKeyboardButton(text="8 мг", callback_data="8 мг периндоприл")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Периндоприл в дозуванні 10 мг міститься в таких препаратах: \n\U00002764 ПРЕСТАРІУМ , \n\U00002764 ПЕРИНДОПРИЛ-ТЕВА   ", reply_markup =keyboard14)

#периндоприл з індапамідом
        elif call.data == "2 мг Периндоприл + Індапамід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625 ", callback_data="2,5 мг Периндоприл + Індапамід")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 1,25 ", callback_data="4 мг Периндоприл + Індапамід")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 1,25 ", callback_data="5 мг Периндоприл + Індапамід")
            callback_button5 = types.InlineKeyboardButton(text="8\U000026A1 2,5 ", callback_data="8 мг Периндоприл + Індапамід")
            callback_button6 = types.InlineKeyboardButton(text="10\U000026A1 2,5", callback_data="10 мг Периндоприл + Індапамід")
            keyboard14.add(callback_button2, callback_button3, callback_button4, callback_button5, callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 2 мг периндоприла і 0,625 мг індапаміда доступна в настпних препаратах:\n\U00002764 ЕРУПНІЛ ПЛЮС \n\U00002764 ІН-АЛІТЕР \n\U00002764 КО-ПРЕНЕСА  \n\U00002764  НОЛІПРЕЛ \n\U00002764 ПЕРИНДОПРИЛ /ІНДАПАМІД КРКА \n\U00002764  ПРИЛАМІД ", reply_markup =keyboard14)
        elif call.data == "2,5 мг Периндоприл + Індапамід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625", callback_data="2 мг Периндоприл + Індапамід")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 1,25", callback_data="4 мг Периндоприл + Індапамід")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 1,25", callback_data="5 мг Периндоприл + Індапамід")
            callback_button5 = types.InlineKeyboardButton(text="8\U000026A1 2,5 ", callback_data="8 мг Периндоприл + Індапамід")
            callback_button6 = types.InlineKeyboardButton(text="10\U000026A1 2,5 ", callback_data="10 мг Периндоприл + Індапамід")
            keyboard14.add(callback_button1, callback_button3, callback_button4, callback_button5, callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 2,5 мг периндоприла і 0,625 мг індапаміда доступна в настпних препаратах: \n\U00002764 НОЛІПРЕЛ АРГІНІН \n\U00002764  ПЕРИНДОПРИЛ/ІНДАПАМІД-ТЕВА ", reply_markup =keyboard14)

        elif call.data == "4 мг Периндоприл + Індапамід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625", callback_data="2 мг Периндоприл + Індапамід")
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625 ", callback_data="2,5 мг Периндоприл + Індапамід")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 1,25 ", callback_data="5 мг Периндоприл + Індапамід")
            callback_button5 = types.InlineKeyboardButton(text="8\U000026A1 2,5 ", callback_data="8 мг Периндоприл + Індапамід")
            callback_button6 = types.InlineKeyboardButton(text="10\U000026A1 2,5", callback_data="10 мг Периндоприл + Індапамід")
            keyboard14.add(callback_button1, callback_button2, callback_button4, callback_button5, callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 4 мг периндоприла і 1,25 мг індапаміда доступна в настпних препаратах:\n\U00002764 ЕРУПНІЛ ПЛЮС \n\U00002764 ІН-АЛІТЕР \n\U00002764  КО-ПРЕНЕСА  \n\U00002764 НОЛІПРЕЛ ФОРТЕ \n\U00002764  ПЕРИНДОПРИЛ /ІНДАПАМІД КРКА \n\U00002764 ПРИЛАМІД ", reply_markup =keyboard14)

        elif call.data == "5 мг Периндоприл + Індапамід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625 ", callback_data="2 мг Периндоприл + Індапамід")
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625 ", callback_data="2,5 мг Периндоприл + Індапамід")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 1,25 ", callback_data="4 мг Периндоприл + Індапамід")
            callback_button5 = types.InlineKeyboardButton(text="8\U000026A1 2,5 ", callback_data="8 мг Периндоприл + Індапамід")
            callback_button6 = types.InlineKeyboardButton(text="10\U000026A1 2,5 ", callback_data="10 мг Периндоприл + Індапамід")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button5, callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 5 мг периндоприла і 1,25 мг індапаміда доступна в настпних препаратах:\n\U00002764 НОЛІПРЕЛ АРГІНІН ФОРТЕ \n\U00002764  ПЕРИНДОПРИЛ/ІНДАПАМІД ФОРТЕ-ТЕВА \n\U00002764  ПРЕСТАРІУМ АРГІНІН КОМБІ ", reply_markup =keyboard14)

        elif call.data == "8 мг Периндоприл + Індапамід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625 ", callback_data="2 мг Периндоприл + Індапамід")
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625 ", callback_data="2,5 мг Периндоприл + Індапамід")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 1,25 ", callback_data="4 мг Периндоприл + Індапамід")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 1,25 ", callback_data="5 мг Периндоприл + Індапамід")
            callback_button6 = types.InlineKeyboardButton(text="10\U000026A1 2,5 ", callback_data="10 мг Периндоприл + Індапамід")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button6)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 8 мг периндоприла і 2,5 мг індапаміда доступна в настпних препаратах:\n\U00002764 ІН-АЛІТЕР  \n\U00002764  КО-ПРЕНЕСА \n\U00002764 ПЕРИНДОПРИЛ /ІНДАПАМІД КРКА   ", reply_markup =keyboard14)

        elif call.data == "10 мг Периндоприл + Індапамід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625", callback_data="2 мг Периндоприл + Індапамід")
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625 ", callback_data="2,5 мг Периндоприл + Індапамід")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 1,25 ", callback_data="4 мг Периндоприл + Індапамід")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 1,25 ", callback_data="5 мг Периндоприл + Індапамід")
            callback_button5 = types.InlineKeyboardButton(text="8\U000026A1 2,5 ", callback_data="8 мг Периндоприл + Індапамід")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг периндоприла і 2,5 мг індапаміда доступна в настпних препаратах: \n\U00002764 НОЛІПРЕЛ \n\U00002764 БІ-ФОРТЕ ", reply_markup =keyboard14)

#периндоприл з амлодипіном

        elif call.data == "3,5 мг Периндоприл + 2,5Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="4\U000026A1 5 ", callback_data="4 мг Периндоприл + 5Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 10 ", callback_data="4 мг Периндоприл + 10Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 5 ", callback_data="5 мг Периндоприл + 5Амлодипін")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 10 ", callback_data="5 мг Периндоприл + 10Амлодипін")
            callback_button6 = types.InlineKeyboardButton(text="7\U000026A1 5 ", callback_data="7 мг Периндоприл + 5Амлодипін")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 5 ", callback_data="8 мг Периндоприл + 5Амлодипін")
            callback_button8 = types.InlineKeyboardButton(text="8\U000026A1 10 ", callback_data="8 мг Периндоприл + 10Амлодипін")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 5 ", callback_data="10 мг Периндоприл + 5Амлодипін")
            callback_button10 = types.InlineKeyboardButton(text="10\U000026A1 10", callback_data="10 мг Периндоприл + 10Амлодипін")
            callback_button11 = types.InlineKeyboardButton(text="14\U000026A1 10", callback_data="14 мг Периндоприл + 10Амлодипін")
            keyboard14.add(callback_button2, callback_button3, callback_button4, callback_button5, callback_button6, callback_button7, callback_button8, callback_button9, callback_button10, callback_button11)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 3,5 мг периндоприла і 2,5 мг амлодипіна доступна в настпних препаратах: \n\U00002764 БІ-ПРЕСТАРІУМ N  \n\U00002764  ВІАКОРАМ ", reply_markup =keyboard14)
       
        elif call.data == "4 мг Периндоприл + 5Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,5\U000026A1 2,5", callback_data="3,5 мг Периндоприл + 2,5Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 10 ", callback_data="4 мг Периндоприл + 10Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 5 ", callback_data="5 мг Периндоприл + 5Амлодипін")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 10 ", callback_data="5 мг Периндоприл + 10Амлодипін")
            callback_button6 = types.InlineKeyboardButton(text="7\U000026A1 5 ", callback_data="7 мг Периндоприл + 5Амлодипін")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 5 ", callback_data="8 мг Периндоприл + 5Амлодипін")
            callback_button8 = types.InlineKeyboardButton(text="8\U000026A1 10 ", callback_data="8 мг Периндоприл + 10Амлодипін")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 5 ", callback_data="10 мг Периндоприл + 5Амлодипін")
            callback_button10 = types.InlineKeyboardButton(text="10\U000026A1 10  ", callback_data="10 мг Периндоприл + 10Амлодипін")
            callback_button11 = types.InlineKeyboardButton(text="14\U000026A1 10 ", callback_data="14 мг Периндоприл + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button3, callback_button4, callback_button5, callback_button6, callback_button7, callback_button8, callback_button9, callback_button10, callback_button11)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 4 мг периндоприла і 5 мг амлодипіна доступна в настпних препаратах:\n\U00002764 АМ-АЛІТЕР \n\U00002764  АМЛЕCСА \n\U00002764 АМЛОДИПІН-ПЕРИНДОПРИЛ-РІХТЕР  \n\U00002764 ПЕРИНДОПРИЛ /АМЛОДИПІН КРКА  ", reply_markup =keyboard14)
 
        elif call.data == "4 мг Периндоприл + 10Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,5\U000026A1 2,5", callback_data="3,5 мг Периндоприл + 2,5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="4\U000026A1 5 ", callback_data="4 мг Периндоприл + 5Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 5 ", callback_data="5 мг Периндоприл + 5Амлодипін")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 10 ", callback_data="5 мг Периндоприл + 10Амлодипін")
            callback_button6 = types.InlineKeyboardButton(text="7\U000026A1 5 ", callback_data="7 мг Периндоприл + 5Амлодипін")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 5 ", callback_data="8 мг Периндоприл + 5Амлодипін")
            callback_button8 = types.InlineKeyboardButton(text="8\U000026A1 10 ", callback_data="8 мг Периндоприл + 10Амлодипін")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 5 ", callback_data="10 мг Периндоприл + 5Амлодипін")
            callback_button10 = types.InlineKeyboardButton(text="10\U000026A1 10  ", callback_data="10 мг Периндоприл + 10Амлодипін")
            callback_button11 = types.InlineKeyboardButton(text="14\U000026A1 10 ", callback_data="14 мг Периндоприл + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button4, callback_button5, callback_button6, callback_button7, callback_button8, callback_button9, callback_button10, callback_button11)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 4 мг периндоприла і 10 мг амлодипіна доступна в настпних препаратах:\n\U00002764 АМ-АЛІТЕР \n\U00002764 АМЛЕCСА \n\U00002764 АМЛОДИПІН-ПЕРИНДОПРИЛ-РІХТЕР  \n\U00002764 ПЕРИНДОПРИЛ /АМЛОДИПІН КРКА   ", reply_markup =keyboard14)
       

        elif call.data == "5 мг Периндоприл + 5Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,5\U000026A1 2,5", callback_data="3,5 мг Периндоприл + 2,5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="4\U000026A1 5 ", callback_data="4 мг Периндоприл + 5Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 10 ", callback_data="4 мг Периндоприл + 10Амлодипін")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 10 ", callback_data="5 мг Периндоприл + 10Амлодипін")
            callback_button6 = types.InlineKeyboardButton(text="7\U000026A1 5 ", callback_data="7 мг Периндоприл + 5Амлодипін")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 5 ", callback_data="8 мг Периндоприл + 5Амлодипін")
            callback_button8 = types.InlineKeyboardButton(text="8\U000026A1 10 ", callback_data="8 мг Периндоприл + 10Амлодипін")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 5 ", callback_data="10 мг Периндоприл + 5Амлодипін")
            callback_button10 = types.InlineKeyboardButton(text="10\U000026A1 10  ", callback_data="10 мг Периндоприл + 10Амлодипін")
            callback_button11 = types.InlineKeyboardButton(text="14\U000026A1 10 ", callback_data="14 мг Периндоприл + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button5, callback_button6, callback_button7, callback_button8, callback_button9, callback_button10, callback_button11)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 5 мг периндоприла і 5 мг амлодипіна доступна в настпних препаратах: \n\U00002764 БІ-ПРЕСТАРІУМ  \n\U00002764 ПЕРИНДОПРИЛ/АМЛОДИПІН-ТЕВА", reply_markup =keyboard14)
       

        elif call.data == "5 мг Периндоприл + 10Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,5\U000026A1 2,5", callback_data="3,5 мг Периндоприл + 2,5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="4\U000026A1 5 ", callback_data="4 мг Периндоприл + 5Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 10 ", callback_data="4 мг Периндоприл + 10Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 5 ", callback_data="5 мг Периндоприл + 5Амлодипін")
            callback_button6 = types.InlineKeyboardButton(text="7\U000026A1 5 ", callback_data="7 мг Периндоприл + 5Амлодипін")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 5 ", callback_data="8 мг Периндоприл + 5Амлодипін")
            callback_button8 = types.InlineKeyboardButton(text="8\U000026A1 10 ", callback_data="8 мг Периндоприл + 10Амлодипін")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 5 ", callback_data="10 мг Периндоприл + 5Амлодипін")
            callback_button10 = types.InlineKeyboardButton(text="10\U000026A1 10  ", callback_data="10 мг Периндоприл + 10Амлодипін")
            callback_button11 = types.InlineKeyboardButton(text="14\U000026A1 10 ", callback_data="14 мг Периндоприл + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button6, callback_button7, callback_button8, callback_button9, callback_button10, callback_button11)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 5 мг периндоприла і 10 мг амлодипіна доступна в настпних препаратах:\n\U00002764 БІ-ПРЕСТАРІУМ \n\U00002764 ПЕРИНДОПРИЛ/АМЛОДИПІН-ТЕВА ", reply_markup =keyboard14)
        elif call.data == "7 мг Периндоприл + 5Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,5\U000026A1 2,5", callback_data="3,5 мг Периндоприл + 2,5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="4\U000026A1 5 ", callback_data="4 мг Периндоприл + 5Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 10 ", callback_data="4 мг Периндоприл + 10Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 5 ", callback_data="5 мг Периндоприл + 5Амлодипін")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 10 ", callback_data="5 мг Периндоприл + 10Амлодипін")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 5 ", callback_data="8 мг Периндоприл + 5Амлодипін")
            callback_button8 = types.InlineKeyboardButton(text="8\U000026A1 10 ", callback_data="8 мг Периндоприл + 10Амлодипін")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 5 ", callback_data="10 мг Периндоприл + 5Амлодипін")
            callback_button10 = types.InlineKeyboardButton(text="10\U000026A1 10  ", callback_data="10 мг Периндоприл + 10Амлодипін")
            callback_button11 = types.InlineKeyboardButton(text="14\U000026A1 10 ", callback_data="14 мг Периндоприл + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5,  callback_button7, callback_button8, callback_button9, callback_button10, callback_button11)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 7 мг периндоприла і 5 мг амлодипіна доступна в настпних препаратах:\n\U00002764 БІ-ПРЕСТАРІУМ N \n\U00002764 ВІАКОРАМ ", reply_markup =keyboard14)
        elif call.data == "8 мг Периндоприл + 5Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,5\U000026A1 2,5", callback_data="3,5 мг Периндоприл + 2,5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="4\U000026A1 5 ", callback_data="4 мг Периндоприл + 5Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 10 ", callback_data="4 мг Периндоприл + 10Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 5 ", callback_data="5 мг Периндоприл + 5Амлодипін")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 10 ", callback_data="5 мг Периндоприл + 10Амлодипін")
            callback_button6 = types.InlineKeyboardButton(text="7\U000026A1 5 ", callback_data="7 мг Периндоприл + 5Амлодипін")
            callback_button8 = types.InlineKeyboardButton(text="8\U000026A1 10 ", callback_data="8 мг Периндоприл + 10Амлодипін")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 5 ", callback_data="10 мг Периндоприл + 5Амлодипін")
            callback_button10 = types.InlineKeyboardButton(text="10\U000026A1 10  ", callback_data="10 мг Периндоприл + 10Амлодипін")
            callback_button11 = types.InlineKeyboardButton(text="14\U000026A1 10 ", callback_data="14 мг Периндоприл + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6, callback_button8, callback_button9, callback_button10, callback_button11)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 8 мг периндоприла і 5 мг амлодипіна доступна в настпних препаратах:\n\U00002764 АМ-АЛІТЕР  \n\U00002764 АМЛЕCСА \n\U00002764 АМЛОДИПІН-ПЕРИНДОПРИЛ- РІХТЕР  \n\U00002764 ПЕРИНДОПРИЛ /АМЛОДИПІН КРКА   ", reply_markup =keyboard14)
       

        elif call.data == "8 мг Периндоприл + 10Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,5\U000026A1 2,5", callback_data="3,5 мг Периндоприл + 2,5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="4\U000026A1 5 ", callback_data="4 мг Периндоприл + 5Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 10 ", callback_data="4 мг Периндоприл + 10Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 5 ", callback_data="5 мг Периндоприл + 5Амлодипін")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 10 ", callback_data="5 мг Периндоприл + 10Амлодипін")
            callback_button6 = types.InlineKeyboardButton(text="7\U000026A1 5 ", callback_data="7 мг Периндоприл + 5Амлодипін")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 5 ", callback_data="8 мг Периндоприл + 5Амлодипін")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 5 ", callback_data="10 мг Периндоприл + 5Амлодипін")
            callback_button10 = types.InlineKeyboardButton(text="10\U000026A1 10  ", callback_data="10 мг Периндоприл + 10Амлодипін")
            callback_button11 = types.InlineKeyboardButton(text="14\U000026A1 10 ", callback_data="14 мг Периндоприл + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6, callback_button7, callback_button9, callback_button10, callback_button11)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 8 мг периндоприла і 10 мг амлодипіна доступна в настпних препаратах:\n\U00002764 АМ-АЛІТЕР  \n\U00002764 АМЛЕCСА \n\U00002764 АМЛОДИПІН-ПЕРИНДОПРИЛ-РІХТЕР  \n\U00002764 ПЕРИНДОПРИЛ /АМЛОДИПІН КРКА   ", reply_markup =keyboard14)
        elif call.data == "10 мг Периндоприл + 5Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,5\U000026A1 2,5", callback_data="3,5 мг Периндоприл + 2,5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="4\U000026A1 5 ", callback_data="4 мг Периндоприл + 5Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 10 ", callback_data="4 мг Периндоприл + 10Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 5 ", callback_data="5 мг Периндоприл + 5Амлодипін")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 10 ", callback_data="5 мг Периндоприл + 10Амлодипін")
            callback_button6 = types.InlineKeyboardButton(text="7\U000026A1 5 ", callback_data="7 мг Периндоприл + 5Амлодипін")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 5 ", callback_data="8 мг Периндоприл + 5Амлодипін")
            callback_button8 = types.InlineKeyboardButton(text="8\U000026A1 10 ", callback_data="8 мг Периндоприл + 10Амлодипін")
            callback_button10 = types.InlineKeyboardButton(text="10\U000026A1 10  ", callback_data="10 мг Периндоприл + 10Амлодипін")
            callback_button11 = types.InlineKeyboardButton(text="14\U000026A1 10 ", callback_data="14 мг Периндоприл + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6, callback_button7,callback_button8, callback_button10, callback_button11)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг периндоприла і 5 мг амлодипіна доступна в настпних препаратах:\n\U00002764 БІ-ПРЕСТАРІУМ \n\U00002764  ПЕРИНДОПРИЛ/АМЛОДИПІН-ТЕВА     ", reply_markup =keyboard14)
       




        elif call.data == "10 мг Периндоприл + 10Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,5\U000026A1 2,5", callback_data="3,5 мг Периндоприл + 2,5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="4\U000026A1 5 ", callback_data="4 мг Периндоприл + 5Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 10 ", callback_data="4 мг Периндоприл + 10Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 5 ", callback_data="5 мг Периндоприл + 5Амлодипін")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 10 ", callback_data="5 мг Периндоприл + 10Амлодипін")
            callback_button6 = types.InlineKeyboardButton(text="7\U000026A1 5 ", callback_data="7 мг Периндоприл + 5Амлодипін")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 5 ", callback_data="8 мг Периндоприл + 5Амлодипін")
            callback_button8 = types.InlineKeyboardButton(text="8\U000026A1 10 ", callback_data="8 мг Периндоприл + 10Амлодипін")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 5 ", callback_data="10 мг Периндоприл + 5Амлодипін")
            callback_button11 = types.InlineKeyboardButton(text="14\U000026A1 10 ", callback_data="14 мг Периндоприл + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6, callback_button7,callback_button8, callback_button9,  callback_button11)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг периндоприла і 10 мг амлодипіна доступна в настпних препаратах: \n\U00002764 БІ-ПРЕСТАРІУМ \n\U00002764  ПЕРИНДОПРИЛ/АМЛОДИПІН-ТЕВА   ", reply_markup =keyboard14)
       



        elif call.data == "14 мг Периндоприл + 10Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,5\U000026A1 2,5", callback_data="3,5 мг Периндоприл + 2,5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="4\U000026A1 5 ", callback_data="4 мг Периндоприл + 5Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="4\U000026A1 10 ", callback_data="4 мг Периндоприл + 10Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="5\U000026A1 5 ", callback_data="5 мг Периндоприл + 5Амлодипін")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 10 ", callback_data="5 мг Периндоприл + 10Амлодипін")
            callback_button6 = types.InlineKeyboardButton(text="7\U000026A1 5 ", callback_data="7 мг Периндоприл + 5Амлодипін")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 5 ", callback_data="8 мг Периндоприл + 5Амлодипін")
            callback_button8 = types.InlineKeyboardButton(text="8\U000026A1 10 ", callback_data="8 мг Периндоприл + 10Амлодипін")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 5 ", callback_data="10 мг Периндоприл + 5Амлодипін")
            callback_button10 = types.InlineKeyboardButton(text="10\U000026A1 10  ", callback_data="10 мг Периндоприл + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6, callback_button7,callback_button8, callback_button9, callback_button10)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 14 мг периндоприла і 10 мг амлодипіна доступна в настпних препаратах: \n\U00002764 БІ-ПРЕСТАРІУМ N \n\U00002764  ВІАКОРАМ ", reply_markup =keyboard14)
       
#периндоприл і бісопролол
        elif call.data == " 5Периндоприл + 5Бісопролол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="5\U000026A1 10", callback_data=" 5Периндоприл + 10Бісопролол ")
            callback_button3 = types.InlineKeyboardButton(text="10\U000026A1 5", callback_data=" 10Периндоприл + 5Бісопролол")
            callback_button4 = types.InlineKeyboardButton(text="10\U000026A1 10", callback_data="10 Периндоприл + 10Бісопролол")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 5 мг периндоприла і 5 мг бісопролола доступна в настпних препаратах: \n\U00002764 КОСІРЕЛЬ \n\U00002764 ПРЕСТИЛОЛ ", reply_markup =keyboard14)
        elif call.data == " 5Периндоприл + 10Бісопролол ":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="5\U000026A1 5", callback_data=" 5Периндоприл + 5Бісопролол")
            callback_button3 = types.InlineKeyboardButton(text="10\U000026A1 5 ", callback_data=" 10Периндоприл + 5Бісопролол")
            callback_button4 = types.InlineKeyboardButton(text="10\U000026A1 10 ", callback_data="10 Периндоприл + 10Бісопролол")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 5 мг периндоприла і 10 мг бісопролола доступна в настпних препаратах: \n\U00002764 КОСІРЕЛЬ \n\U00002764 ПРЕСТИЛОЛ", reply_markup =keyboard14)
        elif call.data == " 10Периндоприл + 5Бісопролол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="5\U000026A1 5 ", callback_data=" 5Периндоприл + 5Бісопролол")
            callback_button2 = types.InlineKeyboardButton(text="5\U000026A1 10 ", callback_data=" 5Периндоприл + 10Бісопролол ")
            callback_button4 = types.InlineKeyboardButton(text="10\U000026A1 10 ", callback_data="10 Периндоприл + 10Бісопролол")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг периндоприла і 5 мг бісопролола доступна в настпних препаратах: \n\U00002764 КОСІРЕЛЬ \n\U00002764 ПРЕСТИЛОЛ", reply_markup =keyboard14)
        elif call.data == "10 Периндоприл + 10Бісопролол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="5\U000026A1 5 ", callback_data=" 5Периндоприл + 5Бісопролол")
            callback_button2 = types.InlineKeyboardButton(text="5\U000026A1 10 ", callback_data=" 5Периндоприл + 10Бісопролол ")
            callback_button3 = types.InlineKeyboardButton(text="10\U000026A1 5 ", callback_data=" 10Периндоприл + 5Бісопролол")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг периндоприла і 10 мг бісопролола доступна в настпних препаратах: \n\U00002764 КОСІРЕЛЬ \n\U00002764 ПРЕСТИЛОЛ", reply_markup =keyboard14)
       
#периндоприл індапамід і амлодипін
            
        elif call.data == "2 мг\0,625 мг\5 мгПериндоприл ":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625\U000026A1 5 мг", callback_data="2,5 мг\0,625 мг\5 мг Периндоприл ")
            callback_button3 = types.InlineKeyboardButton(text="4 \U000026A1 1,25 \U000026A1 5 мг", callback_data="4 мг\1,25 мг\5 мг Периндоприл ")
            callback_button4 = types.InlineKeyboardButton(text="4\U000026A1 1,25\U000026A1 10 мг", callback_data="4 мг\1,25 мг\10 мг Периндоприл ")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 1,25\U000026A1 10 мг", callback_data="5 мг\1,25 мг\10 мг Периндоприл ")
            callback_button6 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 5 мг", callback_data="8 мг\2,5 мг\5 мг Периндоприл ")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 10 мг", callback_data="8 мг\2,5 мг\10 мг Периндоприл ")
            callback_button8 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 5 мг", callback_data="10 мг\2,5 мг\5 мг Периндоприл ")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 10 мг", callback_data="10 мг\2,5 мг\10 мг Периндоприл ")
            keyboard14.add(callback_button2, callback_button3)   
            keyboard14.add(callback_button4, callback_button5)
            keyboard14.add(callback_button6, callback_button7)
            keyboard14.add(callback_button8, callback_button9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 2 мг периндоприла і 0,625 мг індапаміда і 5 мг амлодипіна доступна в настпних препаратах:\n\U00002764 КО-АМЛЕССА ", reply_markup =keyboard14) 
       
        elif call.data == "2,5 мг\0,625 мг\5 мг Периндоприл ":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625\U000026A1 5 ", callback_data="2 мг\0,625 мг\5 мгПериндоприл ")
            callback_button3 = types.InlineKeyboardButton(text="4 \U000026A1 1,25 \U000026A1 5 мг", callback_data="4 мг\1,25 мг\5 мг Периндоприл ")
            callback_button4 = types.InlineKeyboardButton(text="4\U000026A1 1,25\U000026A1 10 мг", callback_data="4 мг\1,25 мг\10 мг Периндоприл ")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 1,25\U000026A1 10 мг", callback_data="5 мг\1,25 мг\10 мг Периндоприл ")
            callback_button6 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 5 мг", callback_data="8 мг\2,5 мг\5 мг Периндоприл ")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 10 мг", callback_data="8 мг\2,5 мг\10 мг Периндоприл ")
            callback_button8 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 5 мг", callback_data="10 мг\2,5 мг\5 мг Периндоприл ")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 10 мг", callback_data="10 мг\2,5 мг\10 мг Периндоприл ")
            keyboard14.add(callback_button1, callback_button3)  
            keyboard14.add(callback_button4, callback_button5)
            keyboard14.add(callback_button6, callback_button7)
            keyboard14.add(callback_button8, callback_button9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 2,5 мг периндоприла і 0,625 мг індапаміда і 5 мг амлодипіна доступна в настпних препаратах:\n\U00002764 ТРИПЛІКСАМ  ", reply_markup =keyboard14)
       
        elif call.data == "4 мг\1,25 мг\5 мг Периндоприл ":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625\U000026A1 5 ", callback_data="2 мг\0,625 мг\5 мгПериндоприл ")
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625\U000026A1 5 мг", callback_data="2,5 мг\0,625 мг\5 мг Периндоприл ")
            callback_button4 = types.InlineKeyboardButton(text="4\U000026A1 1,25\U000026A1 10 мг", callback_data="4 мг\1,25 мг\10 мг Периндоприл ")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 1,25\U000026A1 10 мг", callback_data="5 мг\1,25 мг\10 мг Периндоприл ")
            callback_button6 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 5 мг", callback_data="8 мг\2,5 мг\5 мг Периндоприл ")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 10 мг", callback_data="8 мг\2,5 мг\10 мг Периндоприл ")
            callback_button8 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 5 мг", callback_data="10 мг\2,5 мг\5 мг Периндоприл ")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 10 мг", callback_data="10 мг\2,5 мг\10 мг Периндоприл ")
            keyboard14.add(callback_button1, callback_button2)  
            keyboard14.add(callback_button4, callback_button5)
            keyboard14.add(callback_button6, callback_button7)
            keyboard14.add(callback_button8, callback_button9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 4 мг периндоприла і 1,25 мг індапаміда і 5 мг амлодипіна доступна в настпних препаратах:\n\U00002764 КО-АМЛЕССА   ", reply_markup =keyboard14)
       
        elif call.data == "4 мг\1,25 мг\10 мг Периндоприл ":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625\U000026A1 5 ", callback_data="2 мг\0,625 мг\5 мгПериндоприл ")
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625\U000026A1 5 мг", callback_data="2,5 мг\0,625 мг\5 мг Периндоприл ")
            callback_button3 = types.InlineKeyboardButton(text="4 \U000026A1 1,25 \U000026A1 5 мг", callback_data="4 мг\1,25 мг\5 мг Периндоприл ")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 1,25\U000026A1 10 мг", callback_data="5 мг\1,25 мг\10 мг Периндоприл ")
            callback_button6 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 5 мг", callback_data="8 мг\2,5 мг\5 мг Периндоприл ")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 10 мг", callback_data="8 мг\2,5 мг\10 мг Периндоприл ")
            callback_button8 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 5 мг", callback_data="10 мг\2,5 мг\5 мг Периндоприл ")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 10 мг", callback_data="10 мг\2,5 мг\10 мг Периндоприл ")
            keyboard14.add(callback_button1, callback_button2)   
            keyboard14.add(callback_button3, callback_button5)
            keyboard14.add(callback_button6, callback_button7)
            keyboard14.add(callback_button8, callback_button9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 4 мг периндоприла і 1,25 мг індапаміда і 10 мг амлодипіна доступна в настпних препаратах:\n\U00002764 КО-АМЛЕССА   ", reply_markup =keyboard14)

        elif call.data == "5 мг\1,25 мг\10 мг Периндоприл ":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625\U000026A1 5 ", callback_data="2 мг\0,625 мг\5 мгПериндоприл ")
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625\U000026A1 5 мг", callback_data="2,5 мг\0,625 мг\5 мг Периндоприл ")
            callback_button3 = types.InlineKeyboardButton(text="4 \U000026A1 1,25 \U000026A1 5 мг", callback_data="4 мг\1,25 мг\5 мг Периндоприл ")
            callback_button4 = types.InlineKeyboardButton(text="4\U000026A1 1,25\U000026A1 10 мг", callback_data="4 мг\1,25 мг\10 мг Периндоприл ")
            callback_button6 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 5 мг", callback_data="8 мг\2,5 мг\5 мг Периндоприл ")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 10 мг", callback_data="8 мг\2,5 мг\10 мг Периндоприл ")
            callback_button8 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 5 мг", callback_data="10 мг\2,5 мг\5 мг Периндоприл ")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 10 мг", callback_data="10 мг\2,5 мг\10 мг Периндоприл ")
            keyboard14.add(callback_button1, callback_button2)   
            keyboard14.add(callback_button3, callback_button4)
            keyboard14.add(callback_button6, callback_button7)
            keyboard14.add(callback_button8, callback_button9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 5 мг периндоприла і 1,25 мг індапаміда і 10 мг амлодипіна доступна в настпних препаратах:\n\U00002764 ТРИПЛІКСАМ  ", reply_markup =keyboard14)
       
        elif call.data == "8 мг\2,5 мг\5 мг Периндоприл ":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625\U000026A1 5 ", callback_data="2 мг\0,625 мг\5 мгПериндоприл ")
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625\U000026A1 5 мг", callback_data="2,5 мг\0,625 мг\5 мг Периндоприл ")
            callback_button3 = types.InlineKeyboardButton(text="4 \U000026A1 1,25 \U000026A1 5 мг", callback_data="4 мг\1,25 мг\5 мг Периндоприл ")
            callback_button4 = types.InlineKeyboardButton(text="4\U000026A1 1,25\U000026A1 10 мг", callback_data="4 мг\1,25 мг\10 мг Периндоприл ")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 1,25\U000026A1 10 мг", callback_data="5 мг\1,25 мг\10 мг Периндоприл ")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 10 мг", callback_data="8 мг\2,5 мг\10 мг Периндоприл ")
            callback_button8 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 5 мг", callback_data="10 мг\2,5 мг\5 мг Периндоприл ")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 10 мг", callback_data="10 мг\2,5 мг\10 мг Периндоприл ")
            keyboard14.add(callback_button1, callback_button2)   
            keyboard14.add(callback_button3, callback_button4)
            keyboard14.add(callback_button5, callback_button7)
            keyboard14.add(callback_button8, callback_button9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 8 мг периндоприла і 2,5 мг індапаміда і 5 мг амлодипіна доступна в настпних препаратах:\n\U00002764 КО-АМЛЕССА ", reply_markup =keyboard14)
       
        elif call.data == "8 мг\2,5 мг\10 мг Периндоприл ":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625\U000026A1 5 ", callback_data="2 мг\0,625 мг\5 мгПериндоприл ")
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625\U000026A1 5 мг", callback_data="2,5 мг\0,625 мг\5 мг Периндоприл ")
            callback_button3 = types.InlineKeyboardButton(text="4 \U000026A1 1,25 \U000026A1 5 мг", callback_data="4 мг\1,25 мг\5 мг Периндоприл ")
            callback_button4 = types.InlineKeyboardButton(text="4\U000026A1 1,25\U000026A1 10 мг", callback_data="4 мг\1,25 мг\10 мг Периндоприл ")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 1,25\U000026A1 10 мг", callback_data="5 мг\1,25 мг\10 мг Периндоприл ")
            callback_button6 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 5 мг", callback_data="8 мг\2,5 мг\5 мг Периндоприл ")
            callback_button8 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 5 мг", callback_data="10 мг\2,5 мг\5 мг Периндоприл ")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 10 мг", callback_data="10 мг\2,5 мг\10 мг Периндоприл ")
            keyboard14.add(callback_button1, callback_button2)  
            keyboard14.add(callback_button3, callback_button4)
            keyboard14.add(callback_button5, callback_button6)
            keyboard14.add(callback_button8, callback_button9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 8 мг периндоприла і 2,5 мг індапаміда і 10 мг амлодипіна доступна в настпних препаратах:\n\U00002764 КО-АМЛЕССА   ", reply_markup =keyboard14)
       
        elif call.data == "10 мг\2,5 мг\5 мг Периндоприл ":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625\U000026A1 5 ", callback_data="2 мг\0,625 мг\5 мгПериндоприл ")
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625\U000026A1 5 мг", callback_data="2,5 мг\0,625 мг\5 мг Периндоприл ")
            callback_button3 = types.InlineKeyboardButton(text="4 \U000026A1 1,25 \U000026A1 5 мг", callback_data="4 мг\1,25 мг\5 мг Периндоприл ")
            callback_button4 = types.InlineKeyboardButton(text="4\U000026A1 1,25\U000026A1 10 мг", callback_data="4 мг\1,25 мг\10 мг Периндоприл ")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 1,25\U000026A1 10 мг", callback_data="5 мг\1,25 мг\10 мг Периндоприл ")
            callback_button6 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 5 мг", callback_data="8 мг\2,5 мг\5 мг Периндоприл ")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 10 мг", callback_data="8 мг\2,5 мг\10 мг Периндоприл ")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 10 мг", callback_data="10 мг\2,5 мг\10 мг Периндоприл ")
            keyboard14.add(callback_button1, callback_button2)  
            keyboard14.add(callback_button3, callback_button4) 
            keyboard14.add(callback_button5, callback_button6)
            keyboard14.add(callback_button7, callback_button9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг периндоприла і 2,5 мг індапаміда і 5 мг амлодипіна доступна в настпних препаратах:\n\U00002764 ТРИПЛІКСАМ ", reply_markup =keyboard14)
       

        elif call.data == "10 мг\2,5 мг\10 мг Периндоприл ":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625\U000026A1 5 ", callback_data="2 мг\0,625 мг\5 мгПериндоприл ")
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625\U000026A1 5 мг", callback_data="2,5 мг\0,625 мг\5 мг Периндоприл ")
            callback_button3 = types.InlineKeyboardButton(text="4 \U000026A1 1,25 \U000026A1 5 мг", callback_data="4 мг\1,25 мг\5 мг Периндоприл ")
            callback_button4 = types.InlineKeyboardButton(text="4\U000026A1 1,25\U000026A1 10 мг", callback_data="4 мг\1,25 мг\10 мг Периндоприл ")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 1,25\U000026A1 10 мг", callback_data="5 мг\1,25 мг\10 мг Периндоприл ")
            callback_button6 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 5 мг", callback_data="8 мг\2,5 мг\5 мг Периндоприл ")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 10 мг", callback_data="8 мг\2,5 мг\10 мг Периндоприл ")
            callback_button8 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 5 мг", callback_data="10 мг\2,5 мг\5 мг Периндоприл ")
            keyboard14.add(callback_button1, callback_button2)   
            keyboard14.add(callback_button3, callback_button4)
            keyboard14.add(callback_button5, callback_button6)
            keyboard14.add(callback_button7, callback_button8)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг периндоприла і 2,5 мг індапаміда і 10 мг амлодипіна доступна в настпних препаратах:\n\U00002764 ТРИПЛІКСАМ ", reply_markup =keyboard14)

#раміприл

        elif call.data == "1,25раміприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="2,5 мг ", callback_data="2,5раміприл")
            callback_button3 = types.InlineKeyboardButton(text="5 мг", callback_data="5раміприл")
            callback_button4 = types.InlineKeyboardButton(text="10 мг ", callback_data="10раміприл")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Раміприл в дозуванні 1,25 мг міститься в таких препаратах:\n\U00002764 АМПРИЛ \n\U00002764 РАМІЗЕС  ", reply_markup =keyboard14)
       
        elif call.data == "2,5раміприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="1,25 мг", callback_data="1,25раміприл")
            callback_button3 = types.InlineKeyboardButton(text="5 мг", callback_data="5раміприл")
            callback_button4 = types.InlineKeyboardButton(text="10 мг ", callback_data="10раміприл")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Раміприл в дозуванні 2,5 мг міститься в таких препаратах:\n\U00002764 АМПРИЛ \n\U00002764 АНГІРАМ \n\U00002764 БРЮМІПРИЛ \n\U00002764 КАРДИПРИЛ \n\U00002764 ПОЛАПРИЛ \n\U00002764 РАМІ САНДОЗ   \n\U00002764 РАМІЗЕС \n\U00002764 РАМІМЕД   \n\U00002764 РАМІПРИЛ-ТЕВА  \n\U00002764 РАМКОР \n\U00002764 ТОПРИЛ \n\U00002764 ХАРТИЛ ", reply_markup =keyboard14)
       
        elif call.data == "5раміприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="1,25 мг", callback_data="1,25раміприл")
            callback_button2 = types.InlineKeyboardButton(text="2,5 мг ", callback_data="2,5раміприл")
            callback_button4 = types.InlineKeyboardButton(text="10 мг ", callback_data="10раміприл")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Раміприл в дозуванні 5 мг міститься в таких препаратах:\n\U00002764 АМПРИЛ \n\U00002764 АНГІРАМ \n\U00002764 БРЮМІПРИЛ \n\U00002764 КАРДИПРИЛ \n\U00002764 ПОЛАПРИЛ \n\U00002764 РАМАГ \n\U00002764 РАМІ САНДОЗ   \n\U00002764 РАМІЗЕС \n\U00002764 РАМІМЕД  \n\U00002764 РАМІПРИЛ АЙКОР  \n\U00002764 РАМІПРИЛ-ТЕВА  \n\U00002764 РАМКОР \n\U00002764 ТОПРИЛ \n\U00002764  ТРИТАЦЕ \n\U00002764  ХАРТИЛ  ", reply_markup =keyboard14)
       
        elif call.data == "10раміприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="1,25 мг", callback_data="1,25раміприл")
            callback_button2 = types.InlineKeyboardButton(text="2,5 мг ", callback_data="2,5раміприл")
            callback_button3 = types.InlineKeyboardButton(text="5 мг", callback_data="5раміприл")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Раміприл в дозуванні 10 мг міститься в таких препаратах:\n\U00002764 АМПРИЛ \n\U00002764 АНГІРАМ \n\U00002764 БРЮМІПРИЛ \n\U00002764 КАРДИПРИЛ \n\U00002764 ПОЛАПРИЛ \n\U00002764 РАМАГ \n\U00002764 РАМІ САНДОЗ  \n\U00002764 РАМІЗЕС \n\U00002764 РАМІМЕД  \n\U00002764 РАМІПРИЛ АЙКОР  \n\U00002764 РАМІПРИЛ-ТЕВА  \n\U00002764 РАМКОР \n\U00002764 ТРИТАЦЕ \n\U00002764 ХАРТИЛ ", reply_markup =keyboard14)
       



       
#раміприл + гідрохлортіазид
        elif call.data == "2,5Раміприл+ 12,5Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="5 \U000026A1 12,5", callback_data="5Раміприл+ 12,5Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="5 \U000026A1 25", callback_data="5Раміприл+ 25Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="10 \U000026A1 12,5", callback_data="10Раміприл+ 12,5Гідрохлортіазид")
            callback_button5 = types.InlineKeyboardButton(text="10 \U000026A1 25", callback_data="10Раміприл+ 25Гідрохлортіазид")
            keyboard14.add(callback_button2, callback_button3, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 2,5 мг раміприла і 12,5 мг гідрохлортіазида  доступна в настпних препаратах:\n\U00002764 АМПРИЛ HL  \n\U00002764 ПРЕВЕНКОР ПЛЮС  \n\U00002764 РАМАГ Н \n\U00002764 РАМАЗІД Н \n\U00002764 РАМІЗЕС КОМ \n\U00002764  РАМІМЕД КОМБІ  \n\U00002764  ХАРТИЛ-Н   ", reply_markup =keyboard14)
        elif call.data == "5Раміприл+ 12,5Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 \U000026A1 12,5", callback_data="2,5Раміприл+ 12,5Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="5 \U000026A1 25", callback_data="5Раміприл+ 25Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="10 \U000026A1 12,5", callback_data="10Раміприл+ 12,5Гідрохлортіазид")
            callback_button5 = types.InlineKeyboardButton(text="10 \U000026A1 25", callback_data="10Раміприл+ 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button3, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 5 мг раміприла і 12,5 мг гідрохлортіазида  доступна в настпних препаратах:\n\U00002764 РАМАЗІД Н \n\U00002764  РАМІЗЕС КОМ  \n\U00002764  ТРИТАЦЕ ПЛЮС ", reply_markup =keyboard14)
        elif call.data == "5Раміприл+ 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 \U000026A1 12,5", callback_data="2,5Раміприл+ 12,5Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="5 \U000026A1 12,5", callback_data="5Раміприл+ 12,5Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="10 \U000026A1 12,5", callback_data="10Раміприл+ 12,5Гідрохлортіазид")
            callback_button5 = types.InlineKeyboardButton(text="10 \U000026A1 25", callback_data="10Раміприл+ 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2,  callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 5 мг раміприла і 25 мг гідрохлортіазида  доступна в настпних препаратах:\n\U00002764  АМПРИЛ HD  \n\U00002764  ПРЕВЕНКОР ПЛЮС \n\U00002764  РАМАГ Н \n\U00002764  РАМАЗІД Н \n\U00002764  РАМІ САНДОЗ КОМПОЗИТУМ \n\U00002764  РАМІЗЕС КОМ \n\U00002764  РАМІМЕД КОМБІ \n\U00002764  ХАРТИЛ-Н   ", reply_markup =keyboard14)
        elif call.data == "10Раміприл+ 12,5Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 \U000026A1 12,5", callback_data="2,5Раміприл+ 12,5Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="5 \U000026A1 12,5", callback_data="5Раміприл+ 12,5Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="5 \U000026A1 25", callback_data="5Раміприл+ 25Гідрохлортіазид")
            callback_button5 = types.InlineKeyboardButton(text="10 \U000026A1 25", callback_data="10Раміприл+ 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг раміприла і 12,5 мг гідрохлортіазида  доступна в настпних препаратах:\n\U00002764 ПРЕВЕНКОР ПЛЮС \n\U00002764 РАМІЗЕС КОМ  \n\U00002764 ТРИТАЦЕ ПЛЮС  ", reply_markup =keyboard14)
        elif call.data == "10Раміприл+ 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 \U000026A1 12,5", callback_data="2,5Раміприл+ 12,5Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="5 \U000026A1 12,5", callback_data="5Раміприл+ 12,5Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="5 \U000026A1 25", callback_data="5Раміприл+ 25Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="10 \U000026A1 12,5", callback_data="10Раміприл+ 12,5Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг раміприла і  25 мг гідрохлортіазида  доступна в настпних препаратах:\n\U00002764 РАМІЗЕС КОМ   ", reply_markup =keyboard14)
#раміприл і амлодипін

        elif call.data == "5Раміприл+ 5Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="5 \U000026A1 10", callback_data="5Раміприл + 10Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="10 \U000026A1 5", callback_data="10Раміприл + 5Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="10 \U000026A1 10", callback_data="10Раміприл + 10Амлодипін")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 5 мг раміприла і  5 мг амлодипіна  доступна в настпних препаратах: \n\U00002764 БІ-РАМАГ   \n\U00002764 СУМІЛАР \n\U00002764 ТРИТАЦЕ-А ", reply_markup =keyboard14)
       
        elif call.data == "5Раміприл + 10Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="5 \U000026A1 5", callback_data="5Раміприл+ 5Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="10 \U000026A1 5", callback_data="10Раміприл + 5Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="10 \U000026A1 10", callback_data="10Раміприл + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 5 мг раміприла і  10 мг амлодипіна  доступна в настпних препаратах:\n\U00002764 БІ-РАМАГ   \n\U00002764 СУМІЛАР ", reply_markup =keyboard14)
       
        elif call.data == "10Раміприл + 5Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="5 \U000026A1 5", callback_data="5Раміприл+ 5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="5 \U000026A1 10", callback_data="5Раміприл + 10Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="10 \U000026A1 10", callback_data="10Раміприл + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг раміприла і  5 мг амлодипіна  доступна в настпних препаратах:\n\U00002764 БІ-РАМАГ  \n\U00002764 СУМІЛАР \n\U00002764 ТРИТАЦЕ-А ", reply_markup =keyboard14)
       
        elif call.data == "10Раміприл + 10Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="5 \U000026A1 5", callback_data="5Раміприл+ 5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="5 \U000026A1 10", callback_data="5Раміприл + 10Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="10 \U000026A1 5", callback_data="10Раміприл + 5Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг раміприла і  10 мг амлодипіна  доступна в настпних препаратах:\n\U00002764 БІ-РАМАГ  \n\U00002764 СУМІЛАР \n\U00002764 ТРИТАЦЕ-А ", reply_markup =keyboard14)
#Лізиноприл

        elif call.data == "2,5лізиноприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5лізиноприл")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10лізиноприл")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20лізиноприл")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лізиноприл в дозуванні 2,5 мг міститься в таких препаратах:\n\U00002764 ВІТОПРИЛ  \n\U00002764 ЛІЗИНОПРИЛ-ТЕВА   ", reply_markup =keyboard14)

        elif call.data == "5лізиноприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5лізиноприл")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10лізиноприл")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20лізиноприл")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лізиноприл в дозуванні 5 мг міститься в таких препаратах: \n\U00002764 АУРОЛАЙЗА \n\U00002764 ВІТОПРИЛ \n\U00002764 ДАПРИЛ \n\U00002764 ДИРОТОН \n\U00002764 ІРУМЕД \n\U00002764 ЛІЗИ САНДОЗ   \n\U00002764 ЛІЗИНОПРИЛ \n\U00002764 ЛІЗИНОПРИЛ КРКА  \n\U00002764 ЛІЗИНОПРИЛ \n\U00002764 ЛЮПІН   \n\U00002764 ЛІЗИНОПРИЛ-АСТРАФАРМ  \n\U00002764 ЛІЗИНОПРИЛ-ТЕВА  \n\U00002764 ЛІНОТОР \n\U00002764 ЛІПРИЛ \n\U00002764 ЛОПРИЛ \n\U00002764 БОСНАЛЕК ", reply_markup =keyboard14)

        elif call.data == "10лізиноприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5лізиноприл")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5лізиноприл")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20лізиноприл")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лізиноприл в дозуванні 10 мг міститься в таких препаратах:\n\U00002764 АУРОЛАЙЗА \n\U00002764 ВІТОПРИЛ \n\U00002764 ДАПРИЛ \n\U00002764 ДИРОТОН \n\U00002764 ІРУМЕД \n\U00002764 ЛІЗИ САНДОЗ   \n\U00002764 ЛІЗИНОПРИЛ \n\U00002764 ЛІЗИНОПРИЛ КРКА \n\U00002764 ЛІЗИНОПРИЛ ЛЮПІН  \n\U00002764 ЛІЗИНОПРИЛ-АСТРАФАРМ \n\U00002764 ЛІЗИНОПРИЛ-ТЕВА  \n\U00002764 ЛІНОТОР \n\U00002764 ЛІПРИЛ \n\U00002764 ЛОПРИЛ \n\U00002764 БОСНАЛЕК \n\U00002764 СКОПРИЛ   ", reply_markup =keyboard14)

        elif call.data == "20лізиноприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5лізиноприл")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5лізиноприл")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10лізиноприл")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лізиноприл в дозуванні 20 мг міститься в таких препаратах:\n\U00002764 АУРОЛАЙЗА \n\U00002764 ВІТОПРИЛ \n\U00002764 ДАПРИЛ \n\U00002764 ДИРОТОН \n\U00002764 ІРУМЕД \n\U00002764 ЛІЗИ САНДОЗ   \n\U00002764 ЛІЗИНОПРИЛ \n\U00002764 ЛІЗИНОПРИЛ КРКА \n\U00002764 ЛІЗИНОПРИЛ ЛЮПІН  \n\U00002764 ЛІЗИНОПРИЛ-АСТРАФАРМ \n\U00002764 ЛІЗИНОПРИЛ-ТЕВА  \n\U00002764 ЛІНОТОР \n\U00002764 ЛІПРИЛ \n\U00002764 ЛОПРИЛ \n\U00002764 БОСНАЛЕК \n\U00002764 СКОПРИЛ  ", reply_markup =keyboard14)

#Лізиноприл з гідрохлортіазидом

        elif call.data == "10Лізиноприл+ 12,5Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="20 \U000026A1 12,5", callback_data="20Лізиноприл+ 12,5Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="20 \U000026A1 25", callback_data="20Лізиноприл+ 25Гідрохлортіазид")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг лізиноприла і  12,5 мг гідрохлортіазида  доступна в настпних препаратах:5 \n\U00002764 КО-ДИРОТОН \n\U00002764 ЛІЗИНОПРАЗИД \n\U00002764 ЛІЗИНОПРИЛ 10 НЛ КРКА \n\U00002764 ЛІЗОРЕТИК \n\U00002764 ЛІЗОТІАЗИД-ТЕВА \n\U00002764 ЛІПРАЗИД \n\U00002764 ЛОПРИЛ \n\U00002764 БОСНАЛЕК Н ", reply_markup =keyboard14)
        elif call.data == "20Лізиноприл+ 12,5Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="10 \U000026A1 12,5", callback_data="10Лізиноприл+ 12,5Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="20 \U000026A1 25", callback_data="20Лізиноприл+ 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 20 мг лізиноприла і  12,5 мг гідрохлортіазида  доступна в настпних препаратах: \n\U00002764 ІРУЗИД \n\U00002764 КО-ДИРОТОН \n\U00002764 ЛІЗИНОПРАЗИД \n\U00002764 ЛІЗИНОПРИЛ 20 НЛ КРКА \n\U00002764 ЛІЗОРЕТИК \n\U00002764 ЛІЗОТІАЗИД-ТЕВА \n\U00002764 ЛІПРАЗИД \n\U00002764 ЛОПРИЛ \n\U00002764 БОСНАЛЕК Н \n\U00002764 СКОПРИЛ ПЛЮС ", reply_markup =keyboard14)
       
        elif call.data == "20Лізиноприл+ 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="10 \U000026A1 12,5", callback_data="10Лізиноприл+ 12,5Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="20 \U000026A1 12,5", callback_data="20Лізиноприл+ 12,5Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 20 мг лізиноприла і  25 мг гідрохлортіазида  доступна в настпних препаратах:20\25  \n\U00002764 ІРУЗИД  ", reply_markup =keyboard14)
       
#Лізиноприл з амлодипіном

        
        
        elif call.data == "5Лізиноприл+ 5Амлодипіна":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="10 \U000026A1 5", callback_data="10Лізиноприл+ 5Амлодипіна")
            callback_button3 = types.InlineKeyboardButton(text="20 \U000026A1 5", callback_data="20Лізиноприл+ 5Амлодипіна")
            callback_button4 = types.InlineKeyboardButton(text="20 \U000026A1 10", callback_data="20Лізиноприл+ 10Амлодипіна")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 5 мг лізиноприла і   5 мг амлодипіна  доступна в наступних препаратах:\n\U00002764 АМАПІН-Л \n\U00002764 АМЛІПІН ", reply_markup =keyboard14)
        elif call.data == "10Лізиноприл+ 5Амлодипіна":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="5 \U000026A1 5", callback_data="5Лізиноприл+ 5Амлодипіна")
            callback_button3 = types.InlineKeyboardButton(text="20 \U000026A1 5", callback_data="20Лізиноприл+ 5Амлодипіна")
            callback_button4 = types.InlineKeyboardButton(text="20 \U000026A1 10", callback_data="20Лізиноприл+ 10Амлодипіна")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг лізиноприла і   5 мг амлодипіна  доступна в наступних препаратах:\n\U00002764 ЕКВАТОР \n\U00002764 КОМБІПРИЛ-КВ ", reply_markup =keyboard14)
        elif call.data == "20Лізиноприл+ 5Амлодипіна":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="5 \U000026A1 5", callback_data="5Лізиноприл+ 5Амлодипіна")
            callback_button2 = types.InlineKeyboardButton(text="10 \U000026A1 5", callback_data="10Лізиноприл+ 5Амлодипіна")
            callback_button4 = types.InlineKeyboardButton(text="20 \U000026A1 10", callback_data="20Лізиноприл+ 10Амлодипіна")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 20 мг лізиноприла і   5 мг амлодипіна  доступна в наступних препаратах:\n\U00002764 ЕКВАТОР ", reply_markup =keyboard14)
        elif call.data == "20Лізиноприл+ 10Амлодипіна":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="5 \U000026A1 5", callback_data="5Лізиноприл+ 5Амлодипіна")
            callback_button2 = types.InlineKeyboardButton(text="10 \U000026A1 5", callback_data="10Лізиноприл+ 5Амлодипіна")
            callback_button3 = types.InlineKeyboardButton(text="20 \U000026A1 5", callback_data="20Лізиноприл+ 5Амлодипіна")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 20 мг лізиноприла і   10 мг амлодипіна  доступна в наступних препаратах:\n\U00002764 ЕКВАТОР ", reply_markup =keyboard14)
#Каптоприл
        elif call.data == "Каптоприл":  
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="12,5 мг", callback_data="Каптоприл")
            callback_button2 = types.InlineKeyboardButton(text="25 мг ", callback_data="Каптоприл")
            callback_button3 = types.InlineKeyboardButton(text="50 мг", callback_data="Каптоприл")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Каптоприл має такі дозування: ", reply_markup =keyboard14)
       





            
        elif call.data == "50Каптоприл+ 12,5Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="50 \U000026A1 25", callback_data="50Каптоприл+ 25Гідрохлортіазид")
            keyboard14.add(callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 50 мг каптоприла і   12,5 мг гідрохлортіазида  доступна в наступних препаратах:\n\U00002764 КАПОТІАЗИД \n\U00002764 КАПТОПРЕС 12,5-ДАРНИЦЯ   ", reply_markup =keyboard14)
        elif call.data == "50Каптоприл+ 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="50 \U000026A1 12,5", callback_data="50Каптоприл+ 12,5Гідрохлортіазид")
            keyboard14.add(callback_button1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 50 мг каптоприла і   25 мг гідрохлортіазида  доступна в наступних препаратах:\n\U00002764 КАПТОПРЕС-ДАРНИЦЯ  \n\U00002764 НОРМОПРЕС ", reply_markup =keyboard14)
       
#Еналаприл
        elif call.data == "2,5Еналаприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5Еналаприл")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10Еналаприл")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20Еналаприл")
            callback_button5 = types.InlineKeyboardButton(text="Розчин", callback_data="РозчинЕналаприл")
            keyboard14.add(callback_button2, callback_button3, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Еналаприл в дозуванні 2,5 мг міститься в таких препаратах:\n\U00002764 ЕНАЛАПРИЛ КРКА \n\U00002764 ЕНАЛАПРИЛ-ТЕВА \n\U00002764 ЕНАМ \n\U00002764 ЕНАП ", reply_markup =keyboard14)
        elif call.data == "5Еналаприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5Еналаприл")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10Еналаприл")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20Еналаприл")
            callback_button5 = types.InlineKeyboardButton(text="Розчин", callback_data="РозчинЕналаприл")
            keyboard14.add(callback_button1, callback_button3, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Еналаприл в дозуванні,5 мг міститься в таких препаратах: \n\U00002764 БЕРЛІПРИЛ \n\U00002764  ЕНАЛАПРИЛ КРКА \n\U00002764 ЕНАЛАПРИЛ-ЗДОРОВ'Я \n\U00002764 ЕНАЛАПРИЛ-ТЕВА \n\U00002764 ЕНАЛОЗИД МОНО \n\U00002764 ЕНАМ \n\U00002764 ЕНАП ", reply_markup =keyboard14)
       
        elif call.data == "10Еналаприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5Еналаприл")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5Еналаприл")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20Еналаприл")
            callback_button5 = types.InlineKeyboardButton(text="Розчин", callback_data="РозчинЕналаприл")
            keyboard14.add(callback_button1, callback_button2, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Еналаприл в дозуванні 10 мг міститься в таких препаратах:\n\U00002764 БЕРЛІПРИЛ \n\U00002764 ЕНА САНДОЗ \n\U00002764 ЕНАЛАПРИЛ \n\U00002764 ЕНАЛАПРИЛ КРКА \n\U00002764 ЕНАЛАПРИЛ-АСТРАФАРМ \n\U00002764 ЕНАЛАПРИЛ-ДAРНИЦЯ \n\U00002764 ЕНАЛАПРИЛ-ЗДОРОВ'Я \n\U00002764 ЕНАЛАПРИЛ-ТЕВА \n\U00002764 ЕНАЛОЗИД МОНО \n\U00002764 ЕНАМ \n\U00002764 ЕНАП \n\U00002764 РЕНІТЕК ", reply_markup =keyboard14)
        elif call.data == "20Еналаприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5Еналаприл")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5Еналаприл")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10Еналаприл")
            callback_button5 = types.InlineKeyboardButton(text="Розчин", callback_data="РозчинЕналаприл")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Еналаприл в дозуванні 20 мг міститься в таких препаратах:\n\U00002764 БЕРЛІПРИЛ \n\U00002764 ЕНА САНДОЗ\n\U00002764  ЕНАЛАПРИЛ\n\U00002764  ЕНАЛАПРИЛ КРКА \n\U00002764 ЕНАЛАПРИЛ-АСТРАФАРМ \n\U00002764 ЕНАЛАПРИЛ-ЗДОРОВ'Я \n\U00002764 ЕНАЛАПРИЛ-ТЕВА \n\U00002764 ЕНАП \n\U00002764 РЕНІТЕК ", reply_markup =keyboard14)
        elif call.data == "РозчинЕналаприл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5Еналаприл")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5Еналаприл")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10Еналаприл")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20Еналаприл")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Розчин для ін’єкцій 1мл – 1,25 мг еналаприлату містить:   \n\U00002764 ЕНАП ", reply_markup =keyboard14)
#Еналаприл + Гідрохлортіазид

        elif call.data == "5Еналаприл+ 12,5Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="10 \U000026A1 12,5", callback_data="10Еналаприл+ 12,5Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="10 \U000026A1 25", callback_data="10Еналаприл+ 25Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="20 \U000026A1 12,5", callback_data="20Еналаприл+ 12,5Гідрохлортіазид")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 5 мг каптоприла і   12,5 мг гідрохлортіазида  доступна в наступних препаратах: \n\U00002764 ЕНАПРІЛ-Н ", reply_markup =keyboard14)
        
        elif call.data == "10Еналаприл+ 12,5Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="5 \U000026A1 12,5", callback_data="5Еналаприл+ 12,5Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="10 \U000026A1 25", callback_data="10Еналаприл+ 25Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="20 \U000026A1 12,5", callback_data="20Еналаприл+ 12,5Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг каптоприла і   12,5 мг гідрохлортіазида  доступна в наступних препаратах: \n\U00002764 ЕНАЛАПРИЛ /ГІДРОХЛОРОТІАЗИД  КРКА   \n\U00002764 ЕНАЛАПРИЛ-НL-ЗДОРОВ'Я \n\U00002764 ЕНАЛОЗИД \n\U00002764 ЕНАП-НL ", reply_markup =keyboard14)
        
        elif call.data == "10Еналаприл+ 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="5 \U000026A1 12,5", callback_data="5Еналаприл+ 12,5Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="10 \U000026A1 12,5", callback_data="10Еналаприл+ 12,5Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="20 \U000026A1 12,5", callback_data="20Еналаприл+ 12,5Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 10 мг каптоприла і   25 мг гідрохлортіазида  доступна в наступних препаратах: \n\U00002764 БЕРЛІПРИЛ \n\U00002764 ЕНАЛАПРИЛ /ГІДРОХЛОРОТІАЗИД  КРКА \n\U00002764 ЕНАЛАПРИЛ Н-ТЕВА   \n\U00002764 ЕНАЛАПРИЛ Н-ФАРМЕКС \n\U00002764 ЕНАЛАПРИЛ-Н-ЗДОРОВ'Я \n\U00002764 ЕНАЛОЗИД \n\U00002764 ЕНАП-H ", reply_markup =keyboard14)


        elif call.data == "20Еналаприл+ 12,5Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="5 \U000026A1 12,5", callback_data="5Еналаприл+ 12,5Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="10 \U000026A1 12,5", callback_data="10Еналаприл+ 12,5Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="10 \U000026A1 25", callback_data="10Еналаприл+ 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 20 мг каптоприла і   12,5 мг гідрохлортіазида  доступна в наступних препаратах: \n\U00002764 ЕНАЛАПРИЛ /ГІДРОХЛОРОТІАЗИД  КРКА   \n\U00002764 ЕНАЛОЗИД ФОРТЕ \n\U00002764 ЕНАП 20 HL \n\U00002764 КО-РЕНІТЕК", reply_markup =keyboard14)

        elif call.data == "10Еналаприл+ Індапамід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="20 \U000026A1 2,5", callback_data="20Еналаприл+ Індапамід")
            keyboard14.add(callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 10 мг еналаприла і 2,5 мг індапаміда має такі дозування: \n\U00002764 ЕНЗИКС, \n\U00002764 ЕНЗИКС ДУО   ", reply_markup =keyboard14)
        elif call.data == "20Еналаприл+ Індапамід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="10 \U000026A1 2,5", callback_data="10Еналаприл+ Індапамід")
            keyboard14.add(callback_button1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 20 мг еналаприла і 2,5 мг індапаміда має такі дозування: \n\U00002764 ЕНЗИКС ДУО ФОРТЕ  ", reply_markup =keyboard14)


        elif call.data == "10Еналаприл+ 10Лерканідипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="20 \U000026A1 10", callback_data="20Еналаприл+ 10Лерканідипін")
            callback_button3 = types.InlineKeyboardButton(text="20 \U000026A1 20", callback_data="200Еналаприл+ 20Лерканідипін")
            keyboard14.add( callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 10 мг еналаприла і 10 мг лерканідипіна  має такі дозування: \n\U00002764 ЕНАП Л КОМБІ, \n\U00002764 КОРІПРЕН", reply_markup =keyboard14)
       
        elif call.data == "20Еналаприл+ 10Лерканідипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="10 \U000026A1 10", callback_data="10Еналаприл+ 10Лерканідипін")
            callback_button3 = types.InlineKeyboardButton(text="20 \U000026A1 20", callback_data="200Еналаприл+ 20Лерканідипін")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 20 мг еналаприла і 10 мг лерканідипіна  має такі дозування:\n\U00002764 ЕНАП Л КОМБІ, \n\U00002764 КОРІПРЕН ", reply_markup =keyboard14)
       
        elif call.data == "200Еналаприл+ 20Лерканідипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="10 \U000026A1 10", callback_data="10Еналаприл+ 10Лерканідипін")
            callback_button2 = types.InlineKeyboardButton(text="20 \U000026A1 10", callback_data="20Еналаприл+ 10Лерканідипін")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 20 мг еналаприла і 20 мг лерканідипіна  має такі дозування: \n\U00002764 КОРІПРЕН", reply_markup =keyboard14)
       
 #АРА ІІ
 #Лозартан


        elif call.data == "12,5лозартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="25 мг ", callback_data="25лозартан")
            callback_button3 = types.InlineKeyboardButton(text="50 мг", callback_data="50лозартан")
            callback_button4 = types.InlineKeyboardButton(text="100 мг ", callback_data="100лозартан")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лозартан в дозуванні 12,5 мг міститься в таких препаратах: \n\U00002764 ВАЗОТЕНЗ \n\U00002764 ЛОЗАРТАН-ТЕВА  \n\U00002764 ЛОРІСТА   ", reply_markup =keyboard14)
       
        elif call.data == "25лозартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="12,5 мг", callback_data="12,5лозартан")
            callback_button3 = types.InlineKeyboardButton(text="50 мг", callback_data="50лозартан")
            callback_button4 = types.InlineKeyboardButton(text="100 мг ", callback_data="100лозартан")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Лозартан в дозуванні 25 мг міститься в таких препаратах: \n\U00002764 АНГІЗАР \n\U00002764 ВАЗОТЕНЗ \n\U00002764 КЛОСАРТ \n\U00002764 ЛОЗАРТАН-ТЕВА   \n\U00002764 ЛОРІСТА \n\U00002764 ТРОСАН   ", reply_markup =keyboard14)
       
        elif call.data == "50лозартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="12,5 мг", callback_data="12,5лозартан")
            callback_button2 = types.InlineKeyboardButton(text="25 мг ", callback_data="25лозартан")
            callback_button4 = types.InlineKeyboardButton(text="100 мг ", callback_data="100лозартан")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лозартан в дозуванні 50 мг міститься в таких препаратах: \n\U00002764 АНГІЗАР \n\U00002764 ВАЗОТЕНЗ \n\U00002764 КЛОСАРТ  \n\U00002764 ЛОЗАП \n\U00002764 ЛОЗАРТАН КРКА  \n\U00002764 ЛОЗАРТАН-ТЕВА   \n\U00002764 ЛОРІСТА \n\U00002764 ЛОТАР \n\U00002764 ПРЕСАРТАН \n\U00002764 СЕНТОР \n\U00002764 ТРОСАН   ", reply_markup =keyboard14)
       
        elif call.data == "100лозартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="12,5 мг", callback_data="12,5лозартан")
            callback_button2 = types.InlineKeyboardButton(text="25 мг ", callback_data="25лозартан")
            callback_button3 = types.InlineKeyboardButton(text="50 мг", callback_data="50лозартан")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Лозартан в дозуванні 100 мг міститься в таких препаратах:\n\U00002764 ВАЗОТЕНЗ \n\U00002764 КЛОСАРТ  \n\U00002764 ЛОЗАП  \n\U00002764 ЛОЗАРТАН КРКА  \n\U00002764 ЛОЗАРТАН-ТЕВА \n\U00002764 ЛОРІСТА \n\U00002764 ЛОТАР \n\U00002764 ПРЕСАРТАН \n\U00002764 СЕНТОР \n\U00002764 ТРОСАН ", reply_markup =keyboard14)
       
#Лозартан і гідрохлортіазид

        elif call.data == "50Лозартан + 12,5Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="100 \U000026A1 12,5", callback_data="100Лозартан + 12,5Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="100 \U000026A1 25", callback_data="100Лозартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 50 мг лозартана і 12,5 мг гідрохлортіазида має такі дозування: \n\U00002764 АНГІЗАР ПЛЮС  \n\U00002764 ВАЗОТЕНЗ Н \n\U00002764 КО-СЕНТОР  \n\U00002764 ЛОЗАП ПЛЮС \n\U00002764 ЛОЗАРТАН /ГІДРОХЛОРОТІАЗИД  КРКА  \n\U00002764 ЛОЗАРТАН ПЛЮС-ТЕВА  \n\U00002764 ЛОРІСТА Н \n\U00002764 ПРЕСАРТАН Н-50  \n\U00002764 САРТОКАД-Н   ", reply_markup =keyboard14)
        elif call.data == "100Лозартан + 12,5Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="50 \U000026A1 12,5", callback_data="50Лозартан + 12,5Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="100 \U000026A1 25", callback_data="100Лозартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 100 мг лозартана і 12,5 мг гідрохлортіазида має такі дозування:\n\U00002764 ВАЗОТЕНЗ Н \n\U00002764 КО-СЕНТОР  \n\U00002764 ЛОЗАРТАН /ГІДРОХЛОРОТІАЗИД  КРКА \n\U00002764 ЛОРІСТА Н 100    ", reply_markup =keyboard14)
       
        elif call.data == "100Лозартан + 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="50 \U000026A1 12,5", callback_data="50Лозартан + 12,5Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="100 \U000026A1 12,5", callback_data="100Лозартан + 12,5Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 100 мг лозартана і 25 мг гідрохлортіазида має такі дозування:\n\U00002764 ВАЗОТЕНЗ Н \n\U00002764 КО-СЕНТОР  \n\U00002764 ЛОЗАП 100 ПЛЮС  \n\U00002764 ЛОЗАРТАН /ГІДРОХЛОРОТІАЗИД  КРКА \n\U00002764 ЛОЗАРТАН ПЛЮС-ТЕВА  \n\U00002764 ЛОРІСТА НD \n\U00002764 САРТОКАД-Н", reply_markup =keyboard14)
       
#Лозартан і амлодипін

        elif call.data == "50Лозартан + 5Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="50 \U000026A1 10", callback_data="50Лозартан + 10Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="100 \U000026A1 5", callback_data="100Лозартан + 5Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="100 \U000026A1 10", callback_data="100Лозартан + 10Амлодипін")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 50 мг лозартана і 5 мг амлодипіна має такі дозування: \n\U00002764 АМОСАРТАН \n\U00002764 ЛОРТЕНЗА   ", reply_markup =keyboard14)
       
        elif call.data == "50Лозартан + 10Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="50 \U000026A1 5", callback_data="50Лозартан + 5Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="100 \U000026A1 5", callback_data="100Лозартан + 5Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="100 \U000026A1 10", callback_data="100Лозартан + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 50 мг лозартана і 10 мг амлодипіна має такі дозування:\n\U00002764 ЛОРТЕНЗА   ", reply_markup =keyboard14)


        elif call.data == "100Лозартан + 5Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="50 \U000026A1 5", callback_data="50Лозартан + 5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="50 \U000026A1 10", callback_data="50Лозартан + 10Амлодипін")
            callback_button4 = types.InlineKeyboardButton(text="100 \U000026A1 10", callback_data="100Лозартан + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 100 мг лозартана і 5 мг амлодипіна має такі дозування: \n\U00002764 АМОСАРТАН \n\U00002764 ЛОРТЕНЗА  ", reply_markup =keyboard14)
       
        elif call.data == "100Лозартан + 10Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="50 \U000026A1 5", callback_data="50Лозартан + 5Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="50 \U000026A1 10", callback_data="50Лозартан + 10Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="100 \U000026A1 5", callback_data="100Лозартан + 5Амлодипін")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 100 мг лозартана і 10 мг амлодипіна має такі дозування: \n\U00002764 ЛОРТЕНЗА  ", reply_markup =keyboard14)
       
#Валсартан
            
        elif call.data == "40валсартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="80 мг ", callback_data="80валсартан")
            callback_button3 = types.InlineKeyboardButton(text="160 мг", callback_data="160валсартан")
            callback_button4 = types.InlineKeyboardButton(text="320 мг ", callback_data="320валсартан")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Валсартан в дозуванні 40 мг міститься в таких препаратах: \n\U00002764 ВАЗАР \n\U00002764  ВАЛЕЗА \n\U00002764 ВАЛМІСАР \n\U00002764 ВАЛСАРТАН \n\U00002764 ВАЛСАРТАН-РІХТЕР \n\U00002764 ВАЛЬСАКОР  ", reply_markup =keyboard14)
       
        elif call.data == "80валсартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40валсартан")
            callback_button3 = types.InlineKeyboardButton(text="160 мг", callback_data="160валсартан")
            callback_button4 = types.InlineKeyboardButton(text="320 мг ", callback_data="320валсартан")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Валсартан в дозуванні 80 мг міститься в таких препаратах:\n\U00002764 ВАЗАР \n\U00002764 ВАЛЕЗА \n\U00002764 ВАЛМІСАР \n\U00002764 ВАЛСАР \n\U00002764 ВАЛСАРТАН  \n\U00002764 ВАЛСАРТАН КРКА   \n\U00002764 ВАЛСАРТАН САНДОЗ  \n\U00002764 ВАЛСАРТАН-РІХТЕР \n\U00002764 ВАЛЬСАКОР \n\U00002764 ВАНАТЕКС \n\U00002764 ДІОВАН \n\U00002764 ДІОКОР СОЛО \n\U00002764 ДІОСТАР \n\U00002764 КАРДОПАН-САНОВЕЛЬ \n\U00002764  САКОРД \n\U00002764 САРТОКАД-В      ", reply_markup =keyboard14)
       
        
        elif call.data == "160валсартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40валсартан")
            callback_button2 = types.InlineKeyboardButton(text="80 мг ", callback_data="80валсартан")
            callback_button4 = types.InlineKeyboardButton(text="320 мг ", callback_data="320валсартан")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Валсартан в дозуванні 160 мг міститься в таких препаратах: \n\U00002764 ВАЗАР \n\U00002764 ВАЛЕЗА \n\U00002764 ВАЛМІСАР  \n\U00002764 ВАЛСАР  \n\U00002764 ВАЛСАРТАН  \n\U00002764 ВАЛСАРТАН КРКА  \n\U00002764 ВАЛСАРТАН САНДОЗ   \n\U00002764 ВАЛСАРТАН-РІХТЕР  \n\U00002764 ВАЛЬСАКОР \n\U00002764 ВАНАТЕКС \n\U00002764 ДІОВАН \n\U00002764 ДІОКОР СОЛО \n\U00002764 ДІОСТАР \n\U00002764 КАРДОПАН-САНОВЕЛЬ  \n\U00002764 САКОРД \n\U00002764 САРТОКАД-В     ", reply_markup =keyboard14)
       

        elif call.data == "320валсартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40валсартан")
            callback_button2 = types.InlineKeyboardButton(text="80 мг ", callback_data="80валсартан")
            callback_button3 = types.InlineKeyboardButton(text="160 мг", callback_data="160валсартан")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Валсартан в дозуванні 320 мг міститься в таких препаратах:\n\U00002764 ВАЗАР \n\U00002764 ВАЛМІСАР  \n\U00002764 ВАЛСАРТАН  \n\U00002764 ВАЛСАРТАН КРКА  \n\U00002764 ВАЛЬСАКОР  \n\U00002764 КАРДОПАН-САНОВЕЛЬ      ", reply_markup =keyboard14)
       
#Валсартан і гідрохлортіазид
       

        elif call.data == "80Валсартан + Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="160 \U000026A1 12,5", callback_data="160Валсартан + Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="160 \U000026A1 25", callback_data="160Валсартан + 25Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="320 \U000026A1 12,5", callback_data="320Валсартан + Гідрохлортіазид")
            callback_button5 = types.InlineKeyboardButton(text="320 \U000026A1 25", callback_data="320Валсартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button2, callback_button3, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 80 мг валсартана і 12,5 мг гідрохлортіазида має такі дозування: \n\U00002764 ВАЗАР Н  \n\U00002764 ВАЛМІСАР H  \n\U00002764 ВАЛСАР-Н  \n\U00002764 ВАЛСАРТАН /ГІДРОХЛОРОТІАЗИД  КРКА  \n\U00002764 ВАЛСАРТАН САНДОЗ КОМПОЗИТУМ  \n\U00002764 ВАЛЬСАКОР Н \n\U00002764 ВАНАТЕКС КОМБІ  \n\U00002764 ДІОКОР 80 \n\U00002764 КО-ДІОВАН  \n\U00002764 КОРСАР Н  \n\U00002764 САКОРД Н  \n\U00002764 ТІАРА ДУО    ", reply_markup =keyboard14)
       
        elif call.data == "160Валсартан + Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="80 \U000026A1 12,5", callback_data="80Валсартан + Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="160 \U000026A1 25", callback_data="160Валсартан + 25Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="320 \U000026A1 12,5", callback_data="320Валсартан + Гідрохлортіазид")
            callback_button5 = types.InlineKeyboardButton(text="320 \U000026A1 25", callback_data="320Валсартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button3, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 160 мг валсартана і 12,5 мг гідрохлортіазида має такі дозування: \n\U00002764 ВАЗАР Н  \n\U00002764 ВАЛМІСАР H  \n\U00002764 ВАЛСАРТАН /ГІДРОХЛОРОТІАЗИД  КРКА  \n\U00002764 ВАЛСАРТАН САНДОЗ КОМПОЗИТУМ  \n\U00002764 ВАЛЬСАКОР H \n\U00002764 ВАНАТЕКС КОМБІ  \n\U00002764 ДІОКОР 160 \n\U00002764 КО-ДІОВАН  \n\U00002764 КОРСАР Н \n\U00002764 САКОРД Н \n\U00002764 ТІАРА ДУО    ", reply_markup =keyboard14)
       
        elif call.data == "160Валсартан + 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="80 \U000026A1 12,5", callback_data="80Валсартан + Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="160 \U000026A1 12,5", callback_data="160Валсартан + Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="320 \U000026A1 12,5", callback_data="320Валсартан + Гідрохлортіазид")
            callback_button5 = types.InlineKeyboardButton(text="320 \U000026A1 25", callback_data="320Валсартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 160 мг валсартана і 25 мг гідрохлортіазида має такі дозування: \n\U00002764 ВАЗАР Н  \n\U00002764 ВАЛМІСАР H  \n\U00002764 ВАЛСАР-Н  \n\U00002764 ВАЛСАРТАН /ГІДРОХЛОРОТІАЗИД  КРКА \n\U00002764 ВАЛСАРТАН САНДОЗ КОМПОЗИТУМ \n\U00002764 ВАЛЬСАКОР HD \n\U00002764 ВАНАТЕКС КОМБІ \n\U00002764 КО-ДІОВАН \n\U00002764 КОРСАР Н  \n\U00002764  ТІАРА ДУО     ", reply_markup =keyboard14)
       
        elif call.data == "320Валсартан + Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="80 \U000026A1 12,5", callback_data="80Валсартан + Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="160 \U000026A1 12,5", callback_data="160Валсартан + Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="160 \U000026A1 25", callback_data="160Валсартан + 25Гідрохлортіазид")
            callback_button5 = types.InlineKeyboardButton(text="320 \U000026A1 25", callback_data="320Валсартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 320 мг валсартана і 12,5 мг гідрохлортіазида має такі дозування:\n\U00002764 ВАЗАР Н  \n\U00002764 ВАЛМІСАР H \n\U00002764 ВАЛСАРТАН /ГІДРОХЛОРОТІАЗИД  КРКА \n\U00002764 ВАЛЬСАКОР Н \n\U00002764 КО-ДІОВАН  \n\U00002764 КОРСАР Н    ", reply_markup =keyboard14)
       
        
        elif call.data == "320Валсартан + 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="80 \U000026A1 12,5", callback_data="80Валсартан + Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="160 \U000026A1 12,5", callback_data="160Валсартан + Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="160 \U000026A1 25", callback_data="160Валсартан + 25Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="320 \U000026A1 12,5", callback_data="320Валсартан + Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 320 мг валсартана і 25 мг гідрохлортіазида має такі дозування:\n\U00002764 ВАЗАР Н  \n\U00002764 ВАЛМІСАР H  \n\U00002764 ВАЛСАРТАН /ГІДРОХЛОРОТІАЗИД  КРКА  \n\U00002764 ВАЛЬСАКОР НD \n\U00002764 КО-ДІОВАН  \n\U00002764 КОРСАР Н   ", reply_markup =keyboard14)
       
#Валсартан і амлодипін

        elif call.data == "80Валсартан + Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="160 \U000026A1 5", callback_data="160Валсартан + Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="160 \U000026A1 10", callback_data="160Валсартан + 10Амлодипін")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 80 мг валсартана і 5 мг амлодипіна має такі дозування: \n\U00002764 АМЛОСАРТАН \n\U00002764 БІ-САКОРД \n\U00002764 ВАЗАР А \n\U00002764 ВАЛОДІП  \n\U00002764 ДІФОРС  \n\U00002764 ЕКСФОРЖ  ", reply_markup =keyboard14)
       
        elif call.data == "160Валсартан + Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="80 \U000026A1 5", callback_data="80Валсартан + Амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="160 \U000026A1 10", callback_data="160Валсартан + 10Амлодипін")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 160 мг валсартана і 5 мг амлодипіна має такі дозування: \n\U00002764 АМЛОСАРТАН \n\U00002764 БІ-САКОРД \n\U00002764 ВАЗАР А \n\U00002764 ВАЛЄМБІК  \n\U00002764 ВАЛОДІП  \n\U00002764 ВАЛСАР-АМ  \n\U00002764 ДІФОРС \n\U00002764 ЕКСФОРЖ \n\U00002764 КОМБІСАРТ   ", reply_markup =keyboard14)
       
        
        elif call.data == "160Валсартан + 10Амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="80 \U000026A1 5", callback_data="80Валсартан + Амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="160 \U000026A1 5", callback_data="160Валсартан + Амлодипін")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 160 мг валсартана і 10 мг амлодипіна має такі дозування: \n\U00002764 АМЛОСАРТАН  \n\U00002764 БІ-САКОРД  \n\U00002764 ВАЗАР А \n\U00002764 ВАЛЄМБІК  \n\U00002764 ВАЛОДІП  \n\U00002764 ВАЛСАР-АМ   \n\U00002764 ДІФОРС XL   \n\U00002764 ЕКСФОРЖ \n\U00002764 КОМБІСАРТ  ", reply_markup =keyboard14)
                   
#валсартан гідрохлортіазид і амлодипін


        elif call.data == "160Валсартан + 12,5Гідрохлортіазид +А":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="160 \U000026A1 12,5 \U000026A1 10", callback_data="160Валсартан + 12,5Гідрохлортіазид +10А")
            callback_button3 = types.InlineKeyboardButton(text="160 \U000026A1 25 \U000026A1 5 ", callback_data="160Валсартан + 25Гідрохлортіазид + А")
            callback_button4 = types.InlineKeyboardButton(text="320 \U000026A1 25 \U000026A1 10", callback_data="320Валсартан + 25Гідрохлортіазид + 10А")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Потрійна комбінація 160 мг валсартана, 12,5 мг гідрохлортіазида і 5 мг амлодипіна має такі дозування: \n\U00002764 ЕКСФОРЖ Н \n\U00002764 КОМБІСАРТ Н \n\U00002764 ТІАРА ТРІО    ", reply_markup =keyboard14)
       
        elif call.data == "160Валсартан + 12,5Гідрохлортіазид +10А":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="160 \U000026A1 12,5 \U000026A1 5", callback_data="160Валсартан + 12,5Гідрохлортіазид +А")
            callback_button3 = types.InlineKeyboardButton(text="160 \U000026A1 25 \U000026A1 5 ", callback_data="160Валсартан + 25Гідрохлортіазид + А")
            callback_button4 = types.InlineKeyboardButton(text="320 \U000026A1 25 \U000026A1 10", callback_data="320Валсартан + 25Гідрохлортіазид + 10А")
            keyboard14.add(callback_button1,callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Потрійна комбінація 160 мг валсартана, 12,5 мг гідрохлортіазида і 10 мг амлодипіна має такі дозування:\n\U00002764 ЕКСФОРЖ Н  \n\U00002764 КОМБІСАРТ Н  \n\U00002764 ТІАРА ТРІО      ", reply_markup =keyboard14)
       
        elif call.data == "160Валсартан + 25Гідрохлортіазид + А":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="160 \U000026A1 12,5 \U000026A1 5", callback_data="160Валсартан + 12,5Гідрохлортіазид +А")
            callback_button2 = types.InlineKeyboardButton(text="160 \U000026A1 12,5 \U000026A1 10", callback_data="160Валсартан + 12,5Гідрохлортіазид +10А")
            callback_button4 = types.InlineKeyboardButton(text="320 \U000026A1 25 \U000026A1 10", callback_data="320Валсартан + 25Гідрохлортіазид + 10А")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Потрійна комбінація 160 мг валсартана, 25 мг гідрохлортіазида і 5 мг амлодипіна має такі дозування: \n\U00002764 ЕКСФОРЖ Н", reply_markup =keyboard14)
       
        elif call.data == "320Валсартан + 25Гідрохлортіазид + 10А":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="160 \U000026A1 12,5 \U000026A1 5", callback_data="160Валсартан + 12,5Гідрохлортіазид +А")
            callback_button2 = types.InlineKeyboardButton(text="160 \U000026A1 12,5 \U000026A1 10", callback_data="160Валсартан + 12,5Гідрохлортіазид +10А")
            callback_button3 = types.InlineKeyboardButton(text="160 \U000026A1 25 \U000026A1 5 ", callback_data="160Валсартан + 25Гідрохлортіазид + А")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Потрійна комбінація 160 мг валсартана, 25 мг гідрохлортіазида і 10 мг амлодипіна має такі дозування: \n\U00002764 ЕКСФОРЖ Н", reply_markup =keyboard14)
#Ірбесартан

        elif call.data == "75ірбесартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="150 мг ", callback_data="150ірбесартан")
            callback_button3 = types.InlineKeyboardButton(text="300 мг", callback_data="300ірбесартан")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Ірбесартан в дозуванні 75 мг містять препарати: \n\U00002764  ІСТАР \n\U00002764  РОТАЗАР \n\U00002764 ФІРМАСТА   ", reply_markup =keyboard14)
       
        elif call.data == "150ірбесартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="75 мг", callback_data="75ірбесартан")
            callback_button3 = types.InlineKeyboardButton(text="300 мг", callback_data="300ірбесартан")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Ірбесартан в дозуванні 150 мг містять препарати: \n\U00002764 АПРОВЕЛЬ \n\U00002764 ІРБЕССО \n\U00002764 ІСТАР \n\U00002764 КОНВЕРІУМ \n\U00002764 РОТАЗАР \n\U00002764 ФІРМАСТА   ", reply_markup =keyboard14)
       

        elif call.data == "300ірбесартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="75 мг", callback_data="75ірбесартан")
            callback_button2 = types.InlineKeyboardButton(text="150 мг ", callback_data="150ірбесартан")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Ірбесартан в дозуванні 300 мг містять препарати: \n\U00002764 АПРОВЕЛЬ \n\U00002764 ІРБЕССО \n\U00002764 ІРБЕТАН \n\U00002764 ІСТАР \n\U00002764 КОНВЕРІУМ \n\U00002764 РОТАЗАР \n\U00002764 ФІРМАСТА   ", reply_markup =keyboard14)
       
#Ірбесартан і гідрохлортіазид
        elif call.data == "150Ірбесартан + Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="300 \U000026A1 12,5", callback_data="300Ірбесартан + Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="300 \U000026A1 25", callback_data="300Ірбесартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 150 мг ірбесартана і 12,5 мг гідрохлортіазида має такі дозування: \n\U00002764 ІРБАТАЛ-Н \n\U00002764  ІРБЕТАН-Н \n\U00002764 ІСТАР H \n\U00002764 КО-ІРБЕСАН \n\U00002764 КО-ІРБЕССО \n\U00002764  ФІРМАСТА Н  ", reply_markup =keyboard14)

        elif call.data == "300Ірбесартан + Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="150 \U000026A1 12,5", callback_data="150Ірбесартан + Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="300 \U000026A1 25", callback_data="300Ірбесартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 300 мг ірбесартана і 12,5 мг гідрохлортіазида має такі дозування:\n\U00002764  ІРБАТАЛ-Н  \n\U00002764 ІРБЕТАН-Н \n\U00002764 ІСТАР H \n\U00002764 КО-ІРБЕСАН \n\U00002764 КО-ІРБЕССО \n\U00002764 ФІРМАСТА Н    ", reply_markup =keyboard14)

        elif call.data == "300Ірбесартан + 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="150 \U000026A1 12,5", callback_data="150Ірбесартан + Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="300 \U000026A1 12,5", callback_data="300Ірбесартан + Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 300 мг ірбесартана і 25 мг гідрохлортіазида має такі дозування: \n\U00002764 ІСТАР H \n\U00002764 ФІРМАСТА НD   ", reply_markup =keyboard14)
       
#Кандесартан
            
        elif call.data == "4кандесартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="8 мг ", callback_data="8кандесартан")
            callback_button3 = types.InlineKeyboardButton(text="16 мг", callback_data="16кандесартан")
            callback_button4 = types.InlineKeyboardButton(text="32 мг ", callback_data="32кандесартан")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Кандесартан в дозуванні 4 мг містять препарати: \n\U00002764 КАНДЕКОР \n\U00002764 КАНДЕСАР        ", reply_markup =keyboard14)
        elif call.data == "8кандесартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="4 мг", callback_data="4кандесартан")
            callback_button3 = types.InlineKeyboardButton(text="16 мг", callback_data="16кандесартан")
            callback_button4 = types.InlineKeyboardButton(text="32 мг ", callback_data="32кандесартан")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Кандесартан в дозуванні 8 мг містять препарати:\n\U00002764  АЙРА-САНОВЕЛЬ \n\U00002764 АТАКАНД  \n\U00002764 КАНДЕКОР \n\U00002764 КАНДЕСАР  \n\U00002764 КАНТАБ  \n\U00002764 КАРЗАП  \n\U00002764 КАСАРК     ", reply_markup =keyboard14)
       
        elif call.data == "16кандесартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="4 мг", callback_data="4кандесартан")
            callback_button2 = types.InlineKeyboardButton(text="8 мг ", callback_data="8кандесартан")
            callback_button4 = types.InlineKeyboardButton(text="32 мг ", callback_data="32кандесартан")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Кандесартан в дозуванні 16 мг містять препарати: \n\U00002764 АЙРА-САНОВЕЛЬ  \n\U00002764  АТАКАНД  \n\U00002764 КАНДЕКОР \n\U00002764 КАНДЕСАР  \n\U00002764 КАНТАБ  \n\U00002764 КАРЗАП  \n\U00002764 КАСАРК    ", reply_markup =keyboard14)
       
        elif call.data == "32кандесартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="4 мг", callback_data="4кандесартан")
            callback_button2 = types.InlineKeyboardButton(text="8 мг ", callback_data="8кандесартан")
            callback_button3 = types.InlineKeyboardButton(text="16 мг", callback_data="16кандесартан")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Кандесартан в дозуванні 32 мг містять препарати: \n\U00002764 КАНДЕКОР \n\U00002764 КАНДЕСАР \n\U00002764 КАНТАБ  \n\U00002764 КАСАРК    ", reply_markup =keyboard14)
       
#Кандесартан і гідрохлортіазид
        
        elif call.data == "8Кандесартан + Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="16 \U000026A1 12,5", callback_data="16Кандесартан + Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="32 \U000026A1 12,5", callback_data="32Кандесартан + Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="32 \U000026A1 25", callback_data="32Кандесартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 8 мг кандесартана і 12,5 мг гідрохлортіазида має такі дозування: \n\U00002764 КАНДЕКОР H   ", reply_markup =keyboard14)
       
        elif call.data == "16Кандесартан + Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="8 \U000026A1 12,5", callback_data="8Кандесартан + Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="32 \U000026A1 12,5", callback_data="32Кандесартан + Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="32 \U000026A1 25", callback_data="32Кандесартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 16 мг кандесартана і 12,5 мг гідрохлортіазида має такі дозування: \n\U00002764 АТАКАНД ПЛЮС  \n\U00002764 КАНДЕКОР H \n\U00002764 КАНТАБ ПЛЮС  \n\U00002764 ХІЗАРТ-H   ", reply_markup =keyboard14)
       
        elif call.data == "32Кандесартан + Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="8 \U000026A1 12,5", callback_data="8Кандесартан + Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="16 \U000026A1 12,5", callback_data="16Кандесартан + Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="32 \U000026A1 25", callback_data="32Кандесартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2,  callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 32 мг кандесартана і 12,5 мг гідрохлортіазида має такі дозування:  \n\U00002764 КАНДЕКОР H \n\U00002764 КАНТАБ ПЛЮС   ", reply_markup =keyboard14)
       
        elif call.data == "32Кандесартан + 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="8 \U000026A1 12,5", callback_data="8Кандесартан + Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="16 \U000026A1 12,5", callback_data="16Кандесартан + Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="32 \U000026A1 12,5", callback_data="32Кандесартан + Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 32 мг кандесартана і 25 мг гідрохлортіазида має такі дозування: \n\U00002764 КАНДЕКОР HD \n\U00002764 ХІЗАРТ-H-ДС   ", reply_markup =keyboard14)
       
#Кандесартан і амлодипін
        elif call.data == "8Кандесартан + 5Амлодипіна":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="16 \U000026A1 5", callback_data="Кандесартан + 5Амлодипіна")
            callback_button3 = types.InlineKeyboardButton(text="16 \U000026A1 10", callback_data="Кандесартан + 10Амлодипіна")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 8 мг кандесартана і 5 мг амлодипіна має такі дозування: \n\U00002764 КАРЗАП-А  \n\U00002764 САРТАПІН   ", reply_markup =keyboard14)
        elif call.data == "Кандесартан + 5Амлодипіна":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="8 \U000026A1 5", callback_data="8Кандесартан + 5Амлодипіна")
            callback_button3 = types.InlineKeyboardButton(text="16 \U000026A1 10", callback_data="Кандесартан + 10Амлодипіна")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 16 мг кандесартана і 5 мг амлодипіна має такі дозування: \n\U00002764 САРТАПІН   ", reply_markup =keyboard14)
       
        elif call.data == "Кандесартан + 10Амлодипіна":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="8 \U000026A1 5", callback_data="8Кандесартан + 5Амлодипіна")
            callback_button2 = types.InlineKeyboardButton(text="16 \U000026A1 5", callback_data="Кандесартан + 5Амлодипіна")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 16 мг кандесартана і 10 мг амлодипіна має такі дозування: \n\U00002764 КАРЗАП-А \n\U00002764 САРТАПІН   ", reply_markup =keyboard14)
       
#Телмісартан
        elif call.data == "20телмісартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="40 мг ", callback_data="40телмісартан")
            callback_button3 = types.InlineKeyboardButton(text="80 мг", callback_data="80телмісартан")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Телмісартан в дозуванні 20 мг містять препарати: \n\U00002764 ТЕЛМІЛАКС \n\U00002764 ТЕЛМІСТА \n\U00002764 ТЕЛНОР  \n\U00002764 ТЕЛПРЕС  \n\U00002764 ХІПОТЕЛ  ", reply_markup =keyboard14)
        elif call.data == "40телмісартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="20 мг", callback_data="20телмісартан")
            callback_button3 = types.InlineKeyboardButton(text="80 мг", callback_data="80телмісартан")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Телмісартан в дозуванні 40 мг містять препарати: \n\U00002764 ТЕЛМІЛАКС \n\U00002764 ТЕЛМІСТА \n\U00002764 ТЕЛНОР  \n\U00002764 ТЕЛПРЕС  \n\U00002764 ТЕЛСАРТАН  \n\U00002764 ТСАРТ \n\U00002764 ХІПОТЕЛ   ", reply_markup =keyboard14)
        elif call.data == "80телмісартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="20 мг", callback_data="20телмісартан")
            callback_button2 = types.InlineKeyboardButton(text="40 мг ", callback_data="40телмісартан")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Телмісартан в дозуванні 80 мг містять препарати:\n\U00002764 МІКАРДИС \n\U00002764 ТЕЛМІЛАКС \n\U00002764 ТЕЛМІНОРМ \n\U00002764 ТЕЛМІСАРТАН-ТЕВА \n\U00002764 ТЕЛМІСТА \n\U00002764 ТЕЛНОР  \n\U00002764 ТЕЛПРЕС  \n\U00002764 ТЕЛСАРТАН \n\U00002764 ТСАРТ  \n\U00002764 ХІПОТЕЛ ", reply_markup =keyboard14)

#Телмісартан і гідрохлортіазид
        elif call.data == "40Телмісартан + Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="80 \U000026A1 12,5", callback_data="80Телмісартан + Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="80 \U000026A1 25", callback_data="80Телмісартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 40 мг телмісартана і 12,5 мг гідрохлортіазида має такі дозування:\n\U00002764 ІЗІКАРД Н \n\U00002764 МІКАРДИСПЛЮС \n\U00002764 ТЕЛМІЛАКС ПЛЮС  \n\U00002764 ТЕЛПРЕС ПЛЮС \n\U00002764 ТЕЛСАРТАН-Н  \n\U00002764 ТЕЛСІ Н \n\U00002764 ТЕЛЬМІСТА H   ", reply_markup =keyboard14)
        elif call.data == "80Телмісартан + Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 \U000026A1 12,5", callback_data="40Телмісартан + Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="80 \U000026A1 25", callback_data="80Телмісартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 80 мг телмісартана і 12,5 мг гідрохлортіазида має такі дозування:\n\U00002764 ІЗІКАРД Н \n\U00002764 МІКАРДИСПЛЮС \n\U00002764 ТЕЛМІЛАКС ПЛЮС  \n\U00002764 ТЕЛПРЕС ПЛЮС \n\U00002764 ТЕЛСАРТАН-Н \n\U00002764 ТЕЛЬМІСТА H    ", reply_markup =keyboard14)
        elif call.data == "80Телмісартан + 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 \U000026A1 12,5", callback_data="40Телмісартан + Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="80 \U000026A1 12,5", callback_data="80Телмісартан + Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 80 мг телмісартана і 25 мг гідрохлортіазида має такі дозування: \n\U00002764 ІЗІКАРД Н \n\U00002764 ТЕЛМІЛАКС ПЛЮС  \n\U00002764 ТЕЛПРЕС ПЛЮС \n\U00002764 ТЕЛЬМІСТА НD   ", reply_markup =keyboard14)
       


            
#Телмісартан і амлодипін
        elif call.data == "40Телмісартан+ 5Амлодипіна":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="40 \U000026A1 10", callback_data="40Телмісартан+ 10Амлодипіна")
            callback_button3 = types.InlineKeyboardButton(text="80 \U000026A1 5", callback_data="80Телмісартан+ 5Амлодипіна")
            callback_button4 = types.InlineKeyboardButton(text="80 \U000026A1 10", callback_data="80Телмісартан+ 10Амлодипіна")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 40 мг телмісартана і 5 мг амлодипіна має такі дозування: \n\U00002764 ІЗІКАРД A  \n\U00002764 ТЕЛДІПІН  ", reply_markup =keyboard14)
        elif call.data == "40Телмісартан+ 10Амлодипіна":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 \U000026A1 5", callback_data="40Телмісартан+ 5Амлодипіна")
            callback_button3 = types.InlineKeyboardButton(text="80 \U000026A1 5", callback_data="80Телмісартан+ 5Амлодипіна")
            callback_button4 = types.InlineKeyboardButton(text="80 \U000026A1 10", callback_data="80Телмісартан+ 10Амлодипіна")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 40 мг телмісартана і 10 мг амлодипіна має такі дозування: \n\U00002764 ІЗІКАРД A  \n\U00002764 ТЕЛДІПІН  ", reply_markup =keyboard14)
        elif call.data == "80Телмісартан+ 5Амлодипіна":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 \U000026A1 5", callback_data="40Телмісартан+ 5Амлодипіна")
            callback_button2 = types.InlineKeyboardButton(text="40 \U000026A1 10", callback_data="40Телмісартан+ 10Амлодипіна")
            callback_button4 = types.InlineKeyboardButton(text="80 \U000026A1 10", callback_data="80Телмісартан+ 10Амлодипіна")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Комбінація 80 мг телмісартана і 5 мг амлодипіна має такі дозування: \n\U00002764 ІЗІКАРД A  \n\U00002764 ТЕЛДІПІН   ", reply_markup =keyboard14)
        elif call.data == "80Телмісартан+ 10Амлодипіна":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 \U000026A1 5", callback_data="40Телмісартан+ 5Амлодипіна")
            callback_button2 = types.InlineKeyboardButton(text="40 \U000026A1 10", callback_data="40Телмісартан+ 10Амлодипіна")
            callback_button3 = types.InlineKeyboardButton(text="80 \U000026A1 5", callback_data="80Телмісартан+ 5Амлодипіна")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 80 мг телмісартана і 10 мг амлодипіна має такі дозування: \n\U00002764 ІЗІКАРД A  \n\U00002764 ТЕЛДІПІН   ", reply_markup =keyboard14)
#Олмесартан
            
        elif call.data == "10олмесартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="20 мг ", callback_data="20олмесартан")
            callback_button3 = types.InlineKeyboardButton(text="40 мг", callback_data="40олмесартан")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Олмесартан в дозуванні 10 мг містять препарати: \n\U00002764 КАРДОСАЛ  \n\U00002764 ОЛІМЕСТРА    ", reply_markup =keyboard14)
       
        elif call.data == "20олмесартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="10 мг", callback_data="10олмесартан")
            callback_button3 = types.InlineKeyboardButton(text="40 мг", callback_data="40олмесартан")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Олмесартан в дозуванні 20 мг містять препарати:\n\U00002764 КАРДОСАЛ  \n\U00002764 ОЛЕМБІК \n\U00002764 ОЛІМЕСТРА \n\U00002764 ОЛМЕСАР  ", reply_markup =keyboard14)
        elif call.data == "40олмесартан":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="10 мг", callback_data="10олмесартан")
            callback_button2 = types.InlineKeyboardButton(text="20 мг ", callback_data="20олмесартан")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Олмесартан в дозуванні 40 мг містять препарати: \n\U00002764 КАРДОСАЛ  \n\U00002764 ОЛЕМБІК \n\U00002764 ОЛІМЕСТРА   ", reply_markup =keyboard14)
#Олмесартан і гідротіазид

        elif call.data == "20Олмесартан + Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="20 \U000026A1 25", callback_data="20Олмесартан + 25Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="40 \U000026A1 12,5", callback_data="40Олмесартан + Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="40 \U000026A1 25", callback_data="40Олмесартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button2, callback_button3, callback_button4 )
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 20 мг олмесартана і 12,5 мг гідрохлортіазида має такі дозування: \n\U00002764 КАРДОСАЛ ПЛЮС \n\U00002764 ОЛЕМБІК-Н \n\U00002764 ОЛІМЕСТРА H   ", reply_markup =keyboard14)
       
        elif call.data == "20Олмесартан + 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="20 \U000026A1 12,5", callback_data="20Олмесартан + Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="40 \U000026A1 12,5", callback_data="40Олмесартан + Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="40 \U000026A1 25", callback_data="40Олмесартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button3,callback_button4 )
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="  Комбінація 20 мг олмесартана і 25 мг гідрохлортіазида має такі дозування: \n\U00002764 КАРДОСАЛ ПЛЮС  \n\U00002764 ОЛІМЕСТРА HD    ", reply_markup =keyboard14)
       
        elif call.data == "40Олмесартан + Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="20 \U000026A1 12,5", callback_data="20Олмесартан + Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="20 \U000026A1 25", callback_data="20Олмесартан + 25Гідрохлортіазид")
            callback_button4 = types.InlineKeyboardButton(text="40 \U000026A1 25", callback_data="40Олмесартан + 25Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 40 мг олмесартана і 12,5 мг гідрохлортіазида має такі дозування: \n\U00002764 ОЛЕМБІК-Н \n\U00002764 ОЛІМЕСТРА H     ", reply_markup =keyboard14)
       
        elif call.data == "40Олмесартан + 25Гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="20 \U000026A1 12,5", callback_data="20Олмесартан + Гідрохлортіазид")
            callback_button2 = types.InlineKeyboardButton(text="20 \U000026A1 25", callback_data="20Олмесартан + 25Гідрохлортіазид")
            callback_button3 = types.InlineKeyboardButton(text="40 \U000026A1 12,5", callback_data="40Олмесартан + Гідрохлортіазид")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Комбінація 40 мг олмесартана і 25 мг гідрохлортіазида має такі дозування: \n\U00002764 ОЛІМЕСТРА HD ", reply_markup =keyboard14)
#Діуретики
        elif call.data == "25гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="100 мг ", callback_data="100гідрохлортіазид")
            keyboard14.add( callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Гідрохлортіазид в дозуванні 25 мг містять препарати: \n\U00002764 ГІДРОХЛОРТІАЗИД \n\U00002764 ГІПОТІАЗИД   ", reply_markup =keyboard14)


        elif call.data == "100гідрохлортіазид":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="25 мг", callback_data="25гідрохлортіазид")
            keyboard14.add(callback_button1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Гідрохлортіазид в дозуванні 100 мг містять препарати: \n\U00002764 ГІПОТІАЗИД ", reply_markup =keyboard14)

        elif call.data == "125індапамід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="1,5 мг ", callback_data="15індапамід")
            callback_button3 = types.InlineKeyboardButton(text="2,5 мг", callback_data="25індапамід")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Індапамід в дозуванні 1,25 мг містять препарати:\n\U00002764 ІНДАП    ", reply_markup =keyboard14)
        elif call.data == "15індапамід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="1,25 мг", callback_data="125індапамід")
            callback_button3 = types.InlineKeyboardButton(text="2,5 мг", callback_data="25індапамід")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Індапамід в дозуванні 1,5 мг містять препарати:\n\U00002764 АРИФОН РЕТАРД  \n\U00002764 ВАЗОПАМІД \n\U00002764 ІНДАПАМІД-ТЕВА \n\U00002764 ІНДАПЕН SR \n\U00002764 РАВЕЛ SR \n\U00002764 СОФТЕНЗИФ \n\U00002764 ХЕМОПАМІД РЕТАРД      ", reply_markup =keyboard14)
        
        elif call.data == "25індапамід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="1,25 мг", callback_data="125індапамід")
            callback_button2 = types.InlineKeyboardButton(text="1,5 мг ", callback_data="15індапамід")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Індапамід в дозуванні 2,5 мг містять препарати: \n\U00002764 АРИФОН \n\U00002764 ІНДАБРЮ \n\U00002764 ІНДАП \n\U00002764 ІНДАПАМІД \n\U00002764 ІНДАПАМІД-АСТРАФАРМ  \n\U00002764 ІНДАПЕН  \n\U00002764 ІНДОПРЕС  \n\U00002764 ІПАМІД   ", reply_markup =keyboard14)
       
        elif call.data == "40фуросемід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="Розчин", callback_data="Розчин фуросемід")
            keyboard14.add(callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Фуросемід в дозуванні 40 мг містять препарати: \n\U00002764 ЛАЗИКС \n\U00002764 ФУРОСЕМІД \n\U00002764 ФУРОСЕМІД СОФАРМА  \n\U00002764 ФУРОСЕМІД-ДАРНИЦЯ     ", reply_markup =keyboard14)
       
        elif call.data == "Розчин фуросемід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40фуросемід")
            keyboard14.add(callback_button1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Фуросемід в розчинній формі для ін'єкцій  2 мл 1% амп. містять препарати: \n\U00002764 ЛАЗИКС НЕО  \n\U00002764 ФУРОСЕМІД  \n\U00002764 ФУРОСЕМІД-ДАРНИЦЯ     ", reply_markup =keyboard14)

        elif call.data == "2,5торасемід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5торасемід")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10торасемід")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20торасемід")
            callback_button5 = types.InlineKeyboardButton(text="50 мг", callback_data="50торасемід")
            callback_button6 = types.InlineKeyboardButton(text="100 мг ", callback_data="100торасемід")
            callback_button7 = types.InlineKeyboardButton(text="200 мг", callback_data="200торасемід")
            callback_button8 = types.InlineKeyboardButton(text="2 мл 0,5%", callback_data="2млторасемід")
            callback_button9 = types.InlineKeyboardButton(text="4 мл 0,5%", callback_data="4млторасемід")
            callback_button10 = types.InlineKeyboardButton(text="20 мл 1%", callback_data="20млторасемід")
            keyboard14.add(callback_button2)
            keyboard14.add(callback_button3, callback_button4)
            keyboard14.add(callback_button5, callback_button6)
            keyboard14.add(callback_button7, callback_button8)
            keyboard14.add(callback_button9, callback_button10)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Торасемід в дозуванні 2,5 мг містить препарат: \n\U00002764 ТРИГРИМ   ", reply_markup =keyboard14)
       
        
        elif call.data == "5торасемід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5торасемід")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10торасемід")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20торасемід")
            callback_button5 = types.InlineKeyboardButton(text="50 мг", callback_data="50торасемід")
            callback_button6 = types.InlineKeyboardButton(text="100 мг ", callback_data="100торасемід")
            callback_button7 = types.InlineKeyboardButton(text="200 мг", callback_data="200торасемід")
            callback_button8 = types.InlineKeyboardButton(text="2 мл 0,5%", callback_data="2млторасемід")
            callback_button9 = types.InlineKeyboardButton(text="4 мл 0,5%", callback_data="4млторасемід")
            callback_button10 = types.InlineKeyboardButton(text="20 мл 1%", callback_data="20млторасемід")
            keyboard14.add(callback_button1)
            keyboard14.add(callback_button3, callback_button4)
            keyboard14.add(callback_button5, callback_button6)
            keyboard14.add(callback_button7, callback_button8)
            keyboard14.add(callback_button9, callback_button10)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Торасемід в дозуванні 5 мг містять препарати: \n\U00002764 БРІТОМАР \n\U00002764 ТОРАСЕМІД САНДОЗ  \n\U00002764 ТОРАСЕМІД-ДАРНИЦЯ  \n\U00002764 ТОРАСЕМІД-ТЕВА  \n\U00002764 ТОРІКАРД \n\U00002764 ТОРСИД \n\U00002764 ТРИГРИМ \n\U00002764 ТРИФАС СOR ", reply_markup =keyboard14)
       
        elif call.data == "10торасемід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5торасемід")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5торасемід")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20торасемід")
            callback_button5 = types.InlineKeyboardButton(text="50 мг", callback_data="50торасемід")
            callback_button6 = types.InlineKeyboardButton(text="100 мг ", callback_data="100торасемід")
            callback_button7 = types.InlineKeyboardButton(text="200 мг", callback_data="200торасемід")
            callback_button8 = types.InlineKeyboardButton(text="2 мл 0,5%", callback_data="2млторасемід")
            callback_button9 = types.InlineKeyboardButton(text="4 мл 0,5%", callback_data="4млторасемід")
            callback_button10 = types.InlineKeyboardButton(text="20 мл 1%", callback_data="20млторасемід")
            keyboard14.add(callback_button1, callback_button2)
            keyboard14.add(callback_button4)
            keyboard14.add(callback_button5, callback_button6)
            keyboard14.add(callback_button7, callback_button8)
            keyboard14.add(callback_button9, callback_button10)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Торасемід в дозуванні 10 мг містять препарати:\n\U00002764 БРІТОМАР \n\U00002764 ТОР-ЛУП \n\U00002764 ТОРАДІВ \n\U00002764 ТОРАРЕН \n\U00002764 ТОРАСЕМІД САНДОЗ \n\U00002764 ТОРАСЕМІД-ДАРНИЦЯ  \n\U00002764 ТОРАСЕМІД-ТЕВА  \n\U00002764 ТОРІКАРД  \n\U00002764 ТОРСИД \n\U00002764 ТРИГРИМ \n\U00002764 ТРИФАС    ", reply_markup =keyboard14)
       
        elif call.data == "20торасемід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5торасемід")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5торасемід")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10торасемід")
            callback_button5 = types.InlineKeyboardButton(text="50 мг", callback_data="50торасемід")
            callback_button6 = types.InlineKeyboardButton(text="100 мг ", callback_data="100торасемід")
            callback_button7 = types.InlineKeyboardButton(text="200 мг", callback_data="200торасемід")
            callback_button8 = types.InlineKeyboardButton(text="2 мл 0,5%", callback_data="2млторасемід")
            callback_button9 = types.InlineKeyboardButton(text="4 мл 0,5%", callback_data="4млторасемід")
            callback_button10 = types.InlineKeyboardButton(text="20 мл 1%", callback_data="20млторасемід")
            keyboard14.add(callback_button1, callback_button2)
            keyboard14.add(callback_button3)
            keyboard14.add(callback_button5, callback_button6)
            keyboard14.add(callback_button7, callback_button8)
            keyboard14.add(callback_button9, callback_button10)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Торасемід в дозуванні 20 мг містять препарати: \n\U00002764 ТОРАСЕМІД САНДОЗ    ", reply_markup =keyboard14)
       

        elif call.data == "50торасемід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5торасемід")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5торасемід")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10торасемід")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20торасемід")
            callback_button6 = types.InlineKeyboardButton(text="100 мг ", callback_data="100торасемід")
            callback_button7 = types.InlineKeyboardButton(text="200 мг", callback_data="200торасемід")
            callback_button8 = types.InlineKeyboardButton(text="2 мл 0,5%", callback_data="2млторасемід")
            callback_button9 = types.InlineKeyboardButton(text="4 мл 0,5%", callback_data="4млторасемід")
            callback_button10 = types.InlineKeyboardButton(text="20 мл 1%", callback_data="20млторасемід")
            keyboard14.add(callback_button1, callback_button2)
            keyboard14.add(callback_button3, callback_button4)
            keyboard14.add(callback_button6)
            keyboard14.add(callback_button7, callback_button8)
            keyboard14.add(callback_button9, callback_button10)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Торасемід в дозуванні 50 мг містять препарати:  \n\U00002764 ТОРАСЕМІД САНДОЗ    ", reply_markup =keyboard14)
       

        elif call.data == "100торасемід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5торасемід")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5торасемід")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10торасемід")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20торасемід")
            callback_button5 = types.InlineKeyboardButton(text="50 мг", callback_data="50торасемід")
            callback_button7 = types.InlineKeyboardButton(text="200 мг", callback_data="200торасемід")
            callback_button8 = types.InlineKeyboardButton(text="2 мл 0,5%", callback_data="2млторасемід")
            callback_button9 = types.InlineKeyboardButton(text="4 мл 0,5%", callback_data="4млторасемід")
            callback_button10 = types.InlineKeyboardButton(text="20 мл 1%", callback_data="20млторасемід")
            keyboard14.add(callback_button1, callback_button2)
            keyboard14.add(callback_button3, callback_button4)
            keyboard14.add(callback_button5)
            keyboard14.add(callback_button7, callback_button8)
            keyboard14.add(callback_button9, callback_button10)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Торасемід в дозуванні 100 мг містять препарати:  \n\U00002764 ТОРАСЕМІД САНДОЗ    ", reply_markup =keyboard14)
       

        elif call.data == "200торасемід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5торасемід")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5торасемід")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10торасемід")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20торасемід")
            callback_button5 = types.InlineKeyboardButton(text="50 мг", callback_data="50торасемід")
            callback_button6 = types.InlineKeyboardButton(text="100 мг ", callback_data="100торасемід")
            callback_button8 = types.InlineKeyboardButton(text="2 мл 0,5%", callback_data="2млторасемід")
            callback_button9 = types.InlineKeyboardButton(text="4 мл 0,5%", callback_data="4млторасемід")
            callback_button10 = types.InlineKeyboardButton(text="20 мл 1%", callback_data="20млторасемід")
            keyboard14.add(callback_button1, callback_button2)
            keyboard14.add(callback_button3, callback_button4)
            keyboard14.add(callback_button5, callback_button6)
            keyboard14.add(callback_button8)
            keyboard14.add(callback_button9, callback_button10)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Торасемід в дозуванні 200 мг містять препарати: \n\U00002764 ТОРАСЕМІД САНДОЗ  \n\U00002764 ТРИФАС  ", reply_markup =keyboard14)
       

        elif call.data == "2млторасемід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5торасемід")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5торасемід")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10торасемід")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20торасемід")
            callback_button5 = types.InlineKeyboardButton(text="50 мг", callback_data="50торасемід")
            callback_button6 = types.InlineKeyboardButton(text="100 мг ", callback_data="100торасемід")
            callback_button7 = types.InlineKeyboardButton(text="200 мг", callback_data="200торасемід")
            callback_button9 = types.InlineKeyboardButton(text="4 мл 0,5%", callback_data="4млторасемід")
            callback_button10 = types.InlineKeyboardButton(text="20 мл 1%", callback_data="20млторасемід")
            keyboard14.add(callback_button1, callback_button2)
            keyboard14.add(callback_button3, callback_button4)
            keyboard14.add(callback_button5, callback_button6)
            keyboard14.add(callback_button7)
            keyboard14.add(callback_button9, callback_button10)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Торасемід в ампулах 2 мл 0,5% містять препарати: \n\U00002764 ТОРСИД \n\U00002764 ТРИФАС АМПУЛИ     ", reply_markup =keyboard14)
       



        elif call.data == "4млторасемід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5торасемід")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5торасемід")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10торасемід")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20торасемід")
            callback_button5 = types.InlineKeyboardButton(text="50 мг", callback_data="50торасемід")
            callback_button6 = types.InlineKeyboardButton(text="100 мг ", callback_data="100торасемід")
            callback_button7 = types.InlineKeyboardButton(text="200 мг", callback_data="200торасемід")
            callback_button8 = types.InlineKeyboardButton(text="2 мл 0,5%", callback_data="2млторасемід")
            callback_button10 = types.InlineKeyboardButton(text="20 мл 1%", callback_data="20млторасемід")
            keyboard14.add(callback_button1, callback_button2)
            keyboard14.add(callback_button3, callback_button4)
            keyboard14.add(callback_button5, callback_button6)
            keyboard14.add(callback_button7, callback_button8)
            keyboard14.add(callback_button10)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Торасемід в ампулах 4 мл 0,5% містять препарати: \n\U00002764 ТОРАДІВ \n\U00002764 ТОРАСЕМІД-ДАРНИЦЯ  \n\U00002764 ТОРСИД \n\U00002764 ТРИФАС АМПУЛИ      ", reply_markup =keyboard14)
       


        elif call.data == "20млторасемід":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5торасемід")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5торасемід")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10торасемід")
            callback_button4 = types.InlineKeyboardButton(text="20 мг ", callback_data="20торасемід")
            callback_button5 = types.InlineKeyboardButton(text="50 мг", callback_data="50торасемід")
            callback_button6 = types.InlineKeyboardButton(text="100 мг ", callback_data="100торасемід")
            callback_button7 = types.InlineKeyboardButton(text="200 мг", callback_data="200торасемід")
            callback_button8 = types.InlineKeyboardButton(text="2 мл 0,5%", callback_data="2млторасемід")
            callback_button9 = types.InlineKeyboardButton(text="4 мл 0,5%", callback_data="4млторасемід")
            keyboard14.add(callback_button1, callback_button2)
            keyboard14.add(callback_button3, callback_button4)
            keyboard14.add(callback_button5, callback_button6)
            keyboard14.add(callback_button7, callback_button8)
            keyboard14.add(callback_button9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Торасемід в ампулах 20 мл 1% містять препарати: \n\U00002764 ТРИФАС 200 АМПУЛИ    ", reply_markup =keyboard14)
       
        elif call.data == "25спіронолакторн":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="50 мг ", callback_data="50спіронолакторн")
            callback_button3 = types.InlineKeyboardButton(text="100 мг", callback_data="100спіронолакторн")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Спіронолактон в дозуванні 25 мг містять препарати: \n\U00002764 ВЕРОШПІРОН \n\U00002764 СПІЛАКТОН \n\U00002764 СПІРОНОЛАКТОН-ДАРНИЦЯ     ", reply_markup =keyboard14)
       
        elif call.data == "50спіронолакторн":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="25 мг", callback_data="25спіронолакторн")
            callback_button3 = types.InlineKeyboardButton(text="100 мг", callback_data="100спіронолакторн")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Спіронолактон в дозуванні 50 мг містять препарати: \n\U00002764 ВЕРОШПІРОН \n\U00002764 СПІЛАКТОН \n\U00002764 СПІРОНОЛАКТОН САНДОЗ     ", reply_markup =keyboard14)
       
        elif call.data == "100спіронолакторн":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="25 мг", callback_data="25спіронолакторн")
            callback_button2 = types.InlineKeyboardButton(text="50 мг ", callback_data="50спіронолакторн")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Спіронолактон в дозуванні 100 мг містять препарати:  \n\U00002764 ВЕРОШПІРОН \n\U00002764 СПІЛАКТОН \n\U00002764 СПІРОНОЛАКТОН САНДОЗ  \n\U00002764 СПІРОНОЛАКТОН-ДАРНИЦЯ    ", reply_markup =keyboard14)
       
#АК
        elif call.data == "2,5амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10амлодипін")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Амлодипін в дозуванні 2,5 мг містять препарати: \n\U00002764 АЗОМЕКС \n\U00002764 ЕМЛОДИН \n\U00002764 ЕСЛО \n\U00002764 СЕМЛОПІН   ", reply_markup =keyboard14)
       
        elif call.data == "5амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5амлодипін")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10амлодипін")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Амлодипін в дозуванні 5 мг містять препарати: \n\U00002764 АГЕН \n\U00002764 АЗОМЕКС \n\U00002764 АЛАДИН \n\U00002764 АМЛОВАС \n\U00002764 АГЕН \n\U00002764 АМЛОДИЛ БОСНАЛЕК \n\U00002764 АМЛОДИПІН  \n\U00002764 АМЛОДИПІН КРКА  \n\U00002764 АМЛОДИПІН САНДОЗ \n\U00002764 АМЛОДИПІН-ДАРНИЦЯ \n\U00002764 АМЛОДИПІН-ЗДОРОВ'Я  \n\U00002764 АМЛОДИПІН-КВ  \n\U00002764 АМЛОДИПІН-ТЕВА \n\U00002764 АМЛОДИПІН-ФАРМАК  \n\U00002764 АМЛОДИПІН-ФІТОФАРМ  \n\U00002764 АМЛОЦИМ  \n\U00002764 ВАЗОТАЛ  \n\U00002764 ЕМЛОДИН \n\U00002764 ЕСЛО \n\U00002764 НОРВАСК \n\U00002764 НОРМОДИПІН \n\U00002764 СЕМЛОПІН \n\U00002764 СТАМЛО   ", reply_markup =keyboard14)
       
        elif call.data == "10амлодипін":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5амлодипін")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5амлодипін")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Амлодипін в дозуванні 10 мг містять препарати: \n\U00002764 АГЕН \n\U00002764 АЛАДИН \n\U00002764 АМЛОВАС \n\U00002764 АГЕН \n\U00002764 АМЛОДИПІН \n\U00002764 АМЛОДИПІН КРКА \n\U00002764 АМЛОДИПІН САНДОЗ  \n\U00002764 АМЛОДИПІН-ДАРНИЦЯ  \n\U00002764 АМЛОДИПІН-ЗДОРОВ'Я  \n\U00002764 АМЛОДИПІН-КВ  \n\U00002764 АМЛОДИПІН-ТЕВА \n\U00002764 АМЛОДИПІН-ФАРМАК  \n\U00002764 АМЛОЦИМ \n\U00002764 ВАЗОТАЛ  \n\U00002764 ЕМЛОДИН \n\U00002764 НОРВАСК \n\U00002764 НОРМОДИПІН \n\U00002764 СТАМЛО   ", reply_markup =keyboard14)
       
        elif call.data == "40верапаміл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="80 мг ", callback_data="80верапаміл")
            callback_button3 = types.InlineKeyboardButton(text="180 мг", callback_data="180верапаміл")
            callback_button4 = types.InlineKeyboardButton(text="240 мг ", callback_data="240верапаміл")
            callback_button5 = types.InlineKeyboardButton(text="Розчин", callback_data="розчинверапаміл")
            keyboard14.add(callback_button2, callback_button3, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Верапаміл в дозуванні 40 мг містять препарати: \n\U00002764  ВЕРАПАМІЛ-ДАРНИЦЯ  \n\U00002764  ВЕРАПАМІЛУ ГІДРОХЛОРИД  \n\U00002764  ЛЕКОПТИН  ", reply_markup =keyboard14)
        elif call.data == "80верапаміл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40верапаміл")
            callback_button3 = types.InlineKeyboardButton(text="180 мг", callback_data="180верапаміл")
            callback_button4 = types.InlineKeyboardButton(text="240 мг ", callback_data="240верапаміл")
            callback_button5 = types.InlineKeyboardButton(text="Розчин", callback_data="розчинверапаміл")
            keyboard14.add(callback_button1, callback_button3, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Верапаміл в дозуванні 80 мг містять препарати: \n\U00002764  ВЕРАПАМІЛ-ДАРНИЦЯ \n\U00002764  ВЕРАПАМІЛУ ГІДРОХЛОРИД \n\U00002764  ІЗОПТИН \n\U00002764  ЛЕКОПТИН   ", reply_markup =keyboard14)
       
        elif call.data == "180верапаміл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40верапаміл")
            callback_button2 = types.InlineKeyboardButton(text="80 мг ", callback_data="80верапаміл")
            callback_button4 = types.InlineKeyboardButton(text="240 мг ", callback_data="240верапаміл")
            callback_button5 = types.InlineKeyboardButton(text="Розчин", callback_data="розчинверапаміл")
            keyboard14.add(callback_button1, callback_button2, callback_button4, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Верапаміл в дозуванні 180 мг містять препарати: \n\U00002764  ВЕРАТАРД     ", reply_markup =keyboard14)
       
        elif call.data == "240верапаміл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40верапаміл")
            callback_button2 = types.InlineKeyboardButton(text="80 мг ", callback_data="80верапаміл")
            callback_button3 = types.InlineKeyboardButton(text="180 мг", callback_data="180верапаміл")
            callback_button5 = types.InlineKeyboardButton(text="Розчин", callback_data="розчинверапаміл")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button5)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Верапаміл в дозуванні 240 мг містять препарати: \n\U00002764  ІЗОПТИН SR     ", reply_markup =keyboard14)
       
        elif call.data == "розчинверапаміл":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40верапаміл")
            callback_button2 = types.InlineKeyboardButton(text="80 мг ", callback_data="80верапаміл")
            callback_button3 = types.InlineKeyboardButton(text="180 мг", callback_data="180верапаміл")
            callback_button4 = types.InlineKeyboardButton(text="240 мг ", callback_data="240верапаміл")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Розчин верапамілу в дозуванні 2 мл 0,25% амп. містять препарати: \n\U00002764  ВЕРАПАМІЛ-ДАРНИЦЯ     ", reply_markup =keyboard14)



        elif call.data == "60Дилтіазем":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="90 мг ", callback_data="90Дилтіазем")
            callback_button3 = types.InlineKeyboardButton(text="120 мг", callback_data="120Дилтіазем")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Дилтіазем в дозуванні 60 мг містять препарати: \n\U00002764  ДИЛТІАЗЕМ \n\U00002764  ДІАКОРДИН      ", reply_markup =keyboard14)

        elif call.data == "90Дилтіазем":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="60 мг", callback_data="60Дилтіазем")
            callback_button3 = types.InlineKeyboardButton(text="120 мг", callback_data="120Дилтіазем")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Дилтіазем в дозуванні 90 мг містять препарати: \n\U00002764  АЛДІЗЕМ \n\U00002764  ДІАКОРДИН \n\U00002764  РЕТАРД  ", reply_markup =keyboard14)
       
        elif call.data == "120Дилтіазем":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="60 мг", callback_data="60Дилтіазем")
            callback_button2 = types.InlineKeyboardButton(text="90 мг ", callback_data="90Дилтіазем")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Дилтіазем в дозуванні 120 мг містять препарати: \n\U00002764  ДІАКОРДИН \n\U00002764  РЕТАРД   ", reply_markup =keyboard14)
#ББ
        elif call.data == "40соталол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="80 мг ", callback_data="80соталол")
            callback_button3 = types.InlineKeyboardButton(text="160 мг", callback_data="160соталол")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Соталол в дозуванні 40 мг містять препарати:  \n\U00002764 СОТАЛОЛ САНДОЗ    ", reply_markup =keyboard14)
       

        elif call.data == "80соталол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40соталол")
            callback_button3 = types.InlineKeyboardButton(text="160 мг", callback_data="160соталол")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Соталол в дозуванні 80 мг містять препарати:\n\U00002764 СОРИТМІК \n\U00002764 СОТАЛОЛ САНДОЗ   ", reply_markup =keyboard14)
       

        elif call.data == "160соталол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="40 мг", callback_data="40соталол")
            callback_button2 = types.InlineKeyboardButton(text="80 мг ", callback_data="80соталол")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Соталол в дозуванні 160 мг містять препарати: \n\U00002764 СОРИТМІК \n\U00002764 СОТАЛОЛ САНДОЗ     ", reply_markup =keyboard14)
       
        elif call.data == "25метопролол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="50 мг ", callback_data="50метопролол")
            callback_button3 = types.InlineKeyboardButton(text="100 мг", callback_data="100метопролол")
            callback_button4 = types.InlineKeyboardButton(text="Розчин", callback_data="Розчинметопролол")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Метопролол в дозуванні 25 мг містять препарати:\n\U00002764 БЕТАЛОК ЗОК \n\U00002764 ЕГІЛОК \n\U00002764 МЕТОПРОЛОЛ    ", reply_markup =keyboard14)
       
        
        elif call.data == "50метопролол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="25 мг", callback_data="25метопролол")
            callback_button3 = types.InlineKeyboardButton(text="100 мг", callback_data="100метопролол")
            callback_button4 = types.InlineKeyboardButton(text="Розчин", callback_data="Розчинметопролол")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Метопролол в дозуванні 50 мг містять препарати:\n\U00002764 БЕТАЛОК ЗОК \n\U00002764 ЕГІЛОК \n\U00002764 КОРВІТОЛ \n\U00002764 МЕТОПРОЛОЛ \n\U00002764 МЕТОПРОЛОЛУ ТАРТРАТ     ", reply_markup =keyboard14)
       
        elif call.data == "100метопролол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="25 мг", callback_data="25метопролол")
            callback_button2 = types.InlineKeyboardButton(text="50 мг ", callback_data="50метопролол")
            callback_button4 = types.InlineKeyboardButton(text="Розчин", callback_data="Розчинметопролол")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Метопролол в дозуванні 100 мг містять препарати: \n\U00002764 БЕТАЛОК ЗОК \n\U00002764 ЕГІЛОК \n\U00002764 КОРВІТОЛ \n\U00002764 МЕТОПРОЛОЛ \n\U00002764 МЕТОПРОЛОЛУ ТАРТРАТ  ", reply_markup =keyboard14)
       
        elif call.data == "Розчинметопролол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="25 мг", callback_data="25метопролол")
            callback_button2 = types.InlineKeyboardButton(text="50 мг ", callback_data="50метопролол")
            callback_button3 = types.InlineKeyboardButton(text="100 мг", callback_data="100метопролол")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Розчин метопрололу в дозуванні 5 мл 0,1%  (амп) містять препарати: \n\U00002764 БЕТАЛОК  \n\U00002764 КАРДОЛАКС   ", reply_markup =keyboard14)

        elif call.data == "10бетаксолол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="20 мг", callback_data="20бетаксолол")
            keyboard14.add(callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Бетаксолол в дозуванні 10 мг містить: \n\U00002764  БЕТАК   ", reply_markup =keyboard14)

        elif call.data == "20бетаксолол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="10 мг", callback_data="10бетаксолол")
            keyboard14.add(callback_button1)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Бетаксолол в дозуванні 20 мг містять препарати:\n\U00002764  БЕТАК \n\U00002764  БЕТАКОР \n\U00002764  ЛОКРЕН   ", reply_markup =keyboard14)
       
        elif call.data == "2,5бісопролол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5бісопролол")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10бісопролол")
            keyboard14.add(callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Бісопролол в дозуванні 2,5 мг містять препарати: \n\U00002764  БІСОПРОЛ \n\U00002764  БІСОПРОЛОЛ АУРОБІНДО \n\U00002764  БІСОПРОЛОЛ КРКА \n\U00002764  ДОРЕЗ  \n\U00002764  КОНКОР КОР  ", reply_markup =keyboard14)
        elif call.data == "5бісопролол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5бісопролол")
            callback_button3 = types.InlineKeyboardButton(text="10 мг", callback_data="10бісопролол")
            keyboard14.add(callback_button1, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Бісопролол в дозуванні 5 мг містять препарати: \n\U00002764  БІКАРД \n\U00002764  БІПРОЛОЛ \n\U00002764  БІСОПРОЛ \n\U00002764  БІСОПРОЛОЛ АУРОБІНДО  \n\U00002764  БІСОПРОЛОЛ КРКА \n\U00002764  БІСОПРОЛОЛ САНДОЗ  \n\U00002764  БІСОПРОЛОЛ-АСТРАФАРМ  \n\U00002764  БІСОПРОЛОЛ-КВ  \n\U00002764  БІСОПРОЛОЛ-ТЕВА  \n\U00002764  БІСОСТАД ДОРЕЗ \n\U00002764  ЄВРОБІСОПРОЛОЛ \n\U00002764  КОНКОР \n\U00002764  КОРОНАЛ", reply_markup =keyboard14)
        elif call.data == "10бісопролол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2,5 мг", callback_data="2,5бісопролол")
            callback_button2 = types.InlineKeyboardButton(text="5 мг ", callback_data="5бісопролол")
            keyboard14.add(callback_button1, callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Бісопролол в дозуванні 10 мг містять препарати: \n\U00002764  БІКАРД \n\U00002764  БІПРОЛОЛ \n\U00002764  БІСОПРОЛ \n\U00002764  БІСОПРОЛОЛ АУРОБІНДО \n\U00002764  БІСОПРОЛОЛ КРКА  \n\U00002764  БІСОПРОЛОЛ САНДОЗ  \n\U00002764  БІСОПРОЛОЛ-АСТРАФАРМ  \n\U00002764  БІСОПРОЛОЛ-КВ  \n\U00002764  БІСОПРОЛОЛ-ТЕВА  \n\U00002764  БІСОСТАД \n\U00002764  ДОРЕЗ \n\U00002764  ЄВРОБІСОПРОЛОЛ \n\U00002764  КОНКОР \n\U00002764  КОРОНАЛ", reply_markup =keyboard14)

        elif call.data == "3,125карведілол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="6,25 мг", callback_data="6,25карведілол")
            callback_button3 = types.InlineKeyboardButton(text="12,5 мг", callback_data="12,5карведілол")
            callback_button4 = types.InlineKeyboardButton(text="25 мг", callback_data="25карведілол")
            keyboard14.add(callback_button2, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Карведілол в дозуванні 3,125 мг містить препарат: \n\U00002764 КОРІОЛ ", reply_markup =keyboard14)

        elif call.data == "6,25карведілол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,125 мг", callback_data="3,125карведілол")
            callback_button3 = types.InlineKeyboardButton(text="12,5 мг", callback_data="12,5карведілол")
            callback_button4 = types.InlineKeyboardButton(text="25 мг", callback_data="25карведілол")
            keyboard14.add(callback_button1, callback_button3, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Карведілол в дозуванні 6,25 мг містять препарати: \n\U00002764 КАРВЕДИЛОЛ АУРОБІНДО  \n\U00002764 КАРВИДЕКС \n\U00002764 КАРВІУМ \n\U00002764 КАРДІОСТАД \n\U00002764 КОРІОЛ \n\U00002764 ТАЛЛІТОН   ", reply_markup =keyboard14)
        elif call.data == "12,5карведілол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,125 мг", callback_data="3,125карведілол")
            callback_button2 = types.InlineKeyboardButton(text="6,25 мг", callback_data="6,25карведілол")
            callback_button4 = types.InlineKeyboardButton(text="25 мг", callback_data="25карведілол")
            keyboard14.add(callback_button1, callback_button2, callback_button4)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Карведілол в дозуванні 12,5 мг містять препарати: \n\U00002764 КАРВЕДИЛОЛ АУРОБІНДО  \n\U00002764 КАРВЕДИЛОЛ САНДОЗ  \n\U00002764 КАРВЕДИЛОЛ-КВ  \n\U00002764 КАРВИДЕКС \n\U00002764 КАРВІУМ \n\U00002764 КАРДІОСТАД \n\U00002764 КОРВАЗАН \n\U00002764 КОРІОЛ \n\U00002764 ТАЛЛІТОН   ", reply_markup =keyboard14)

        elif call.data == "25карведілол":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="3,125 мг", callback_data="3,125карведілол")
            callback_button2 = types.InlineKeyboardButton(text="6,25 мг", callback_data="6,25карведілол")
            callback_button3 = types.InlineKeyboardButton(text="12,5 мг", callback_data="12,5карведілол")
            keyboard14.add(callback_button1, callback_button2, callback_button3)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Карведілол в дозуванні 25 мг містять препарати: \n\U00002764 КАРВЕДИЛОЛ АУРОБІНДО  \n\U00002764 КАРВЕДИЛОЛ САНДОЗ  \n\U00002764 КАРВЕДИЛОЛ-КВ  \n\U00002764 КАРВИДЕКС \n\U00002764 КАРВІУМ \n\U00002764 КАРДІОСТАД \n\U00002764 КОРВАЗАН \n\U00002764 КОРІОЛ \n\U00002764 ТАЛЛІТОН   ", reply_markup =keyboard14)
       
        elif call.data == "Селективні":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="\U0001F49B Не селективні", callback_data="Не селективні")
            callback_button3 = types.InlineKeyboardButton(text="\U0001F49A Альфа і Бета-блокатори", callback_data="А і В блокатори")
            keyboard14.add(callback_button2)
            keyboard14.add(callback_button3)    
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\U00002705 Селективні бета-блокатори: \n\U00002764 Небівалол \n\U00002764 Бетаксолол \n\U00002764 Бісопролол \n\U00002764 Есмолол \n\U00002764 Метопролол \n\U00002764 Атенолол", reply_markup =keyboard14)
        
        elif call.data == "Не селективні":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="\U00002764 Селективні", callback_data="Селективні")
            callback_button3 = types.InlineKeyboardButton(text="\U0001F49A Альфа і Бета-блокатори", callback_data="А і В блокатори")
            keyboard14.add(callback_button1)
            keyboard14.add(callback_button3)    
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\U00002705 Не селективні бета блокатори: \n\U0001F49B Пропранолол \n\U0001F49B Соталол ", reply_markup =keyboard14)
        

        elif call.data == "А і В блокатори":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="\U00002764 Селективні", callback_data="Селективні")
            callback_button2 = types.InlineKeyboardButton(text="\U0001F49B Не селективні", callback_data="Не селективні")
            keyboard14.add(callback_button1)
            keyboard14.add(callback_button2)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\U00002705 Альфа і бета-блокатор: \n\U0001F49A Карведілол", reply_markup =keyboard14)

        elif call.data == "БКК судини":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="\U0001F49B Не дигідропіридинові", callback_data="БКК серце")
            keyboard14.add(callback_button2)    
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="\U00002705 Блокатори кальцієвих каналів з переважною дією на судини: \n\U00002764 Амлодипін \n\U00002764 Лацидипін \n\U00002764 Лерканідипін    ", reply_markup =keyboard14)

        elif call.data == "БКК серце":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="\U00002764 Дигідропіридинові", callback_data="БКК судини")
            keyboard14.add(callback_button1)   
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" \U00002705 Блокатори кальцієвих каналів з переважною дією на серце: \n\U0001F49B Верапаміл  \n\U0001F49B Дилтіазем  ", reply_markup =keyboard14)
        
        elif call.data == "Тіазидні":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button2 = types.InlineKeyboardButton(text="\U0001F49B Петльові", callback_data="Петльові")
            callback_button3 = types.InlineKeyboardButton(text="\U0001F49A Калійзберігаючі", callback_data="Калійзберігаючі")
            keyboard14.add(callback_button2)
            keyboard14.add(callback_button3)  
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=" Тіазидні і тіазидоподібні діуретики: \n\U00002764 Гідрохлортіазид \n\U00002764 Хлорталідон \n\U00002764 Індапамід", reply_markup =keyboard14)

        elif call.data == "Петльові":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="\U00002764 Тіазидні і тіазидоподібні", callback_data="Тіазидні")
            callback_button3 = types.InlineKeyboardButton(text="\U0001F49A Калійзберігаючі", callback_data="Калійзберігаючі")
            keyboard14.add(callback_button1)
            keyboard14.add(callback_button3)  
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Петльові діуретики: \n\U0001F49B Фуросемід \n\U0001F49B Торасемід  ", reply_markup =keyboard14)
        
        elif call.data == "Калійзберігаючі":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="\U00002764 Тіазидні і тіазидоподібні", callback_data="Тіазидні")
            callback_button2 = types.InlineKeyboardButton(text="\U0001F49B Петльові", callback_data="Петльові")
            keyboard14.add(callback_button1)
            keyboard14.add(callback_button2)  
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Калійзберігаючі діуретики: \n\U0001F49A Спіронолактон \n\U0001F49A Еплеренон", reply_markup =keyboard14)
        

        
#Черновик


        elif call.data == "8 мг ":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="2\U000026A1 0,625\U000026A1 5 ", callback_data="2 мг\0,625 мг\5 мгПериндоприл ")
            callback_button2 = types.InlineKeyboardButton(text="2,5\U000026A1 0,625\U000026A1 5 мг", callback_data="2,5 мг\0,625 мг\5 мг Периндоприл ")
            callback_button3 = types.InlineKeyboardButton(text="4 \U000026A1 1,25 \U000026A1 5 мг", callback_data="4 мг\1,25 мг\5 мг Периндоприл ")
            callback_button4 = types.InlineKeyboardButton(text="4\U000026A1 1,25\U000026A1 10 мг", callback_data="4 мг\1,25 мг\10 мг Периндоприл ")
            callback_button5 = types.InlineKeyboardButton(text="5\U000026A1 1,25\U000026A1 10 мг", callback_data="5 мг\1,25 мг\10 мг Периндоприл ")
            callback_button6 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 5 мг", callback_data="8 мг\2,5 мг\5 мг Периндоприл ")
            callback_button7 = types.InlineKeyboardButton(text="8\U000026A1 2,5\U000026A1 10 мг", callback_data="8 мг\2,5 мг\10 мг Периндоприл ")
            callback_button8 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 5 мг", callback_data="10 мг\2,5 мг\5 мг Периндоприл ")
            callback_button9 = types.InlineKeyboardButton(text="10\U000026A1 2,5\U000026A1 10 мг", callback_data="10 мг\2,5 мг\10 мг Периндоприл ")
            keyboard14.add(callback_button1, callback_button2, callback_button3, callback_button4, callback_button5, callback_button6, callback_button7, callback_button8, callback_button9)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="    ", reply_markup =keyboard14)

        elif call.data == "8 мг ":
            keyboard14 = types.InlineKeyboardMarkup()
            callback_button1 = types.InlineKeyboardButton(text="\U00002764 Тіазидні і тіазидоподібні", callback_data="Тіазидні")
            callback_button2 = types.InlineKeyboardButton(text="\U0001F49B Петльові", callback_data="Петльові")
            callback_button3 = types.InlineKeyboardButton(text="\U0001F49A Калійзберігаючі", callback_data="Калійзберігаючі")
            keyboard14.add(callback_button1)
            keyboard14.add(callback_button2)
            keyboard14.add(callback_button3)  
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="    ", reply_markup =keyboard14)
        

        





        



        
bot.polling (none_stop = True)
