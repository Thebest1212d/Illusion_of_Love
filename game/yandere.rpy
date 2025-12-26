label secret_yandere_end:

    "Вечір був тихий. Занадто тихий"
    "Я не пам’ятаю, коли саме опинився тут"

    "Останнє, що пам’ятаю — дорогу"
    "А далі… ніби щось стерлося"

    play sound krok1
    show solomia blink with dissolve

    "Я не одразу зрозумів, що вона стоїть переді мною"
    "Ніби я просто зупинився — і вона вже була тут"

    s "Ти пізно"
    "Її голос був спокійний. Майже лагідний"

    h "Соломіє?.."
    "Я намагався зрозуміти, що відбувається"
    h "Як... ти мене знайшла?"
    play sound heart

    s "Я хвилювалась"
    s "Ти не відповідав"

    "Я хотів запитати, звідки вона знала, де я"
    "Але не запитав"

    s "Ти ж пам’ятаєш…"
    s "Я казала, що буду поруч"

    show solomia smiled with dissolve

    "Вона усміхнулась"
    "Ця усмішка була точною. Вивченою"

    s "Навіть коли ти мене відштовхнув"
    s "Навіть коли обрав ігри"
    s "Навіть коли вирішив, що я зникла"

    show solomia blink with dissolve
    "Я не пам’ятаю, скільки часу ми просто стояли одне навпроти одного"
    show solomia blink at zoomin with dissolve
    play sound krok1
    "Я зрозумів, що не пам’ятаю, чи робив кроки сам"

    s "Ти просто втомився"
    s "Тобі потрібен хтось, хто не піде"

    show solomia blink at zoomin with dissolve

    s "Я не піду"

    "Я відчув, як у грудях стає важко"
    "Ніби світ звузився до однієї точки"
    "Її очі дивилися прямо в мене"
    play sound heart 
    pause 1.0
    s "Зі мною тобі не доведеться більше обирати"
    s "Я вже все вирішила"

    scene dark with fade
    pause 1.5
    play sound heart
    pause 0.5

    s "Тепер ми разом."
    pause 0.7
    s "Назавжди, [usID]."


    stop music fadeout 3.0
    scene black with fade
    if not achievement.has("yandere_end"):  # Перевіряємо, чи досягнення ще не здобуте
        achieve yandere_end
        play sound achievement 
    pause 1.0
    "{i}Тепер ти не один, [usID].{/i}"
    pause 4.0
    "..."
    return
