init python:
    def check_banned(heroname):
        banned_words = [    "сука", "підор", "гандон", "блять", "їблан", "урод", "повія", "блядун", "клоун", "підарас",
    "сучка", "лох", "шлюха", "шалава", "хуй", "член", "негр", "мудак", "еблан", "гнида", "дебіл",
    "кретин", "імбецил", "кончений", "долбоєб", "хуєсос", "залупа", "тварь", "випердок", "паскуда",
    "мразь", "падло", "сволота", "дрищ", "ебать", "дрочер", "гівно", "засранець", "чмо", "покидьок",
    "нечисть", "цицьки", "ублюдок", "хер", "курва", "манда", "збоченець", "єбать", "лошара",
    "хуєвий", "хуєла", "хуєсос", "бидло", "ебанат", "псина", "скотина", "сукин", "убогий",  
    "засранец", "дегенерат", "параша", "опущений", "тупиця", "даун", "малолєтка", "жополиз",  
    "мандавошка", "задрот", "шмаркач", "обмудок", "дурень", "недоумок", "сракота", "пердун", "лярва",  
    "півень", "курво", "мать твою", "єбать твою", "в рот", "в сраку", "гівнюк", "гівняр", "гівножер", "хвойда"]
        lowercase_heroname = heroname.lower()

        # Перевірка, чи містить ім'я заборонені слова
        if any(word in lowercase_heroname for word in banned_words):
            return True
        else:
            return False


    #Код змійки
init python:
    import random

    class SnakeGame:
        def __init__(self):
            self.width = 1920
            self.height = 1080
            self.grid_size = 60  # Збільшений розмір клітинок (для більшого екрана)
            self.running = True
            self.score = 0  # Додано лічильник очок
            self.is_dead = False  # Змінна для перевірки смерті змійки

            # Створення змійки (початкове положення)
            self.snake = [(self.width // 2, self.height // 2)]
            self.direction = (0, -self.grid_size)
            self.food = self.spawn_food()

        def spawn_food(self):
            while True:
                food = (random.randint(0, (self.width // self.grid_size) - 1) * self.grid_size,
                        random.randint(0, (self.height // self.grid_size) - 1) * self.grid_size)
                if food not in self.snake:
                    return food

        def move(self):
            if not self.running:
                return

            # Оновлення координат голови змії
            new_head = (self.snake[0][0] + self.direction[0], self.snake[0][1] + self.direction[1])

            # Перевірка на зіткнення з тілом або стінами
            if new_head in self.snake or not (0 <= new_head[0] < self.width and 0 <= new_head[1] < self.height):
                self.is_dead = True  # Змійка померла
                self.running = False
                renpy.call("snake_game_over")
                return

            # Додаємо нову голову змії
            self.snake.insert(0, new_head)

            # Якщо змія з'їла яблуко, спавнимо нове яблуко і збільшуємо очки
            if abs(new_head[0] - self.food[0]) < self.grid_size and abs(new_head[1] - self.food[1]) < self.grid_size:
                self.food = self.spawn_food()
                self.score += 1  # Збільшуємо рахунок
            else:
                self.snake.pop()  # Видаляємо останній елемент змії (якщо не з'їли яблуко)

        def change_direction(self, new_direction):
            # Не дозволяємо змінити напрямок на протилежний
            if (new_direction[0] == -self.direction[0] and new_direction[0] != 0) or \
            (new_direction[1] == -self.direction[1] and new_direction[1] != 0):
                return
            self.direction = new_direction

# Ініціалізація гри
init python:
    game_instance = SnakeGame()

# Оновлення екрану змійки
screen snake_game:
    key "K_UP" action Function(game_instance.change_direction, (0, -game_instance.grid_size))
    key "K_DOWN" action Function(game_instance.change_direction, (0, game_instance.grid_size))
    key "K_LEFT" action Function(game_instance.change_direction, (-game_instance.grid_size, 0))
    key "K_RIGHT" action Function(game_instance.change_direction, (game_instance.grid_size, 0))
    
    timer 0.1 repeat True action Function(game_instance.move)

    # Фон екрану
    add Solid("#000")

    # Малюємо змію
    if game_instance:
        for segment in game_instance.snake:
            add Solid("#0F0", xsize=game_instance.grid_size, ysize=game_instance.grid_size) xpos segment[0] ypos segment[1]
        
        # Малюємо яблуко
        add Solid("#F00", xsize=game_instance.grid_size, ysize=game_instance.grid_size) xpos game_instance.food[0] ypos game_instance.food[1]
        
        # Вивести рахунок
        add Text("Score: " + str(game_instance.score), xpos=10, ypos=10, size=40, color="#FFF")

# Перехід до кінця гри
label snake_game_over:
    $ score = game_instance.score  # Зберігаємо рахунок у змінну
    "Гра закінчена! Ти набрав [score] очок."  # Використовуємо змінну без фігурних дужок
    return


# Старт гри
label snake_game_start:
    $ game_instance = SnakeGame()
    $ renpy.pause(0.5)  # Час на старт гри
    call screen snake_game


