**Technical Manual for the «Звуковой компас» VK Chatbot**

**1. General Information**

Purpose:\
Training word stress placement in Russian (preparation for different
types of exams).\
Platform: VKontakte.\
Library: vk_api.\
Word source: FIPI orthoepic dictionary 2026.

Project participants:

Kaizerova Anna

Kuznetsova Olga

Mylnikova Viktoria

Ruina Svetlana

Bot link: <https://vk.com/sound_compass>

**2. Technologies & Mechanisms**

VK API is a software interface that allows permanent websites, programs,
and mobile applications to connect to the VK platform and perform
actions.

vk_api -- library that works with VK API.

To use this library, it is necessary to install it and import it:

pip install vk_api

import vk_api

longpoll is a module for working with User Long Poll API

from vk_api.longpoll import VkLongPoll, VkEventType

Long Poll (VkLongPoll) is a persistent connection to VK servers, listens
for new events.

VkEventType is a event type constants (e.g., MESSAGE_NEW).

Community token is used for bot authentication.

**3. Data Structures**

3.1. parts_of_speech (dictionary)

Stores parts of speech as keys, each containing a list of words with the
stressed vowel capitalised.

parts_of_speech = {

\"существительные\": \[\"аэропОрты\", \...\],

\"прилагательные\": \[\"вернА\", \...\],

...

}

3.2. mnemonics (dictionary)

Associates a word with a mnemonic phrase to remember the correct stress.

mnemonics = {

\"тОрты\": \"Долго ели тОрты -- Не налезли шОрты!\",

\"шОрты\": \"Долго ели тОрты -- Не налезли шОрты!\",

...

}

3.3. user_data (dictionary)

Key: uid (user ID).\
Value: dictionary containing user progress:

  -----------------------------------------------------------------------
  Field              Purpose
  ------------------ ----------------------------------------------------
  state              Current state: \"waiting\", \"quiz\", \"repeat\"

  mistakes           List of words the user answered incorrectly

  words              Remaining words in the current quiz

  current_word       The word currently being asked
  -----------------------------------------------------------------------

**4. Core Functions**

4.1. Function send(id, text)

Sends a message to the user.\
Uses vk_session.method("messages.send", \...) with random_id = 0 to
prevent duplication.

4.2. Function ask_question(uid, word)

Generates a question in the format:\
"Какое ударение в слове «{word.lower()}»?"

4.3. Function finish_quiz(uid, data)

Sends "Викторина завершена!"

Changes state to "waiting"

Clears current_word.

**5. Program Logic (Event Loop)**

An infinite loop:\
for event in longpoll.listen():...

Upon receiving a new personal message** **(event.type == MESSAGE_NEW and
event.to_me):

1.  Extract the sender\'s user_id and message text.

2.  If the user does not exist in the user_data dictionary, initialize a
    new entry with the default state.

5.1. Command Handling

  -----------------------------------------------------------------------
  Command            Action
  ------------------ ----------------------------------------------------
  "помощь"           Calls show_help(uid) -- lists available commands

  "начать"           Sends welcome message and instructions

  "готов(а) начать"  Resets data, changes state = \"waiting\", sends
                     part-of-speech selection

  "давай отработаем  If no mistakes, "Ошибок нет.", state = "waiting". If
  ошибки"            mistakes exist, state = "repeat", shuffles mistake
                     list, sets current_word via pop()

  "хочу выбрать      Allows user to change the part of speech
  другую часть речи" 
  -----------------------------------------------------------------------

5.2. Quiz Mode (state = "quiz")

User selects a part of speech from parts_of_speech.keys() while state is
"waiting".

State changes to "quiz".

All words from the chosen part are copied to words (lowercase for
display).

current_word is selected via pop().

ask_question() is called repeatedly.

If answer is corrert, sends message to user: "Верно! Вы хорошо
справились!"

If answer is incorrect, sends message to user: "К сожалению, это
неверно. Правильный вариант: X", word added to mistakes.

If a mnemonic exists for the word, it is sent as a tip.

When words is empty, finish_quiz() is called.

5.3. Repeat Mode (state = "repeat")

Used to retrain mistakes.

Words are taken from mistakes list.

Function ask_question() is used for each word.

If answer is correct, sends message to user: "Верно! Ошибка
исправлена!" -- word removed from mistakes.

If answer is incorrect, sends message to user: "Неверно. Правильный
ответ: X" -- if a mnemonic exists, it is also sent; the word remains
in mistakes.

When mistakes is empty, sends "Отлично! Ты исправил(а) все ошибки!",
changes state to \"waiting\".

**6. Notes**

Mistake correction only works within the same part of speech. Changing
the part of speech clears the current mistake list for the previous
part.

The bot uses pop() to remove words from the list as they are asked,
ensuring no repetition within a single quiz session.

The random_id = 0 in message sending prevents VK from duplicating
messages.
