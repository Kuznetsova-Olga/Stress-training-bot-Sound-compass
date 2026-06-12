# **User Manual for the «Звуковой компас» Training Bot**
1. ## **Introduction**
   **«Звуковой компас»** is a free VK chatbot that helps you quickly and effectively prepare for orthoepy (word stress) tasks in the OGE, Unified State Exam, VPR, and other examinations.

   **What you get:**

   Training on words from the current FIPI word list.

   Instant answer verification and detailed progress statistics.

   The ability to study anytime, anywhere – right in the messenger.

   **Target audience:**\
   Students in grades 9-11, applicants, teachers, tutors, and anyone who wants to test and improve their literacy.

   **What you need to get started:**

1. The VK messenger installed.
1. An account in that messenger.
1. An Internet connection.
1. ## **How to Start Using**
   **Step 1. Launch the bot.**\
   Write the command "начать".

   **Step 2. Launch the bot.**\
   After receiving the welcome email, type the command «готов(а) начать».

   **Step 3. Choose a part of speech.**\
   The bot will ask you to choose a part of speech: nouns, adjectives, verbs, participles, gerunds, and adverbs. Write one of the suggested parts of speech in a message.

1. **How to Answer Correctly**

   After starting, the bot sends a word card, e.g.:

   Word: каталог  

   You need to write a capital vowel in the word: А, У, О, И, Э, Ы, Я, Ю, Е, Ё

   You send the entire word with a capital letter that corresponds to the stressed sound.  

   Correct answer: каталОг.

   The bot replies:

   - ✅ "Correct! You did well!"

   - ❌ "Unfortunately, that's wrong. Correct variant: каталОг"

   Then a message will appear asking about the next word.
1. ## ` `**How the Bot Works (Principle of Operation)**
   The bot is a **training simulator** that helps you learn correct word stress through interactive quizzes. The logic is based on the following steps.
   ### **4.1 Choosing a part of speech**
   After the initial greeting, the bot asks you to choose a part of speech:

Choose a part of speech: nouns, adjectives, verbs, participles, gerunds, adverbs.

You reply with one of them, e. g. “nouns” or “verbs”. The bot then starts a quiz with words from that category.
### **4.2 Question format**
For each word, the bot asks:

What is the stress in the word «X»?

You answer by typing the whole word with the vowel capitalized (А, Е, И, О, У, Ы, Э, Ю, Я).
### **4.3 Answer evaluation**
Correct answer -> bot says "Correct! You did well!" and moves to the next word.

Incorrect answer -> bot says "Unfortunately, that's wrong. The correct variant is: X." and then asks a new word immediately.
### **4.4 Special commands during the quiz**

|**Command phrase**|**Effect**|
| - | - |
|Готов(а) начать|Launching the bot and receiving a message with suggested parts of speech.|
|Давай отработаем ошибки|A message asking about the stress in a word that previously contained an error.  |
|Хочу выбрать другую часть речи |A message with a choice of six parts of speech.|
|Помощь|A message listing the available commands: ready to start, let's work out the mistakes, I want to choose another part of speech, help.|
### **4.5 End of quiz and error report**
To complete the test, you need to send the bot the command "давай отработаем ошибки".

After this message, the bot will suggest the words that you previously made mistakes with.

After all the errors in the words are corrected, the bot will display the message «Отлично! Ты исправил(а) все ошибки!». If you make the same mistake again, the bot will ask you again where to put the stress in the word.

Important clarification: it is necessary to correct errors within the same part of speech, that is, before writing the command «Хочу выбрать другую часть речи». Otherwise, the bot will only display the words of the last selected part of speech.

1. **Typical problems and their solutions**

   |**Problem**|**Solution**|
   | - | - |
   |The bot is not responding|Check your internet connection. Send the command "готов(а) начать" or restart the bot.|
   |The bot writes «К сожалению мне неизвестна такая команда( Выберите один из вариантов...»|Write one of the commands suggested by the bot.|
1. ## **Glossary** 

   |**Term**|**Meaning**|
   | - | - |
   |The orthoepical dictionary|The official list of words with standard stress, approved by FIPI for conducting exams (OGE, EGE).|
   |FIPI|The Federal Institute of Pedagogical Measurements is an organization that develops control and measurement materials (CMM) for the Unified State Exam and the Main State Exam.|
   |Command|A special message that triggers a specific action, instructing the bot on what to do.|

1. ## **Appendix – Full Interaction Example** 
   Bot: Ready to start? Choose a part of speech: nouns, adjectives, verbs...

   User: Verbs

   Bot: What is the stress in the word «озлобить»?

   User: озлОбить

   Bot: Correct! You did well!

   Bot: What is the stress in the word «взяла»?

   User: взялА

   Bot: Correct! You did well!

   Bot: What is the stress in the word «принять»?

   User: принЯть

   Bot: Correct! You did well!

   Bot: What is the stress in the word «плодонОсить»?

   User: плодонОсить

   Bot: Incorrect. Correct variant: плодоносИть.

   Bot: What is the stress in the word «перелила»?

   User: I want to choose a different part of speech

   Bot: Choose a part of speech: nouns, adjectives, verbs...

   User: Adverbs

   Bot: What is the stress in the word «засветло»?

   User: зАсветло

   Bot: Correct! You did well!

   Bot: What is the stress in the word «плодонОсить»?

   User: Let's work out the mistakes.

   Bot: What is the stress in the word «плодонОсить»?

   User: плодоносИть

   Bot: Correct! You did well!

   Bot: Quiz completed! 

   Bot: Errors: плодоносИть.


