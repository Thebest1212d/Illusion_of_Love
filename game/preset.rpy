#---------------------------------------------------------------------------------------------------------------
# У цьому файлі міститяться всі предодатки

# Оголошення символів, які використовуються в цій грі. Колірний аргумент розфарбовує
# ім'я персонажа.

define h = Character("[heroname]", color="#00ff4c")
define s = Character("Соломія")
define u = Character("Учитель", color="#eb9b11")
define re = Character("Реєстратор шлюбу", color="#f21cd5")

#Музика та звуки
define audio.song1 = "audio/Evening.mp3"
define audio.surp = "audio/surprised.mp3"
define audio.krok1 = "audio/krok1.mp3"
define audio.zvonok = "audio/japanschool.mp3"
define audio.door = "audio/door.mp3"
define audio.heart = "audio/heartbeat.mp3"
define audio.budilnik = "audio/budilnik.mp3"
define audio.dusch = "audio/dusch.mp3"
define audio.CaptainScurvy = "audio/CaptainScurvy.mp3"
define audio.pochoka = "audio/udar-po-scheke.mp3"
define audio.song2 = "audio/Summer Day.mp3"
define audio.song3 = "audio/Facile.mp3"
define audio.song4 = "audio/Angel Share.mp3"
define audio.song5 = "audio/Almost Bliss.mp3"
define audio.song6 = "audio/Starting Out Waltz Vivace.mp3"
define audio.smix_tolp = "audio/smeh_tolpa.mp3"
define audio.udar_kulak = "audio/kulak_udar.mp3"
define audio.baka = "audio/baka.mp3"
define audio.kiss1 = "audio/kiss1.mp3"
define audio.kiss2 = "audio/kiss2.mp3"
define audio.stony_short = "audio/stony_short.mp3"
define audio.sad_piano = "audio/Promising Relationship.mp3"
define audio.sad_music = "audio/Sad Trio1.mp3"
define audio.pobeda = "audio/pobeda.mp3"
define audio.achievement = "audio/achievement.mp3"
define audio.wedding = "audio/Wedding.mp3"
define audio.ring = "audio/ring.mp3"


#---------------------------------------------------------------------------------------------------------------

init python:
    import random

    # Функція для відтворення випадкових пісень.
    def play_random_playlist():
        playlist = [
            audio.song1,
            audio.song2,
            audio.song3,
            audio.song4,
            audio.song5,
            audio.song6
        ]
        random.shuffle(playlist)
        renpy.music.play(playlist, loop=True)


init python:
    # звук для всіх кнопок (у т.ч. textbutton)
    style.button.activate_sound = "audio/UI/button-press.mp3"
    style.button.hover_sound = "audio/UI/hover.mp3"

    # Якщо у тебе є окремі стилі для меню
    style.mm_button.activate_sound = "audio/UI/button-press.mp3"
    style.mm_button.hover_sound = "audio/UI/hover.mp3"

    style.quit_button.activate_sound = "audio/UI/button-press.mp3"
    style.quit_button.hover_sound = "audio/UI/hover.mp3"



#---------------------------------------------------------------------------------------------------------------

#Початкова заставка
label splashscreen:

pause(1.0)

scene black with fade

$ renpy.movie_cutscene('video/video.mkv')


screen dark_overlay:
    modal True
    add "dark.jpg"  # Зображення з темним фоном


#---------------------------------------------------------------------------------------------------------------

#Моргання Соломії 1
image solomia blink:
    "solomia normal"
    choice:
        pause 3.0
    choice:
        pause 4.0
    choice:
        pause 5.0
    "solomia closed"
    pause 0.25
    repeat

#Моргання Соломії 2
image solomia2 blink:
    "solomia2 normal"
    choice:
        pause 3.0
    choice:
        pause 4.0
    choice:
        pause 5.0
    "solomia2 closed"
    pause 0.25
    repeat

transform zoomin:
    zoom 2.0  # Збільшення персонажа вдвічі
    xpos 0.5  # Переміщення персонажа до центру екрану
    ypos 2100

transform normal:
    zoom 1.0  # Значення за замовчуванням
    xpos 0.5  # Значення за замовчуванням
    ypos 1.0  # Значення за замовчуванням

#---------------------------------------------------------------------------------------------------------------

#Витяг імені власника ПК
init python:
    import os
    usID=os.environ.get("USERNAME")

#---------------------------------------------------------------------------------------------------------------

#ГАЧА
init python:
    import random

    # Список персонажів з шансами
    characters = [
        # 5★ Characters (3% total, розподілено між 5 персонажами)
        {"name": "Соломія", "rarity": "5★", "chance": 2.0},
        {"name": "Фіона", "rarity": "5★", "chance": 1.4},
        {"name": "Астрея", "rarity": "5★", "chance": 0.6},
        {"name": "Серафіна", "rarity": "5★", "chance": 0.8},
        {"name": "Валерія", "rarity": "5★", "chance": 0.6},

        # 4★ Characters (15% total, розподілено між 5 персонажами)
        {"name": "Елара", "rarity": "4★", "chance": 3},
        {"name": "Маеліс", "rarity": "4★", "chance": 3},
        {"name": "Лісандра", "rarity": "4★", "chance": 3},
        {"name": "Доріан", "rarity": "4★", "chance": 3},
        {"name": "Вівіан", "rarity": "4★", "chance": 3},

        # 3★ Characters (82% total, розподілено між 9 персонажами)
        {"name": "Ронан", "rarity": "3★", "chance": 9.11},
        {"name": "Торн", "rarity": "3★", "chance": 9.11},
        {"name": "Неріна", "rarity": "3★", "chance": 9.11},
        {"name": "Каден", "rarity": "3★", "chance": 9.11},
        {"name": "Міра", "rarity": "3★", "chance": 9.11},
        {"name": "Алістер", "rarity": "3★", "chance": 9.11},
        {"name": "Селен", "rarity": "3★", "chance": 9.11},
        {"name": "Рея", "rarity": "3★", "chance": 9.11},
        {"name": "Арден", "rarity": "3★", "chance": 9.11}
    ]
    
    # Функція для витягування випадкового персонажа
    def pull_gacha():
        random_number = random.randint(1, 100)  # Генеруємо випадкове число від 1 до 100
        cumulative_chance = 0  # Лічильник шансів
        
        for char in characters:
            cumulative_chance += char["chance"]  # Додаємо шанс поточного персонажа до загального
            if random_number <= cumulative_chance:  # Якщо випадкове число в межах шансу персонажа
                return char

#---------------------------------------------------------------------------------------------------------------
#Вітальне повідомлення перед початком гри
screen intro_message():
    modal True  # не дозволяє натискати на гру поки вікно відкрите
    tag menu    # щоб інші екрани не накладались одночасно

    frame:
        style "menu_frame"
        xalign 0.5
        yalign 0.5
        xmaximum 1000
        ymaximum 300
        xpadding 30
        ypadding 30

        vbox:
            spacing 15
            text "Привіт, [usID]!" size 30
            text "Граючи в цю історію, не поспішай. Насолоджуйся кожним моментом, кожною зустріччю, кожним словом!" size 25
            text "Це твій час, щоб відчути тепло, ніжність і радість разом із героями." size 25

            textbutton "Розпочати гру":
                action Hide("intro_message")  # закриває вікно
                xalign 0.5

#---------------------------------------------------------------------------------------------------------------

#Вимкнення прокрутки колесика мишки
#$ config.rollback_enabled = False

#---------------------------------------------------------------------------------------------------------------

#   Код скинення досягнень
# label clear_achievements:
#     python:
#         # Перевіряємо, чи існує список досягнень, і ініціалізуємо, якщо потрібно
#         if persistent._achievements is None:
#             persistent._achievements = []
#         if persistent._achievements_synced is None:
#             persistent._achievements_synced = []

#         # Очищення списків досягнень
#         persistent._achievements.clear()
#         persistent._achievements_synced.clear()

#         # Зберігаємо зміни в персистентних даних
#         renpy.save_persistent()
#     "Всі досягнення було очищено."
#     return

