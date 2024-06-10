import pygame
import sys
import random

# Инициализация pygame
pygame.init()

# Создаем окно меню
menu_screen = pygame.display.set_mode((400, 300))
pygame.display.set_caption("DuckHunt Menu")

# Фон меню
menu_background_color = (255, 255, 255)

# Шрифт для меню
font = pygame.font.Font(None, 36)

# Меню
menu_items = ["Начать игру", "Настройки", "Выход"]

# Текущий пункт меню
current_menu_item = 0

# Глобальные переменные для настроек
difficulty = [1]  # Сложность: 1 - низкая, 2 - средняя, 3 - высокая
duck_speeds = {1: 2, 2: 4, 3: 6}  # Скорости утки для разных уровней сложности


# Функция для отображения меню
def draw_menu():
    menu_screen.fill(menu_background_color)
    for i, item in enumerate(menu_items):
        if i == current_menu_item:
            text = font.render(item, True, (0, 0, 0))
        else:
            text = font.render(item, True, (128, 128, 128))
        menu_screen.blit(text, (100, 100 + i * 50))
    pygame.display.flip()


# Функция для обработки ввода в меню
def handle_menu_input(event):
    global current_menu_item
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_UP:
            current_menu_item = (current_menu_item - 1) % len(menu_items)
        elif event.key == pygame.K_DOWN:
            current_menu_item = (current_menu_item + 1) % len(menu_items)
        elif event.key == pygame.K_RETURN:
            if current_menu_item == 0:  # Начать игру
                start_game()
            elif current_menu_item == 1:  # Настройки
                settings()
            elif current_menu_item == 2:  # Выход
                pygame.quit()
                sys.exit()


# Функция для запуска игры
def start_game():
    global menu_screen
    global difficulty

    # Создаем окно игры
    game_screen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("DuckHunt")

    # Инициализация игры
    duck_image = pygame.image.load("duck.png")  # Убедитесь, что файл существует и путь верен
    duck_rect = duck_image.get_rect()
    duck_rect.x = random.randint(0, 700)
    duck_rect.y = random.randint(0, 500)
    duck_speed = duck_speeds[difficulty[0]]

    clock = pygame.time.Clock()  # Создаем объект Clock

    # Главный цикл игры
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        # Обновление координат качки
        duck_rect.x += duck_speed
        if duck_rect.x > 800 or duck_rect.x < 0:
            duck_speed = -duck_speed

        # Отрисовка фона и качки
        game_screen.fill((135, 206, 235))
        game_screen.blit(duck_image, duck_rect)

        # Обновление экрана
        pygame.display.flip()

        # Контроль скорости игры
        clock.tick(60)


# Функция для настройки сложности
def settings():
    global menu_screen
    global difficulty

    # Создаем окно настроек
    settings_screen = pygame.display.set_mode((400, 300))
    pygame.display.set_caption("DuckHunt Settings")

    # Фон настроек
    settings_background_color = (255, 255, 255)

    # Функция для отображения настроек
    def draw_settings():
        settings_screen.fill(settings_background_color)
        text = font.render("Сложность:", True, (0, 0, 0))
        settings_screen.blit(text, (100, 100))
        text = font.render(str(difficulty[0]), True, (0, 0, 0))
        settings_screen.blit(text, (250, 100))
        pygame.display.flip()

    # Функция для обработки ввода в настройках
    def handle_settings_input(event):
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if difficulty[0] < 3:  # Максимальная сложность - 3
                    difficulty[0] += 1
            elif event.key == pygame.K_DOWN:
                if difficulty[0] > 1:  # Минимальная сложность - 1
                    difficulty[0] -= 1
            elif event.key == pygame.K_RETURN:
                start_game()

    # Главный цикл настроек
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            handle_settings_input(event)

        draw_settings()


# Главный цикл меню
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        handle_menu_input(event)

    draw_menu()
