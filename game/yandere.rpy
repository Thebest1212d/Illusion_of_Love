label secret_yandere_end:
    play music horror fadein 1.0
    scene bg out2night with fade

    "Вечір опустився на місто. Я йшов по вулиці додому, коли відчув дивний погляд на собі…"
    
    show solomia2 blink with dissolve
    play sound krok1

    s "Я… я ніколи не відпущу тебе, [h]… ніколи…" 
    "Її посмішка здавалась ніжною, але в очах блищав небезпечний вогник."
    
    show solomia2 blink with dissolve
    play sound heart
    
    s "Навіть якщо всі інші тебе забудуть… я буду поряд. Завжди."

    "Я спробував крокнути назад, але вона непомітно наблизилася, її руки злегка торкнули моєї руки."
    
    show solomia2 blink at zoomin with dissolve
    "Вона нахилилася трохи ближче, і відчуття небезпеки змішалося з якимось дивним теплом…"

    menu yandere_decision:
        "Що роблю?"
        "Втікаю":
            "Я відступив, намагаючись втекти, але її погляд не відпускав мене…"
            jump secret_yandere_chase
        "Заспокоюю її":
            "Я спробував говорити спокійно, тримаючи руки обережно, намагаючись не налякати її ще більше…"
            jump secret_yandere_close

label secret_yandere_chase:
    scene dark with fade
    play sound heart
    "Соломія тихо сміялася, але її кроки були точними — вона завжди знала, де я."
    "Це був момент, коли я зрозумів, що вона дійсно помішана на мені…"
    jump secret_yandere_final

label secret_yandere_close:
    scene dark with fade
    play sound heart
    "Її руки обережно тримали мене, а погляд не залишав місця сумніву."
    s "Ти належиш лише мені… і ніхто більше не має права на тебе."
    jump secret_yandere_final

label secret_yandere_final:
    scene room_heronight with fade
    show solomia2 smiled with dissolve
    play sound heart
    s "Ми залишилися тут удвох. Світ навколо зник, залишилися лише я і вона…"
    "Ця ніч запам’ятається мені назавжди."
    
    # $ achievement.add("yandere_end")
    return
