pip install vk_api

import vk_api

from vk_api.longpoll import VkLongPoll, VkEventType

vk_session = vk_api.VkApi(token="vk1.a.fyOXCCI0ypVb_nNRbdAMLs7z-_nTm-sIRJFmsSHhTxWfjGT1G2lyn-yM7DNF571zZd8te9zYMZcBHkog1SWWa-CDeNJYl5N7oy2CtKnj8dFiygWHDULh7XdvvyEhQbMNCglr9CZFDz2u1OBNhKT5ACGTgYxbQMbx66c6oHMzk0idy7Bd-uskFIwT6vgb66i0ijHNrP9vzMjy6RZsMSRVFg")

session_api = vk_session.get_api()

longpool = VkLongPoll(vk_session)

parts_of_speech = {
    "существительные": [
        "аэропОрты", "бАнты", "бОроду", "бухгАлтеров",
        "вероисповЕдание", "водопровОд", "газопровОд", "граждАнство", "дефИс", "дешевИзна",
        "диспансЕр", "договорЁнность", "докумЕнт", "досУг", "еретИк", "жалюзИ", "знАчимость",
        "Иксы", "каталОг", "квартАл", "киломЕтр", "кОнусов", "корЫсть", "крАны",
        "кремЕнь", "кремнЯ", "лЕкторов", "локтЕй", "лОктя", "лыжнЯ", "мЕстностей",
        "намЕрение", "нЕдруг", "недУг", "некролОг", "нЕнависть", "нефтепровОд", "новостЕй",
        "ногтЕй", "нОгтя", "отзЫв (посла)", "Отзыв (о книге)", "Отрочество", "партЕр", "портфЕль",
        "придАное", "призЫв", "свЁкла", "сирОты", "созЫв", "сосредотОчение",
        "срЕдства", "стАтуя", "столЯр", "тамОжня", "тОрты", "тУфля", "цемЕнт",
        "цЕнтнер", "цепОчка", "шАрфы", "шофЁр", "экспЕрт"
    ],
    "прилагательные": [
        "вернА", "знАчимый", "красИвее", "красИвейший", "кУхонный",
        "ловкА", "мозаИчный", "оптОвый", "прозорлИва", "прозорлИвый", "слИвовый"
    ],
    "глаголы": [
        "бралА", "бралАсь", "взялА", "взялАсь", "влилАсь", "ворвалАсь", "воспринялА",
        "воспринЯть", "воссоздалА", "вручИт", "гналА", "гналАсь",
        "добралА", "добралАсь", "дождалАсь", "дозвонИтся", "дозИровать", "ждалА",
        "закУпорить", "занялА", "занЯть", "зАнял", "зАняли", "заперлА", "запломбировАть",
        "защемИт", "звалА", "звонИт", "кАшлянуть", "клАла", "клЕить",
        "крАлась", "кровоточИть", "лгалА", "лилА", "лилАсь", "наделИт", "надорвалАсь",
        "назвалАсь", "накренИтся", "налилА", "нарвалА", "началА", "нАчал", "нАчали",
        "обзвонИт", "облегчИт", "облегчИть", "облилАсь", "обнялАсь", "обогналА", "ободралА",
        "ободрИт", "ободрИтся", "ободрИть", "ободрИться", "обострИть", "одолжИт", "одолжИть",
        "озлОбить", "оклЕить", "окружИт", "опОшлить", "освЕдомится", "освЕдомиться",
        "отбылА", "отдалА", "откУпорить", "отозвалА", "отозвалАсь",
        "перезвонИт", "перелилА", "плодоносИть", "пломбировАть", "повторИт",
        "позвалА", "позвонИт", "полилА", "положИл", "положИть", "понялА", "понЯть",
        "послАла", "прибылА", "прибЫть", "прИбыл", "прИбыли", "принЯть", "принялА",
        "прИнял", "прИняли", "рвалА", "сверлИт", "снялА", "создалА", "сорвалА",
        "убралА", "углубИть", "укрепИт", "чЕрпать", "щемИт", "щЁлкать"
    ],
    "причастия": [
        "довезЁнный", "зАгнутый", "занятА", "зАнятый", "зАпертый", "заселенА", "заселЁнный",
        "кровоточАщий", "нажИвший", "налИвший", "нанЯвшийся", "начАвший", "нАчатый",
        "низведЁнный", "облегчЁнный", "ободрЁнный", "обострЁнный", "отключЁнный",
        "повторЁнный", "поделЁнный", "понЯвший", "принятА", "прИнятый", "приручЁнный",
        "прожИвший", "снятА", "сОгнутый", "углублЁнный"
    ],
    "деепричастия": [
        "закУпорив", "начАв", "начАвшись", "отдАв", "понЯв", "прибЫв", "создАв"
    ],
    "наречия": [
        "вОвремя", "дОверху", "дОнизу", "дОсуха", "зАсветло", "красИвее", "надОлго", "ненадОлго"
    ]
}

mnemonics = {
    "тОрты": "Долго ели тОрты – Не налезли шОрты!",
    "шОрты": "Долго ели тОрты – Не налезли шОрты!",
    "свЁкла": "Фёкла красная, как свЁкла!",
    "столЯр": "Красит нам забор маляр, Стулья делает столЯр!",
    "шАрфы": "Как у нашей Марфы Есть в полоску шАрфы!",
    "бАнты": "А вот у Аланты – Есть в горошек бАнты!",
    "вОры": "ВОры украли у нас договОры.",
    "договОры": "ВОры украли у нас договОры.",
    "каталОг": "Рассердиться папа смог — Не нашёл он каталОг.",
    "бОроду": "Ох, как часто смОлоду Мы не бреем бОроду!"
}

def send(id, text):
  vk_session.method("messages.send", {"user_id": id, "message": text, "random_id": 0})

user_data = {}

import random

def ask_question(uid, word):
    send(uid, f"Какое ударение в слове «{word.lower()}»?")

def finish_quiz(uid, data):
    send(uid, "Викторина завершена!")
    data["state"] = "waiting"
    data["current_word"] = None

def show_help(uid):
    send(uid, "Доступные команды: готов(а) начать, давай отработаем ошибки, хочу выбрать другую часть речи, помощь")

for event in longpool.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me:
        uid = event.user_id
        raw_text = event.text.strip()
        text_lower = raw_text.lower()

        if uid not in user_data:
            user_data[uid] = {
                "state": "waiting",
                "mistakes": [],
                "words": [],
                "current_word": None
            }

        data = user_data[uid]

        # Обработка команды "начать"
        if text_lower == "начать":
            send(uid, """Добро пожаловать в «Звуковой компас»! Этот бот поможет улучшить навык правильной постановки ударений. Он подойдет для подготовки к экзаменам или проверки своей грамотности.
Чтобы начать, напиши «готов(а) начать», затем выбери часть речи из предложенных. На каждое слово отвечай, записывая его полностью строчными буквами, а ударную гласную выделяй заглавной (например, «каталОг»). Если контекст необходим, пиши словосочетание целиком. После завершения теста, для исправления ошибок отправь «давай отработаем ошибки». Тренировка считается законченной, когда ошибок не останется. В любой момент можно сменить часть речи командой «хочу выбрать другую часть речи» или вызвать подсказку командой «помощь». Удачи!
            """)
            continue

        # Обработка команды "помощь"
        if text_lower == "помощь":
            show_help(uid)
            continue

        # Обработка команды "готов(а) начать"
        if text_lower == "готов начать" or text_lower == "готова начать":
            data["state"] = "waiting"
            data["mistakes"] = []
            data["words"] = []
            data["current_word"] = None
            send(uid, "Выбери часть речи: " + ", ".join(parts_of_speech.keys()))
            continue

        # Обрабокта команды "давай отработаем ошибки"
        if text_lower == "давай отработаем ошибки":
            if data["mistakes"]:
                data["state"] = "repeat"
                data["words"] = data["mistakes"][:]
                random.shuffle(data["words"])
                if data["words"]:
                    data["current_word"] = data["words"].pop()
                    ask_question(uid, data["current_word"])
                else:
                    data["state"] = "waiting"
                    data["current_word"] = None
                    send(uid, "Ошибок нет.")
            else:
                send(uid, "Ошибок нет.")
                data["state"] = "waiting"
                data["current_word"] = None
            continue

        # Обработка команды "хочу выбрать другую часть речи"
        if text_lower == "хочу выбрать другую часть речи":
            data["state"] = "waiting"
            data["mistakes"] = []
            data["words"] = []
            data["current_word"] = None
            send(uid, "Выбери другую часть речи: " + ", ".join(parts_of_speech.keys()))
            continue

        # Режим ожидания выбора части речи
        if data["state"] == "waiting":
            if text_lower in parts_of_speech:
                data["state"] = "quiz"
                data["words"] = parts_of_speech[text_lower][:]
                random.shuffle(data["words"])
                data["mistakes"] = []
                if data["words"]:
                    data["current_word"] = data["words"].pop()
                    ask_question(uid, data["current_word"])
                else:
                    send(uid, "Нет слов.")
                    data["state"] = "waiting"
            else:
                send(uid, "К сожалению, мне неизвестна такая команда(\nВыберите один из вариантов: готов(а) начать, давай отработаем ошибки, хочу выбрать другую часть речи, помощь")
            continue

        # Режим викторины
        if data["state"] == "quiz":
            current = data.get("current_word")
            if current is None:
                if data["words"]:
                    data["current_word"] = data["words"].pop()
                    ask_question(uid, data["current_word"])
                else:
                    finish_quiz(uid, data)
                continue

            if raw_text == current:
                send(uid, "Верно! Вы хорошо справились!")
            else:
                if current not in data["mistakes"]:
                    data["mistakes"].append(current)
                send(uid, f"К сожалению, это неверно. Правильный вариант: {current}.")
                if current in mnemonics.keys():
                  send(uid, f"Специальная мнемотехника для запоминания: {mnemonics.get(current)}")

            if data["words"]:
                data["current_word"] = data["words"].pop()
                ask_question(uid, data["current_word"])
            else:
                finish_quiz(uid, data)


        # Режим отработки ошибок
        if data["state"] == "repeat":
            current = data.get("current_word")

            if current is None and data["words"]:
                data["current_word"] = data["words"].pop()
                ask_question(uid, data["current_word"])
                continue

            if raw_text == current:
                send(uid, "Верно! Ошибка исправлена!")

                if data["words"]:
                    data["current_word"] = data["words"].pop()
                    ask_question(uid, data["current_word"])
                else:
                    send(uid, "Отлично! Ты исправил(а) все ошибки!")
                    data["state"] = "waiting"
                    data["current_word"] = None
                    data["mistakes"] = []
            else:
                send(uid, f"Неверно. Правильный ответ: {current}.")
                if current in mnemonics:
                    send(uid, f"Мнемотехника: {mnemonics[current]}")
                ask_question(uid, current)

            continue
