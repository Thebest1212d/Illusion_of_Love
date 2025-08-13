# У цьому файлі міститяться всі предодатки

# Оголошення символів, які використовуються в цій грі. Колірний аргумент розфарбовує
# ім'я персонажа.

define h = Character("[heroname]", color="#00ff4c")
define s = Character("Соломія")

#Музика та звуки
define audio.calmmus = "audio/Evening.mp3"
define audio.surp = "audio/surprised.mp3"

#початкова заставка
label splashscreen:

pause(1.0)

scene black with fade

$ renpy.movie_cutscene('video/intro.mkv')

#Моргання Соломії
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